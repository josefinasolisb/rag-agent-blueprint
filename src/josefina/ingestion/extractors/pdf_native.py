from __future__ import annotations

from .base import ExtractionResult, Extractor


class PDFNativeExtractor(Extractor):
    """Extracts embedded text directly from a PDF's text layer, without OCR."""

    def can_handle(self, filename: str, content_type: str) -> bool:
        raise NotImplementedError

    def extract(self, raw_bytes: bytes) -> ExtractionResult:
        raise NotImplementedError
