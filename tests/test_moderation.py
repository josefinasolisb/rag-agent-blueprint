from __future__ import annotations

import asyncio

import pytest

from rag_agent_blueprint.moderation.classifier import ContentClassifier
from rag_agent_blueprint.moderation.models import ClassificationSignals, ModerationStatus, ReviewRecord
from rag_agent_blueprint.moderation.rules import RuleEngine, RulePriority, SafetyRule
from rag_agent_blueprint.moderation.store import ModerationStore


def test_review_record_and_status_construct():
    record = ReviewRecord(
        document_id="doc-1",
        status=ModerationStatus.PENDING_REVIEW,
        quality_score=0.0,
        reason=None,
        reviewed_by_human=False,
        ruleset_version=1,
    )
    assert record.status is ModerationStatus.PENDING_REVIEW


def test_rule_engine_evaluate_raises_not_implemented():
    engine = RuleEngine(rules=[])
    with pytest.raises(NotImplementedError):
        engine.evaluate(signals=ClassificationSignals(signals={}), quality_score=0.5)


def test_safety_rule_sorts_ahead_of_quality_rules():
    assert RulePriority.SAFETY < RulePriority.QUALITY
    assert SafetyRule.priority is RulePriority.SAFETY


def test_safety_rule_matches_and_resolve_raise_not_implemented():
    rule = SafetyRule()
    with pytest.raises(NotImplementedError):
        rule.matches(signals=ClassificationSignals(signals={}), quality_score=0.0)
    with pytest.raises(NotImplementedError):
        rule.resolve()


def test_content_classifier_classify_raises_not_implemented():
    classifier = ContentClassifier(client=None, model="stub-classifier")
    with pytest.raises(NotImplementedError):
        classifier.classify("some document text")


def test_moderation_store_raises_not_implemented():
    store = ModerationStore(connection=None)
    with pytest.raises(NotImplementedError):
        asyncio.run(store.get("doc-1"))
