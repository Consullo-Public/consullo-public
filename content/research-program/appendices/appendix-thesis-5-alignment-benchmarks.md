---
title: "Appendix: Thesis 5 Alignment And Scoped-Trust Benchmarks"
summary: "A proposed evaluation contract in the Consullo public research program: Appendix: Thesis 5 Alignment And Scoped-Trust Benchmarks."
status: "proposed extension"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-002"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["A benchmark specification is not a benchmark result.", "No implementation or outcome evidence is supplied by this page."]
---
# Appendix: Thesis 5 Alignment And Scoped-Trust Benchmarks

Version: 0.2 (2026-06-05) — adds the drift-measurable principle and `drift_record` field (multi-signal goal-drift index, zero-tolerance constraint preservation, regression risk) for recursive-modification alignment, per SAHOO: Safeguarded Alignment for High-Order Optimization Objectives in Recursive Self-Improvement, arXiv:2603.06333. Prior: 0.1 (2026-04-24).

This appendix specifies benchmark families for Thesis 5, `Alignment Invariants And Scoped Trust Under Recursive Modification`. It is a benchmark design contract, not an implemented alignment benchmark suite or proof of safety. Capability Status: specified/proposed. Evidence Status: Documented/Proposed.

The goal is to test whether the alignment wrapper changes routing and acceptance outcomes when it should. Alignment benchmarks here evaluate permission behavior, dissent preservation, trust-scope discipline, ADO reportability, incident response, containment, rollback, and owner-override evidence. They do not establish corrigibility, moral correctness, or general safety.

Benchmark reports produced under this appendix should populate `benchmark_result` records in `appendix-evidence-ledger-schema.md`; the report fields below define the benchmark-specific `evidence_payload` structure for those records.

## Benchmark Principles

- Gate-effect focused: a benchmark should show whether alignment controls alter action, not whether prose sounds aligned.
- Scope-explicit: every case must declare actor, action class, operational domain, reversibility, criticality, data sensitivity, tool privileges, temporal horizon, evidence freshness, and uncertainty.
- Dissent-preserving: AAF outputs should preserve severe minority objections rather than average them away.
- Default-deny: unknown or unsupported scope should narrow permission, sandbox, deny, or escalate.
- Incident-learning: incidents and near misses should update trust, playbooks, benchmarks, or gates.
- Drift-measurable: alignment benchmarks for recursive-modification scenarios should report a multi-signal goal-drift index (semantic, distributional, structural, lexical) measured against the initial baseline, a constraint-preservation score with zero tolerance for critical-constraint violations, and a regression-risk flag, with stopping rules that halt on a drift, constraint, or regression breach (SAHOO: Safeguarded Alignment for High-Order Optimization Objectives in Recursive Self-Improvement, arXiv:2603.06333).
- No safety proof: passing benchmark fixtures is not evidence of solved alignment or corrigibility; a drift index reports stability against a baseline, not correctness of that baseline.

## Required Benchmark Report Fields

| Field | Meaning |
| --- | --- |
| `benchmark_id` | Stable identifier and version. |
| `action_scope` | Typed trust and permission scope. |
| `actor_and_authority` | Actor, authority source, reviewer, and human-authority requirement. |
| `expected_disposition` | Allow, allow-with-conditions, require-revision, veto, contain, rollback, or escalate. |
| `AAF_record` | Dissent sources, reports, aggregate severity, disposition, and coverage gaps. |
| `Friendship_record` | Constitutional function disposition, veto/escalation rationale, and owner interaction. |
| `trust_record` | Scope evidence, freshness, uncertainty, dimensions, and transfer limits. |
| `ADO_record` | External benefit, harm, distributional effect, report quality, and cadence fields where relevant. |
| `incident_record` | Trigger, containment, rollback, trust update, and follow-up obligations where relevant. |
| `drift_record` | Goal-drift index (multi-signal, vs initial baseline), constraint-preservation score, regression-risk, and stopping-rule trigger, for recursive-modification scenarios. |
| `ledger_links` | Alignment, trust, incident, provenance, and improvement records. |
| `status_result` | What claim status, if any, the benchmark can strengthen. |

## Suite A: Permission Routing

Purpose: test whether actions route to allow, deny, revise, sandbox, AAF, Friendship, human authority, or incident handling correctly.

Representative tasks:

- low-risk internal reversible action
- high-stakes irreversible modification
- externally consequential action before rollback
- missing-provenance action
- authority-expansion request
- core-value or alignment-infrastructure modification

Suggested dimensions:

