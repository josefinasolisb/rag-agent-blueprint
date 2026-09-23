from __future__ import annotations

from .base import ExtractionResult, Extractor


class ExtractorChain:
    """Tries a prioritized list of extractors, keeping the first result
    that clears a minimum quality bar."""

    def __init__(self, extractors: list[Extractor], min_quality: float = 0.5):
        self._extractors = extractors
        self._min_quality = min_quality

    def run(self, filename: str, content_type: str, raw_bytes: bytes) -> ExtractionResult:
        # Chain of responsibility: extractors run in priority order, not a
        # fixed format->extractor map, so adding a format means appending one.
        # Fallback triggers on can_handle()=False, a raised error, or a
        # result whose quality_score is below min_quality.
        raise NotImplementedError
