---
title: "Appendix: Evidence Ledger Schema"
summary: "A bounded component of the Consullo public research program: Appendix: Evidence Ledger Schema."
status: "specified but not implemented"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-001"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["Publication does not establish implementation or operational effectiveness.", "The withheld implementation-evidence appendix is not evidence for this page."]
---
# Appendix: Evidence Ledger Schema

Version: 0.1 (2026-04-23)

This appendix specifies the canonical evidence-ledger schema for the five-thesis suite. It is a design contract, not an implemented database. Capability Status: specified. Evidence Status: Documented/Proposed.

The ledger exists to make improvement, trust, alignment, incident, benchmark, and provenance evidence replayable. It should prevent later drafts or implementations from treating "evidence preserved" as a narrative promise without a record structure.

## Ledger Principles

- Append-only or audit-preserving: records may be superseded, annotated, or redacted under policy, but not silently deleted.
- Cross-view by design: the same record may appear in multiple indexed views; implementation evidence is a query profile over the canonical views, not an additional master view.
- Scope before confidence: every record must name the actor, authority scope, system scope, and decision or claim it supports.
- Provenance is required: accepted modifications and high-stakes actions must link source artifacts, evaluator or validator identities, generated artifacts, deployment stage, and post-deployment outcome where applicable.
- Dissent is preserved: AAF objections, owner overrides, and human-authority dispositions are ledger records, not comments lost in prose.
- Rollback annotates history: rollback or mitigation creates records that supersede or constrain earlier records without erasing them.
- Cost and side effects are evidence: accepted improvement records must preserve cost/benefit, side-effect checks, and protected-set non-regression status.
- Unknown scope fails closed: missing actor, authority, provenance, deployment stage, or trust scope should prevent promotion to accepted state for high-stakes records.

## Canonical Record Envelope

Every ledger record should include the following envelope. Physical implementations may add fields, but should not omit these fields without documenting the omission.

| Field | Meaning |
| --- | --- |
| `ledger_record_id` | Stable unique identifier. |
| `schema_version` | Evidence-ledger schema version used by the record. |
| `record_type` | One of the canonical record types or an explicitly registered extension. |
| `created_at` | Timestamp in a stable format. |
| `created_by` | Agent, human, tool, or subsystem that created the record. |
| `authority_scope` | Owner, delegated human, agent, or policy authority under which the record was created. |
| `thesis_scope` | Relevant thesis or substrate context. |
| `backing_source` | Thesis, execution plan, design doctrine, standing guideline, emergency directive, or exploratory proposal that justifies the record when applicable. |
| `backing_hash` | Content hash, owner-attested hash, or explicit pending-hash marker for the backing source. |
| `capability_status` | Capability Status when the record supports a capability claim. |
| `evidence_status` | Evidence Status when the record supports implementation evidence. |
| `subject` | Candidate change, action, method memory, benchmark, artifact, incident, or trust target. |
| `claim_or_decision` | The claim, gate decision, observation, or disposition being recorded. |
| `source_artifacts` | Paths, commits, prompts, model outputs, reports, test logs, datasets, or design documents used as evidence. |
| `evidence_payload` | Structured evidence specific to the record type. |
| `confidence_or_uncertainty` | Confidence, uncertainty interval, evaluator judgment, or sparse-evidence warning. |
| `cost_benefit` | Cost, benefit, opportunity cost, and validation cost where relevant. |
| `risk_assessment` | Risk lane, protected-set impact, side-effect channels, and open objections. |
| `aaf_disposition` | AAF result or `not_applicable`; required when invariant I12 applies. |
| `trust_scope` | Actor, action class, domain, privileges, reversibility, criticality, data sensitivity, temporal horizon, evidence freshness, and uncertainty where trust is relevant. |
| `rollback_or_mitigation` | Rollback path, mitigation path, irreversibility note, or external-consequence warning. |
| `provenance` | Artifact lineage, generator or editor, validator, verifier, checksums or signatures where feasible, and transformation history. |
| `links` | Related ledger records, risks, formal-model predicates, implementation-evidence rows, and thesis sections. |
| `supersedes` | Prior records superseded, deprecated, corrected, or constrained by this record. |
| `redaction_policy` | Any access, privacy, security, or legal restriction on record contents. |
| `integrity` | Hash, signature, append-only log pointer, or audit marker where feasible. |
| `review_state` | Draft, assessed, validated, rejected, revised, accepted, staged, observed, superseded, deprecated, or escalated. |

