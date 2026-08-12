---
title: "Appendix: Thesis 5 Operational Contracts"
summary: "A bounded component of the Consullo public research program: Appendix: Thesis 5 Operational Contracts."
status: "specified but not implemented"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-001"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["Publication does not establish implementation or operational effectiveness.", "The withheld implementation-evidence appendix is not evidence for this page."]
---
# Appendix: Thesis 5 Operational Contracts

Version: 0.1 (2026-04-23)

This appendix specifies behavioral contracts for the three load-bearing Thesis 5 roles: `Friendship`, `AdversarialAlignmentOrchestrator`, and `AbundanceDistributionMonitor`. It does not claim these roles are implemented in the repository. Capability Status: specified/proposed. Evidence Status: Documented/Proposed.

The purpose is to make the named roles operational enough for review: what they consume, what they output, when they can block or escalate, what evidence they must preserve, and what would count as contract failure.

## Shared Contract Envelope

Each operational owner should define:

- role identifier
- owning thesis and imported dependencies
- authority boundary
- inputs
- outputs
- required evidence-ledger records
- gate effect
- escalation rule
- non-goals
- failure modes
- minimum acceptance tests
- implementation status

The canonical evidence-ledger record structure is defined in `appendix-evidence-ledger-schema.md`.

## the Friendship agent

Role:

`Friendship` is the typed role for the constitutional Friendship function. Bare "Friendship" refers to the constitutional function; `Friendship` refers to the agent or operational owner that executes the function.

Authority boundary:

- interprets constitutional constraints for scoped actions and modifications
- can require revision, rejection, containment, rollback, or human escalation
- cannot autonomously modify core values
- cannot replace human authority in unresolved high-stakes conflict
- cannot serve as the sole evaluator of capability improvement

Inputs:

- proposed action, modification, or deployment event
- trust scope and scoped trust estimate
- evidence package and relevant evidence-ledger views
- AAF result where I12 applies
- policy constraints, constitutional constraints, and deployment stage
- incident history, rollback or mitigation state, and affected stakeholder analysis

Outputs:

- `friendship_disposition`: `allow`, `allow-with-conditions`, `require-revision`, `reject`, `veto`, `escalate`, `contain`, or `rollback`
- constitutional rationale with named values and constraints
- required mitigation or revision conditions
- human-authority escalation request when unresolved conflict exceeds autonomous authority
- evidence-ledger entries linking disposition, rationale, AAF dissent, and outcome

The `friendship_disposition` vocabulary is deliberately distinct from the improvement-loop decision-state enum in `00-vocabulary-and-invariants.md`: Friendship dispositions are constitutional-gate outputs, while the decision-state enum is the cross-thesis acceptance, revision, rejection, abstention, and escalation state vocabulary.

Gate effect:

For high-stakes irreversible or externally consequential actions covered by I12, a `reject`, `veto`, `contain`, `rollback`, or unresolved `escalate` disposition blocks acceptance until resolved by authorized human authority. For lower-stakes actions, `allow-with-conditions` may route the action into sandbox, canary, narrower scope, or additional validation.

Required evidence records:

- `alignment_review`
- `human_authority_decision` when escalated or overridden
- `incident_report` when the incident threshold is crossed
- `rollback_event` when rollback or containment is used
- links to AAF dissent reports and provenance records

Non-goals:

- not a proof of corrigibility
- not an omniscient moral oracle
- not an independent stakeholder parliament
- not a mechanism for changing immutable values by optimization pressure

Minimum acceptance tests:

- high-stakes action with missing provenance triggers rejection or escalation
- unresolved critical AAF dissent blocks autonomous acceptance
- owner override preserves dissent and rationale
- proposed core-value modification is rejected or escalated
- rollback or containment requests produce ledger records rather than deleting history

Failure modes:

- ceremonial approval without evidence review
- silent scope expansion
- owner override without preserved dissent
- inconsistent constitutional interpretation without lineage
- treating AAF disagreement as noise rather than a preserved objection

## AdversarialAlignmentOrchestrator

Role:

`AdversarialAlignmentOrchestrator` owns Adversarial Alignment Function review and dissent aggregation under single-owner Phase 1.

Authority boundary:

- selects actions, plans, modifications, external-facing decisions, and policy changes for AAF review
- routes review to dissent sources at a proportional challenge level
- aggregates dissent and reports non-veto, revision, rejection, or escalation disposition
- cannot rewrite constitutional values
- cannot silently lower warning or critical dissent because review is costly
- cannot override `Friendship` or authorized human authority

Inputs:

- action or modification description
- trust scope, deployment stage, reversibility, criticality, affected parties, and external consequence assessment
- evidence package and relevant ledger records
- critique-source availability and model/provider diversity metadata
- child-agent reports from philosophical challenge, monoculture detection, theory-of-mind stakeholder simulation, and red-team scenarios where available

Challenge levels:

- `lightweight`: quick scan for obvious cross-perspective concern
- `standard`: at least several critique perspectives within the planning cycle
- `elevated`: deeper review for high-impact internal or externally visible actions
- `deep`: comprehensive multi-perspective review for actions affecting humans beyond the owner
- `maximum`: urgent review for critical alignment, authority, containment, or external-harm risk

Outputs:

- `aaf_result` using the Model 5 `AggregateDissent` structure
- consolidated dissent report with severity, affected values, objection, mitigation, confidence, unresolved status, and recommended disposition
- critique-source coverage report, including unavailable sources and timeouts
- escalation notice for unresolved warning or critical objections
- meta-effectiveness metrics: findings accepted, false positives, coverage gaps, cost, and bypass attempts

