from __future__ import annotations

from abc import ABC, abstractmethod

from .models import FeedbackRecord


class FeedbackStore(ABC):
    """DESIGN PROPOSAL — no concrete implementation or wiring exists yet.
    A real deployment would decide here whether feedback also promotes a
    turn into the evals golden dataset."""

    @abstractmethod
    def record(self, feedback: FeedbackRecord) -> None:
        raise NotImplementedError
