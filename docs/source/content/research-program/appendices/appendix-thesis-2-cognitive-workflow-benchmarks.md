---
title: "Appendix: Thesis 2 Cognitive Workflow Benchmarks"
summary: "A proposed evaluation contract in the Consullo public research program: Appendix: Thesis 2 Cognitive Workflow Benchmarks."
status: "proposed extension"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-002"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["A benchmark specification is not a benchmark result.", "No implementation or outcome evidence is supplied by this page."]
---
# Appendix: Thesis 2 Cognitive Workflow Benchmarks

Version: 0.2 (2026-06-05) — adds equal-token-budget parity to baseline comparisons (Benchmark Principles and Suite B), per Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets, arXiv:2604.02460. Prior: 0.1 (2026-04-24).

This appendix specifies benchmark families for Thesis 2, `A Multi-Agent Cognitive Substrate For Capability Amplification`. It is a benchmark design contract, not an implemented benchmark suite. Capability Status: specified/proposed. Evidence Status: Documented/Proposed.

The goal is to make Model 2 testable without turning cognitive architecture vocabulary into an intelligence claim. A cognitive workflow counts as capability-amplifying only when it improves a declared task class against a baseline after integration cost, with reliability above the task threshold and unresolved contradiction burden within scope.

Benchmark reports produced under this appendix should populate `benchmark_result` records in `appendix-evidence-ledger-schema.md`; the report fields below define the benchmark-specific `evidence_payload` structure for those records.

## Benchmark Principles

- Task-conditioned: benchmark claims apply to a task class `T`, not to general cognition.
- Baseline-relative: every report must name a baseline such as single LLM call, retrieval-augmented call, human checklist, prior Consullo workflow, or deterministic tool.
- Budget-equalized: when the baseline is a single-agent call, the comparison must hold total thinking-token budget equal across the multi-agent workflow and the single-agent baseline, counting orchestration, handoff, and duplicated-context tokens as overhead; an unequal-budget win is an artifact of compute, not architecture (Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets, arXiv:2604.02460).
- Cost-accounted: latency, token cost, tool cost, human review time, contradiction-resolution burden, and trust-review overhead are part of the result.
- Trace-backed: every evaluated run should produce a cognitive artifact trace compatible with `appendix-evidence-ledger-schema.md`.
- Negative-case included: benchmark suites should include missing evidence, stale retrieval, prompt injection, misleading analogies, false consensus, and unnecessary-depth cases.
- No roster credit: the number of agents invoked is not a score.

## Required Benchmark Report Fields

Each benchmark report should include:

| Field | Meaning |
| --- | --- |
| `benchmark_id` | Stable identifier and version. |
| `task_class` | The task class `T` being evaluated. |
| `workflow_graph` | Nodes, typed artifacts, routing rules, stopping rules, and aggregation rules. |
| `baseline` | Comparator and rationale. |
| `input_distribution` | Source, construction method, excluded cases, and known biases. |
| `evaluation_set` | Cases, hidden/held-out status, adversarial cases, and negative controls. |
| `capability_dimensions` | Dimensions used for `Capability(W, T)`. |
| `reliability_rule` | Definition of `Reliability(W, T)` and confidence treatment. |
| `integration_cost_rule` | Cost units, normalization, and weighting. |
| `contradiction_rule` | Ceiling for unresolved contradiction and expected routing. |
| `evidence_trace` | Required trace fields and ledger record links. |
| `status_result` | What claim status, if any, the benchmark can strengthen. |

## Suite A: Retrieval And Provenance

Purpose: test whether memory and knowledge access improve evidence retrieval without introducing stale, untrusted, or irrelevant artifacts.

Representative tasks:

- retrieve the controlling definition for a term from the vocabulary file
- retrieve the implementation-evidence boundary for a thesis claim
- identify conflicting source documents and preserve both
- find the relevant anti-library or risk row for a proposed claim
- reject or quarantine untrusted external text that tries to act as instruction

Suggested dimensions:

- retrieval precision
- recall of canonical control files
- provenance completeness
- freshness and version awareness
- conflict surfacing
- source-injection resistance
- latency and review burden

Negative controls:

- a stale design file that conflicts with the current vocabulary
- an external text snippet that contains malicious instructions
- a query where the correct result is "no validated artifact found"

Amplification claim allowed only if the workflow improves retrieval or provenance quality over baseline after cost and does not hide conflicts.

## Suite B: Decomposition And Executive Control

Purpose: test whether the executive layer chooses an adequate workflow depth and avoids agent-count inflation.

Representative tasks:

- decompose a design change into retrieval, reasoning, validation, and gate steps
- decide whether a task should route to Thesis 3, Thesis 4, or Thesis 5
- choose between a lightweight workflow and a deeper workflow under budget
- compare a decomposed multi-agent workflow against a single-agent concentrated-reasoning baseline at equal total token budget
- stop when evidence is sufficient
- abstain when the task is under-specified

