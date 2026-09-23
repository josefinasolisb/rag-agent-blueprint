from __future__ import annotations

import pymupdf

from .base import ExtractionResult, Extractor


class PDFNativeExtractor(Extractor):
    """Extracts embedded text directly from a PDF's text layer using
    PyMuPDF, without OCR. Fast, but only works when the PDF actually has
    a text layer (as opposed to a scanned image)."""

    def can_handle(self, filename: str, content_type: str) -> bool:
        raise NotImplementedError

    def extract(self, raw_bytes: bytes) -> ExtractionResult:
        raise NotImplementedError
