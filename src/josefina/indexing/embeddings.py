from __future__ import annotations

from abc import ABC, abstractmethod


class EmbeddingModel(ABC):
    """Pluggable embedding backend. A reference deployment might combine a
    self-hosted general-purpose model with an optional higher-quality
    provider reserved for priority content."""

    dimensions: int

    @abstractmethod
    def embed(self, texts: list[str]) -> list[list[float]]:
        raise NotImplementedError
