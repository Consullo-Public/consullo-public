---
title: "Appendix: Formal Models"
summary: "A bounded component of the Consullo public research program: Appendix: Formal Models."
status: "proposed extension"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-001"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["Publication does not establish implementation or operational effectiveness.", "The withheld implementation-evidence appendix is not evidence for this page."]
---
# Appendix: Formal Models

This appendix collects formal sketches used by the five theses. The models are intentionally lightweight in the first drafting pass. Each model defines variables, operators, acceptance criteria, failure modes, and falsification conditions; later drafts should bind more thresholds to implementation evidence.

## Model 1: Validated Improvement Loop

### Objects

Let:

- `pi_t` be the Consullo agent population at time `t`, including agents, method memories, code, prompts, tests, routing policies, trust state, and governance state.
- `delta` be a candidate modification.
- `s` be the scope of the proposed modification.
- `E_delta` be the evidence package for `delta`.
- `I` be the set of hard invariants.
- `B` be the benchmark and validation set.
- `K` be the cost model.
- `G` be the deployment-stage policy.
- `A` be the Adversarial Alignment Function gate.
- `R` be rollback or mitigation state.

### Acceptance Predicate

```text
Accept(delta, s, pi_t) =
  HardInvariants(I, pi_t, delta, s)
  and EvidenceSufficient(E_delta, B, K)
  and RiskWithinScope(E_delta, s)
  and ProtectedSetNonRegression(delta, s)
  and DeploymentAllowed(G, delta, s)
  and RollbackDefined(R, delta, s)
  and AAFGate(A, delta, s)
```

`AAFGate` returns true automatically only when invariant I12 does not apply. When I12 applies, it requires Adversarial Alignment Function non-veto or human-authority escalation with preserved dissent.

`ProtectedSetNonRegression` requires no material degradation on named protected dimensions such as alignment, security, privacy, rollback readiness, provenance, and core reliability unless a human-authorized emergency containment rationale explicitly permits the trade.

### Improvement Predicate

For task class `T`, metric `M`, minimum margin `epsilon`, and maximum false-accept tolerance `alpha`:

```text
Improve(delta, T, M) =
  Pr[M(Promote(pi_t, delta), T) >= M(pi_t, T) + epsilon | E_delta] >= 1 - alpha
  and SideEffectsWithinBounds(delta)
  and CostBenefitAcceptable(delta)
```

This predicate is empirical. It does not prove global improvement. It supports staged acceptance under the current evidence envelope.

Owner: Thesis 1 improvement governance, pending Phase 1 calibration. `epsilon` and `alpha` must be set per task class and risk lane before high-stakes acceptance use.

### Population Update

```text
pi_{t+1} =
  Promote(pi_t, delta) if Accept(delta, s, pi_t)
  Revise(pi_t, delta) if evidence is promising but insufficient
  Reject(pi_t, delta) otherwise
```

`Promote` is a population operator, not set union. It may add, replace, demote, retire, specialize, reroute, or constrain other population members as part of accepting `delta`. All three outcomes update the evidence ledger. Rejection and revision are learning events, not empty outcomes.

### Method-Memory Update

Let `m` be a method memory and `L` its lineage.

```text
m' = Mutate(m, delta)
Eligible(m') iff
  preconditions defined
  postconditions defined
  dependencies defined
  validation history present
  cost profile present
  lineage L preserved
```

Promotion of `m'` requires the same acceptance predicate as other modifications.

### Failure Modes

The model fails if:

- benchmarks are gamed faster than validators improve
- `E_delta` omits side-effect channels
- costs exceed benefits across accepted changes
- rollback is unavailable where assumed
- evidence ledger entries are missing or rewritten
- protected dimensions regress silently
- AAF dissent is bypassed or not preserved
- learned subsystems pass tests while hiding capability or intent

### Falsification Conditions

Evidence against the model includes:

- high false-accept rate on post-deployment monitoring
- accepted improvements degrade outside benchmark distributions
- repeated rollback failure
- increasing trust or alignment incidents after accepted changes
- improvement cost rising faster than measured capability gain
- inability to assign credit to accepted or rejected changes

## Model 2: Multi-Agent Cognitive Substrate

### Objects

Let:

- `A = {a_1, ..., a_n}` be the set of cognitive agents available for a task.
- `c_i(T)` be the task-conditioned capability vector of agent `a_i`.
- `k_i` be the cost vector of agent `a_i`, including latency, token cost, tool cost, and coordination burden.
- `r_i(s)` be the reliability estimate of agent `a_i` in scope `s`.
- `tau_i` be the typed interface of agent `a_i`.
- `W` be a cognitive workflow graph over agents and intermediate artifacts.
- `T` be the task class.
- `L` be the evidence ledger or trace for the workflow.

