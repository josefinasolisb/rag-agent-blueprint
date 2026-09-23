from __future__ import annotations

from typing import Any

from ...indexing.vector_store import VectorStore
from .base import Tool


class GetDocumentFragmentTool(Tool):
    """Fetches one specific chunk by document_id + fragment_index directly
    from the VectorStore, with no similarity search involved."""

    name = "get_document_fragment"
    description = "Retrieve a single specific fragment of a document by its index."

    def __init__(self, vector_store: VectorStore):
        self._vector_store = vector_store

    def run(self, document_id: str, fragment_index: int, **kwargs: Any) -> dict:
        raise NotImplementedError
