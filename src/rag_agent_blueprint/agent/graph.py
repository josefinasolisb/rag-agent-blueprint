from __future__ import annotations

from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from langgraph.graph.state import CompiledStateGraph
from openai import OpenAI

from .router import ModeRouter
from .tools.base import Tool


def build_graph(
    router: ModeRouter,
    tools: list[Tool],
    llm_client: OpenAI,
    model: str,
    checkpointer: AsyncPostgresSaver,
) -> CompiledStateGraph:
    """Builds the agent graph with LangGraph: a `StateGraph` wires the
    router node, per-mode subgraphs (each an agent<->tools loop bound to
    `llm_client`, assembling its system content each turn as a stable
    prefix plus a per-turn suffix via `PromptBuilder` and
    `agent.prompts.caching.prepare_for_caching`), and the guardrail node,
    then compiles with an async Postgres checkpointer for conversation
    persistence."""
    raise NotImplementedError
