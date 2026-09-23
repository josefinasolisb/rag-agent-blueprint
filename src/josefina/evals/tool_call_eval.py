from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ToolCallCase:
    turn_id: str
    expected_tool: str | None
    transcript: list[dict]


@dataclass
class ToolCallResult:
    turn_id: str
    passed: bool
    actual_tool: str | None


def run_tool_call_eval(cases: list[ToolCallCase]) -> list[ToolCallResult]:
    """Deterministic check: did the transcript call the expected tool (or
    correctly call none)? No LLM involved. Meant to run as a blocking check
    before shipping a prompt or model change."""
    raise NotImplementedError
