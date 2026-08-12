---
title: "Standing Guidelines Registry"
summary: "A bounded component of the Consullo public research program: Standing Guidelines Registry."
status: "proposed extension"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-001"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["Publication does not establish implementation or operational effectiveness.", "The withheld implementation-evidence appendix is not evidence for this page."]
---
# Standing Guidelines Registry

Version: 0.1 (2026-04-25)

Status: specified/proposed. Evidence Status: Documented/Proposed.

This registry lists standing guidelines that may serve as limited backing for routine CampaignPlanner or OperationalPlanner work. A standing guideline is not a thesis and not a substitute for Friendship or owner authorization. It is a bounded source for low-stakes, reversible, routine work where a full thesis goal anchor would be disproportionate.

High-stakes, self-improvement, governance, external-facing, customer-facing, benchmark-writing, validator-writing, tool-privilege, successor-scope, or alignment-layer work may not use a standing guideline as sole backing unless the owner explicitly approves the exception.

## Registered Standing Guidelines

| Guideline ID | Source | Owner | Scope | Allowed planner uses | Validity | Required ledger records |
| --- | --- | --- | --- | --- | --- | --- |
| `SG-DOC-HYGIENE-001` | `docs/documentation-programming-guidelines.md` | Owner | Routine documentation consistency, broken link repair, typo correction, formatting consistency | campaign backing for documentation cleanup; operational backing for reversible documentation tasks | Revalidate quarterly or on guideline change | `plan_object_lifecycle`, `provenance_attestation`, `validator_decision` |
| `SG-TEST-HYGIENE-001` | `docs/testing-programming-guidelines.md` | Owner | Routine test naming, test organization, non-semantic test documentation cleanup | operational backing for reversible test hygiene tasks | Revalidate quarterly or on guideline change | `plan_object_lifecycle`, `provenance_attestation`, `validator_decision` |
| `SG-CODE-HYGIENE-001` | `docs/core-programming-guidelines.md` | Owner | Routine low-risk code style, organization, and maintainability work that does not change behavior or privileges | operational backing for reversible code hygiene tasks | Revalidate quarterly or on guideline change | `plan_object_lifecycle`, `provenance_attestation`, `validator_decision` |

## Emergency Directives

Emergency directives are not standing guidelines. They are time-limited backing sources for urgent containment or repair.

An emergency directive must include:

- owner or Friendship source
- expiration no later than 72 hours unless renewed by owner
- affected systems and authority scope
- required post-hoc `human_authority_decision`
- required `incident_report` when the emergency concerns safety, security, or alignment controls
- explicit non-claims stating that emergency action is not capability evidence

## Exploratory Proposals

Exploratory proposals may back exploratory planning only. They must use `evidence_status: exploratory`, may not support capability claims, and may not promote results without a later thesis, execution plan, or owner-approved goal anchor.

## Registry Failure Signals

The registry is failing if:

- campaigns repeatedly use standing guidelines for self-improvement or governance work
- source paths move or hashes drift without plan invalidation
- emergency directives become recurring substitutes for normal authorization
- exploratory proposals produce claims without follow-on validation
- dashboards count standing-guideline-backed plan creation as outcome evidence
