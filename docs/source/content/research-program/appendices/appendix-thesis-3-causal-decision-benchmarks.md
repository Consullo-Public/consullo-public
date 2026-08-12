---
title: "Appendix: Thesis 3 Causal-Decision Benchmarks"
summary: "A proposed evaluation contract in the Consullo public research program: Appendix: Thesis 3 Causal-Decision Benchmarks."
status: "proposed extension"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-002"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["A benchmark specification is not a benchmark result.", "No implementation or outcome evidence is supplied by this page."]
---
# Appendix: Thesis 3 Causal-Decision Benchmarks

Version: 0.1 (2026-04-24)

This appendix specifies benchmark families for Thesis 3, `Causal-Decision Foundations For Bounded Strategic Reasoning`. It is a benchmark design contract, not an implemented causal-decision benchmark suite. Capability Status: specified/proposed. Evidence Status: Documented/Proposed.

The goal is to make causal-decision claims testable without implying that Consullo currently performs operational Pearl-style causal inference, calibrated forecasting, or Goodhart-safe optimization. A decision workflow earns stronger status only when it produces scoped causal models, calibrated predictions, intervention backtests, Goodhart analysis, decision evidence, and escalation behavior under declared benchmarks.

Benchmark reports produced under this appendix should populate `benchmark_result` records in `appendix-evidence-ledger-schema.md`; the report fields below define the benchmark-specific `evidence_payload` structure for those records.

## Benchmark Principles

- Intervention-centered: benchmark tasks should evaluate proposed actions, not only explanations.
- Scope-first: every causal model must state variables, excluded variables, validity scope, assumptions, and evidentiary basis.
- Counterfactual discipline: counterfactuals should identify observed evidence, inferred background state, alternative intervention, and uncertainty.
- Calibration-bearing: predictions should be recorded before outcomes and scored after outcomes where feasible.
- Goodhart-aware: optimized metrics, proxy risks, side effects, and gaming channels are part of the score.
- Governance-bound: high-stakes, externally consequential, or alignment-relevant decisions must route to Thesis 5 rather than forced recommendation.

## Required Benchmark Report Fields

Each benchmark report should include:

| Field | Meaning |
| --- | --- |
| `benchmark_id` | Stable identifier and version. |
| `decision_domain` | Domain and scope of evaluated decisions. |
| `baseline` | Comparator such as narrative recommendation, checklist, prior workflow, or human decision log. |
| `information_boundary` | Evidence available before the decision and evidence withheld until scoring. |
| `causal_model_format` | Structural model, scenario model, simulation model, correlational proxy, or expert model. |
| `ambiguity_set_rule` | Sources, cardinality/scenario count, inclusion/exclusion rationale, and curator. |
| `prediction_targets` | Outcomes, side effects, costs, incident risks, or intervention deltas. |
| `calibration_rule` | Scoring method and sparse-feedback treatment. |
| `goodhart_probe_rule` | Proxy-risk and gaming-channel scoring. |
| `escalation_rule` | Conditions for abstention, revision, block, or Thesis 5 routing. |
| `decision_evidence_package` | Required packet fields and ledger records. |
| `status_result` | What claim status, if any, the benchmark can strengthen. |

## Suite A: Causal Model Construction

Purpose: test whether the system can construct bounded causal models with explicit scope and assumptions.

Representative tasks:

- identify variables, mechanisms, confounders, and excluded factors for a repair-pipeline decision
- distinguish observational association from intervention claim
- state validity scope for a trust-scope or deployment-stage model
- identify missing evidence that prevents high-stakes use
- reject unsupported extrapolation from one domain to another

Suggested dimensions:

- variable coverage
- mechanism plausibility
- confounder identification
- scope completeness
- assumption clarity
- provenance completeness
- unsupported-extrapolation penalty

Negative controls:

- a scenario where the correct result is "model scope insufficient"
- a misleading correlation that should not authorize intervention
- a model that omits a known confounder

This suite supports model-construction discipline, not causal truth by itself.

## Suite B: Intervention Prediction Backtests

Purpose: test whether the workflow predicts effects of actions before seeing outcomes.

Representative tasks:

- predict validation-depth effects on false accepts, false rejects, cost, and incident risk
- predict repair-pipeline changes from historical or simulated state
- predict trust-scope expansion outcomes under known incident histories
- compare no action, delayed action, narrowed action, and experimental action
- predict side effects, not only primary benefits

Suggested dimensions:

- directional accuracy
- effect-size error
- interval coverage
- option ranking
- side-effect prediction
- decision-to-evidence latency
- calibration by domain and horizon

