# tests/test_endpoints.py

import io
import zipfile
from PIL import Image

import fitz  # PyMuPDF
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def create_sample_pdf(pages=1) -> bytes:
    """Creates a simple in-memory PDF with 'pages' blank pages"""
    pdf = fitz.open()
    for _ in range(pages):
        pdf.new_page()
    buffer = io.BytesIO()
    pdf.save(buffer)
    pdf.close()
    buffer.seek(0)
    return buffer.read()


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Paddy says Hello!"}


def test_extract_single_page_image():
    pdf_bytes = create_sample_pdf(pages=1)
    files = {"file": ("single_page.pdf", pdf_bytes, "application/pdf")}

    response = client.post("/extract-images", files=files)

    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    assert "attachment; filename=page_1.png" in response.headers["content-disposition"]
    assert len(response.content) > 1000  # Some image bytes


def test_extract_multi_page_zip():
    pdf_bytes = create_sample_pdf(pages=3)
    files = {"file": ("multi_page.pdf", pdf_bytes, "application/pdf")}

    response = client.post("/extract-images", files=files)

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/zip"
    assert "attachment; filename=images.zip" in response.headers["content-disposition"]

    # Check ZIP file contents
    zip_buf = io.BytesIO(response.content)
    with zipfile.ZipFile(zip_buf) as zf:
        assert len(zf.namelist()) == 3
        assert "page_1.png" in zf.namelist()


def test_merge_pdfs():
    pdf1 = create_sample_pdf(pages=1)
    pdf2 = create_sample_pdf(pages=2)

    files = [
        ("files", ("doc1.pdf", pdf1, "application/pdf")),
        ("files", ("doc2.pdf", pdf2, "application/pdf")),
    ]

    response = client.post("/merge-pdfs", files=files)

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert "attachment; filename=merged.pdf" in response.headers["content-disposition"]

    # Validate merged PDF has 3 pages
    merged_stream = io.BytesIO(response.content)
    doc = fitz.open(stream=merged_stream, filetype="pdf")
    assert len(doc) == 3
    doc.close()


def test_image_to_pdf():
    img = Image.new("RGB", (100, 100), color="red")
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    files = {"files": ("red.png", img_bytes, "image/png")}
    response = client.post("/image-to-pdf", files=files)

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert "attachment; filename=output.pdf" in response.headers["content-disposition"]
    assert len(response.content) > 100


def test_markdown_to_pdf():
    md_text = "# Hello\nThis is **bold** text."
    data = {"text": md_text}
    response = client.post("/markdown-to-pdf", json=data)

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert (
        "attachment; filename=markdown.pdf" in response.headers["content-disposition"]
    )
    assert len(response.content) > 100
