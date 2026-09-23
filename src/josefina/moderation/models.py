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


class RejectionReason(str, Enum):
    POLICY_VIOLATION = "policy_violation"
    LOW_QUALITY = "low_quality"
    DUPLICATE_CONTENT = "duplicate_content"
    OFF_TOPIC = "off_topic"


@dataclass
class ReviewRecord:
    document_id: str
    status: ModerationStatus
    quality_score: float
    rejection_reason: RejectionReason | None
    reviewed_by_human: bool
    ruleset_version: int
