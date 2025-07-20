# app/modules/image_to_pdf.py

import fitz  # PyMuPDF
from fastapi import UploadFile
from typing import List
import io

async def paddy_image_to_pdf(files: List[UploadFile]) -> io.BytesIO:
    output_pdf = fitz.open()
    for file in files:
        image_data = await file.read()
        img_doc = fitz.open("png", image_data)
        pdf_bytes = img_doc.convert_to_pdf()
        img_pdf = fitz.open("pdf", pdf_bytes)
        output_pdf.insert_pdf(img_pdf)
        img_pdf.close()
        img_doc.close()
    output = io.BytesIO()
    output_pdf.save(output)
    output_pdf.close()
    output.seek(0)
    return output
