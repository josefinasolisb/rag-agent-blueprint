from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Tool(ABC):
    """Contract every agent tool implements, so the graph can invoke any
    of them uniformly regardless of what each one actually does."""

    name: str
    description: str

    @abstractmethod
    def run(self, **kwargs: Any) -> Any:
        raise NotImplementedError
