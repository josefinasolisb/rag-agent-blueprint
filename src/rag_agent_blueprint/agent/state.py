from __future__ import annotations

from dataclasses import dataclass, field
from typing import Annotated, Any

from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages


@dataclass
class AgentState:
    """Shared LangGraph state threaded through every node. `messages` uses
    LangGraph's `add_messages` reducer so nodes can return new messages
    without manually merging them into the existing history."""

    messages: Annotated[list[AnyMessage], add_messages] = field(default_factory=list)
    mode: str | None = None
    search_history: list[str] = field(default_factory=list)
    scratch: dict[str, Any] = field(default_factory=dict)
