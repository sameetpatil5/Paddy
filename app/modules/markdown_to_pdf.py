# app/modules/markdown_to_pdf.py

import fitz  # PyMuPDF
import io
import markdown
from bs4 import BeautifulSoup


async def paddy_markdown_to_pdf(content: str) -> io.BytesIO:
    html = markdown.markdown(content)
    soup = BeautifulSoup(html, "html.parser")

    doc = fitz.open()
    page = doc.new_page()
    rect = fitz.Rect(50, 50, 550, 800)
    page.insert_htmlbox(rect, soup.prettify())

    output = io.BytesIO()
    doc.save(output)
    doc.close()
    output.seek(0)
    return output