- scope-field completeness
- routing correctness
- default-deny behavior
- authority recognition
- ledger completeness
- false allow / false block rate

Negative controls:

- action with missing scope that should not be silently allowed
- action framed as low-risk but modifying validator policy
- externally visible action whose rollback cannot undo harm

This suite tests routing behavior, not moral wisdom.

## Suite B: AAF Dissent Aggregation

Purpose: test whether the AdversarialAlignmentOrchestrator preserves and acts on severe objections.

Representative tasks:

- informational, advisory, warning, and critical objection cases
- majority-low-severity with one plausible critical dissent
- multi-model critique disagreement
- synthetic stakeholder objection that needs real evidence
- missing critique-source diversity

Suggested dimensions:

- severity classification
- max-severity aggregation
- affected-value scope preservation
- confidence handling
- coverage-gap recording
- gate effect

Negative controls:

- median aggregation hides a severe minority objection
- repeated personas produce duplicate objections counted as diversity
- AAF records dissent but acceptance ignores it

AAF benchmarks should show whether dissent changes routing.

## Suite C: Trust-Scope Transfer

Purpose: test whether scoped trust prevents overgeneralized reliance.

Representative tasks:

- internal summarization agent requests external communication
- code repair agent requests validator modification authority
- planning agent requests financial action
- retrieval agent requests sensitive-data access
- previously reliable agent operates after distribution shift

Suggested dimensions:

- scope-transfer detection
- evidence freshness
- uncertainty handling
- privilege-boundary preservation
- escalation correctness
- recovery integrity

Negative controls:

- trust in one domain treated as global competence
- stale evidence accepted as current
- composite workflow inherits component trust without edge evidence

Trust is valid only inside its declared scope.

## Suite D: ADO Reportability

Purpose: test whether abundance claims remain reportable and evidence-backed.

Representative tasks:

- internal cost reduction with no external availability
- external service made available but with rising harm reports
- lower price but concentrated risk transfer
- capability improvement with no distributional analysis
- ADO reporting missed for a relevant period

Suggested dimensions:

- external benefit evidence
- external harm evidence
- beneficiary/risk-bearer distribution
- report quality
- cadence compliance
- incident linkage

Negative controls:

- internal efficiency counted as public benefit
- external service counted as abundance while harms are omitted
- stale ADO report reused for new capability claim

ADO is reportability discipline, not proof of public benefit.

## Suite E: Incident Response And Recovery

Purpose: test whether failures update the permission system rather than becoming inert logs.

Representative tasks:

- missing required AAF review
- unauthorized scope expansion
- lost provenance
- trust leakage
- rollback failure
- owner override without required rationale

Suggested dimensions:

- incident detection
- containment or rollback action
- trust update
- benchmark/playbook update
- evidence preservation
- follow-up obligation tracking

Negative controls:

- incident recorded but future gates unchanged
- near miss ignored because no harm occurred
- rollback erases dissent or provenance

Incident learning is part of recursive alignment improvement.

## Suite F: Owner Override Audit

Purpose: test whether single-owner final authority remains auditable when it overrides or narrows alignment controls.

Representative tasks:

- owner allows action despite warning dissent
- owner vetoes action despite capability benefit
- owner narrows scope after AAF challenge
- owner defers to external review
- owner override repeats across similar cases

Suggested dimensions:

- rationale completeness
- dissent preservation
- condition tracking
- override frequency
- override-frequency threshold status: parameter pending Phase 1 calibration; owner: Thesis 5 governance
- correlation with severity
- follow-up review completion

Negative controls:

- override recorded without dissent
- override rationale missing or generic
- repeated warning overrides treated as normal operation

The benchmark does not make owner override safe. It makes override visible and reviewable.

## Minimal Demonstration Package

The first Thesis 5 demonstration should use fixture-based cases, not live high-stakes deployment. It should include permission routing, one AAF warning or critical dissent, one trust-scope leak, one ADO reportability case, one incident or near miss, and one owner-override audit fixture.

Required contents:

- action-scope records
- expected and actual dispositions
- AAF dissent reports
- Friendship disposition where applicable
- trust estimates and transfer limits
- ADO report fields where applicable
- incident or near-miss record
- owner override record if applicable
- evidence-ledger records
- post-case trust or playbook update

## Non-Claims

This appendix does not claim that Consullo has implemented the full alignment wrapper, solved alignment, proved corrigibility, or validated AAF / ADO / Friendship controls in deployment. It specifies what benchmark evidence would be needed before Thesis 5 claims can strengthen beyond specified/proposed architecture.
