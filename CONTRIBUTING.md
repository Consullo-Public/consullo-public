# Contributing

Consullo welcomes precise criticism, reproducibility improvements, accessibility fixes, and
well-scoped research contributions. The strongest contribution is one that makes a claim easier to
test or easier to reject.

## Before opening a change

1. Read [`README.md`](README.md), [`STATUS.md`](STATUS.md), and [`GOVERNANCE.md`](GOVERNANCE.md).
2. Keep capability status separate from implementation and evidence status.
3. Do not submit private, restricted, personal, credential, or operational material.
4. Do not paste unreleased Consullo source text into an issue or pull request. Public review occurs
   only after release approval; a public pull request is already publication.
5. Run `python3 tools/verify_public.py` and the local publication gate before requesting review.

## Good contributions

- a failing example that identifies a bounded contradiction;
- an independently reproducible experiment with environment and method recorded;
- a negative result that narrows a claim;
- a generator, verifier, accessibility, or documentation improvement; or
- a correction with exact old and new language and a reason for the change.

## Claim requirements

Every substantive claim must have a stable claim ID; one canonical capability status
(`implemented`, `specified but not implemented`, `proposed extension`, or `speculative research
target`); an implementation stratum; an evidence stratum; a review date; explicit non-claims; and a
linked release receipt when source-derived content is present. Self-authored tests must not be
described as independent evidence.

## Licensing and review

By submitting a prose or data contribution, you agree that accepted work will be licensed under
CC BY 4.0. By submitting code, workflows, or tools, you agree that accepted work will be licensed
under Apache-2.0. The custodian may ask for provenance, narrower wording, tests, or a release review
before acceptance.

Use the issue and pull-request templates. Repository setup and hosting are intentionally deferred
until the owner selects a namespace.
