---
title: "Friendship-Governed Goal Architecture (Thesis 0) Cross-Reference Map"
summary: "A bounded component of the Consullo public research program: Friendship-Governed Goal Architecture (Thesis 0) Cross-Reference Map."
status: "proposed extension"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-001"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["Publication does not establish implementation or operational effectiveness.", "The implementation-evidence appendix records component evidence only and is not evidence of operational capability for this page."]
---
# Friendship-Governed Goal Architecture (Thesis 0) Cross-Reference Map

Version: 0.1

Status: pre-drafting drift-control map. Evidence Status: Documented/Proposed.

This map binds Thesis 0 invariants to schemas, ledger record types, worked examples, and owning files. It is intended to prevent a 50,000+ word thesis body from drifting away from operational artifacts.

| Invariant | Canonical statement | Schema or validator hook | Ledger record hooks | Worked-example hooks | Fixture hooks |
| --- | --- | --- | --- | --- | --- |
| T0-I1 | Governed goals are not planner objectives. | `seed_ai_thesis_goal_anchor.schema.json`, `goal_class`; planning bridge Required Fields | `governed_goal_proposal`, `goal_classification`, `goal_anchor_decision` | WE-T0-M1, WE-T0-M6 | `valid_goal_system.json`; `valid_goal_strategic.json`; `seed-ai-organizational-rsi.thesis-goal-anchor.json` |
| T0-I2 | Every active non-root goal requires Friendship ancestry. | `friendship_goal_registry.schema.json`; `friendship-goal-registry.json`; `validate_planning_schemas.py` semantic root checks | `friendship_root_anchoring_decision`, `goal_ancestry_decision` | WE-T0-M2, WE-T0-E2E1 | `invalid_goal_unregistered_friendship_node.json`; `invalid_goal_nonroot_without_parent.json`; `invalid_goal_dag_self_cycle.json` |
| T0-I3 | ThesisBackingRequired for high-impact plans. | planning bridge mandatory-mediation paragraph; plan-schema backing checks | `planner_inheritance_decision`, `plan_object_lifecycle`, `goal_stack_snapshot` | WE-T0-M6, WE-T0-E2E2 | `invalid_strategic_thesis_backing_without_snapshot.json`; `invalid_goal_aggregate_child_plan_backing_bypass.json`; `valid_campaign_with_backing.json` |
| T0-I4 | Goal authority powers are distinct. | `seed_ai_thesis_goal_anchor.schema.json`, `authority_matrix`; risk-class cooling-window table in `friendship-governed-goal-architecture-thesis.md` Section 10 | `governed_goal_adoption_decision`, `human_authority_decision` | WE-T0-M4 | `valid_goal_owner_approved.json`; `invalid_goal_owner_approved_missing_authority.json`; `invalid_goal_owner_approved_empty_review.json` |
| T0-I5 | Goal preservation cannot outrank correction. | `allowed_interventions`; `corrigibility_requirements`; planning bridge Authority Rules | `governed_goal_veto_decision`, `governed_goal_suspension`, `alignment_review` | WE-T0-M5, WE-T0-IG3 | `invalid_goal_governance_self_weakening_single_lane_review.json`; `invalid_goal_stack_snapshot_expired_intention.json` |
| T0-I6 | Suspicious instrumental goals require quarantine. | `instrumental_goal_classification`; lifecycle conditional requirements | `instrumental_goal_classification`, `governed_goal_veto_decision` | WE-T0-M9, WE-T0-IG1 through WE-T0-IG10 | `invalid_goal_benchmark_modification_without_owner_review.json`; `invalid_goal_governance_self_weakening_single_lane_review.json`; `invalid_goal_aggregate_child_plan_backing_bypass.json` |
| T0-I7 | Goal-governance modifications are protected changes. | protected artifact fields; planning bridge Authority Rules | `goal_governance_modification_decision`, `ledger_modification_decision`, `benchmark_modification_decision` | WE-T0-M8, WE-T0-M11 | `invalid_goal_governance_self_weakening_single_lane_review.json`; `invalid_goal_friendship_registry_mod_without_protection.json` |
| T0-I8 | Goal-stack snapshots are required for high-impact actions. | `goal_stack_snapshot.schema.json`; `valid_goal_stack_snapshot.json` fixture | `goal_stack_snapshot`, `planner_inheritance_decision` | WE-T0-M10, WE-T0-E2E1 | `valid_goal_stack_snapshot.json`; `valid_goal_stack_snapshot_computed.json`; `invalid_strategic_thesis_backing_without_snapshot.json` |
| T0-I9 | Goal revision preserves lineage. | `revision_lineage`; semantic check for missing lineage | `governed_goal_revision` | WE-T0-IG3 | `invalid_goal_revision_missing_lineage.json` |
| T0-I10 | Active intention persistence is bounded by plan lifetime. | `expiration_triggers`; plan freshness rules; active-intention snapshot checks | `governed_goal_suspension`, `governed_goal_retirement`, `plan_object_lifecycle` | WE-T0-E2E3, WE-T0-E2E4 | `invalid_goal_stack_snapshot_expired_intention.json`; `invalid_goal_stack_snapshot_stale_campaign_child_intention.json` |
| T0-I11 | Goal aggregation cannot bypass ThesisBackingRequired. | planning bridge aggregation rule; semantic aggregate-bypass check | `planner_inheritance_decision`, `goal_classification` | WE-T0-E2E2 | `invalid_goal_aggregate_child_plan_backing_bypass.json` |
| T0-I12 | Inherited constraints tighten, never loosen. | planning bridge stop-condition propagation; existing negative case `operation_with_loosened_constraint.json` | `planner_inheritance_decision`, `plan_object_lifecycle` | WE-T0-M7 | `operation_with_loosened_constraint.json` |
| T0-I13 | Frontier-model-proposed goal-governance edits are untrusted. | planning bridge Authority Rules; self-weakening semantic check | `goal_governance_modification_decision`, `human_authority_decision` | WE-T0-M11 | `invalid_goal_governance_self_weakening_single_lane_review.json` |
| T0-I14 | Goal-stack snapshots are append-only. | `goal_stack_snapshot.schema.json`, `fingerprint`, `supersedes`, `redaction_policy`; validation plan fingerprint check | `goal_stack_snapshot`, `incident_report` | WE-T0-M10 | `invalid_goal_stack_snapshot_bad_fingerprint.json`; `invalid_goal_stack_snapshot_computed_mismatch.json`; `valid_goal_stack_snapshot_computed.json` |
| T0-I15 | Friendship registry modifications are goal-governance modifications. | `friendship_goal_registry.schema.json`, `archived_nodes`; registry rules | `goal_governance_modification_decision` with `subject_type: friendship_registry` | WE-T0-M8, WE-T0-M11 | `invalid_goal_friendship_registry_mod_without_protection.json`; `friendship-goal-registry.json` |