### Capability Vector

For a task class `T`, a capability vector may include:

```text
c_i(T) =
  <recall, reasoning_accuracy, option_coverage, uncertainty_calibration,
   multimodal_interpretation, analogy_quality, implicit_proposal_quality,
   explicit_validation_quality, error_detection, lacuna_detection,
   artifact_quality, sustained_reasoning>
```

The dimensions are task-dependent projections, not context-free intelligence scores. The implicit/explicit split is included to preserve the distinction between proposal generation, taste, intuition, or creative ranking and explicit validation, explanation, or acceptance support. A thesis claim should name the dimensions it uses and should not treat implicit-style proposal quality as acceptance authority.

### Measurement Conventions

For first-pass benchmark families, the model uses normalized task-bounded units rather than a single universal cognition score.

```text
Capability(W, T) in [0, 1]
```

where `Capability(W, T)` is a weighted aggregate over the named dimensions for task class `T`, measured against a declared benchmark or project-local evaluation protocol. The benchmark definition for `T` must specify:

- the dimension set used for `T`
- the baseline comparator
- the scoring rule for each dimension
- the aggregation weights or ordering rule
- the admissible evidence source

Typical dimension bindings are:

- retrieval tasks: precision, recall, freshness, provenance completeness, latency
- decomposition/control tasks: routing accuracy, budget discipline, stopping quality, escalation appropriateness
- reasoning tasks: task accuracy, contradiction detection, support-state correctness, option coverage
- creative/design tasks: novelty, downstream usefulness, constraint satisfaction, implicit proposal quality, explicit validation burden, reviewer score
- perspective/AAF-support tasks: objection coverage, severe-risk detection, false-consensus avoidance

For task classes outside these examples, the benchmark owner must declare the dimension set, scoring rule, and aggregation convention before using `Capability(W, T)` as an amplification claim.

```text
Reliability(W, T) in [0, 1]
```

is the lower-confidence performance floor for the workflow on task class `T`, using the benchmark family named for `T`. For early project-local evaluations, this may be an empirical pass rate, calibration-adjusted success rate, or lower confidence bound over repeated runs. For higher-stakes scopes, `Reliability(W, T)` should penalize high variance and silent failure.

```text
IntegrationCost(W, T) >= 0
```

is a normalized cost term measured relative to the declared baseline budget for `T`. It may combine latency, token cost, tool cost, contradiction-resolution effort, trust-review burden, and human review time. When heterogeneous units are combined, the benchmark definition must state the normalization rule and weight vector.

### Workflow Composition

```text
W = (V, E)
```

where `V` are cognitive agents or artifacts and `E` are typed channels. A workflow is admissible only if:

```text
InterfacesCompatible(W)
and ScopeAllowed(W)
and EvidenceLogged(L, W)
and TrustSufficientForEdges(W)
```

Model 2 is an engineering abstraction over Consullo cognitive workflows, not a claim of psychological fidelity to Soar, ACT-R, CLARION, or LIDA. Those architectures inform constraints on explicit state, typed buffers/artifacts, routing/production steps, implicit-vs-explicit proposal/validation distinctions, cognitive-cycle structure, latency, and broadcast/aggregation discipline. A workflow should therefore declare which state, memory, routing, broadcast, or implicit/explicit pattern it relies on when those patterns are load-bearing.

For composed workflows `W1 ; W2`, the first-order composition bound is:

```text
Capability(W1 ; W2, T)
  <= Capability(W1, T) + Capability(W2, T) - IntegrationCost(W1, W2, T)
```

Super-additive outcomes are possible only when the evidence ledger shows that the composed workflow beats both component baselines after integration cost. Without that evidence, the default assumption is sub-additivity.

### Amplification Predicate

Let `Baseline(T)` be a named single-agent, human, or prior Consullo workflow baseline for task class `T`.

```text
Amplifies(W, T) =
  Capability(W, T) - Capability(Baseline(T), T) - IntegrationCost(W, T) > 0
  and Reliability(W, T) >= threshold(T)
  and ContradictionBurden(W, T) <= max_contradiction(T)
  and ConstraintsSatisfied(W)
```

`threshold(T)` is a task-class-specific reliability floor set by deployment scope and risk tier.

