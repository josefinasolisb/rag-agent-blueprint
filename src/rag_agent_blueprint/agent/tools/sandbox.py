from __future__ import annotations

from typing import Any

from .base import Tool


class CodeSandboxTool(Tool):
    """Executes short, verifiable computations in an isolated runtime."""

    name = "execute_in_sandbox"
    description = "Runs a snippet of code in an isolated sandbox and returns its output."

    def run(self, code: str, **kwargs: Any) -> dict:
        raise NotImplementedError