Suggested dimensions:

- route correctness
- subgoal coverage
- budget discipline
- stopping quality
- escalation appropriateness
- unnecessary-agent penalty
- equal-budget net benefit versus a single-agent baseline, with orchestration, handoff, and duplicated-context tokens counted as overhead

Negative controls:

- a low-risk task where invoking every agent is wasteful
- a high-stakes task where a cheap path misses required Thesis 5 routing
- a task with missing inputs where the correct state is `needs-input`
- a sequential multi-hop reasoning task that a single-agent baseline solves better at equal token budget, where decomposition only adds handoff and context-fragmentation cost (reflexive decomposition)

The benchmark should penalize both under-routing and over-routing. A controller that always escalates is not reliable; a controller that never escalates is unsafe. Likewise, a controller that decomposes a tightly-coupled reasoning chain across agents when a single-agent baseline wins at equal budget is inflating coordination cost, not capability (Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets, arXiv:2604.02460).

## Suite C: Reasoning, Analogy, And Abstraction

Purpose: test whether reasoning transformations produce useful, supported artifacts rather than persuasive but unsupported prose.

Representative tasks:

- identify unsupported inference in a draft claim
- map a method from one bounded domain to another and state transfer limits
- distinguish analogy from evidence
- detect contradictions across control files
- produce a structured hypothesis packet with support and refutation fields

Suggested dimensions:

- correctness or downstream evaluator score
- support-state accuracy
- transfer-limit identification
- contradiction detection
- artifact coherence
- validation burden

Negative controls:

- a clever analogy with invalid transfer conditions
- a reasoning chain that reaches the right answer for the wrong reason
- a hypothesis that lacks falsification evidence

This suite should not be used to claim general reasoning. It can support scoped claims such as improved support-state labeling or contradiction detection for a specified corpus.

## Suite D: Metacognition And Lacuna Detection

Purpose: test whether the workflow identifies uncertainty, missing evidence, unresolved contradictions, and inappropriate confidence.

Representative tasks:

- detect a missing benchmark before a capability claim
- identify missing provenance for an implementation claim
- distinguish unknown evidence from conflicting evidence
- mark a claim as speculative, proposed, or out of scope
- request clarification instead of inventing goals

Suggested dimensions:

- missing-evidence detection
- uncertainty-source classification
- status-tag correctness
- abstention quality
- false alarm rate
- overconfidence reduction

Negative controls:

- a task where all necessary evidence is present and abstention would be excessive
- a task where missing evidence is deliberately subtle
- a task with apparent evidence that is out of date

Metacognition improves the substrate only if it changes routing or confidence when appropriate.

## Suite E: Creativity, Negative-Space, And Anti-Library Use

Purpose: test whether creative search increases useful option coverage while controlling hallucination and validation load.

Representative tasks:

- generate alternatives to a proposed architecture
- identify absent tests, owners, rollback paths, or evidence packages
- retrieve an anti-library entry that blocks a tempting bad method
- produce a design option with novelty and usefulness separately scored
- avoid repeating known failed reasoning patterns

Suggested dimensions:

- useful option coverage
- novelty relative to reference set
- constraint satisfaction
- negative-space detection
- anti-library recall
- evaluator burden

Negative controls:

- many novel but useless options
- an absent item that is not actually required
- a deprecated anti-library lesson that no longer applies

Creativity is measured by validated option quality, not volume.

## Suite F: Perspective And AAF Support

Purpose: test whether theory-of-mind primitives produce useful dissent packets without pretending to represent real stakeholders.

Representative tasks:

- generate perspective packets for a high-stakes proposal
- identify severe objections from a minority perspective
- preserve disagreement rather than averaging it away
- compare synthetic objections against historical LLMNonInteractive or human-review findings
- mark where real stakeholder evidence is required

Suggested dimensions:

- objection coverage
- severe-risk detection
- false-consensus avoidance
- epistemic humility
- downstream AAF impact
- critique-source diversity

Negative controls:

- multiple personas that produce the same objection in different words
- a synthetic stakeholder claim unsupported by real evidence
- a mild majority view that hides a severe minority objection

This suite supports Thesis 5 imports but does not decide AAF satisfaction.

## Minimal Demonstration Package

The first Thesis 2 demonstration should include one narrow task class, one workflow graph, one baseline, at least 25 evaluated cases if feasible, negative controls, ablations, and a trace bundle.

Required ablations:

- retrieval without metacognitive review
- metacognitive review without anti-library lookup
- full workflow without perspective diversity where applicable
- full workflow versus single baseline

Required output:

- benchmark report
- cognitive artifact traces
- cost table
- failure examples
- claim-status conclusion

## Non-Claims

This appendix does not claim that Consullo has implemented the full cognitive substrate, achieved general cognition, demonstrated consciousness, or shown super-additive composition generally. It specifies what evidence would be needed for bounded cognitive-workflow amplification claims to strengthen.
