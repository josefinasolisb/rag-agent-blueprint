from __future__ import annotations

from typing import Any

from openai import OpenAI

from ...indexing.vector_store import VectorStore
from .base import Tool


class GenerateQuestionsTool(Tool):
    """Generates a fixed number of questions grounded in a document, using
    the same representative-fragment sample as SummarizeDocumentTool
    instead of reading the full document."""

    name = "generate_questions"
    description = "Generate a set of questions based on a document's content."

    def __init__(self, vector_store: VectorStore, llm_client: OpenAI, model: str):
        self._vector_store = vector_store
        self._llm_client = llm_client
        self._model = model

    def run(self, document_id: str, count: int = 10, **kwargs: Any) -> list[str]:
        raise NotImplementedError
