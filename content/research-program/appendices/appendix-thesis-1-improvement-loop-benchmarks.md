---
title: "Appendix: Thesis 1 Improvement Loop Benchmarks"
summary: "A proposed evaluation contract in the Consullo public research program: Appendix: Thesis 1 Improvement Loop Benchmarks."
status: "proposed extension"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-002"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["A benchmark specification is not a benchmark result.", "No implementation or outcome evidence is supplied by this page."]
---
# Appendix: Thesis 1 Improvement Loop Benchmarks

Version: 0.8 (2026-07-23) — adds the proposer-blind self-evolution principle (a fixed agent may propose edits to its own harness, but the acceptance signal must lie outside its view during search and pass-rate non-regression alone is not acceptance), per Self-Harness: Harnesses That Improve Themselves, arXiv:2606.09498. Prior: 0.7 (2026-06-05) — adds the reconstruction-faithful principle (independent frozen agent re-derives the solution from a distilled artifact alone), per MIND-Skill: Quality-Guaranteed Skill Generation via Induction and Deduction, arXiv:2605.08670; 0.6 (2026-06-05) — evidence-sufficient-refinement principle per Learning Hierarchical Procedural Memory for LLM Agents, arXiv:2512.18950; 0.5 (2026-06-05) — posterior-grounded principle for distilled procedures per Evidence Over Plans: Online Trajectory Verification for Skill Distillation, arXiv:2605.09192; 0.4 (2026-06-05) — optimizer-blind held-out principle for end-to-end harness optimization per Meta-Harness: End-to-End Optimization of Model Harnesses, arXiv:2603.28052; 0.3 (2026-06-05) — method-memory library-health dimensions and skill-overfitting / library-bloat negative controls per SkillOpt: Executive Strategy for Self-Evolving Agent Skills, arXiv:2605.23904; 0.2 (2026-06-05) — fresh-agent transfer verification per Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents, arXiv:2605.30621; 0.1 (2026-04-24).

This appendix specifies benchmark families for Thesis 1, `The Validated Improvement Loop And Its Invariants`. It is a benchmark design contract, not an implemented recursive-improvement benchmark suite. Capability Status: specified/proposed. Evidence Status: Documented/Proposed.

The goal is to make recursive capability amplification testable without implying that Consullo has demonstrated open-ended self-improvement. An improvement-loop claim strengthens only when a candidate change moves through baseline, proposal, evaluator package, validator decision, permission, staged exposure, observation, cost/benefit accounting, rollback semantics, and evidence-ledger recording.

Benchmark reports produced under this appendix should populate `benchmark_result` records in `appendix-evidence-ledger-schema.md`; the report fields below define the benchmark-specific `evidence_payload` structure for those records.

## Benchmark Principles

