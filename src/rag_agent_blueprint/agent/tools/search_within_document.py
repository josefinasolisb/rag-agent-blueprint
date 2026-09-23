from __future__ import annotations

from typing import Any

from ...indexing.embeddings import EmbeddingClient
from ...indexing.vector_store import VectorStore
from .base import Tool


class SearchWithinDocumentTool(Tool):
    """The same semantic search as DocumentSearchTool, scoped to a single
    document_id instead of the whole collection."""

    name = "search_within_document"
    description = "Semantic search restricted to a single document."

    def __init__(self, embedder: EmbeddingClient, vector_store: VectorStore):
        self._embedder = embedder
        self._vector_store = vector_store

    def run(self, document_id: str, query: str, top_k: int = 5, **kwargs: Any) -> list[dict]:
        raise NotImplementedError
