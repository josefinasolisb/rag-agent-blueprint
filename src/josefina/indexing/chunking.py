from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Chunk:
    text: str
    index: int
    token_count: int


class Chunker(ABC):
    """Splits full document text into retrieval-sized chunks."""

    @abstractmethod
    def split(self, text: str) -> list[Chunk]:
        raise NotImplementedError


class RecursiveTokenChunker(Chunker):
    """Recursively splits on a separator hierarchy, bounded by token count
    rather than raw character length."""

    def __init__(self, max_tokens: int = 512, overlap_tokens: int = 0):
        self._max_tokens = max_tokens
        self._overlap_tokens = overlap_tokens

    def split(self, text: str) -> list[Chunk]:
        raise NotImplementedError