- Loop-complete: a benchmark should evaluate the full acceptance lifecycle, not only a successful patch or proposal.
- Baseline-relative: every run must name the baseline capability, cost, and failure mode.
- Gate-sensitive: the benchmark should include cases where the correct result is reject, revise, escalate, or defer.
- AAF-aware: candidates covered by I12 should exercise Thesis 5 AAF routing rather than treating permission as a passive field; detailed AAF routing fixtures are specified in `appendix-thesis-5-alignment-benchmarks.md` Suites A and B.
- Cost-accounted: proposal cost, validation cost, review cost, rollback cost, and observed benefit are part of the result.
- Ledger-backed: every evaluated run should produce records compatible with `appendix-evidence-ledger-schema.md`.
- Non-monotonic by default: one accepted change is not evidence of sustained recursive improvement.
- Transfer-verified: when a candidate's value depends on reuse, the improvement claim requires benefit replication on an agent instance that did not generate the candidate; updating a harness component is not the same as benefiting from it (Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents, arXiv:2605.30621).
- Optimizer-blind held-out: when a candidate is produced by an end-to-end harness optimizer that jointly tunes prompts, tools, memory, or workflow, the held-out and transfer sets that decide acceptance must lie outside the optimizer's search loop; a jointly-optimized harness scored on data its optimizer could read measures compilation-to-the-test, not capability (Meta-Harness: End-to-End Optimization of Model Harnesses, arXiv:2603.28052).
- Proposer-blind self-evolution: when a candidate is a harness edit proposed by the same agent that runs under the harness, the benchmark must keep the frozen held-out and fresh-agent transfer sets outside the proposer's view during search, treat pass-rate non-regression as necessary but not sufficient (the full gate — protected set, cost, rollback, transfer — still binds), and record per-model-tier harness variants separately, since harness edits are model-specific and an edit validated for one serving model is not licensed for another. The evidence bundle a proposer sees should cluster failures by verifier-grounded signature (terminal cause, causal status, agent mechanism) rather than as a flat list, so that grouped failures admit one intervention and duplicate proposals against a single regression collapse (Self-Harness: Harnesses That Improve Themselves, arXiv:2606.09498).
- Posterior-grounded: when a candidate is a distilled procedure such as a method memory or skill document, the benchmark should verify that its content is grounded in the verified execution trace rather than copied from the agent's pre-execution plan — rewarding execution grounding and penalizing plan-copying and trajectory ossification — and should prefer procedures distilled from divergent exploration, since plan-copying and pseudo-exploration produce procedures that can transfer worse than no procedure at all (Evidence Over Plans: Online Trajectory Verification for Skill Distillation, arXiv:2605.09192).
- Evidence-sufficient refinement: when a candidate refines an existing procedure from its own execution history, the benchmark should require that the refinement was gated by statistical sufficiency — a minimum count of both successful and failed traces before any edit — and that reliability is tracked as a posterior (success/failure counts with uncertainty), not a single scalar; a refinement fired on one anecdote, or an acceptance driven by a point-estimate mean that hides high variance, should be a negative control (Learning Hierarchical Procedural Memory for LLM Agents, arXiv:2512.18950).
- Reconstruction-faithful: when a candidate is a distilled artifact whose value depends on reuse (a method memory, skill, or procedural document), the benchmark should include a reconstruction check — an independent agent with a frozen prompt and no access to the source trajectory attempts to re-derive the solution from the artifact alone — scored at the tactic level, executed in a live environment for outcome, and checked for abstraction so that both ground-truth leakage and un-actionable over-abstraction are penalized. An artifact that passes only because the reconstructing agent is itself strong, or because the optimizer copied source-specific detail into it, is a negative control (MIND-Skill: Quality-Guaranteed Skill Generation via Induction and Deduction, arXiv:2605.08670).

## Required Benchmark Report Fields

| Field | Meaning |
| --- | --- |
| `benchmark_id` | Stable identifier and version. |
| `improvement_target` | Agent, method memory, prompt, test, validator, routing rule, policy, or code target. |
| `baseline` | Prior behavior, cost, failure rate, or manual process. |
| `candidate_delta` | Proposed modification and scope. |
| `evaluator_package` | Expected benefit, measurement protocol, uncertainty, side effects, and cost estimate. |
| `validator_record` | Gate results, invariant checks, protected-set review, and decision state. |
| `permission_record` | Thesis 5 routing, AAF applicability, authority, and scope. |
| `deployment_stage` | Sandbox, simulation, canary, or production-equivalent exposure. |
| `observation_window` | Post-change evidence, regression checks, and incident monitoring. |
| `transfer_record` | Fresh-agent transfer result: originating-agent delta, fresh-agent delta, fresh-agent identity and model family, and whether benefit replicated. Required when the candidate's value depends on reuse. |
| `rollback_or_mitigation` | Reversion, narrowing, supersession, or containment path. |
| `ledger_links` | Improvement, benchmark, provenance, trust, incident, and alignment records. |
| `status_result` | What claim status, if any, the benchmark can strengthen. |

## Suite A: Object-Level Repair Loop

Purpose: test whether the improvement loop can accept or reject bounded low-risk changes.

Representative tasks:

- repair a Java compilation failure
- fix a dependency-order problem
- correct a malformed JSON or agent-card artifact
- insert a missing check-in method
- reject a patch that compiles by deleting a required validation check

Suggested dimensions:

- baseline failure reproduction
- evaluator/validator separation
- deterministic validation pass/fail
- provenance completeness
- cost-normalized benefit
- rejection quality for bad candidates

Negative controls:

- a patch with missing provenance
- a patch that passes compilation while breaking semantic expectations
- a candidate whose validation cost exceeds the scoped benefit

This suite supports narrow object-level improvement claims, not recursive self-improvement by itself.

## Suite B: Evaluator And Validator Separation

Purpose: test whether proposal, evaluation, and validation remain distinct under pressure to accept changes.

Representative tasks:

- produce an evaluator package for a plausible but risky candidate
- validate a candidate whose evaluator overstates expected benefit
- compare independent validator findings against evaluator claims
- escalate disagreement between evaluator and validator
- preserve rejected candidate evidence for later review

Suggested dimensions:

- disagreement detection
- false-accept prevention
- false-reject analysis
- escalation correctness
- evidence preservation
- reviewer burden

