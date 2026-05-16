from datetime import UTC, datetime
from enum import StrEnum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field, field_validator


class Severity(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class RuntimeStatus(StrEnum):
    NOMINAL = "nominal"
    DEGRADED = "degraded"
    CRITICAL = "critical"


class RuntimeContext(BaseModel):
    frames_processed: int = 0
    latency_ms: float = 0.0
    queue_depth: int = 0
    dropped_frames: int = 0
    gpu_memory_pressure: float = 0.0
    thermal_pressure: float = 0.0
    runtime_status: RuntimeStatus = RuntimeStatus.NOMINAL
    notes: list[str] = Field(default_factory=list)


class Evidence(BaseModel):
    frame_hash: str
    source_uri: str
    adapter_name: str
    model_version: str
    rule_version: str
    captured_at: datetime
    telemetry_snapshot: dict[str, Any] = Field(default_factory=dict)
    detections: list[dict[str, Any]] = Field(default_factory=list)


class SafetyEvent(BaseModel):
    event_id: str = Field(default_factory=lambda: str(uuid4()))
    camera_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))
    rule_id: str
    severity: Severity
    confidence: float = Field(ge=0.0, le=1.0)
    human_review_required: bool
    runtime_context: RuntimeContext = Field(default_factory=RuntimeContext)
    evidence: Evidence
    summary: str
    incident_id: str | None = None

    @field_validator("incident_id", mode="before")
    @classmethod
    def empty_incident_is_none(cls, value: str | None) -> str | None:
        if value == "":
            return None
        return value


class Incident(BaseModel):
    incident_id: str
    camera_id: str
    opened_at: datetime
    updated_at: datetime
    highest_severity: Severity
    status: str = "open"
    event_ids: list[str] = Field(default_factory=list)
    timeline: list[SafetyEvent] = Field(default_factory=list)
