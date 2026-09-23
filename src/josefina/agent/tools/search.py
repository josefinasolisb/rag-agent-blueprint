from __future__ import annotations

from typing import Any

from .base import Tool


class DocumentSearchTool(Tool):
    """Retrieves relevant chunks from the vector store for grounding."""

    name = "search_documents"
    description = "Semantic search over the indexed document collection."

    def run(self, query: str, top_k: int = 5, **kwargs: Any) -> list[dict]:
        raise NotImplementedError
