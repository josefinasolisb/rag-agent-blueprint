from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from ..state import AgentState


@dataclass
class SystemPrompt:
    """A system prompt split into a stable prefix (identity, mode
    guidelines, toolset instructions — rarely changes) and a per-turn
    suffix (retrieved context, date, session data — changes most turns),
    kept separate so the stable prefix can stay servable from a cache."""

    stable_prefix: str
    per_turn_suffix: str


class PromptBuilder(ABC):
    """Assembles the system prompt as a stable prefix and a per-turn
    suffix. Concrete prompt text is intentionally out of scope for this
    scaffold."""

    @abstractmethod
    def build(self, state: AgentState) -> SystemPrompt:
        raise NotImplementedError
