# tests/unit/test_image_to_pdf.py

import pytest
from fastapi import UploadFile
from app.modules.image_to_pdf import paddy_image_to_pdf
from io import BytesIO


class DummyUploadFile:
    def __init__(self, content: bytes, filename="test.jpg"):
        self.file = BytesIO(content)
        self.filename = filename

    async def read(self):
        return self.file.getvalue()


@pytest.mark.asyncio
async def test_paddy_image_to_pdf():
    # Sample 1x1 PNG image
    image_data = (
        b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR"
        b"\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00"
        b"\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\xdac\xf8\x0f\x00\x01\x01\x01\x00"
        b"\x18\xdd\xdcS\x00\x00\x00\x00IEND\xaeB`\x82"
    )
    files = [DummyUploadFile(image_data)]
    result_pdf = await paddy_image_to_pdf(files)
    assert isinstance(result_pdf, BytesIO)
    assert result_pdf.getbuffer().nbytes > 0
