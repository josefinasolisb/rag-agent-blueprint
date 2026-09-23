from __future__ import annotations

from .base import ExtractionResult, Extractor


class ExtractorChain:
    """Tries a prioritized list of extractors, keeping the first result
    that clears a minimum quality bar."""

    def __init__(self, extractors: list[Extractor], min_quality: float = 0.5):
        self._extractors = extractors
        self._min_quality = min_quality

    def run(self, filename: str, content_type: str, raw_bytes: bytes) -> ExtractionResult:
        raise NotImplementedError
