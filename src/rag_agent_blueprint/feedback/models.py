from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class FeedbackVote(str, Enum):
    LIKE = "like"
    DISLIKE = "dislike"


@dataclass
class FeedbackRecord:
    """DESIGN PROPOSAL — no concrete implementation exists yet. Captured by
    `FeedbackStore`; `evals.dataset_promotion.promote_feedback` decides
    whether it becomes an eval dataset case, recorded here via
    `promoted_to_dataset`."""

    turn_id: str
    vote: FeedbackVote
    comment: str | None = None
    promoted_to_dataset: bool = False
