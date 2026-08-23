from qfoldit_scientific_action_envelope import ScientificActionEnvelope


def test_envelope_is_deterministically_hashable() -> None:
    event = ScientificActionEnvelope(
        envelope_id="e-1",
        mission_id="m-1",
        session_id="s-1",
        actor_type="HUMAN",
        actor_id="player-1",
        scientific_object_id="object-1",
        schema_version="1.0",
        state_id="state-2",
        parent_state_id="state-1",
        action_type="rotate",
        action_payload={"axis": "z", "degrees": 15},
        runtime_id="uefn",
        adapter_version="1.0",
        timestamp="2026-08-23T16:00:00Z",
    )
    assert len(event.content_hash()) == 64
    assert event.to_dict()["content_hash"] == event.content_hash()
