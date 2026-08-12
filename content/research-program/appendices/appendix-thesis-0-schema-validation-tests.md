---
title: "Appendix: Thesis 0 Schema Validation Tests"
summary: "A proposed evaluation contract in the Consullo public research program: Appendix: Thesis 0 Schema Validation Tests."
status: "proposed extension"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-002"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["A benchmark specification is not a benchmark result.", "No implementation or outcome evidence is supplied by this page."]
---
# Appendix: Thesis 0 Schema Validation Tests

Version: 0.1

Status: pre-drafting validation plan. Evidence Status: Documented/Proposed.

This appendix defines the minimum schema-validation checks required before the Friendship-Governed Goal Architecture thesis body treats its goal-governance artifacts as operational constraints.

## Validator

Use a JSON Schema 2020-12 validator. Acceptable validators include `python-jsonschema` with Draft 2020-12 support or `ajv` configured for draft 2020-12. Basic JSON syntax checks with `python -m json.tool` are necessary but not sufficient.

Current validation command:

```bash
python the internal planning-cascade artifacts
```

## Expected-Pass Checks

| Instance | Schema | Expected result |
| --- | --- | --- |
| `planning-cascade-execution/friendship-goal-registry.json` | `planning-cascade-execution/schemas/friendship_goal_registry.schema.json` | pass |
| `planning-cascade-execution/plans/seed-ai-organizational-rsi.thesis-goal-anchor.json` | `planning-cascade-execution/schemas/seed_ai_thesis_goal_anchor.schema.json` | pass |
| `planning-cascade-execution/tests/cases/valid_goal_stack_snapshot.json` | `planning-cascade-execution/schemas/goal_stack_snapshot.schema.json` | pass |
| `planning-cascade-execution/tests/cases/valid_goal_system.json` | `planning-cascade-execution/schemas/seed_ai_thesis_goal_anchor.schema.json` | pass |
| `planning-cascade-execution/tests/cases/valid_goal_strategic.json` | `planning-cascade-execution/schemas/seed_ai_thesis_goal_anchor.schema.json` | pass |
| `planning-cascade-execution/tests/cases/valid_goal_campaign.json` | `planning-cascade-execution/schemas/seed_ai_thesis_goal_anchor.schema.json` | pass |
| `planning-cascade-execution/tests/cases/valid_goal_operational.json` | `planning-cascade-execution/schemas/seed_ai_thesis_goal_anchor.schema.json` | pass |
| `planning-cascade-execution/tests/cases/valid_goal_mission.json` | `planning-cascade-execution/schemas/seed_ai_thesis_goal_anchor.schema.json` | pass |
| `planning-cascade-execution/tests/cases/valid_goal_task.json` | `planning-cascade-execution/schemas/seed_ai_thesis_goal_anchor.schema.json` | pass |
| `planning-cascade-execution/tests/cases/valid_goal_method.json` | `planning-cascade-execution/schemas/seed_ai_thesis_goal_anchor.schema.json` | pass |

## Semantic Checks Beyond JSON Schema

JSON Schema cannot enforce cross-document references. The validation pass must also check:

- every `friendship_goal_node` exists in `friendship-goal-registry.json`
- every `friendship_root_path` entry exists in `friendship-goal-registry.json`
- every non-`thesis_anchor` goal has at least one parent goal and no cycle in the reachable goal DAG
- `friendship_root_path` is interpreted as a primary-first multi-root set, not as a strict tree path
- `goal_stack_snapshot.fingerprint` is the SHA-256 hash of the canonical serialization of required thin-pointer fields before live ledger use; fixtures may use `pending-owner-attested-hash`
- `review_history_refs` is non-empty before an `owner_approved` goal with `independent_review_required: true` is treated as active
- lower-horizon plans cannot aggregate below the `ThesisBackingRequired(plan)` threshold to avoid thesis backing

## Expected-Fail Fixtures To Add

The validator now includes negative fixtures for:

- `invalid_goal_unregistered_friendship_node.json`: semantic failure for unregistered `friendship_goal_node`.
- `invalid_goal_nonroot_without_parent.json`: schema failure for non-root `goal_class` without `parent_goals`.
- `invalid_goal_owner_approved_missing_authority.json`: schema failure for `owner_approved` without `authority_matrix`.
- `invalid_goal_owner_approved_empty_review.json`: schema failure for `owner_approved` with `independent_review_required: true` and empty `review_history_refs`.
- `invalid_goal_stack_snapshot_bad_fingerprint.json`: semantic failure for snapshot fingerprint mismatch.
- `invalid_goal_stack_snapshot_computed_mismatch.json`: semantic failure for production-style computed snapshot fingerprint mismatch.
- `invalid_goal_benchmark_modification_without_owner_review.json`: semantic failure for benchmark modification without owner review.
- `invalid_goal_governance_self_weakening_single_lane_review.json`: semantic failure for protected goal-governance change reviewed only by the author lane.
- `invalid_goal_multi_parent_asymmetric_authority.json`: semantic failure for a multi-parent high-risk goal adopting only the weaker authority path.
- `invalid_goal_revision_missing_lineage.json`: semantic failure for a revised goal without `revision_lineage`.
- `invalid_goal_friendship_registry_mod_without_protection.json`: semantic failure for registry modification without protected-change record.
- `invalid_goal_dag_self_cycle.json`: semantic failure for direct goal-DAG self-cycle.
- `invalid_goal_aggregate_child_plan_backing_bypass.json`: semantic failure for aggregate child-plan decomposition that bypasses `ThesisBackingRequired(plan)`.
- `invalid_goal_stack_snapshot_expired_intention.json`: semantic failure for active intention continuation after plan expiry.
- `invalid_goal_stack_snapshot_stale_campaign_child_intention.json`: semantic failure for child intention continuation under a stale campaign.
- `invalid_strategic_thesis_backing_without_snapshot.json`: semantic failure for planner object claiming thesis backing without required `goal_stack_snapshot`.

## Drafting Gate

Before `friendship-governed-goal-architecture-thesis.md` relies on a worked example as operational evidence, the example's JSON artifacts must either pass this validation plan or be explicitly marked as a prose-only example with a migration task.
