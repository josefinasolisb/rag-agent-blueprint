from __future__ import annotations

from dataclasses import dataclass

from psycopg import AsyncConnection


@dataclass
class VectorRecord:
    id: str
    document_id: str
    text: str
    embedding: list[float]
    metadata: dict


class VectorStore:
    """Similarity store backed by Postgres + the pgvector extension, using
    an `ivfflat` / cosine-distance index over the `embedding` column."""

    def __init__(self, connection: AsyncConnection):
        self._connection = connection

    async def upsert(self, records: list[VectorRecord]) -> None:
        raise NotImplementedError

    async def similarity_search(
        self, query_embedding: list[float], top_k: int = 5, document_id: str | None = None
    ) -> list[VectorRecord]:
        """Nearest-neighbor search, optionally scoped to a single document_id
        instead of the whole collection."""
        raise NotImplementedError

    async def get_fragment(self, document_id: str, fragment_index: int) -> VectorRecord | None:
        """Direct lookup of one specific chunk, no similarity search involved."""
        raise NotImplementedError

    async def get_representative_fragments(self, document_id: str, k: int = 5) -> list[VectorRecord]:
        # Returns a small, representative subset of a document's chunks so
        # summarization/question-generation don't need the full document.
        raise NotImplementedError
