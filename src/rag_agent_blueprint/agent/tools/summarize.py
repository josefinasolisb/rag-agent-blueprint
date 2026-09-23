from __future__ import annotations

from typing import Any

from openai import OpenAI

from ...indexing.vector_store import VectorStore
from .base import Tool


class SummarizeDocumentTool(Tool):
    """Summarizes a document from a small, representative subset of its
    chunks (`VectorStore.get_representative_fragments`) instead of
    concatenating the full document into the prompt."""

    name = "summarize_document"
    description = "Produce a summary of a document's content."

    def __init__(self, vector_store: VectorStore, llm_client: OpenAI, model: str):
        self._vector_store = vector_store
        self._llm_client = llm_client
        self._model = model

    def run(self, document_id: str, **kwargs: Any) -> str:
        raise NotImplementedError
