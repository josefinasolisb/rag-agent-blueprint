from __future__ import annotations

import pytest

from rag_agent_blueprint.agent.graph import build_graph
from rag_agent_blueprint.agent.prompts import SystemPrompt
from rag_agent_blueprint.agent.prompts.caching import prepare_for_caching
from rag_agent_blueprint.agent.state import AgentState
from rag_agent_blueprint.agent.tools.document_fragment import GetDocumentFragmentTool
from rag_agent_blueprint.agent.tools.generate_questions import GenerateQuestionsTool
from rag_agent_blueprint.agent.tools.sandbox import CodeSandboxTool
from rag_agent_blueprint.agent.tools.search import DocumentSearchTool
from rag_agent_blueprint.agent.tools.search_within_document import SearchWithinDocumentTool
from rag_agent_blueprint.agent.tools.summarize import SummarizeDocumentTool


def test_agent_state_constructs_with_defaults():
    state = AgentState()
    assert state.messages == []
    assert state.mode is None


def test_document_search_tool_run_raises_not_implemented():
    tool = DocumentSearchTool(embedder=None, vector_store=None)
    with pytest.raises(NotImplementedError):
        tool.run(query="anything")


def test_get_document_fragment_tool_run_raises_not_implemented():
    tool = GetDocumentFragmentTool(vector_store=None)
    with pytest.raises(NotImplementedError):
        tool.run(document_id="doc-1", fragment_index=0)


def test_search_within_document_tool_run_raises_not_implemented():
    tool = SearchWithinDocumentTool(embedder=None, vector_store=None)
    with pytest.raises(NotImplementedError):
        tool.run(document_id="doc-1", query="anything")


def test_summarize_document_tool_run_raises_not_implemented():
    tool = SummarizeDocumentTool(vector_store=None, llm_client=None, model="stub-model")
    with pytest.raises(NotImplementedError):
        tool.run(document_id="doc-1")


def test_generate_questions_tool_run_raises_not_implemented():
    tool = GenerateQuestionsTool(vector_store=None, llm_client=None, model="stub-model")
    with pytest.raises(NotImplementedError):
        tool.run(document_id="doc-1", count=10)


def test_code_sandbox_tool_run_raises_not_implemented():
    tool = CodeSandboxTool()
    with pytest.raises(NotImplementedError):
        tool.run(code="print('hi')")


def test_build_graph_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        build_graph(router=None, tools=[], llm_client=None, model="stub-model", checkpointer=None)


def test_system_prompt_constructs():
    prompt = SystemPrompt(stable_prefix="identity + rules", per_turn_suffix="turn context")
    assert prompt.stable_prefix == "identity + rules"


def test_prepare_for_caching_raises_not_implemented():
    prompt = SystemPrompt(stable_prefix="identity + rules", per_turn_suffix="turn context")
    with pytest.raises(NotImplementedError):
        prepare_for_caching(prompt)


@pytest.mark.skip(reason="ModeRouter is abstract; needs a concrete implementation")
def test_mode_router_route():
    ...


@pytest.mark.skip(reason="PromptBuilder is abstract; needs a concrete implementation")
def test_prompt_builder_build():
    ...