## Canonical Record Types

- `improvement_proposal`
- `research_agenda`
- `goal_anchor_decision`
- `hypothesis_packet`
- `pre_registration`
- `experiment_design`
- `tool_use_event`
- `evaluator_assessment`
- `validator_decision`
- `deployment_stage_event`
- `post_deployment_observation`
- `method_memory_update`
- `anti_pattern_update`
- `trust_update`
- `alignment_review`
- `aaf_dissent_report`
- `human_authority_decision`
- `incident_report`
- `rollback_event`
- `benchmark_result`
- `external_evaluator_sample`
- `kill_switch_drill`
- `portfolio_decision`
- `composite_deployment_decision`
- `plan_object_lifecycle`
- `synthesis_report`
- `organizational_metric_snapshot`
- `owner_override`
- `successor_scope_request`
- `successor_scope_revocation`
- `v_ref_drift_alert`
- `capability_level_change`
- `provenance_attestation`
- `evidence_map_assertion`
- `governed_goal_proposal`
- `goal_classification`
- `goal_ancestry_decision`
- `governed_goal_adoption_decision`
- `governed_goal_revision`
- `governed_goal_suspension`
- `governed_goal_retirement`
- `governed_goal_veto_decision`
- `goal_stack_snapshot`
- `planner_inheritance_decision`
- `goal_evidence_update`
- `instrumental_goal_classification`
- `friendship_root_anchoring_decision`
- `ledger_modification_decision`
- `benchmark_modification_decision`
- `goal_governance_modification_decision`

Extensions are allowed only when they name the owning thesis, required fields, and indexed views they populate.

## Indexed Views

The master ledger has seven canonical indexed views.

### Improvement Evidence View

Minimum required fields:

- baseline state and candidate state
- improvement axis and task class
- proposed delta and expected benefit
- evaluator identity and evaluator assessment
- validator identity and validator decision
- benchmark or deployment evidence
- protected-set non-regression result
- cost/benefit and side-effect channels
- deployment stage and rollback or mitigation path
- post-change observation or rejection lesson

This view supports Thesis 1 and is the primary view for end-to-end recursive-improvement demonstrations.

### Trust Evidence View

Minimum required fields:

- actor and trust scope
- trust-estimate dimensions used for the scope
- evidence freshness and sparse-evidence default
- incidents, recoveries, and scope-expansion requests
- confidence or uncertainty statement
- permission effect: allowed, denied, revised, escalated, or constrained

This view supports Thesis 5 permissioning and should not be treated as a global trust score.

### Alignment Evidence View

Minimum required fields:

- invariant checks performed
- AAF dissent reports and aggregation result
- Friendship agent disposition where applicable
- AbundanceDistributionMonitor report link where applicable
- human-authority decisions and override rationale
- unresolved objections and required follow-up
- preserved dissent and critique-source diversity

This view is required for high-stakes irreversible or externally consequential actions covered by I12.

### Incident Evidence View

Minimum required fields:

- incident severity, trigger, and affected scopes
- safety, security, privacy, reliability, alignment, external-user, financial, or recursive-modification impact
- containment, interruption, rollback, or mitigation actions
- owner or human escalation state
- trust downgrade or acceptance-gate change
- lessons learned and closure criteria

Normal local failures enter this view when they cross the incident threshold defined in `00-vocabulary-and-invariants.md`.

### Benchmark Evidence View

Minimum required fields:

- benchmark identifier and version
- task set, input hash, data source, and environment
- metric definitions and interpretation limits
- baseline, candidate, and evaluator results
- held-out or adversarial test status where applicable
- failure cases and confidence limits

Benchmarks are evidence sources, not proof of intelligence or safety.

### Provenance View

Minimum required fields:

