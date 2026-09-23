from __future__ import annotations

from typing import Any

from .router import ModeRouter
from .tools.base import Tool


def build_graph(router: ModeRouter, tools: list[Tool]) -> Any:
    """Builds the agent graph: router -> mode subgraph -> tool loop ->
    guardrail -> response. Returns a compiled, runnable graph object.
    Kept framework-agnostic here; a reference implementation would compile
    this with a graph-orchestration library."""
    raise NotImplementedError