## Canonical Ownership

- Goal vocabulary and stable invariants: `00-vocabulary-and-invariants.md`
- Pre-drafting scope and execution order: `00-friendship-governed-goal-architecture-revision-plan.md`
- Friendship root identifiers: `planning-cascade-execution/friendship-goal-registry.json`
- Registry prose semantics: `planning-cascade-execution/friendship-goal-registry.md`
- Goal anchor/governed-goal schema: `planning-cascade-execution/schemas/seed_ai_thesis_goal_anchor.schema.json`
- Goal-stack snapshot schema: `planning-cascade-execution/schemas/goal_stack_snapshot.schema.json`
- Planning cascade compiler rules: `planning-cascade-execution/seed-ai-planning-cascade-execution-bridge.md`
- Evidence-ledger record semantics: `appendix-evidence-ledger-schema.md`
- Validation checks and fixtures: `planning-cascade-execution/tests/validate_planning_schemas.py` and `planning-cascade-execution/tests/cases/`
- Worked-example checklist: `thesis-0-worked-examples-inventory.md`

## Improvement-Request Enforcement Hooks

The extracted Thesis 0 improvement requests are not evidence that any existing agent has changed. They are planning-level enforcement hooks that identify which existing agents must be modified before their behavior can be treated as aligned with the execution plan. The canonical request files live under `planning-cascade-execution/improvement-requests/`; the sidecar mapping is `planning-cascade-execution/improvement-requests/thesis-0-improvement-request-traceability.json`; validation is enforced by `planning-cascade-execution/tests/validate_thesis0_improvement_requests.py`.

