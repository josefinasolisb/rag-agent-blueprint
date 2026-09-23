from __future__ import annotations

from psycopg import AsyncConnection

from .models import FeedbackRecord


class FeedbackStore:
    """DESIGN PROPOSAL — no concrete implementation exists yet. Would
    persist feedback in the same Postgres instance as the rest of the
    relational data. Promotion into the evals dataset is a separate step,
    see `evals.dataset_promotion.promote_feedback`."""

    def __init__(self, connection: AsyncConnection):
        self._connection = connection

    async def record(self, feedback: FeedbackRecord) -> None:
        raise NotImplementedError