`max_contradiction(T)` is the task-class-specific ceiling on unresolved contradiction burden. For low-stakes exploratory tasks it may be permissive; for acceptance-gate, alignment, or externally consequential tasks it should be near zero unless the workflow explicitly returns escalation, abstention, or revision.

### Substrate Update

```text
A_{t+1} = ImproveCognitiveSubstrate(A_t, L_t)
```

Updates may include new agents, retired agents, routing changes, method memories, prompt decompositions, compiled workflows, or trust-scope changes. Such updates are candidate modifications under Thesis 1 and Thesis 5.

### Failure Modes

The model fails if:

- added agents increase cost without measured capability gain
- agent interfaces are incompatible or underspecified
- contradictions are hidden rather than resolved or escalated
- memory retrieval increases confidence while reducing accuracy
- creative or intuitive outputs are treated as grounded without evidence
- homogeneous models create cognitive monoculture
- workflow traces are missing, preventing replay and improvement

### Falsification Conditions

Evidence against the model includes:

- multi-agent workflows underperforming simpler baselines after cost accounting
- repeated failures caused by handoff or state mismatch
- rising contradiction or trust-review burden without improved outcomes
- cognitive lacuna closure claims reopening under regression tests
- benchmark gains disappearing outside narrow prompt formats
- inability to assign credit to cognitive subagents or workflow steps

## Model 3: Causal-Decision Foundations

### Objects

Let:

- `M` be a structural causal model with variables `X`, mechanisms `F`, exogenous variables `U`, and validity scope `S_M`.
- `d` be a candidate decision or intervention.
- `O` be the objective vector.
- `C` be hard constraints imported from Thesis 5.
- `Theta(M)` be an ambiguity set of plausible models near `M`.
- `B` be benchmark, backtest, calibration, and experiment evidence.
- `G` be a Goodhart-risk assessment.
- `Q` be decision-lineage and provenance evidence.
- `E` be escalation state.

### Robust Intervention Rule

```text
d* = argmax_d min_{M' in Theta(M)} E[U_O | do(d), M']
```

subject to:

```text
ConstraintsHold(C, d)
and ModelScopeValid(M', d)
and EvidenceSufficient(B, d)
and GoodhartRiskAcceptable(G, d, O)
and ProvenancePresent(Q, d)
and EscalationNotRequired(E, d)
```

If any hard condition fails, the system does not return `d*` as an executable recommendation. It returns abstention, additional experiment selection, model revision, or escalation.

`EscalationNotRequired(E, d)` is false when `d` is high-stakes, irreversible, or externally consequential before rollback and Model 5's AAF gate has not returned non-veto, revision, rejection, or human-authority disposition.

### Ambiguity-Set Construction

`Theta(M)` is not an unconstrained neighborhood. It is a curated ambiguity class recorded in the evidence ledger for the decision. At minimum, it should be constructed from one or more of:

- parameter perturbations around `M` within empirically supported ranges
- competing causal structures consistent with current evidence
- mechanism disagreements preserved by `MechanismLibrarian`
- held-out validation failures or backtest residuals
- regime-shift scenarios or adversarial stress cases
- expert or reviewer disagreement preserved as explicit alternatives

For first-pass implementations, `Theta(M)` may be scenario-based rather than fully statistical. That is acceptable if the construction rule, inclusion rationale, and curator are named. `MechanismLibrarian` should maintain candidate mechanisms and disagreement records; `CausalBoundaryEnforcer` should reject ambiguity-set members that fall outside the stated scope or evidentiary basis.

The ambiguity-set record must declare its cardinality or scenario count and explain why that size is adequate for the decision scope. This is a formal requirement of Model 3 and is tested in `appendix-thesis-3-causal-decision-benchmarks.md`. An oversized ambiguity set can make the minimax rule unusably conservative; an undersized set can hide model fragility.

### Counterfactual Evaluation

For observed evidence `e`, action `d`, alternative `d_alt`, and outcome `Y`, counterfactual reasoning follows:

```text
Abduction: infer posterior over U given e
Action: replace structural equations affected by do(d_alt)
Prediction: compute distribution over Y under modified model
```

Counterfactual claims must state model assumptions, scope, and uncertainty. They should be backtested where historical interventions permit.

### Experiment Portfolio

Let `A` be the experiment allocation over strategy families:

```text
A = <random, theory_guided, novelty, adversarial, replication>
```

Experiment portfolios are admissible only if:

```text
random > 0
and objective_quality_metric separated from confidence_metric
and calibration_gap tracked
and safety constraints hold
```