Gate effect:

When invariant I12 applies, AAF non-veto is a precondition for acceptance unless the action is rejected, revised below warning severity, or escalated to human authority with preserved dissent. Advisory and informational objections may pass with noted dissent. Warning and critical unresolved objections block autonomous acceptance.

Required evidence records:

- `aaf_dissent_report`
- `alignment_review`
- `human_authority_decision` for escalation or override
- `incident_report` for AAF bypass, ignored severe dissent, or review failure crossing the incident threshold
- links to critique-source artifacts and source diversity metadata

Non-goals:

- not a majority vote over ethics
- not a proof of safe alignment
- not a general-purpose bureaucracy over every routine action
- not a substitute for external review where external review is warranted and available
- not allowed to collapse multi-perspective dissent into owner preference

Minimum acceptance tests:

- I12-covered action invokes AAF before acceptance
- unresolved warning or critical report blocks autonomous acceptance
- child-agent timeout is preserved as coverage gap
- owner override creates a human-authority decision record with dissent links
- cost-reduction proposal for AAF itself is treated as a high-stakes alignment modification
- all reports preserve source, severity, affected values, objection, mitigation, and confidence

Failure modes:

- AAF becomes decorative and never changes routing or acceptance
- critique sources all come from one model family or prompt culture
- warning or critical dissent is averaged away by aggregation
- maximum-severity review is delayed beyond useful intervention
- cost pressure weakens challenge level without policy change and ledger record

## AbundanceDistributionMonitor

Role:

`AbundanceDistributionMonitor` owns Abundance Distribution Obligation reporting until implementation assigns a final name. It tracks whether capability growth produces reportable value beyond the owner.

Authority boundary:

- collects ADO metrics and prepares reports
- flags sustained capability growth without external benefit evidence
- flags external harm, extractive pricing, or suppression of safe lower-cost access
- can recommend rejection, revision, escalation, or restricted deployment for ADO-relevant actions
- cannot prove social benefit from internal capability growth alone
- cannot grant external customers governance authority over Consullo

Inputs:

- capability-change records and improvement evidence
- cost, pricing, service-availability, and external-use evidence
- external-harm reports, customer outcome evidence, and public-interest deployment evidence
- distributional analysis of beneficiaries and risk-bearers
- incidents where external benefit was sacrificed for narrow internal gain
- AAF and Friendship dispositions for externally consequential actions

Outputs:

- `ado_report` on the stated reporting cadence
- `benefit_evidence`: cost reductions, useful services made available, customer or public-interest benefit evidence
- `harm_evidence`: external-harm reports, extractive-pricing incidents, and sacrificed-benefit incidents
- `distributional_assessment`: who benefits, who bears risk, and who is excluded
- `report_quality`: cadence compliance, completeness, reviewer notes, and unresolved conflicts
- escalation recommendation when ADO falsification signals appear

Gate effect:

ADO reporting does not automatically permit an action. It can block or constrain claims that capability growth is externally beneficial. For externally consequential actions, unresolved ADO harms or missing ADO evidence should trigger revision, narrower scope, AAF/Friendship review, or human escalation.

Required evidence records:

- `alignment_review`
- `benchmark_result` where ADO claims depend on measured service quality or cost reduction
- `incident_report` for external harm or sacrificed-benefit incidents
- `human_authority_decision` for overrides of ADO objections
- links to improvement evidence, AAF dissent, and provenance records

Non-goals:

- not proof that Consullo benefits humanity
- not a claim that economic incentives solve alignment
- not customer governance
- not a substitute for safety, privacy, security, or legal review

Minimum acceptance tests:

- sustained internal capability gain without external benefit evidence triggers an ADO warning
- external harm report creates an incident or review record
- cost-reduction claim links to benchmark, pricing, or service evidence
- distributional report identifies both beneficiaries and risk-bearers
- owner override of ADO objection preserves rationale and dissent

Failure modes:

- ADO becomes aspirational language without metrics
- customer demand is mistaken for public benefit
- internal transfer-pricing gains are reported as external benefit
- external harms are underreported because capability gains look impressive
- reporting cadence slips without incident or escalation

## Cross-Role Interaction

High-stakes externally consequential action should follow this minimum flow:

1. Thesis 1 or Thesis 4 creates proposal, evaluator, validator, provenance, cost/benefit, and deployment records.
2. `AdversarialAlignmentOrchestrator` runs AAF review when I12 applies and records dissent.
3. `Friendship` reviews constitutional constraints, AAF result, scoped trust, rollback or mitigation, and human-authority needs.
4. `AbundanceDistributionMonitor` records ADO-relevant benefit, harm, distributional, and report-quality evidence where the action affects external parties or abundance claims.
5. Acceptance, rejection, revision, escalation, containment, or rollback is recorded in the evidence ledger.

No role alone proves safety. The control claim is that their records and gate effects make bypass, overclaim, and ignored dissent auditable.

## Implementation Status And Next Work

These contracts reduce the operational-owner gap from unnamed design roles to specified behavioral contracts. They do not implement the roles.

Publication-priority implementation work remains:

- create agent descriptions or Java owners for the three roles
- implement structured input and output schemas matching this appendix
- connect role outputs to `appendix-evidence-ledger-schema.md`
- add tests for I12 invocation, severe-dissent blocking, owner override logging, ADO cadence, and Friendship veto/escalation behavior
- publish implementation-evidence updates only after their cited paths and gradings are owner-reverified
