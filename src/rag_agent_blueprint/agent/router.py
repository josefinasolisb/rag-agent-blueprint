from __future__ import annotations

from abc import ABC, abstractmethod

from .state import AgentState


class ModeRouter(ABC):
    """Cheap classifier that decides which mode subgraph handles the
    current turn before any expensive model call happens."""

    @abstractmethod
    def route(self, state: AgentState) -> str:
        # Picks which mode subgraph handles this turn so each mode keeps
        # its own prompt/toolset instead of one graph branching on intent.
        raise NotImplementedError
