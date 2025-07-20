# app/modules/merge_pdfs.py

import io
import fitz  # PyMuPDF
from fastapi import UploadFile
from typing import List


async def paddy_merge_pdfs(files: List[UploadFile]) -> io.BytesIO:
    merged_pdf = fitz.open()

    for file in files:
        contents = await file.read()
        pdf_stream = io.BytesIO(contents)
        src_pdf = fitz.open("pdf", pdf_stream)

        merged_pdf.insert_pdf(src_pdf)
        src_pdf.close()

    output = io.BytesIO()
    merged_pdf.save(output)
    merged_pdf.close()
    output.seek(0)
    return output
