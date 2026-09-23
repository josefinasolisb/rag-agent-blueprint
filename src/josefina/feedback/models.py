from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class FeedbackVote(str, Enum):
    LIKE = "like"
    DISLIKE = "dislike"


@dataclass
class FeedbackRecord:
    """DESIGN PROPOSAL — not wired into any pipeline in this scaffold.
    Sketches how user feedback could eventually feed an evals dataset."""

    turn_id: str
    vote: FeedbackVote
    comment: str | None = None
