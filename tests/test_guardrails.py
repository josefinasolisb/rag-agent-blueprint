from __future__ import annotations

import pytest

from rag_agent_blueprint.guardrails.degrade import DegradeReason, build_fallback_response


def test_build_fallback_response_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        build_fallback_response(DegradeReason.MISSING_CONTEXT)


@pytest.mark.skip(reason="GroundingValidator is abstract; needs a concrete implementation")
def test_grounding_validator_verify_and_correct():
    ...
