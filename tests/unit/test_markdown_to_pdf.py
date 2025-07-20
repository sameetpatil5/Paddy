# tests/unit/test_markdown_to_pdf.py

import pytest
from app.modules.markdown_to_pdf import paddy_markdown_to_pdf
from io import BytesIO


@pytest.mark.asyncio
async def test_paddy_markdown_to_pdf():
    content = "# Hello Paddy\nThis is a test."
    result_pdf = await paddy_markdown_to_pdf(content)
    assert isinstance(result_pdf, BytesIO)
    assert result_pdf.getbuffer().nbytes > 0
