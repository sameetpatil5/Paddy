# app/routes.py

from typing import List

from fastapi import UploadFile, File, Form
from fastapi.responses import StreamingResponse
from fastapi import APIRouter

from app.modules.extract_images import paddy_extract_images
from app.modules.merge_pdfs import paddy_merge_pdfs

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

