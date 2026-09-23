from __future__ import annotations

from .base import ExtractionResult, Extractor


class OCRFallbackExtractor(Extractor):
    """Runs OCR when native extraction is unavailable or below quality bar."""

    def can_handle(self, filename: str, content_type: str) -> bool:
        raise NotImplementedError

    def extract(self, raw_bytes: bytes) -> ExtractionResult:
        raise NotImplementedError
