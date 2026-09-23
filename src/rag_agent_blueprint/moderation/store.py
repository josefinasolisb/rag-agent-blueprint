from __future__ import annotations

from psycopg import AsyncConnection

from .models import ReviewRecord


class ModerationStore:
    """Persists moderation decisions in Postgres, alongside the other
    relational tables (the vector store and conversation checkpointer
    also live in Postgres, via pgvector and LangGraph's Postgres saver)."""

    def __init__(self, connection: AsyncConnection):
        self._connection = connection

    async def save(self, record: ReviewRecord) -> None:
        raise NotImplementedError

    async def get(self, document_id: str) -> ReviewRecord | None:
        raise NotImplementedError
