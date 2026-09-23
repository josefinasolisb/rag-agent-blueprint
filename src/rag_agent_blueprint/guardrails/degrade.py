from __future__ import annotations

from enum import Enum


class DegradeReason(str, Enum):
    ROUTER_FAILURE = "router_failure"
    MISSING_CONTEXT = "missing_context"
    TOOL_SCHEMA_ERROR = "tool_schema_error"
    UNSUPPORTED_REQUEST = "unsupported_request"


def build_fallback_response(reason: DegradeReason) -> str:
    """Returns a predefined, honest fallback message for a closed set of
    known failure modes instead of letting the model improvise."""
    raise NotImplementedError
