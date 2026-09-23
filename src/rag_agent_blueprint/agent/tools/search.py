from __future__ import annotations

from typing import Any

from ...indexing.embeddings import EmbeddingClient
from ...indexing.vector_store import VectorStore
from .base import Tool


class DocumentSearchTool(Tool):
    """Embeds the query with `EmbeddingClient` and retrieves the closest
    chunks from the pgvector-backed `VectorStore` for grounding."""

    name = "search_documents"
    description = "Semantic search over the indexed document collection."

    def __init__(self, embedder: EmbeddingClient, vector_store: VectorStore):
        self._embedder = embedder
        self._vector_store = vector_store

    def run(self, query: str, top_k: int = 5, **kwargs: Any) -> list[dict]:
        raise NotImplementedError
