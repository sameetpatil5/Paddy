# app/modules/image_to_pdf.py

import fitz  # PyMuPDF
from fastapi import UploadFile
from typing import List
import io


async def paddy_image_to_pdf(files: List[UploadFile]) -> io.BytesIO:
    pdf_doc = fitz.open()
    for file in files:
        image_data = await file.read()
        img_pdf = fitz.open(
            "pdf", fitz.Pixmap(fitz.open(stream=image_data, filetype="image"))
        )
        pdf_doc.insert_pdf(img_pdf)
        img_pdf.close()

    output = io.BytesIO()
    pdf_doc.save(output)
    pdf_doc.close()
    output.seek(0)
    return output
