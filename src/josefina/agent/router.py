from __future__ import annotations

from abc import ABC, abstractmethod

from .state import AgentState


class ModeRouter(ABC):
    """Cheap classifier that decides which mode subgraph handles the
    current turn before any expensive model call happens."""

    @abstractmethod
    def route(self, state: AgentState) -> str:
        raise NotImplementedError
