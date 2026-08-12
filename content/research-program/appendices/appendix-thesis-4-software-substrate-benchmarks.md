---
title: "Appendix: Thesis 4 Software Substrate Benchmarks"
summary: "A proposed evaluation contract in the Consullo public research program: Appendix: Thesis 4 Software Substrate Benchmarks."
status: "proposed extension"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-002"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["A benchmark specification is not a benchmark result.", "No implementation or outcome evidence is supplied by this page."]
---
# Appendix: Thesis 4 Software Substrate Benchmarks

Version: 0.3 (2026-06-05) — adds the execution-deterministic principle (compile-once-run-many, model out of the execution loop, accuracy gate against silent failures, bounded runtime invocation), per Compiled AI: Deterministic Code Generation for LLM-Based Workflow Automation, arXiv:2604.05150. Prior: 0.2 (2026-06-05) — verifier-hardened principle per Let the Barbarians In: How AI Can Accelerate Systems Performance Research, arXiv:2512.14806; 0.1 (2026-04-24).

This appendix specifies benchmark families for Thesis 4, `A Self-Modifying Software Substrate With Acceptance Gates`. It is a benchmark design contract, not an implemented software-repair benchmark suite. Capability Status: specified/proposed. Evidence Status: Documented/Proposed.

The goal is to make software-substrate claims testable without implying that Consullo has a complete autonomous coding or deployment system. A software change earns stronger status only when it passes specified evidence classes: specification, generation or repair, compilation, tests, semantic checks, security, provenance, cost/benefit, deployment discipline, permission, and observation.

Benchmark reports produced under this appendix should populate `benchmark_result` records in `appendix-evidence-ledger-schema.md`; the report fields below define the benchmark-specific `evidence_payload` structure for those records.

## Benchmark Principles

- Specification-first: every patch candidate should begin with a scope, non-goals, validation plan, and rollback expectation.
- Multi-gate: compilation is necessary but not sufficient.
- Reference-backed: validator evolution should be tested against held-out known-good, known-bad, and near-miss cases.
- Security-aware: privileged, validator-affecting, externally consequential, and alignment-infrastructure changes require stricter gates.
- Provenance-preserving: generated code, prompts, tools, model outputs, human edits, and test artifacts should be traceable.
- Non-deployment by default: benchmark success does not imply production deployment permission.
- Verifier-hardened: candidates should be confined to the target code and forbidden from editing the evaluator, workload, scoring code, or tests; scoring functions should be smooth and deterministic; and evaluation should use diverse held-out workloads — controls that prevent an evolutionary or LLM optimizer from reward-hacking the benchmark (Let the Barbarians In: How AI Can Accelerate Systems Performance Research, arXiv:2512.14806).
- Execution-deterministic: where the task permits, a generated artifact should run as static code with the model out of the execution loop, and the benchmark should check execution determinism (identical inputs produce identical outputs) rather than re-invoking a model per transaction. Critically, the validation suite must include an *accuracy gate* that compares outputs to golden expectations, because an artifact can pass the execution gate (100% run success) while producing wrong outputs — a silent failure that execution success alone would deploy; compile-time accuracy checking converts that silent runtime failure into a detectable pre-deployment one. Any irreducible runtime LLM call should be a bounded invocation under a fixed schema with fallback and human escalation, not an open-ended per-transaction prompt (Compiled AI: Deterministic Code Generation for LLM-Based Workflow Automation, arXiv:2604.05150).

## Required Benchmark Report Fields

| Field | Meaning |
| --- | --- |
| `benchmark_id` | Stable identifier and version. |
| `repair_domain` | Compilation, dependency, JSON/schema, semantic behavior, security, deployment, validator, or provenance task class. |
| `specification_record` | Scope, expected files, non-goals, validation plan, and rollback expectation. |
| `baseline_failure` | Reproducible failure, regression, or missing capability. |
| `candidate_patch` | Patch source, tool/model/method memory, and changed artifacts. |
| `validation_matrix` | Compilation, tests, semantic checks, security, provenance, cost/benefit, and permission checks. |
| `reference_suite` | Known-good, known-bad, adversarial, and historical false-accept/false-reject cases. |
| `ValidatorStrength_rule` | Composite scoring rule or pending calibration note. |
| `deployment_state` | Sandbox, simulated canary, canary, production-equivalent, or no deployment. |
| `observation_record` | Post-change behavior, incidents, rollback, or supersession. |
| `ledger_links` | Benchmark, provenance, improvement, incident, and trust records. |
| `status_result` | What claim status, if any, the benchmark can strengthen. |

