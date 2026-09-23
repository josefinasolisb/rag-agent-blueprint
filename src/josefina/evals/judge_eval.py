from __future__ import annotations

from dataclasses import dataclass


@dataclass
class JudgeCase:
    turn_id: str
    transcript: list[dict]
    rubric_path: str


@dataclass
class JudgeScore:
    turn_id: str
    scores: dict[str, float]
    passed: bool


def run_judge_eval(cases: list[JudgeCase], passes: int = 1) -> list[JudgeScore]:
    """LLM-as-judge check: a separate model scores each transcript against
    a markdown rubric. Intended to run multiple passes and compare the
    median against a committed baseline with a fixed tolerance."""
    raise NotImplementedError
