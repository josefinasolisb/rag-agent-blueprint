from __future__ import annotations

from openai import OpenAI


class EmbeddingClient:
    """Wraps an OpenAI-compatible API client to call an embedding model
    (OpenAI itself, or a self-hosted / third-party server implementing the
    same endpoint) — the `base_url` on `client` is what actually selects
    the backend. Named `Client`, not `Model`: this class doesn't embed
    anything itself, it calls a model that does."""

    def __init__(self, client: OpenAI, model: str, dimensions: int):
        self._client = client
        self._model = model
        self.dimensions = dimensions

    def embed(self, texts: list[str]) -> list[list[float]]:
        raise NotImplementedError