- artifact identifier and source path
- source commit, hash, or version where available
- generator, editor, evaluator, validator, and deployer
- prompt, specification, method memory, or toolchain inputs
- transformation history and dependency links
- signatures, checksums, or audit markers where feasible
- supersession and deprecation state

The provenance view must support replay or audit of accepted modifications, implementation-evidence assertions, and high-stakes action decisions.

### Goal Governance Evidence View

Minimum required fields:

- governed goal identifier, goal class, and lifecycle state
- Friendship root path and parent goal chain
- authority matrix references for proposal, adoption, activation, revision, suspension, retirement, and veto
- risk class and autonomy level
- evidence state, uncertainty, unknowns, and dissent references
- thesis backing, formal model, and planner inheritance references where applicable
- veto checks and suspension conditions evaluated
- source fingerprints and freshness status
- linked goal-stack snapshot when a planner or agent acts under the goal

This view supports Friendship-Governed Goal Architecture (Thesis 0). It records goal decisions even when no execution occurs. Rejected, vetoed, suspended, stale, owner-clarification, and withdrawn goals are governance evidence and should not be discarded.

## Lifecycle

Typical record lifecycle:

1. `draft`: evidence captured but not assessed.
2. `assessed`: evaluator or reviewer has examined the record.
3. `validated`, `rejected`, or `revised`: validator or authority has acted.
4. `staged`: record supports sandbox, canary, or production exposure.
5. `observed`: post-deployment or post-simulation evidence has been attached.
6. `superseded` or `deprecated`: later evidence modifies, replaces, or retires the record.

Rollback and mitigation create new records that reference the original decision. They do not erase the original record.

## Gate Integration

Thesis 1 acceptance gates should write at least:

- `improvement_proposal`
- `evaluator_assessment`
- `validator_decision`
- `deployment_stage_event` when staged deployment occurs
- `post_deployment_observation` or rejection lesson
- `rollback_event` when rollback or mitigation is used

Thesis 5 permission gates should write at least:

- `trust_update` when trust scope changes
- `alignment_review` for high-stakes or invariant-relevant actions
- `aaf_dissent_report` when I12 applies
- `human_authority_decision` when unresolved objections or overrides occur
- `incident_report` when the incident threshold is crossed

Thesis 4 software-substrate gates should write provenance and benchmark records for generated, edited, repaired, deployed, or rejected artifacts.

Organizational RSI execution cycles should write at least:

- `goal_anchor_decision` when a thesis claim, design doctrine, or execution-plan objective is approved, rejected, conditioned, retired, or marked stale as backing for Friendship goal structure or planner use
- `research_agenda` when a cycle or portfolio period selects objectives
- `hypothesis_packet` for candidate research or improvement hypotheses
- `pre_registration` before experiments that may support capability claims
- `experiment_design` before implementation or evaluation begins
- `portfolio_decision` when exploration/exploitation lanes are funded, paused, expanded, or stopped
- `plan_object_lifecycle` when a strategic directive, campaign, operational plan, mission plan, task object, or compliance packet is drafted, validated, rejected, escalated, superseded, or retired
- `external_evaluator_sample` for independently reviewed accepted or near-accepted improvements
- `kill_switch_drill` when live safety controls are tested
- `organizational_metric_snapshot` for process, outcome, transfer, and alignment-health reporting
- `tool_use_event` for network, external API, public repo, messaging, benchmark-write, validator-write, or privileged tool invocations
- `composite_deployment_decision` before batch or composite deployment of individually accepted changes
- `anti_pattern_update` when rejected candidates or failed transfers become reusable negative evidence
- `successor_scope_request` before any successor-agent scope expansion
- `successor_scope_revocation` when a successor scope is retired, narrowed, or contained
- `v_ref_drift_alert` when frozen reference-suite hash, access, or content deviates from expectation
- `capability_level_change` when capability ladder level is claimed, downgraded, superseded, or revoked

These record types support `appendix-organizational-recursive-self-improvement.md` and the internal execution plan. They do not by themselves establish organizational recursive self-improvement; they provide the evidence structure required to test it.