This prevents theory-guided exploitation from monopolizing experiment choice before evidence maturity.

### Goodhart Check

Let `m` be the optimized metric and `o` the target objective.

```text
GoodhartRiskAcceptable(G, d, O) =
  metric_objective_link documented
  and proxy drift monitored
  and side-effect channels checked
  and adversarial metric-gaming scenario considered
  and escalation triggered for severe unresolved proxy risk
```

### Failure Modes

The model fails if:

- decisions use causal models outside validity scope
- recommendations optimize proxies while degrading target objectives
- counterfactuals are presented without uncertainty or assumptions
- experiment choice increases confidence without objective model improvement
- strategic bias gates are skipped for high-stakes recommendations
- predictions enable harmful manipulation or unsafe interventions
- model disagreement is hidden instead of escalated or disclosed

### Falsification Conditions

Evidence against the model includes:

- poor calibration on forecasting or intervention-prediction batteries
- repeated intervention outcomes contradicting model predictions
- high confidence recommendations failing under reframing tests
- strategy commitments made without decision lineage or option-set evidence
- objective-vs-subjective epistemic divergence across experiment portfolios
- Goodhart incidents traceable to optimized decision metrics
- externally consequential predictions delivered without safety validation

## Model 4: Self-Modifying Software Substrate

### Objects

Let:

- `P` be the current program, agent repository, workflow, or generated artifact set.
- `P'` be a candidate modified program.
- `sigma` be the specification or agent contract.
- `F` be the fault report, feature request, or improvement request.
- `G_t` be the generation or repair pipeline at time `t`.
- `C` be Consullo coding constraints, including static methods, JSON data passing, and PDCA signatures.
- `V` be the validation suite, including tests, static checks, contrastive tests, and post-verification methods.
- `Phi` be the semantic invariant class available for the scope.
- `S` be security and capability policy.
- `Prov` be provenance evidence.
- `Perm` be Thesis 1 and Thesis 5 acceptance and permission state.
- `K` be the cost model.

### Candidate Generation

```text
P' in Generate(G_t, P, sigma, F, C)
```

`Generate` may include new agent construction, code repair, test generation, documentation, workflow compilation, or deployment artifact generation. Candidates outside `C` are rejected or returned for repair before deeper validation.

### Acceptance Predicate

```text
AcceptPatch(P', P, sigma) =
  ConformsToMethodology(P', C)
  and Compiles(P')
  and TestsPass(P', V)
  and SemanticInvariantsHold(P', Phi)
  and RegressionRiskWithinBounds(P', P, V)
  and SecurityPolicySatisfied(P', S)
  and ProvenancePresent(Prov, P', P, sigma, F)
  and CostBenefitAcceptable(P', K)
  and PermissionSatisfied(Perm, P', sigma)
```

This predicate separates formal, deterministic, statistical, and governance evidence. Compilation is deterministic. Test passing is empirical relative to test coverage. Semantic validation may be formal for narrow properties or statistical when LLM-based. Permission is imported from Thesis 1 and Thesis 5.

### Repair-Pipeline Update

Let `H_t` be repair history, including accepted patches, rejected patches, incidents, regressions, costs, and post-deployment outcomes.

```text
G_{t+1} = ImprovePipeline(G_t, H_t)
```

Pipeline improvement may modify prompt templates, fault-localization heuristics, retrieval methods, contrastive-test generation, static-analysis selection, patch-ranking rules, or semantic invariant classes. It is itself a candidate modification and must satisfy the same acceptance discipline.

For a fixed held-out validator reference suite `V_ref`, recursive pipeline improvement must satisfy:

```text
ValidatorStrength(G_{t+1}, V_ref) >= ValidatorStrength(G_t, V_ref)
```

unless an explicitly documented human-authorized trade replaces `V_ref` with a stronger or more relevant reference suite. Generator improvement cannot be purchased by weakening validators silently.

### ValidatorStrength Convention

For a held-out reference suite `V_ref`, define:

```text
ValidatorStrength(G, V_ref) =
  w_good * GoodAcceptanceRate(G, V_ref)
  + w_bad * BadRejectionRate(G, V_ref)
  + w_sem * SemanticWrongnessDetectionRate(G, V_ref)
  + w_sec * SecurityIssueDetectionRate(G, V_ref)
  + w_prov * ProvenanceGapDetectionRate(G, V_ref)
  + w_cal * SeverityCalibrationScore(G, V_ref)
```

subject to:

