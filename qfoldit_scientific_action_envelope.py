"""Canonical qFoldIT Scientific Action Envelope.

This is qFoldIT-original code. It does not reproduce the historical Foldit
Remote Control wire protocol; it defines a modern, engine-neutral event model
for Human–AI Collective Scientific Search.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from hashlib import sha256
import json
from typing import Any, Literal

ActorType = Literal["HUMAN", "AI_AGENT", "SYSTEM", "VALIDATOR"]


@dataclass(frozen=True)
class ScientificActionEnvelope:
    envelope_id: str
    mission_id: str
    session_id: str
    actor_type: ActorType
    actor_id: str
    scientific_object_id: str
    schema_version: str
    state_id: str
    parent_state_id: str | None
    action_type: str
    action_payload: dict[str, Any]
    runtime_id: str
    adapter_version: str
    timestamp: str
    validator_id: str | None = None
    validator_version: str | None = None
    acceptance_status: str | None = None
    score: float | None = None
    evidence_reference: str | None = None

    def canonical_dict(self) -> dict[str, Any]:
        return asdict(self)

    def canonical_json(self) -> str:
        return json.dumps(self.canonical_dict(), sort_keys=True, separators=(",", ":"))

    def content_hash(self) -> str:
        return sha256(self.canonical_json().encode("utf-8")).hexdigest()

    def validate(self) -> None:
        required = {
            "envelope_id": self.envelope_id,
            "mission_id": self.mission_id,
            "session_id": self.session_id,
            "actor_id": self.actor_id,
            "scientific_object_id": self.scientific_object_id,
            "schema_version": self.schema_version,
            "state_id": self.state_id,
            "action_type": self.action_type,
            "runtime_id": self.runtime_id,
            "adapter_version": self.adapter_version,
            "timestamp": self.timestamp,
        }
        missing = [key for key, value in required.items() if not value]
        if missing:
            raise ValueError(f"Missing required envelope fields: {', '.join(missing)}")
        if self.actor_type not in {"HUMAN", "AI_AGENT", "SYSTEM", "VALIDATOR"}:
            raise ValueError(f"Unsupported actor_type: {self.actor_type}")

    def to_dict(self) -> dict[str, Any]:
        self.validate()
        result = self.canonical_dict()
        result["content_hash"] = self.content_hash()
        return result