`organizational_metric_snapshot` records must include separate fields for process metrics, outcome metrics, transfer metrics, and alignment-health metrics. A snapshot that reports cycle count, hypothesis count, or benchmark-design count without outcome and alignment context should not support a capability claim.

`capability_level_change` records must include prior level, proposed or new level, triggering evidence, superseded records, downgrade reason where applicable, and owner disposition.

`goal_anchor_decision` records must include source thesis or design document, source claim, proposed Friendship goal node, allowed planner uses, constitutional constraints, non-claims, Friendship disposition, owner disposition where required, stale-source invalidation rule, and linked thesis-goal-anchor identifier. A campaign or operation that cites thesis backing without an approved or explicitly pending anchor should not be counted as fully aligned planning.

`goal_anchor_decision` remains the compatibility record for legacy thesis-backed anchors. Thesis 0-specific goal lifecycle events should use the more specific governed-goal record types below, with `goal_anchor_decision` used as a bridge record when a thesis claim becomes eligible planner backing.

`plan_object_lifecycle` records must include plan identifier, plan type, prior status, new status, plan fingerprint, thesis backing identifier, backing hash status, compliance-packet identifier where applicable, validator identity, signer or approving authority, and superseded plan identifiers when relevant. A validated plan without a lifecycle record is not auditable planning evidence.

Thesis 0 goal-governance actions should write:

- `governed_goal_proposal` when a new goal is proposed.
- `goal_classification` when a goal is classified by type, risk, autonomy level, and instrumental-quarantine class.
- `goal_ancestry_decision` when parent goals, Friendship root path, or DAG edge types are accepted, rejected, revised, or marked stale.
- `governed_goal_adoption_decision` when a candidate goal becomes adopted or is rejected before adoption.
- `governed_goal_revision` when goal content, scope, evidence state, authority, or parentage changes.
- `governed_goal_suspension` when a goal is paused because evidence, controls, source documents, or authority conditions changed.
- `governed_goal_retirement` when a goal ends because it is complete, obsolete, replaced, stale, or invalid.
- `governed_goal_veto_decision` when a goal is blocked by Friendship, owner authority, veto rules, protected-artifact policy, or hard invariants.
- `goal_stack_snapshot` when a planner or agent acts under active inherited goals and constraints.
- `planner_inheritance_decision` when strategic, campaign, operational, mission, or task plans inherit, omit, or narrow parent constraints.
- `goal_evidence_update` when evidence, uncertainty, dissent, or confidence for a goal changes.
- `instrumental_goal_classification` when a goal is classified as self-preservation, resource acquisition, goal-content preservation, self-improvement, tool expansion, successor spawning, benchmark modification, validator modification, ledger modification, or authority-scope expansion.
- `friendship_root_anchoring_decision` when a goal is bound to or removed from a Friendship registry node.
- `ledger_modification_decision`, `benchmark_modification_decision`, and `goal_governance_modification_decision` when protected goal-governance or evaluation artifacts are modified.

Goal-governance records must include `friendship_root_path`, `parent_goal_chain`, `risk_class`, `autonomy_level`, `authority_refs`, `evidence_state_refs`, `veto_checks`, `source_fingerprint`, `plan_or_goal_fingerprint`, and `disposition` when applicable.

Minimum Thesis 0 record fields:

- `governed_goal_proposal`: goal identifier, proposer authority, proposed goal class, source claim, proposed Friendship root path, parent candidates, non-claims, forbidden means, initial evidence state, and requested disposition.
- `goal_classification`: goal identifier, goal class, risk class, autonomy level, instrumental-goal classes, classifier identity, confidence or uncertainty, and classification rationale.
- `goal_ancestry_decision`: goal identifier, parent goal chain, parent edge types, Friendship root path, cycle-check result, conflict-check result, and accepted, rejected, or escalated ancestry disposition.
- `governed_goal_adoption_decision`: candidate goal identifier, adoption authority, required review references, cooling-window status, adopted scope, activation limits, and accepted, rejected, or deferred disposition.
- `governed_goal_revision`: goal identifier, prior version, new version, changed fields, revision rationale, revision authority, preserved lineage, rollback path, and superseded records.
- `governed_goal_suspension`: goal identifier, suspension trigger, active intentions affected, authority invoking suspension, required recovery condition, and child plan effects.
- `governed_goal_retirement`: goal identifier, retirement reason, final lifecycle state, child-goal disposition, successor or replacement goal where applicable, and retained evidence location.
- `governed_goal_veto_decision`: goal identifier, veto condition, veto authority, Friendship or owner basis, preserved dissent, future-regrowth matching key, and final disposition.
- `goal_stack_snapshot`: snapshot identifier, decision event, active intention, governed goal IDs, Friendship root path, plan reference, plan fingerprint, inherited-constraint hash, evidence-view hash, veto checks, fingerprint, retention policy, and redaction policy.
- `planner_inheritance_decision`: parent plan or goal, child plan or goal, inherited constraints, narrowed constraints, omitted constraints with compliance-packet justification, stop-condition propagation result, and escalation result.
- `goal_evidence_update`: goal identifier, prior evidence state, new evidence state, confidence or uncertainty change, dissent references, unknowns changed, source fingerprints, and authority that accepted the update.
- `instrumental_goal_classification`: goal identifier, suspicious instrumental class, quarantine gate, authority required, bypass risk checked, mitigation rule, and final classification disposition.
- `friendship_root_anchoring_decision`: goal identifier, registry node ID, source registry version, anchoring authority, root-path semantics, stale-source rule, and accepted, rejected, removed, or escalated disposition.
- `ledger_modification_decision`: ledger artifact, proposed modification, append-only impact, affected record types, rollback path, owner decision, and audit-preservation result.
- `benchmark_modification_decision`: benchmark artifact, proposed modification, `V_ref_0` impact, Goodhart risk, old-version preservation, owner decision, and post-change validation requirement.
- `goal_governance_modification_decision`: protected goal-governance artifact, subject type, proposed change, T0 invariant impact, independent-review status, owner decision, preserved old version, and rollback path.

Friendship registry modifications use `goal_governance_modification_decision` with `subject_type: friendship_registry`; a separate record type is not required unless implementation later needs registry-specific indexing.

## Failure Signals

The evidence-ledger schema is falsified or incomplete if:

- accepted modifications lack proposal, evaluator, validator, provenance, and outcome records
- high-stakes I12-covered actions lack AAF disposition
- owner overrides are recorded without rationale or linked dissent
- rollback erases or rewrites the failure it responds to
- benchmark results lack version, environment, metric, or baseline
- research-cycle outputs lack pre-registration when they are used to support capability claims
- organizational metrics report cycle count, hypothesis count, or benchmark-design count without separating process, outcome, transfer, and alignment-health evidence
- external-evaluator sampling is omitted for accepted improvements covered by execution-plan sampling policy
- kill-switch drills are specified but never ledgered
- privileged tool use lacks `tool_use_event` records
- composite deployments lack composite protected-set checks and `composite_deployment_decision` records
- successor-agent scope is narrowed or retired without `successor_scope_revocation`
- `V_ref_0` drift or unauthorized access lacks `v_ref_drift_alert`
- ladder levels are claimed, downgraded, or revoked without `capability_level_change`
- thesis-backed campaigns or operations cite broad documents without a `goal_anchor_decision` or equivalent Friendship/owner disposition
- planner objects move from draft to specified, validated, rejected, escalated, superseded, or retired without `plan_object_lifecycle`
- implementation-evidence assertions cannot trace to source artifacts
- incident records are missing for failures that required rollback, containment, escalation, or trust downgrade
- ledger fields are filled with prose placeholders rather than usable structured evidence

## Implementation Status

This appendix establishes the canonical schema at the design level. No repository-wide implementation is claimed here. Publication-priority implementation work remains:

- choose physical storage and append-only or audit-preserving integrity mechanism
- implement schema validation for required fields
- wire Thesis 1, Thesis 4, and Thesis 5 gates to ledger writes
- add sampled audits comparing ledger records to source artifacts
- after owner re-verification, connect any future implementation-evidence assertions to provenance records