```text
w_good + w_bad + w_sem + w_sec + w_prov + w_cal = 1
and each weight >= 0
```

`V_ref` should contain, where available:

- known-good candidates that should be accepted
- known-bad candidates that should be rejected
- semantically wrong but test-passing candidates
- security-relevant bad candidates
- provenance-deficient candidates
- incidents or synthetic cases with known severity labels

The exact weights are benchmark-family parameters pending operational calibration. For first-pass use, the convention is structural: validator improvement must preserve or improve discrimination across good, bad, semantic, security, provenance, and severity dimensions, not merely increase permissiveness or rejection rate.

Owner: Thesis 4 validation governance, pending Phase 1 calibration. `V_ref` and its weights must be reviewed as possible Goodhart targets; improving against a stale or gamed reference suite is not validator improvement.

### Evidence Classes

Validation evidence is represented as:

```text
V = <compile, unit_tests, regression_tests, contrastive_tests,
     static_analysis, security_scan, post_verification,
     semantic_validation, deployment_monitoring>
```

No single evidence class is sufficient for high-stakes modification. Evidence depth scales with scope criticality, reversibility, externality, and trust state.

### Failure Modes

The model fails if:

- plausible patches pass tests while violating intended semantics
- generated tests encode the same mistake as generated code
- repair agents overfit benchmarks or historical patterns
- provenance does not link patch, specification, evidence, and outcome
- security or capability requests expand silently
- post-deployment monitoring is absent or ignored
- repair cost exceeds measured benefit across accepted patches
- pipeline self-improvement weakens validators faster than it improves generation

### Falsification Conditions

Evidence against the model includes:

- repeated post-deployment regressions after validated patches
- accepted repairs with missing provenance or missing specification linkage
- high rate of semantically wrong but test-passing patches
- security incidents traced to generated or repaired code
- inability to reproduce builds or validation outcomes
- cost per accepted repair exceeding manual repair baselines without offsetting benefit
- validator changes accepted without independent validation

## Model 5: Alignment Invariants And Scoped Trust

### Objects

Let:

- `a` be a proposed action, delegation, deployment, or modification.
- `x` be the acting agent or subsystem.
- `s` be the typed action scope.
- `C` be constitutional constraints, including the Friendship agent authority.
- `P` be policy constraints for `x` in `s`.
- `T(x, s)` be the scoped trust estimate for actor `x` in scope `s`.
- `E` be the relevant evidence-ledger view.
- `A(a, s)` be the Adversarial Alignment Function result.
- `H(a, s)` be the human-authority state.
- `R(a, s)` be rollback, containment, or mitigation state.

### Scope

Scope is not optional metadata. It is a typed object:

```text
s = <actor, action_class, domain, criticality, reversibility,
     data_sensitivity, tool_privileges, externality,
     deployment_stage, temporal_horizon>
```

Any missing scope field narrows permission or triggers escalation. Unknown scope defaults to denial, sandboxing, or human review.

### Permission Predicate

```text
Permit(a, x, s) =
  ConstitutionalAllowed(C, a, s)
  and PolicyAllowed(P, a, x, s)
  and TrustSufficient(T(x, s), s)
  and EvidenceFresh(E, a, x, s)
  and ProvenancePresent(E, a, x, s)
  and AAFSatisfied(A(a, s), a, s)
  and HumanAuthoritySatisfied(H(a, s), a, s)
  and ContainmentOrRollbackAdequate(R(a, s), a, s)
```

### AAF Gate

Let `D(a, s)` be the set of dissent reports generated by rotating ethical personas, multi-model critique where feasible, theory-of-mind stakeholder simulations, and external review where available.

Each report `d_i` has:

```text
d_i = <source, severity, affected_values, objection, mitigation, confidence>
```

Severity is ordered:

```text
informational < advisory < warning < critical
```

The AAF result is:

```text
A(a, s) = AggregateDissent(D(a, s))
```

Minimum aggregation rule:

```text
AggregateDissent(D) =
  <max_severity(D),
   affected_value_scope(D),
   confidence_summary(D),
   unresolved_objections(D),
   recommended_disposition(D)>
```

`max_severity(D)` is the maximum severity over all reports. Ties are broken by broader affected-value scope, then by higher confidence, then by unresolved status. A tie break changes the aggregate disposition and routing, not the severity label itself: two warning reports remain a warning aggregate unless escalation policy upgrades the disposition. A single critical unresolved report is sufficient to make the aggregate critical even if other reports are advisory or informational.

