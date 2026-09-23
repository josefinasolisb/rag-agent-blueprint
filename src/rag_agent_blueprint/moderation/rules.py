from __future__ import annotations

from abc import ABC, abstractmethod
from enum import IntEnum

from .models import ClassificationSignals, RuleOutcome


class RulePriority(IntEnum):
    """Lower sorts first. Safety must sort ahead of policy and quality so a
    good or bad quality_score can never override a safety signal."""

    SAFETY = 0
    POLICY = 10
    QUALITY = 20


class ModerationRule(ABC):
    """A single rule evaluated in priority order; the first match wins."""

    priority: RulePriority = RulePriority.QUALITY

    @abstractmethod
    def matches(self, signals: ClassificationSignals, quality_score: float) -> bool:
        raise NotImplementedError

    @abstractmethod
    def resolve(self) -> RuleOutcome:
        raise NotImplementedError


class SafetyRule(ModerationRule):
    """Example concrete rule: matches on a safety signal from the
    classifier output (e.g. offensive/illegal content) and resolves to a
    suspension. Illustrates the pattern; the actual signal keys and
    resolution are left to a real implementation."""

    priority = RulePriority.SAFETY

    def matches(self, signals: ClassificationSignals, quality_score: float) -> bool:
        raise NotImplementedError

    def resolve(self) -> RuleOutcome:
        raise NotImplementedError


class RuleEngine:
    """Evaluates rules in priority order. Safety rules should be registered
    ahead of quality-based rules so a low score can never override them."""

    def __init__(self, rules: list[ModerationRule]):
        self._rules = sorted(rules, key=lambda r: r.priority)

    def evaluate(self, signals: ClassificationSignals, quality_score: float) -> RuleOutcome:
        # Safety rules must sort ahead of quality rules: a low score can
        # never override a safety signal, nor can a good score excuse one.
        raise NotImplementedError
