---
title: Public evidence
summary: Evidence strata, public experiments, and negative results.
status: specified
provenance: repository-authored
claim_ids: [CP-001, CP-002]
last_reviewed: 2026-08-12
receipt: none
non_claims:
  - No public evidence artifact exists in this release.
  - Build verification is process evidence, not research outcome evidence.
---

# Public evidence

This ledger is intentionally sparse. There are currently no public experiments, negative results,
witnessed evaluations, or independent evaluations.

## Evidence strata

| Stratum | Meaning |
|---|---|
| `none` | No public evidence artifact supports the claim. |
| `self-authored diagnostic` | Consullo selected the scope, method, evidence, and interpretation. Useful for debugging; not independent. |
| `witnessed` | A named external party observed a recorded procedure but did not independently design or reproduce it. |
| `independent` | An external party selected or reproduced the method without Consullo controlling the result. Scope and limitations still apply. |

Positive and negative results belong at equal navigational depth in
[`public-experiments/`](public-experiments/) and [`negative-results/`](negative-results/).
An evidence record must identify the configuration, method, observation, interpretation, residual
failures, and claim IDs it can and cannot update.

