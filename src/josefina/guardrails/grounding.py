from __future__ import annotations

from abc import ABC, abstractmethod


class GroundingValidator(ABC):
    """Deterministic, post-generation check: extracts a verified vocabulary
    of entities from actual tool outputs and rewrites only the claims in
    the model's response that are proven false by that data. Never deletes
    or invents content it cannot verify."""

    @abstractmethod
    def verify_and_correct(self, response_text: str, tool_outputs: list[dict]) -> str:
        raise NotImplementedError
