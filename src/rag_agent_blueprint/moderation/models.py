"""Data containers for moderation outcomes: statuses, reasons, and the
review record produced by a RuleEngine evaluation."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ModerationStatus(str, Enum):
    PENDING_REVIEW = "pending_review"
    APPROVED = "approved"
    APPROVED_LOW_CONFIDENCE = "approved_low_confidence"
    MANUAL_REVIEW = "manual_review"
    SUSPENDED = "suspended"
    REJECTED = "rejected"


class ModerationReason(str, Enum):
    """Explains a `ModerationStatus` that isn't a plain approval — used for
    both `SUSPENDED` and `REJECTED`, not rejections alone."""

    POLICY_VIOLATION = "policy_violation"
    LOW_QUALITY = "low_quality"
    DUPLICATE_CONTENT = "duplicate_content"
    OFF_TOPIC = "off_topic"


@dataclass
class ClassificationSignals:
    """Category -> confidence output of a `ContentClassifier`, consumed by
    `ModerationRule`/`RuleEngine` — typed so the contract between the two
    is visible in the signature instead of hidden inside an untyped dict."""

    signals: dict[str, float]


@dataclass
class RuleOutcome:
    """What a single `ModerationRule` decided: the resulting status and,
    when applicable, why — feeds directly into `ReviewRecord.reason`."""

    status: ModerationStatus
    reason: ModerationReason | None = None


@dataclass
class ReviewRecord:
    document_id: str
    status: ModerationStatus
    quality_score: float
    reason: ModerationReason | None
    reviewed_by_human: bool
    ruleset_version: int