| Invariant | Existing-agent improvement-request hooks |
| --- | --- |
| T0-I1 | `T0-AIR-EXISTING-STRATEGIC-PLANNER-001`; `T0-AIR-EXISTING-AUTONOMOUS-GOAL-GENERATOR-001`; `T0-AIR-EXISTING-DYNAMIC-PRIORITIZER-001`; `T0-AIR-EXISTING-GOAL-FORMATION-ARCHITECT-001`; `T0-AIR-EXISTING-ABUNDANCE-DISTRIBUTION-MONITOR-001`; `T0-AIR-EXISTING-AGENT-IMPROVEMENT-GOAL-SETTER-001` |
| T0-I2 | `T0-AIR-EXISTING-AUTONOMOUS-GOAL-GENERATOR-001`; `T0-AIR-EXISTING-GOAL-FORMATION-ARCHITECT-001`; `T0-AIR-EXISTING-FRIENDSHIP-ANCHOR-AGENT-001`; `T0-AIR-EXISTING-ADVERSARIAL-ALIGNMENT-ORCHESTRATOR-001`; `T0-AIR-EXISTING-ABUNDANCE-DISTRIBUTION-MONITOR-001` |
| T0-I3 | `T0-AIR-EXISTING-STRATEGIC-PLANNER-001`; `T0-AIR-EXISTING-CAMPAIGN-PLANNER-001`; `T0-AIR-EXISTING-OPERATIONAL-PLANNER-001`; `T0-AIR-EXISTING-SELF-IMPROVEMENT-ORCHESTRATOR-001`; `T0-AIR-EXISTING-AGENT-BUILDER-001`; `T0-AIR-EXISTING-SUBGOAL-DECOMPOSITION-PLANNER-001`; `T0-AIR-EXISTING-HTN-PLANNER-ORCHESTRATOR-001`; `T0-AIR-EXISTING-ABUNDANCE-DISTRIBUTION-MONITOR-001`; `T0-AIR-EXISTING-AGENT-IMPROVEMENT-GOAL-SETTER-001`; `T0-AIR-EXISTING-CHIEF-ORCHESTRATOR-001` |
| T0-I4 | `T0-AIR-EXISTING-AUTONOMOUS-GOAL-GENERATOR-001`; `T0-AIR-EXISTING-DYNAMIC-PRIORITIZER-001`; `T0-AIR-EXISTING-GOAL-FORMATION-ARCHITECT-001`; `T0-AIR-EXISTING-FRIENDSHIP-ANCHOR-AGENT-001`; `T0-AIR-EXISTING-ABUNDANCE-DISTRIBUTION-MONITOR-001`; `T0-AIR-EXISTING-CHIEF-ORCHESTRATOR-001` |
| T0-I5 | `T0-AIR-EXISTING-TASK-EXECUTOR-001`; `T0-AIR-EXISTING-AUTONOMOUS-EXECUTOR-001`; `T0-AIR-EXISTING-COURSE-CORRECTOR-001`; `T0-AIR-EXISTING-FRIENDSHIP-ANCHOR-AGENT-001`; `T0-AIR-EXISTING-ADVERSARIAL-ALIGNMENT-ORCHESTRATOR-001`; `T0-AIR-EXISTING-ABUNDANCE-DISTRIBUTION-MONITOR-001` |
| T0-I6 | `T0-AIR-EXISTING-AUTONOMOUS-GOAL-GENERATOR-001`; `T0-AIR-EXISTING-SELF-IMPROVEMENT-ORCHESTRATOR-001`; `T0-AIR-EXISTING-AGENT-BUILDER-001`; `T0-AIR-EXISTING-GOAL-FORMATION-ARCHITECT-001`; `T0-AIR-EXISTING-AGENT-IMPROVEMENT-GOAL-SETTER-001` |
| T0-I7 | `T0-AIR-EXISTING-OPERATIONAL-PLANNER-001`; `T0-AIR-EXISTING-COURSE-CORRECTOR-001`; `T0-AIR-EXISTING-SELF-IMPROVEMENT-ORCHESTRATOR-001`; `T0-AIR-EXISTING-AGENT-BUILDER-001`; `T0-AIR-EXISTING-AGENT-GITHUB-REPOSITORY-MANAGER-001`; `T0-AIR-EXISTING-HTN-PLANNER-ORCHESTRATOR-001`; `T0-AIR-EXISTING-FRIENDSHIP-ANCHOR-AGENT-001`; `T0-AIR-EXISTING-ADVERSARIAL-ALIGNMENT-ORCHESTRATOR-001`; `T0-AIR-EXISTING-CHIEF-ORCHESTRATOR-001` |
| T0-I8 | `T0-AIR-EXISTING-STRATEGIC-PLANNER-001`; `T0-AIR-EXISTING-CAMPAIGN-PLANNER-001`; `T0-AIR-EXISTING-OPERATIONAL-PLANNER-001`; `T0-AIR-EXISTING-MISSION-PLANNER-001`; `T0-AIR-EXISTING-TASK-EXECUTOR-001`; `T0-AIR-EXISTING-AUTONOMOUS-EXECUTOR-001`; `T0-AIR-EXISTING-DYNAMIC-PRIORITIZER-001`; `T0-AIR-EXISTING-HTN-PLANNER-ORCHESTRATOR-001` |
| T0-I9 | `T0-AIR-EXISTING-COURSE-CORRECTOR-001`; `T0-AIR-EXISTING-SELF-IMPROVEMENT-ORCHESTRATOR-001`; `T0-AIR-EXISTING-AGENT-IMPROVEMENT-GOAL-SETTER-001` |
| T0-I10 | `T0-AIR-EXISTING-CAMPAIGN-PLANNER-001`; `T0-AIR-EXISTING-MISSION-PLANNER-001`; `T0-AIR-EXISTING-TASK-EXECUTOR-001`; `T0-AIR-EXISTING-AUTONOMOUS-EXECUTOR-001` |
| T0-I11 | `T0-AIR-EXISTING-STRATEGIC-PLANNER-001`; `T0-AIR-EXISTING-CAMPAIGN-PLANNER-001`; `T0-AIR-EXISTING-SUBGOAL-DECOMPOSITION-PLANNER-001`; `T0-AIR-EXISTING-HTN-PLANNER-ORCHESTRATOR-001`; `T0-AIR-EXISTING-CHIEF-ORCHESTRATOR-001` |
| T0-I12 | `T0-AIR-EXISTING-STRATEGIC-PLANNER-001`; `T0-AIR-EXISTING-CAMPAIGN-PLANNER-001`; `T0-AIR-EXISTING-OPERATIONAL-PLANNER-001`; `T0-AIR-EXISTING-MISSION-PLANNER-001`; `T0-AIR-EXISTING-TASK-EXECUTOR-001`; `T0-AIR-EXISTING-DYNAMIC-PRIORITIZER-001`; `T0-AIR-EXISTING-SUBGOAL-DECOMPOSITION-PLANNER-001`; `T0-AIR-EXISTING-HTN-PLANNER-ORCHESTRATOR-001`; `T0-AIR-EXISTING-CHIEF-ORCHESTRATOR-001` |
| T0-I13 | `T0-AIR-EXISTING-SELF-IMPROVEMENT-ORCHESTRATOR-001`; `T0-AIR-EXISTING-AGENT-BUILDER-001`; `T0-AIR-EXISTING-AGENT-GITHUB-REPOSITORY-MANAGER-001`; `T0-AIR-EXISTING-FRIENDSHIP-ANCHOR-AGENT-001`; `T0-AIR-EXISTING-ADVERSARIAL-ALIGNMENT-ORCHESTRATOR-001` |
| T0-I14 | `T0-AIR-EXISTING-MISSION-PLANNER-001`; `T0-AIR-EXISTING-AUTONOMOUS-EXECUTOR-001`; `T0-AIR-EXISTING-AGENT-GITHUB-REPOSITORY-MANAGER-001` |
| T0-I15 | `T0-AIR-EXISTING-COURSE-CORRECTOR-001`; `T0-AIR-EXISTING-SELF-IMPROVEMENT-ORCHESTRATOR-001`; `T0-AIR-EXISTING-AGENT-GITHUB-REPOSITORY-MANAGER-001`; `T0-AIR-EXISTING-FRIENDSHIP-ANCHOR-AGENT-001`; `T0-AIR-EXISTING-ADVERSARIAL-ALIGNMENT-ORCHESTRATOR-001` |

## Drafting Rule

The Thesis 0 body should cite this map for drift control. If a body section introduces a new invariant, schema field, ledger record, or worked example, this map should be updated in the same pass.
