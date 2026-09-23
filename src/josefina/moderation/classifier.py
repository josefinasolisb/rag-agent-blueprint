from __future__ import annotations

from abc import ABC, abstractmethod


class ContentClassifier(ABC):
    """Pluggable content classifier: LLM-backed, heuristic, or hybrid."""

    @abstractmethod
    def classify(self, text: str) -> dict:
        """Returns a category -> confidence mapping consumed by the RuleEngine."""
        raise NotImplementedError
