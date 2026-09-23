from __future__ import annotations

from abc import ABC, abstractmethod

from .state import AgentState


class PromptBuilder(ABC):
    """Assembles the system prompt from an identity block, mode-specific
    guidelines, and the active toolset's instructions. Concrete prompt
    text is intentionally out of scope for this scaffold."""

    @abstractmethod
    def build(self, state: AgentState) -> str:
        raise NotImplementedError
