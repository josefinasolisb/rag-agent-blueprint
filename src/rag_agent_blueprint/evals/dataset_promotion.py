from __future__ import annotations

from dataclasses import dataclass

from ..feedback.models import FeedbackRecord
from .judge_eval import JudgeCase
from .tool_call_eval import ToolCallCase


@dataclass
class PromotionDecision:
    """Whether a piece of feedback was promoted into an eval dataset, and why."""

    promoted: bool
    reason: str


def promote_feedback(
    feedback: FeedbackRecord, transcript: list[dict], expected_tool: str | None = None
) -> tuple[PromotionDecision, ToolCallCase | JudgeCase | None]:
    """Decides whether a piece of user feedback should become a case in an
    eval dataset. A `dislike` requires human review before promotion (to
    avoid poisoning the golden set with a bad-faith vote); a `like` can be
    promoted more directly as a positive example. Returns the decision and,
    if promoted, the resulting case for `run_tool_call_eval`/`run_judge_eval`."""
    raise NotImplementedError
