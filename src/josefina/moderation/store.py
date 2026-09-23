from __future__ import annotations

from abc import ABC, abstractmethod

from .models import ReviewRecord


class ModerationStore(ABC):
    """Persists moderation decisions. Storage-agnostic by design — a
    reference deployment could back this with a relational or analytical
    store depending on query patterns."""

    @abstractmethod
    def save(self, record: ReviewRecord) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, document_id: str) -> ReviewRecord | None:
        raise NotImplementedError
