# modules/extract_images.py

import io
import zipfile
import fitz  # PyMuPDF
from PIL import Image
from fastapi import UploadFile
from typing import List, Union


async def paddy_extract_images(file: UploadFile) -> Union[io.BytesIO, zipfile.ZipFile]:
    contents = await file.read()
    pdf_stream = io.BytesIO(contents)
    doc = fitz.open(stream=pdf_stream, filetype="pdf")

    zoom = 2  # to improve resolution
    mat = fitz.Matrix(zoom, zoom)

    images = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=mat)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        img_bytes = io.BytesIO()
        img.save(img_bytes, format="PNG", dpi=(300, 300))
        img_bytes.seek(0)
        images.append((f"page_{i+1}.png", img_bytes))

    doc.close()

    if len(images) == 1:
        # Return the single image
        return images[0][1], "image/png", images[0][0]

    # Return zipped images
    zip_bytes = io.BytesIO()
    with zipfile.ZipFile(zip_bytes, mode="w") as zf:
        for name, image_bytes in images:
            zf.writestr(name, image_bytes.read())

    zip_bytes.seek(0)
    return zip_bytes, "application/zip", "images.zip"
