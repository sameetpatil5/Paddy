# tests/unit/test_pdf_merging.py

import io
import fitz  # PyMuPDF


def create_sample_pdf(pages=1) -> io.BytesIO:
    pdf = fitz.open()
    for _ in range(pages):
        pdf.new_page()
    buffer = io.BytesIO()
    pdf.save(buffer)
    buffer.seek(0)
    return buffer


def merge_pdfs_pymupdf(pdf_list: list[io.BytesIO]) -> io.BytesIO:
    merged = fitz.open()
    for pdf_io in pdf_list:
        src = fitz.open(stream=pdf_io.read(), filetype="pdf")
        merged.insert_pdf(src)
    output = io.BytesIO()
    merged.save(output)
    output.seek(0)
    return output


def test_merge_pdfs_unit():
    pdf1 = create_sample_pdf(pages=1)
    pdf2 = create_sample_pdf(pages=2)

    merged = merge_pdfs_pymupdf([pdf1, pdf2])
    doc = fitz.open(stream=merged, filetype="pdf")
    assert len(doc) == 3
    doc.close()

