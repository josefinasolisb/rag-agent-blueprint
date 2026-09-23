from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class VectorRecord:
    id: str
    document_id: str
    text: str
    embedding: list[float]
    metadata: dict


class VectorStore(ABC):
    """Contract for a pgvector-style similarity store."""

    @abstractmethod
    def upsert(self, records: list[VectorRecord]) -> None:
        raise NotImplementedError

    @abstractmethod
    def similarity_search(self, query_embedding: list[float], top_k: int = 5) -> list[VectorRecord]:
        raise NotImplementedError
