from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ExtractionResult:
    text: str
    quality_score: float
    extractor_name: str
    used_fallback: bool = False


class Extractor(ABC):
    """Contract for a single-format text extractor in the ingestion chain."""

    @abstractmethod
    def can_handle(self, filename: str, content_type: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def extract(self, raw_bytes: bytes) -> ExtractionResult:
        raise NotImplementedError
