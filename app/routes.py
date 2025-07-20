# app/routes.py

from typing import List

from fastapi import UploadFile, File, Form
from fastapi.responses import StreamingResponse
from fastapi import APIRouter

from app.modules.extract_images import paddy_extract_images
from app.modules.merge_pdfs import paddy_merge_pdfs
from app.modules.image_to_pdf import paddy_image_to_pdf
from app.modules.markdown_to_pdf import paddy_markdown_to_pdf

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Paddy says Hello!"}


@router.post("/extract-images")
async def extract_images(file: UploadFile = File(...)):
    output_stream, media_type, filename = await paddy_extract_images(file)
    return StreamingResponse(
        output_stream,
        media_type=media_type,
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


@router.post("/merge-pdfs")
async def merge_pdfs(files: List[UploadFile] = File(...)):
    merged_pdf = await paddy_merge_pdfs(files)
    return StreamingResponse(
        merged_pdf,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=merged.pdf"},
    )


@router.post("/image-to-pdf")
async def image_to_pdf(files: List[UploadFile] = File(...)):
    output = await paddy_image_to_pdf(files)
    return StreamingResponse(
        output,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=images.pdf"},
    )


@router.post("/markdown-to-pdf")
async def markdown_to_pdf(content: str = Form(...)):
    output = await paddy_markdown_to_pdf(content)
    return StreamingResponse(
        output,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=markdown.pdf"},
    )
