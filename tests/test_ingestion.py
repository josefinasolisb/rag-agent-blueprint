from __future__ import annotations

import pytest

from rag_agent_blueprint.ingestion.extractors.chain import ExtractorChain
from rag_agent_blueprint.ingestion.extractors.ocr_fallback import OCRFallbackExtractor
from rag_agent_blueprint.ingestion.extractors.pdf_native import PDFNativeExtractor
from rag_agent_blueprint.ingestion.extractors.plain_text import PlainTextExtractor
from rag_agent_blueprint.ingestion.pipeline import ingest_document


@pytest.mark.parametrize(
    "extractor_cls", [PlainTextExtractor, PDFNativeExtractor, OCRFallbackExtractor]
)
def test_extractor_interface_raises_not_implemented(extractor_cls):
    extractor = extractor_cls()
    with pytest.raises(NotImplementedError):
        extractor.can_handle("file.txt", "text/plain")
    with pytest.raises(NotImplementedError):
        extractor.extract(b"")


def test_extractor_chain_run_raises_not_implemented():
    chain = ExtractorChain(extractors=[])
    with pytest.raises(NotImplementedError):
        chain.run("file.txt", "text/plain", b"")


def test_ingest_document_raises_not_implemented():
    chain = ExtractorChain(extractors=[])
    with pytest.raises(NotImplementedError):
        ingest_document("file.txt", "text/plain", b"", chain)
