from __future__ import annotations

from .chunking import Chunker
from .embeddings import EmbeddingClient
from .vector_store import VectorStore


def index_document(
    document_id: str,
    full_text: str,
    chunker: Chunker,
    embedder: EmbeddingClient,
    store: VectorStore,
) -> None:
    """Entry point: chunk -> embed -> upsert. Consumes text approved by
    moderation; feeds the agent's search tool downstream."""
    raise NotImplementedError
