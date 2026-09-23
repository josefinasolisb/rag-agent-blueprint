from __future__ import annotations

from . import SystemPrompt


def prepare_for_caching(prompt: SystemPrompt) -> list[dict]:
    """Splits the request's system content into a stable prefix and a
    per-turn suffix, in that order, so the prefix stays reusable across
    turns instead of being reprocessed on every call.

    Prompt caching, where a provider supports it, works by matching an
    exact prefix -- any change earlier in that prefix invalidates
    everything cached after it. Keeping the per-turn suffix strictly
    after the stable prefix, never mixed into it, is what keeps the
    prefix reusable."""
    # A second cacheable boundary placed after the per-turn suffix rarely
    # helps: once that suffix changes (most turns), everything after it
    # becomes a new prefix too, so it never gets reused either.
    raise NotImplementedError
