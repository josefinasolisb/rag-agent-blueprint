from __future__ import annotations

import asyncio

import pytest

from rag_agent_blueprint.feedback.models import FeedbackRecord, FeedbackVote
from rag_agent_blueprint.feedback.store import FeedbackStore


def test_feedback_record_constructs():
    record = FeedbackRecord(turn_id="t1", vote=FeedbackVote.LIKE)
    assert record.vote is FeedbackVote.LIKE
    assert record.promoted_to_dataset is False


def test_feedback_store_raises_not_implemented():
    # DESIGN PROPOSAL: FeedbackStore has a sketched contract; promotion
    # into the evals dataset is handled separately (see evals/test_evals.py).
    store = FeedbackStore(connection=None)
    with pytest.raises(NotImplementedError):
        asyncio.run(store.record(FeedbackRecord(turn_id="t1", vote=FeedbackVote.LIKE)))
