from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

import tiktoken


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
    (via tiktoken's `cl100k_base` encoding) rather than raw character
    length — the same encoding the OpenAI-compatible chat/embedding APIs
    use, so chunk sizes line up with the model's actual context budget."""

    def __init__(self, max_tokens: int = 512, overlap_tokens: int = 0, encoding_name: str = "cl100k_base"):
        self._max_tokens = max_tokens
        self._overlap_tokens = overlap_tokens
        self._encoding = tiktoken.get_encoding(encoding_name)

    def split(self, text: str) -> list[Chunk]:
        raise NotImplementedError
