from __future__ import annotations

from .extractors.base import ExtractionResult
from .extractors.chain import ExtractorChain


def ingest_document(
    filename: str, content_type: str, raw_bytes: bytes, chain: ExtractorChain
) -> ExtractionResult:
    """Entry point: detect type, run the extractor chain, persist text +
    metadata. Downstream: hands the result to moderation.rules.RuleEngine."""
    raise NotImplementedError
