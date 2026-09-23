from __future__ import annotations

import pytesseract

from .base import ExtractionResult, Extractor


class OCRFallbackExtractor(Extractor):
    """Runs Tesseract OCR (via pytesseract) when native extraction is
    unavailable or falls below the quality bar — e.g. a scanned PDF page
    rendered to an image, or a photographed document."""

    def can_handle(self, filename: str, content_type: str) -> bool:
        raise NotImplementedError

    def extract(self, raw_bytes: bytes) -> ExtractionResult:
        raise NotImplementedError
