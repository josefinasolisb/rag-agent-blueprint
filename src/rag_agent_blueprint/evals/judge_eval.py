from __future__ import annotations

from dataclasses import dataclass

from openai import OpenAI


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


def run_judge_eval(
    cases: list[JudgeCase], client: OpenAI, judge_model: str, passes: int = 1
) -> list[JudgeScore]:
    """LLM-as-judge check: `judge_model` (called via an OpenAI-compatible
    chat completions API, kept separate from whatever model is under
    test) scores each transcript against a markdown rubric. Intended to
    run multiple passes and compare the median against a committed
    baseline with a fixed tolerance."""
    # Multiple passes + median exist because a single judge call is noisy;
    # this is run by hand before a release, not on every commit.
    raise NotImplementedError
