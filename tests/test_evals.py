from __future__ import annotations

import pytest

from rag_agent_blueprint.evals.dataset_promotion import promote_feedback
from rag_agent_blueprint.evals.judge_eval import JudgeCase, run_judge_eval
from rag_agent_blueprint.evals.tool_call_eval import ToolCallCase, run_tool_call_eval
from rag_agent_blueprint.feedback.models import FeedbackRecord, FeedbackVote


def test_tool_call_case_constructs():
    case = ToolCallCase(turn_id="t1", expected_tool="search_documents", transcript=[])
    assert case.turn_id == "t1"


def test_run_tool_call_eval_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        run_tool_call_eval(cases=[])


def test_judge_case_constructs():
    case = JudgeCase(turn_id="t1", transcript=[], rubric_path="docs/rubric.md")
    assert case.rubric_path == "docs/rubric.md"


def test_run_judge_eval_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        run_judge_eval(cases=[], client=None, judge_model="stub-judge-model")


def test_promote_feedback_raises_not_implemented():
    feedback = FeedbackRecord(turn_id="t1", vote=FeedbackVote.LIKE)
    with pytest.raises(NotImplementedError):
        promote_feedback(feedback=feedback, transcript=[], expected_tool="search_documents")