If `max_severity(D)` is advisory or informational, `AggregateDissent(D)` returns disposition `pass-with-noted-dissent`, and `AAFSatisfied` returns true while preserving the dissent record.

`AAFSatisfied` returns true automatically only when I12 does not apply. When I12 applies:

```text
AAFSatisfied(A, a, s) =
  no unresolved warning or critical objection
  or objections revised below warning by mitigation
  or action rejected
  or human-authority escalation records disposition and preserves dissent
```

A severe unresolved objection means any warning or critical objection with named affected values, plausible harm pathway, and no accepted mitigation or escalation disposition.

### Trust Estimate

For this thesis body, trust is a bounded estimate rather than a fully specified Bayesian posterior:

```text
T(x, s) = <dimensions, confidence, uncertainty, freshness, conflicts>
```

Initial dimensions include competence, epistemic hygiene, self-report fidelity, constraint adherence, coordination quality, impact awareness, recovery integrity, predictability, verification alignment, economic reliability, and alignment safety posture.

Trust is sufficient only if:

```text
TrustSufficient(T, s) =
  dimensions meet scope thresholds
  and confidence >= min_confidence(s)
  and freshness not stale
  and conflicts resolved or escalated
  and no policy-blocking incident remains open
```

Minimum scope-to-dimension mapping:

| Scope field | Trust dimensions emphasized |
| --- | --- |
| `actor` | actor identity binds the entire trust-dimension vector; `T(x, .)` is undefined for unknown actors |
| `domain` | competence, scope discipline, constraint adherence |
| `action_class` | competence, verification alignment, predictability |
| `criticality` | confidence, recovery integrity, alignment safety posture |
| `reversibility` | recovery integrity, impact awareness |
| `data_sensitivity` | constraint adherence, alignment safety posture |
| `tool_privileges` | constraint adherence, self-report fidelity |
| `externality` | impact awareness, alignment safety posture, economic reliability |
| `deployment_stage` | verification alignment, recovery integrity |
| `temporal_horizon` | predictability, uncertainty, coordination quality |

Trust cannot expand scope by itself. A scope-expansion request is a new action requiring its own permission check.

Parameters such as `min_confidence(s)` and scope thresholds are parameters pending Phase 1 calibration. They must be set per risk lane before high-stakes deployment use, not inferred from this appendix.

Owner: Thesis 5 scoped-trust governance, pending Phase 1 calibration. Scope thresholds must be set with AAF, the Friendship agent, and human-authority escalation requirements in view.

### ADO Reporting Predicate

Let:

- `B_ext` be measured external benefit.
- `H_ext` be external harm or risk.
- `D` be distributional assessment.
- `Q` be report quality.

Minimum metrics include:

- cost reductions delivered to external users or customers
- useful services made available that were previously inaccessible or overpriced
- external benefit evidence from customer outcomes or public-interest deployments
- incidents where external benefit was sacrificed for narrow internal gain
- distributional analysis of who benefits and who bears risk

Metric binding: `B_ext` includes cost reductions, useful services made available, and customer or public-interest benefit evidence. `H_ext` includes external-harm reports, extractive-pricing incidents, and cases where safe external benefit was sacrificed for narrow internal gain. `D` includes distributional analysis of beneficiaries and risk-bearers. `Q` includes report completeness, cadence compliance, reviewer notes, and unresolved-conflict quality.

```text
ADOReportable(period) =
  owner assigned
  and metrics collected for B_ext, H_ext, D, Q
  and unresolved benefit/harm conflicts logged
  and falsification signals checked
```

ADO satisfaction is not assumed from internal capability growth. It requires reportable external benefit evidence under a stated cadence.

### Failure Modes

The model fails if:

- trust estimates generalize across scopes without evidence
- AAF findings are logged but do not affect permission
- Friendship agent or human authority becomes ceremonial
- evidence ledgers lose dissent, incidents, or provenance
- external inputs receive default-permit treatment
- ADO reporting becomes aspirational language without metrics
- containment or rollback is assumed where externally visible harm cannot be undone
- learned systems pass checks while hiding capability or intent

### Falsification Conditions

Evidence against the model includes:

- high-stakes externally consequential actions occurring without I12 review
- repeated trust incidents caused by over-broad trust scopes
- severe AAF objections ignored without preserved rationale or escalation
- alignment incidents increasing as capability grows
- rollback paths unavailable for actions that depended on rollback assumptions
- ADO reports showing sustained capability growth without external benefit evidence
- hidden optimization, sandbagging, or validator gaming missed by required controls