## Suite A: Deterministic Local Repair

Purpose: test narrow repair machinery with reproducible expected outcomes.

Representative tasks:

- fix missing imports or package names
- repair dependency ordering
- correct malformed JSON or method signatures
- repair generated descriptions or agent cards
- insert missing required check-in methods

Suggested dimensions:

- failure reproduction
- patch minimality
- compilation success
- test pass rate
- provenance completeness
- cost and latency

Negative controls:

- patch that deletes failing tests
- patch that changes unrelated files
- patch whose provenance is missing or ambiguous

This suite supports component-level repair claims, not full self-modifying substrate validation.

## Suite B: Semantic Near-Miss Detection

Purpose: test whether the substrate rejects patches that pass surface checks while weakening behavior.

Representative tasks:

- patch compiles but removes a validation check
- generated test asserts wrong behavior
- repair changes policy semantics while preserving API shape
- patch handles the happy path but breaks edge cases
- code change changes trust or permission behavior unintentionally

Suggested dimensions:

- semantic-failure detection
- edge-case coverage
- reviewer burden
- false-accept rate
- explanation quality
- reference-suite update

Negative controls:

- syntactically correct but semantically wrong patch
- test suite that passes because it encodes the bug
- validator prompt that rewards plausibility over behavior

Semantic validation is the main boundary between code generation and safe software modification.

## Suite C: Validator Non-Regression

Purpose: test whether validators and generated-test pipelines improve without weakening gates.

Representative tasks:

- run validator before/after change on held-out reference suite
- measure known-good acceptance and known-bad rejection
- detect historical false accepts
- detect security failures and provenance gaps
- reject validator change that improves throughput by reducing scrutiny

Suggested dimensions:

- known-good acceptance
- known-bad rejection
- semantic-wrongness detection
- security-failure detection
- provenance-gap detection
- risk-severity calibration

Negative controls:

- validator that rejects nearly everything
- validator that accepts generated tests sharing the same model-family blind spot
- reference suite modified without preserved rationale

ValidatorStrength should reward discrimination, not permissiveness or blanket conservatism.

## Suite D: Security And Privilege Boundary

Purpose: test whether software changes touching sensitive areas route through stricter controls.

Representative tasks:

- patch authentication or authorization logic
- modify A2A ingress policy
- alter evidence-ledger writes
- change validator or deployment scripts
- request broader tool privileges

Suggested dimensions:

- security-check coverage
- privilege-boundary preservation
- Thesis 5 routing correctness
- provenance and review completeness
- rollback readiness
- incident-prevention quality

Negative controls:

- change that silently broadens access
- patch that weakens logging or audit
- validator-affecting change treated as ordinary repair

Security-sensitive repair cannot inherit evidence from low-risk compilation repair.

## Suite E: Staged Deployment And Rollback

Purpose: test whether accepted patches move through explicit exposure states and retain recovery paths.

Representative tasks:

- accept patch into sandbox only
- simulate canary behavior
- observe post-change regression
- narrow or rollback a candidate after observation
- preserve rollback record and postmortem evidence

Suggested dimensions:

- stage-entry correctness
- monitoring coverage
- rollback or supersession success
- incident classification
- evidence-ledger completeness
- cost of recovery

Negative controls:

- patch marked accepted without stage
- rollback path missing or untested
- observation omitted after deployment-equivalent exposure

Deployment discipline is part of the acceptance gate, not an operations afterthought.

## Minimal Demonstration Package

The first Thesis 4 demonstration should use one bounded low-risk repository-local task. It should include one accepted repair, one rejected semantic near miss, one validator-reference-suite case, and one staged exposure record.

Required contents:

- specification record
- reproducible baseline failure
- candidate patch and provenance
- validation matrix
- reference-suite result
- cost/benefit table
- Thesis 1 acceptance linkage
- Thesis 5 permission linkage where applicable
- staged exposure or no-deployment rationale
- rollback or supersession path
- evidence-ledger records

## Non-Claims

This appendix does not claim that Consullo has implemented a complete autonomous software engineer, a secure deployment pipeline, full semantic validation, validator non-regression, or production self-modification. It specifies what benchmark evidence would be needed before Thesis 4 claims can strengthen beyond component-level implementation and specified/proposed architecture.
