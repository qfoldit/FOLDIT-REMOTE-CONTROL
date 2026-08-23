# qFoldIT Human–AI Collective Search Event Contract

## Purpose

Define the canonical event boundary between a human player, an AI agent, a scientific
compute service and a validator.

## Event model

```text
Player / AI Agent
      ↓
Intent + Action
      ↓
Canonical Scientific State
      ↓
Scientific Compute
      ↓
Score / Validation
      ↓
Feedback
      ↓
Next Human or AI Action
```

## Required fields

- `mission_id`
- `scientific_object_id`
- `state_version`
- `actor_type`
- `actor_id`
- `action_type`
- `action_payload`
- `parent_state_id`
- `timestamp`
- `validator_id`
- `validator_version`
- `score`
- `acceptance_status`
- `evidence_reference`

## Actor types

```text
HUMAN
AI_AGENT
SYSTEM
VALIDATOR
```

## Design rule

This transport layer must never become the scientific source of truth. The canonical
scientific state and validator remain authoritative.

## Human–AI Collective Search

The event contract explicitly supports alternating and collaborative search:

```text
AI proposal → Human perturbation → Validation → AI reprioritization
```

This enables measurement of Human Amplification Factor and Strategic Search Diversity
without coupling scientific validity to gameplay presentation.

## License

Original qFoldIT material in this file is licensed under
`QFOLDIT-ADDITIONS-LICENSE.md`.
