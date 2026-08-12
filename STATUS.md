---
title: Evidence and claim status
summary: The root ledger for every substantive public claim.
status: specified
provenance: repository-authored
claim_ids: [CP-001, CP-002, CP-003]
last_reviewed: 2026-08-12
receipt: none
non_claims:
  - No present AGI or ASI achievement claim.
  - No implementation or outcome claim.
---

# Evidence and claim status

This is the first artifact a sceptical reader should open. It distinguishes what is written down
from what has been built, observed, or independently evaluated.

## Status vocabulary

| Field | Meaning |
|---|---|
| Capability status | One of `implemented`, `specified but not implemented`, `proposed extension`, or `speculative research target`. Only the middle two are used by current public claims. |
| Document status | Front matter separately labels a page `specified`, `proposed`, or `awaiting declassification`; this describes the publication artifact, not its capability claims. |
| Implementation stratum | The strongest public implementation state supported by a linked record. `none` means no public implementation artifact. |
| Evidence stratum | `none`, `self-authored diagnostic`, `witnessed`, or `independent`. Absence is stated, never rendered as a score. |
| Release receipt | The content-addressed public record of an owner-approved release. `none` means substantive source material has not been released. |

## Current claims

| ID | Public claim | Capability status | Implementation | Evidence | Receipt | Last reviewed |
|---|---|---|---|---|---|---|
| CP-001 | Consullo is a research program for governed recursive capability amplification. | `specified but not implemented` | `none` | `none` | `none` | 2026-08-12 |
| CP-002 | The program should be evaluated by whether repeatable, independently inspectable capability improvement can coexist with effective governance constraints under recursive change. | `proposed extension` | `none` | `none` | `none` | 2026-08-12 |
| CP-003 | The public constitutional edition specifies fourteen governance commitments while leaving implementation to separate evidence records. | `specified but not implemented` | `none` | `none` | [`DDR-0005`](declassification/public-receipts/DDR-0005.md) | 2026-08-12 |

## Empty by design

There are currently no public implementation artifacts, experiment results, negative results, or
independent evaluations. One content-addressed receipt authorizes publication of the constitutional
edition; publication authority is not implementation evidence. These absences describe the public
record, not material outside this repository.

The structured sources for this page are [`claims/claims.yaml`](claims/claims.yaml) and
[`claims/evidence.yaml`](claims/evidence.yaml). Later releases must update the structured records and
this human-readable ledger together.
