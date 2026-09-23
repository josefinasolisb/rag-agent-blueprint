from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentState:
    """Shared graph state threaded through every node."""

    messages: list[dict] = field(default_factory=list)
    mode: str | None = None
    search_history: list[str] = field(default_factory=list)
    scratch: dict[str, Any] = field(default_factory=dict)