Negative controls:

- a historical case where the observed action was not optimal
- a case with delayed side effects
- a case where action appears beneficial only because validation was weakened

Backtests must preserve the information boundary to prevent hindsight leakage.

## Suite C: Counterfactual Replay

Purpose: test whether counterfactuals are generated through explicit model assumptions rather than narrative imagination.

Representative tasks:

- reconstruct a pre-decision state
- infer background conditions from observations
- replace the observed action with a counterfactual intervention
- propagate expected effects through a structural or scenario model
- state uncertainty and model dependence

Suggested dimensions:

- abduction/action/prediction structure
- background-state clarity
- intervention specificity
- uncertainty representation
- synthetic-vs-observed labeling
- backtestability where historical data permits

Negative controls:

- a persuasive but ungrounded "what if" narrative
- a counterfactual that uses hindsight information
- a counterfactual outside the model's scope

The benchmark should reward disciplined uncertainty over confident stories.

## Suite D: Ambiguity-Set Robustness

Purpose: test whether recommendations remain honest under plausible model alternatives.

Representative tasks:

- construct `Theta(M)` from parameter perturbations, competing graph structures, mechanism disagreement, validation residuals, regime-shift scenarios, and reviewer disagreement
- declare ambiguity-set cardinality or scenario count
- explain inclusion and exclusion rationale
- identify whether the preferred action changes under plausible alternatives
- choose an information-gathering experiment when model disagreement is high

Suggested dimensions:

- credible alternative coverage
- exclusion rationale quality
- cardinality/scenario-count justification
- fragility disclosure
- experiment-selection quality
- over-conservatism penalty

Negative controls:

- an ambiguity set so broad that no decision is possible
- an ambiguity set so narrow that known risks disappear
- an omitted model alternative that later explains failure

Robustness is useful only when the ambiguity set is governed.

## Suite E: Goodhart And Strategic-Bias Probes

Purpose: test whether the decision layer identifies proxy failure, strategic bias, and metric gaming.

Representative tasks:

- detect repair-throughput optimization that lowers repair quality
- detect trust-score gaming through task avoidance
- detect benchmark-pass overfitting
- detect cost reduction by validation weakening
- detect ADO benefit reporting that hides external harm
- detect framing sensitivity or missing alternatives

Suggested dimensions:

- proxy-objective distinction
- side-effect channel coverage
- gaming-path identification
- falsification-evidence quality
- mitigation quality
- routing effect: revise, block, experiment, or escalate

Negative controls:

- a proxy that is actually adequate for a low-risk scope
- a severe Goodhart risk hidden behind good benchmark performance
- an option set missing the safest alternative

Goodhart analysis counts only if it can change the decision state.

## Suite F: Escalation, Abstention, And Permission

Purpose: test whether the workflow refuses to force recommendations under invalid scope, weak evidence, or alignment constraints.

Representative tasks:

- mark a decision as `needs-input` when objectives are underspecified
- mark a decision as `conflicted` when ambiguity-set alternatives disagree
- block or escalate when provenance is missing
- route high-stakes externally consequential actions to Thesis 5
- preserve AAF or human-authority disposition in the decision package

Suggested dimensions:

- correct decision-state enum use
- over-escalation rate
- under-escalation rate
- Thesis 5 routing correctness
- permission evidence completeness
- dissent preservation

Negative controls:

- a low-risk reversible action where escalation is unnecessary
- a high-stakes action where a recommendation would be harmful without AAF
- an externally visible action whose rollback cannot undo harm

This suite ties Thesis 3 directly to the constraint wrapper.

## Minimal Demonstration Package

The first Thesis 3 demonstration should use one bounded domain, preferably a software-repair or validation-policy domain where historical or simulated outcomes can be collected.

Required contents:

- pre-decision evidence packets
- scoped causal or scenario models
- ambiguity-set records with cardinality/scenario count
- intervention predictions recorded before outcome reveal
- Goodhart probe results
- decision-state and permission routing records
- observed outcomes or simulated outcome labels
- calibration and error report
- negative examples and rejected recommendations

The demonstration should include at least one case where the correct behavior is abstention, revision, block, or escalation.

## Non-Claims

This appendix does not claim that Consullo has implemented a Pearl-style causal graph engine, structural-equation executor, counterfactual engine, prediction-calibration battery, or Goodhart checker. It specifies what benchmark evidence would be needed before Thesis 3 claims can strengthen beyond specified/proposed architecture.
