from __future__ import annotations

from abc import ABC, abstractmethod

from .models import ModerationStatus


class ModerationRule(ABC):
    """A single rule evaluated in priority order; the first match wins."""

    priority: int = 0

    @abstractmethod
    def matches(self, classifier_output: dict, quality_score: float) -> bool:
        raise NotImplementedError

    @abstractmethod
    def resolve(self) -> ModerationStatus:
        raise NotImplementedError


class RuleEngine:
    """Evaluates rules in priority order. Safety rules should be registered
    ahead of quality-based rules so a low score can never override them."""

    def __init__(self, rules: list[ModerationRule]):
        self._rules = sorted(rules, key=lambda r: r.priority)

    def evaluate(self, classifier_output: dict, quality_score: float) -> ModerationStatus:
        raise NotImplementedError
