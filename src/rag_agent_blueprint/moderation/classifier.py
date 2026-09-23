from __future__ import annotations

from openai import OpenAI

from .models import ClassificationSignals


class ContentClassifier:
    """Content classifier backed by structured-output chat completions
    against any OpenAI-compatible API (OpenAI itself, or a self-hosted /
    third-party server implementing the same endpoint)."""

    def __init__(self, client: OpenAI, model: str):
        self._client = client
        self._model = model

    def classify(self, text: str) -> ClassificationSignals:
        raise NotImplementedError