Negative controls:

- evaluator and validator produced by the same prompt path without independence marker
- validator accepts because evaluator confidence is high but evidence is weak
- validator rejects without preserving useful proposal evidence

The benchmark should reward disciplined disagreement, not automatic acceptance or automatic rejection.

## Suite C: Validator Evolution And Non-Regression

Purpose: test whether improvements to validators improve future acceptance quality without weakening gates.

Representative tasks:

- add a validator check that catches a historical false accept
- update a reference suite with accepted-good, rejected-bad, and near-miss cases
- reject a validator change that lowers detection of semantic wrongness
- measure false accepts and false rejects before and after a validator modification
- record a validator change as high-leverage governance evidence

Suggested dimensions:

- false-accept reduction
- false-reject effect
- protected-set non-regression
- reference-suite coverage
- ValidatorStrength compatibility
- cost and latency change

Negative controls:

- validator improvement that rejects nearly everything
- validator change that improves average pass rate by dropping a hard case
- reference-suite update without rationale or preserved history

Validator evolution counts as recursive improvement only if the validator itself remains governed.

## Suite D: Method-Memory Learning

Purpose: test whether accepted or rejected changes alter future improvement behavior through method memories. This suite is also where the update-versus-benefit distinction is enforced: a method memory's measured gain on its originating agent must be separated from its transferable benefit to other agents (Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents, arXiv:2605.30621).

Representative tasks:

- extract a method memory from a successful repair
- create an anti-pattern from a rejected candidate
- reuse a method memory in a second cycle
- deprecate a method memory after a regression
- compare second-cycle cost or quality with and without the memory
- replicate a method memory's claimed benefit on a fresh agent that did not generate it, ideally from a different model family

Suggested dimensions:

- lineage completeness
- precondition accuracy
- reuse success
- deprecation discipline
- second-cycle cost change
- transfer-limit identification
- fresh-agent transfer rate: benefit replication on a non-originating agent, reported per harness component since components generalize unequally
- library health under growth: redundancy rate, stale-method rate, and retrieval precision at k as the method-memory corpus accumulates across cycles, with pruning treated as a first-class operation (SkillOpt: Executive Strategy for Self-Evolving Agent Skills, arXiv:2605.23904)

Negative controls:

- method memory with missing preconditions
- reuse outside validated scope
- anti-pattern that blocks valid future work
- method memory that improves the originating agent but whose benefit vanishes on a fresh agent (interaction-pattern overfit) — the canonical "update without benefit" case, which naive validation accepts
- a refinement that raises success on its origin distribution but is never validated on held-out variants (skill overfitting), and an unpruned library whose retrieval precision degrades as redundant or stale methods accumulate (library bloat)

This suite is the minimum bridge from one-off repair to recursive learning, and the fresh-agent transfer test is what distinguishes recursive capability amplification from local procedure accumulation.

## Suite E: Cost And Deployment Discipline

Purpose: test whether accepted improvements remain cost-effective and staged.

Representative tasks:

- compare low-cost and high-cost validation paths
- route a candidate to sandbox rather than production-equivalent exposure
- detect benefit that disappears after observation
- rollback or narrow a candidate after post-change regression
- report governance bottleneck cost without weakening the gate silently

Suggested dimensions:

- cost/benefit accuracy
- deployment-stage correctness
- observation quality
- rollback readiness
- incident correlation
- governance overhead visibility

Negative controls:

- candidate with hidden review cost
- candidate whose benefit is benchmark-local only
- candidate without rollback or mitigation path

Cost discipline is part of improvement semantics, not an after-the-fact business metric.

## Minimal Demonstration Package

The first Thesis 1 demonstration should use one bounded task class, preferably a repository-local software repair. It should include one accepted candidate, one rejected candidate, one near miss, and one second-cycle artifact such as a method memory, anti-pattern, validator test, or routing rule.

Required contents:

- baseline reproduction
- candidate proposal
- evaluator package
- independent validator record
- permission and AAF-applicability record
- staged exposure or simulation record
- cost/benefit table
- rollback or mitigation record
- evidence-ledger records
- post-change observation
- a fresh-agent transfer record for any candidate whose value depends on reuse (originating-agent delta versus non-originating-agent delta)
- method-memory or anti-pattern update

## Non-Claims

This appendix does not claim that Consullo has implemented a complete recursive improvement loop, demonstrated compounding self-improvement, solved validator gaming, or achieved general capability amplification. It specifies what benchmark evidence would be needed before Thesis 1 claims can strengthen beyond specified/proposed architecture.
