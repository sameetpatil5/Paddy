# tests/unit/test_image_extraction.py

import io
import zipfile
import fitz  # PyMuPDF
from PIL import Image


def create_sample_pdf(pages=1) -> bytes:
    pdf = fitz.open()
    for _ in range(pages):
        pdf.new_page()
    buffer = io.BytesIO()
    pdf.save(buffer)
    pdf.close()
    buffer.seek(0)
    return buffer.read()


def extract_images_from_pdf(pdf_bytes: bytes) -> list:
    images = []
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    for i, page in enumerate(doc):
        pix = page.get_pixmap()
        img_io = io.BytesIO()
        img_io.name = f"page_{i+1}.png"
        Image.frombytes("RGB", [pix.width, pix.height], pix.samples).save(
            img_io, format="PNG"
        )
        img_io.seek(0)
        images.append(img_io)
    return images


def test_extract_single_page_image_unit():
    pdf_bytes = create_sample_pdf(pages=1)
    images = extract_images_from_pdf(pdf_bytes)
    assert len(images) == 1
    assert images[0].name == "page_1.png"
    assert len(images[0].read()) > 1000


def test_extract_multi_page_zip_unit():
    pdf_bytes = create_sample_pdf(pages=3)
    images = extract_images_from_pdf(pdf_bytes)

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as zf:
        for img in images:
            zf.writestr(img.name, img.getvalue())

    buffer.seek(0)
    with zipfile.ZipFile(buffer, "r") as zf:
        assert len(zf.namelist()) == 3
        assert "page_1.png" in zf.namelist()
        assert "page_3.png" in zf.namelist()
