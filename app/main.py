from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from app.modules.extract_images import paddy_extract_images
from app.modules.merge_pdfs import paddy_merge_pdfs
from typing import List
import io

app = FastAPI(title="Paddy: PDF Tools API")


@app.get("/")
def root():
    return {"message": "Paddy says Hello!"}


@app.post("/extract-images")
async def extract_images(file: UploadFile = File(...)):
    output_stream, media_type, filename = await paddy_extract_images(file)
    return StreamingResponse(
        output_stream,
        media_type=media_type,
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


@app.post("/merge-pdfs")
async def merge_pdfs(files: List[UploadFile] = File(...)):
    merged_pdf = await paddy_merge_pdfs(files)
    return StreamingResponse(
        merged_pdf,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=merged.pdf"},
    )
