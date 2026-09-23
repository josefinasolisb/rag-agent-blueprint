from __future__ import annotations

from .base import ExtractionResult, Extractor


class PlainTextExtractor(Extractor):
    """Handles formats that are already text-based and need no extraction."""

    def can_handle(self, filename: str, content_type: str) -> bool:
        raise NotImplementedError

    def extract(self, raw_bytes: bytes) -> ExtractionResult:
        raise NotImplementedError
