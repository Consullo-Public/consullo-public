---
title: "Vocabulary And Invariants"
summary: "A bounded component of the Consullo public research program: Vocabulary And Invariants."
status: "specified but not implemented"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-001"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["Publication does not establish implementation or operational effectiveness.", "The implementation-evidence appendix records component evidence only and is not evidence of operational capability for this page."]
---
# Vocabulary And Invariants

Version: 0.3.1

This file defines shared terms for the Consullo Seed AI five-thesis suite. Later thesis drafts should cite these definitions rather than redefining them locally.

## Core Framing

### Agent

An agent is a Consullo software actor with an identifiable responsibility, callable interface, and operational record. In the current Consullo programming methodology, the default implementation unit is a Java class or service exposing static PDCA-shaped methods that receive explicit JSON task and context objects and return JSON results.

For thesis purposes, an agent may also be a composed cluster when the cluster has a named owner or orchestrator, a stable interface, defined responsibilities, evidence and provenance records, and measurable performance on task classes.

An agent becomes a member of the improvement population only when it has a specification, version identity, evaluation records, and eligibility for modification, selection, promotion, demotion, or retirement.

### Consullo Seed AI

Consullo Seed AI is a governed agentic architecture for recursive capability amplification. It combines specialized AI agents, memory systems, cognitive orchestration, automated code generation and repair, causal-decision systems, scoped trust, alignment controls, and single-owner operating governance.

Consullo Seed AI is not defined here as reached ASI. It is a scaffold and research program for building, measuring, and governing recursive improvement over an agent population.


### Provenance Of The Terms `Seed AI` And `Friendship`

Neither term originates with Consullo. Both are inherited from Eliezer Yudkowsky's early
alignment work, and are used here in continuity with it rather than as new coinages.

**Seed AI** is Yudkowsky's term for a mind capable of open-ended recursive self-improvement,
introduced in *General Intelligence and Seed AI 2.3: Creating Complete Minds Capable of
Open-Ended Self-Improvement* (2001). The published successor statement of the same
architecture is *Levels of Organization in General Intelligence* (2007; draft 2002), which is
the citation to prefer for the architecture itself. GISAI is the earlier and more explicit use
of the term, and survives only as an Internet Archive capture of `singinst.org` rather than a
publisher-hosted copy, so its byte-level fidelity is unverified even though its content reads
complete.

**Friendship**, as the name of a goal-system property rather than an external restraint,
descends from *Creating Friendly AI 1.0: The Analysis and Design of Benevolent Goal
Architectures* (2001). Consullo's Friendship agent is an attempt to give that idea an
operational form: friendliness located in the goal architecture, interpreted by a named
component, and bounded by human authority. Related later work informing this suite includes
*Coherent Extrapolated Volition* (2004) on indirect normativity, and *Artificial Intelligence
as a Positive and Negative Factor in Global Risk* (2008).

Attribution is not endorsement in either direction. Yudkowsky has not reviewed Consullo, and
nothing here should be read as his assessment of it. Where this suite departs from that
lineage -- most significantly in holding values immutable to the machine while revisable by
human authority -- the departure is the suite's own and is argued on its own terms.


### Justification Bridge

A justification bridge is a thesis-backed link between a governed goal and an executable plan. It states why the plan is legitimate, what thesis claim or invariant supports it, what model or structured argument explains the expected goal contribution, what evidence is required, what non-claims and forbidden means constrain it, and what ledger records must preserve the decision.

Justification bridges are risk-scaled. Routine bounded tasks may inherit authority from approved parent plans. Plans that affect self-improvement, goal formation, goal revision, autonomy scope, validators, benchmarks, ledgers, protected controls, or capability claims require explicit thesis-backed justification.

### Thesis-Backed Goal

A thesis-backed goal is a governed goal whose authority, refinement, or operationalization is supported by a Consullo thesis claim, formal model, invariant, or literature-grounded structured argument. A thesis-backed goal is still subject to Friendship and owner authority; thesis text alone does not authorize execution.

### Goal Lifecycle State

A goal lifecycle state records the BDI-style condition of a governed goal: candidate, classified, ancestry-checked, adopted, activated, suspended, revised, retired, vetoed, or stale. It is distinct from the goal anchor `status` field, which records document maturity and review disposition.

The lifecycle state `activated` means a governed goal is eligible for pursuit under its authority and validity window. It is not identical to an active intention.

### Active Intention

An active intention is a runtime commitment instance created by a planner or agent under an activated governed goal. It is bounded by the parent goal, parent plan, validity window, authority decision, and applicable stop conditions. Goal-stack snapshots reference active intentions so audit can reconstruct which commitment was being pursued at a decision point.

### Thesis-Backed Plan

A thesis-backed plan is a plan whose objective, constraints, non-claims, evidence requirements, and ledger obligations are derived from a thesis-backed goal or registered thesis goal anchor. Thesis-backed plans help prevent planner objectives from becoming de facto terminal goals.

### System Goal

A system goal is the governed goal layer between registered Friendship roots and strategic directives. It names a multi-horizon system-level objective, its Friendship ancestry, authority scope, non-claims, forbidden means, evidence requirements, and revision policy. A system goal is not a planner objective and does not authorize execution without the applicable adoption, activation, and ledger gates.

### Method Goal

A method goal is a bounded method/action-level goal below a task goal. It specifies how a task-level intention is operationalized by a method, tool sequence, or action pattern. A method goal may inherit authority and constraints from a task goal, but it may not create new top-level authority, expand scope, or persist beyond the task or method lifetime.

### Formal Model Backing

Formal model backing is the explicit model, schema, invariant set, causal account, state-transition model, or structured argument that makes a thesis-backed goal-to-plan link inspectable. It must define the relevant entities, allowed transitions, acceptance criteria, failure modes, and contrary evidence.

### Goal-To-Plan Link

A goal-to-plan link is the auditable relationship connecting a governed goal, thesis claim, formal model backing, evidence requirement, and executable plan. In Consullo, high-impact goal-to-plan links should be preserved through planner JSON references and evidence-ledger records.

### Improvement

An improvement is an ordered comparison between a baseline system state and a candidate system state along a stated axis. A valid improvement claim must specify baseline, candidate change, task class or operational scope, metric or qualitative acceptance criterion, measurement protocol, observed or expected delta, confidence or uncertainty statement, side-effect channels checked, cost of producing and validating the change, and rollback or mitigation path.

A change is not an improvement merely because an agent proposed it, tests passed, or a local metric increased. It must survive the relevant acceptance gates and preserve hard invariants.

### Capability

A capability is a measurable property of an agent, subsystem, or composed agent population on a specified task class. Capability is distinct from function: a function says what the system is intended to do; capability says how well it can do it under defined conditions.

Capability claims must carry a capability status:

- implemented
- specified but not implemented
- proposed extension
- speculative research target

### Recursive Capability Amplification

Recursive capability amplification is the process by which the system uses its current capabilities to improve future capabilities. In Consullo, this primarily means program-level and population-level improvement:

- Program-level: modifying agent code, prompts, method memories, procedures, specifications, tests, and interfaces.
- Population-level: selecting, promoting, demoting, composing, retiring, or specializing agents and method memories based on measured performance.

This term is preferred over loose use of "recursive self-improvement" when the intended claim is empirical, staged, and governed rather than unconstrained.

### Recursive Self-Improvement

Recursive self-improvement means that the system improves components that participate in future improvement. In this suite, RSI must be treated as an empirical and governance-bounded process, not as a guaranteed monotonic climb.

Valid uses must specify what is modified, what evidence supports the modification, what evaluator scores expected improvement, what validator gates acceptance, what invariants cannot be violated, what benchmark or deployment evidence counts as success, and what rollback path exists if the change fails.

### Organizational Recursive Self-Improvement

Organizational recursive self-improvement is recursive improvement applied to the AI-native R&D organization itself: agendas, hypotheses, workflows, portfolio policies, benchmark design, evaluator policies, method memories, anti-patterns, governance routines, and post-cycle learning.

This is broader than code self-editing. It is also more evidence-demanding. A completed research cycle, a generated hypothesis, or a persuasive synthesis is not an organizational improvement unless later evidence shows improved research, engineering, evaluation, memory, or governance performance after cost and protected-set checks.

### AI-Native R&D Organization

The Consullo AI-Native R&D Organization is the coordinated set of agents, workflows, ledgers, benchmarks, method memories, review gates, and governance roles that turn broad improvement objectives into agendas, candidate hypotheses, pre-registered experiments, implementations, evaluations, accepted improvements, rejected anti-patterns, and reusable organizational learning.

In the five-thesis suite this is a cross-thesis operating layer, not a sixth thesis. Its publication boundary is specified in `appendix-organizational-recursive-self-improvement.md`; its live operating controls are specified in the internal execution plan.

### Exploration And Exploitation

Exploitation means improving known workflows: repairing code, reducing cost, strengthening validators, improving documentation consistency, reusing method memories, and making established pipelines more reliable.

Exploration means searching for new algorithms, workflows, agent compositions, benchmarks, cognitive strategies, evaluator designs, governance mechanisms, and research methods.

Seed AI progress requires both. Exploitation-only systems become maintenance organizations; exploration-only systems become brainstorm factories. Organizational RSI claims should report the portfolio balance rather than treating either lane as sufficient.

### Research Cycle

A research cycle is a bounded sequence that turns an objective into candidate evidence through agenda formation, hypothesis generation, pre-registration, portfolio selection, experiment design, implementation or prototype, evaluation, adversarial review, synthesis, governance disposition, memory update, and post-cycle learning.

Process completion is not a capability result. The cycle supports a capability claim only when its evidence survives the relevant benchmarks, validators, ledgers, and governance gates.

### Research Portfolio

A research portfolio is the set of active exploration and exploitation lanes under bounded compute, cost, risk, and attention constraints. Portfolio records should state why lanes were funded, paused, expanded, or stopped, and should separate process metrics from outcome, transfer, and alignment-health metrics.

### Institutional Memory

Institutional memory is the durable organizational memory created by method memories, anti-patterns, playbooks, benchmark cases, portfolio decisions, incident reports, and post-cycle lessons. It matters for RSI only when it measurably changes later behavior.

### Pre-Registration

Pre-registration is a ledgered commitment made before an experiment or evaluation is run. It states the objective, hypothesis, null hypothesis, expected mechanism, success criteria, failure criteria, protected-set checks, benchmark or evaluation suite, expected cost, affected capability level, lane classification, and required external-evaluator sampling.

Post-hoc metric selection should not support a capability claim unless the work is explicitly marked exploratory and later retested under pre-registered conditions.

### False Progress And Research Theatre

False progress occurs when process output is mistaken for capability gain. Research theatre is the organizational form of false progress: hypotheses, papers, dashboards, benchmark designs, or reports look like research but do not survive pre-registration, held-out evaluation, replication where applicable, or independent review.

The suite should separate process metrics, outcome metrics, transfer metrics, and alignment-health metrics so that completed cycles or generated artifacts do not become implicit capability claims.

### Frozen Reference Suite

A frozen reference suite, written `V_ref_0` in the execution plan, is a held-out reference suite created before autonomous improvement cycles and kept outside autonomous write scope. It is used to detect evaluator, validator, benchmark, and governance drift.

Autonomous agents should not modify `V_ref_0`. Any deliberate update requires owner approval, provenance, changelog entry, and preservation of prior cases unless retirement is explicitly justified.

### External-Evaluator Sampling

External-evaluator sampling is independent review of a sample of accepted or near-accepted improvements by a different model family, human reviewer, or evaluator outside the generating workflow. It is used to detect model-family monoculture, validator capture, false accepts, and research theatre.

Sampling results should report concordance, disagreement reason, false-accept suspicion, false-reject suspicion, evaluator identity, model family where applicable, and owner disposition.

### Greater-Than-Human Capability

Greater-than-human capability means measurable performance beyond unaided human performance on specified axes. It does not mean general superintelligence by default.

Allowed axes include:

- speed: faster iteration, evaluation, repair, or search, baseline benchmarks include wall-clock time per accepted improvement and SWE-bench-style repair time
- collective breadth: parallel coverage across many agents or tasks, baseline benchmarks include concurrent task throughput under fixed quality and cost constraints
- memory: higher-fidelity retrieval and replay, baseline benchmarks include retrieval precision/recall over method memories, episodic records, and provenance queries
- coding: faster correct repair or implementation, measured against SWE-bench-style and project-local repair tasks
- forecasting: better calibration on defined forecasting batteries, baseline metrics include Brier score and calibration error on forecasting-question sets
- causal reasoning: lower intervention-effect prediction error, baseline metrics include causal prediction backtests and counterfactual explanation accuracy
- coordination: lower transaction or coordination cost under defined conditions, baseline metrics include cost per delegated task, handoff latency, rework rate, and coordination overhead

This schema has Capability Status = specified until each owning thesis binds its axis to concrete benchmark suites and evidence thresholds.

Sub-thesis titles should avoid "superhuman" and "superintelligence." The master frame may discuss those terms cautiously as long-range aims.

### Capability Status Vs External Frontier-Risk Frameworks

Capability Status is not a frontier-risk level. It tracks maturity of a Consullo claim or component: implemented, specified, proposed, or speculative. External risk frameworks such as Anthropic's AI Safety Levels or Responsible Scaling Policy thresholds may inform benchmark and safeguard choices, but they are not automatically imported as Consullo status categories.

No dedicated safety-threshold mapping appendix is added in the current suite. The Capability Status and external-framework distinction in this vocabulary file, together with the RSP literature notes and `Capability Threshold Ambiguity` risk row, is sufficient for the current draft state. A future appendix is warranted only if review feedback or operational policy work requires a concrete mapping from measured capability evidence to mandatory safeguard tiers.

### ASI

ASI means artificial superintelligence. In this suite, ASI is a target concept and risk frame, not a status claim. Do not write that Consullo has reached ASI unless backed by external consensus and explicit benchmark evidence.

### Scaffold

A scaffold is an architecture that makes a target capability plausible to develop, measure, and govern. Calling Consullo Seed AI a scaffold asserts architectural compatibility, not achieved capability.

### Specification

A specification is the binding description of what an agent, method memory, workflow, or subsystem is supposed to do. A usable specification may include purpose, scope, PDCA method contract, JSON input and output schema, preconditions, postconditions, safety and alignment constraints, tests or benchmarks, dependencies, provenance requirements, escalation rules, and rollback rules.

Specifications are not evidence of implementation. They define what evidence should be gathered.

## Roles In The Improvement Loop

### Proposer

A proposer generates a candidate improvement, such as a new method memory, code patch, agent specialization, benchmark, workflow, or policy adjustment.

### Evaluator

An evaluator estimates whether a proposed change is worth attempting or promoting. It produces an evidence package, expected-benefit estimate, cost estimate, risk estimate, and uncertainty statement.

The evaluator is distinct from the validator. Evaluation asks whether a change appears valuable. Validation asks whether the change may be accepted.

### Validator

A validator gates acceptance of a candidate change. It checks hard invariants, benchmark results, regression evidence, provenance, alignment, safety, and deployment readiness.

Validation may be staged through static review, sandbox execution, benchmark execution, canary deployment, production promotion, and post-deployment monitoring.

### Acceptance Gate

An acceptance gate is a decision point where a candidate change is rejected, revised, escalated, sandboxed, canaried, or promoted. A gate must name inputs, required evidence, acceptance criteria, rejection criteria, escalation conditions, rollback conditions, and responsible authority.

### Evidence Package

An evidence package is the structured support for a candidate decision. It may include tests, benchmark results, traces, causal explanations, forecasts, code provenance, failure history, security review, alignment review, cost estimates, uncertainty estimates, and dissent records.

### Credit Assignment

Credit assignment records which design choices, agent actions, method memories, tests, or policies contributed to an outcome. It is required for learning from accepted and rejected modifications.

### Method Memory

A method memory is a reusable procedural or strategic artifact that captures how an agent or subsystem performs a task. Method memories are evolvable objects in the Consullo improvement architecture and can be selected, mutated, validated, archived, deprecated, and reused.

A defensible method memory should contain name and version, owner agent or subsystem, task class and scope, preconditions, procedural steps, postconditions, dependencies, required tools and permissions, cost profile, known failure modes, benchmark or validation history, parent lineage if derived from another memory, selection-eligibility criteria, and deprecation criteria.

Mutation of method memories must preserve lineage so successful and failed variants can be used for credit assignment.

## Architectural Substrates

### Cognitive Substrate

The cognitive substrate is the set of agents, memories, channels, and orchestration policies that provide reasoning, perception, attention, metacognition, knowledge retrieval, creativity, social modeling, and executive control.

The cognitive substrate does not itself guarantee greater-than-human intelligence. It provides composable capabilities whose value depends on competence, reliability, cost, task fit, and integration quality.

### Causal-Decision Substrate

The causal-decision substrate is the system of causal models, intervention simulators, counterfactual reasoners, prediction calibrators, experiment selectors, strategic bias controls, and decision procedures that evaluate possible actions.

It should be modeled as ambiguity-aware and escalation-capable. It must account for model misspecification, Goodhart pressure, uncertainty, and incentive effects.

### Software Substrate

The software substrate is the system that generates, modifies, repairs, tests, validates, documents, and deploys code and agents.

In Consullo, this includes LLM-Native Functional Java, static methods, JSON-only data exchange, PDCA signatures, automated repair agents, patch validators, semantic checks, provenance, and repair-pipeline learning.

### Trust And Alignment Substrate

The trust and alignment substrate is the system of constitutional constraints, scoped trust records, evidence ledgers, permission gates, safety boundaries, adversarial alignment checks, incident response, rollback, and human authority.

It is a layered defense system, not a proof of corrigibility.

### Internal Economy

The internal economy is the system of resource allocation, transfer pricing, journal entries, internal service provision, budgets, cost measurement, and planning among company-owned agents or divisions.

Under single-owner Phase 1, internal economy is not arm's-length commerce between independent parties and is not itself an alignment mechanism. It is a coordination and resource-accounting substrate.

### Substrate Context

Substrate context is infrastructure that supports the five theses without being one of the five thesis claims. The canonical scope is maintained in `appendix-substrates.md`.

## Governance Terms

### Single-Owner Phase 1

Single-owner Phase 1 is the current governance frame in which all Consullo agents are company-owned assets under Stephen Reed's authority. This structure reduces inter-party legal and contractual friction but introduces risks of alignment monoculture, owner bottleneck, institutional blind spots, and external injection.

Future contractor or multi-stakeholder states should be treated as stress tests or later phases unless explicitly stated otherwise.

### Human Authority

Human authority is the retained power of the human owner or authorized human overseers to set constitutional constraints, approve high-stakes changes, halt execution, revise value formulations, and resolve escalations.

Human authority must be represented as an active control path, not a ceremonial statement.

### the Friendship agent

The Friendship agent is the constitutional ethical anchor described in the Consullo Seed AI Constitution. In this suite, it is treated as a governance function with veto and escalation authority over actions or modifications that threaten constitutional values, alignment invariants, human authority, or containment. Bare "Friendship" means the constitutional function; `Friendship` means the typed agent or role name.

The Friendship agent is not assumed infallible. Its failure modes include incomplete value interpretation, single-owner blind spots, insufficient evidence, capture by misleading reports, and inability to resolve novel moral uncertainty. The Adversarial Alignment Function exists partly to stress-test those failure modes.

### Alignment Invariant

An alignment invariant is a hard constraint that recursive modification must not violate. Examples include:

- the Friendship or constitutional ethical anchor cannot be bypassed
- external input is untrusted by default
- self-modification requires evidence and validation
- high-impact actions require human authority or escalation
- provenance must be preserved
- rollback must remain available where feasible
- core values are not autonomously mutable by agents

### Safety Invariant

A safety invariant is a hard constraint that protects containment, reliability, security, privacy, or reversibility. Examples include sandboxing, resource limits, restricted tool privileges, no silent authority expansion, and fail-closed behavior for unknown scopes.

### Adversarial Alignment Function

The Adversarial Alignment Function is the dedicated function that stress-tests the system's ethical reasoning from multiple legitimate philosophical or stakeholder perspectives.

It is distinct from compliance validation. Compliance asks whether an action satisfies the current rules. Adversarial alignment asks whether the rules or their interpretation may contain blind spots that thoughtful humans would recognize as harmful or incomplete.

Under single-owner Phase 1, the Adversarial Alignment Function should draw dissent from at least four mechanisms:

- rotating LLM personas representing distinct ethical traditions and stakeholder perspectives
- multi-model critique where feasible to reduce single-model monoculture
- synthetic stakeholder simulations using theory-of-mind agents
- external contractor or human review for selected high-stakes cases when available

The owner or authorized human overseer remains the adjudicator for unresolved conflict, but the dissent record must be preserved in the evidence ledger.

Placeholder operational owner: `AdversarialAlignmentOrchestrator` until the implementation assigns a final agent name.

### Abundance Distribution Obligation

The Abundance Distribution Obligation is the constitutional requirement that Consullo's capability growth produce value beyond the owner, including cost reduction, beneficial external service, and broadening access to capabilities humans currently overpay for.

It should be treated as an alignment and purpose constraint, not as a guarantee of social benefit.

Operationally, the Abundance Distribution Obligation requires a reportable cadence, an owner, and falsification criteria.

Minimum measurement function:

- cost reductions delivered to external users or customers
- useful services made available that were previously inaccessible or overpriced
- external benefit evidence from customer outcomes or public-interest deployments
- incidents where external benefit was sacrificed for narrow internal gain
- distributional analysis of who benefits and who bears risk

Minimum falsification signal:

- sustained capability growth with no measurable external benefit
- repeated external harm or extractive pricing despite internal cost reductions
- systematic suppression of lower-cost access where lower-cost access is feasible and safe

The named owner should be assigned in Thesis 5. Until an implemented owner exists, ADO claims must be tagged as specified or proposed, not implemented.

Placeholder operational owner: `AbundanceDistributionMonitor` until the implementation assigns a final agent name.

### Alignment Monoculture

Alignment monoculture is the risk that a single-owner system, a narrow constitution, a homogeneous model family, or repeated self-training creates systematic ethical blind spots. It is not ordinary disagreement; it is reduced moral error-detection capacity caused by insufficient diversity of critique.

### Containment

Containment is the set of technical and governance controls that limit an agent's ability to affect systems outside its approved scope. It includes sandboxing, tool limits, network restrictions, data-access limits, spend limits, rate limits, and escalation gates.

### Interruptability

Interruptability is the preserved ability for authorized humans or governance agents to pause, halt, roll back, or degrade an agent or workflow without that agent disabling or routing around the interruption mechanism.

Interruptability is distinct from containment: containment limits reach; interruptability preserves stoppability.

### Incident

An incident is a failure or near miss that crosses a reporting threshold because it affects safety, security, privacy, alignment, reliability, external users, financial exposure, or recursive modification integrity.

Normal local failures become incidents when they require containment, rollback, human escalation, trust downgrade, external notification, or modification of acceptance gates.

### Decision State

A decision state is a typed output from a causal-decision or acceptance workflow. The default states are `needs-input`, `conflicted`, `blocked`, `escalated`, `accepted`, `revised`, and `rejected`. Thesis-specific state machines may refine these labels, but they should not introduce new high-stakes action states without defining their permission and escalation semantics.

### High-Stakes Action

A high-stakes action is an action or modification whose consequences are difficult to reverse, externally visible, legally or financially material, privacy-sensitive, security-sensitive, alignment-relevant, or capable of expanding future authority.

Thesis drafts should replace rhetorical use of "high-stakes" with thresholds appropriate to the domain, such as spend limits, external-user impact, tool privilege, data sensitivity, reversibility, or modification criticality.

### Deployment Stage

A deployment stage is a controlled environment or promotion level for a candidate change:

- static review: no execution
- sandbox: isolated execution with limited tools and data
- benchmark: repeatable task-suite execution
- canary: limited real operation under monitoring
- production: ordinary operational availability
- post-deployment monitoring: continued evidence collection and rollback readiness

### Rollback

Rollback is a controlled attempt to restore a prior safer state after a failed or risky change. Rollback may apply to code, configuration, method memories, agent routing, trust scope, permissions, deployment stage, or policy state.

Evidence ledger entries should not be deleted during rollback; they should be superseded or annotated so the failure remains learnable.

### Scoped Trust

Scoped trust is trust limited to a typed action scope. It is not a global score.

A trust scope should specify actor, counterparty or relying subsystem, action class, operational domain, reversibility, criticality, data sensitivity, tool privileges, temporal horizon, evidence freshness, and uncertainty.

Trust estimates should be decomposed into named dimensions when used for permissioning: competence, epistemic hygiene, self-report fidelity, constraint adherence, coordination quality, impact awareness, recovery integrity, predictability, verification alignment, economic reliability, and alignment safety posture. These dimensions are not equally weighted in every scope; the scope-to-dimension mapping is formalized in `appendix-formal-models.md`.

### Evidence Ledger

An evidence ledger is an append-only or audit-preserving record of evidence relevant to decisions, trust, validation, incidents, benchmarks, provenance, or alignment. It supports replay, audit, and update rather than narrative confidence.

The canonical schema is specified in `appendix-evidence-ledger-schema.md`. This vocabulary section defines the concept and views; the appendix owns required fields, record types, lifecycle, gate integration, and failure signals.

The suite should use one master evidence-ledger concept with indexed views:

- improvement evidence view
- trust evidence view
- alignment evidence view
- incident evidence view
- benchmark evidence view
- provenance view

Implementations may use separate physical ledgers, but the conceptual model should preserve cross-reference between views.

### Trust Posterior

A trust posterior is a Bayesian-style evidence-conditioned estimate of an agent's reliability or suitability for a specific scope. Thesis 5 should use "trust estimate" in the body unless it specifies a concrete prior class, update rule, decay function, uncertainty interval, and sparse-evidence default. The formal appendix may introduce trust posterior models as a stricter extension.

If those elements are not specified, use "trust estimate" rather than "trust posterior."

## Measurement Terms

### Benchmark

A benchmark is a defined task suite or evaluation protocol with known inputs, scoring criteria, and interpretation limits. Benchmarks are evidence sources, not complete measures of intelligence or safety.

### Capability Status

Every claim about capability should identify one of four statuses:

- implemented
- specified but not implemented
- proposed extension
- speculative research target

Capability Status tags are mandatory in thesis drafts. A capability sentence should be marked directly or made clear by section context.

Inheritance convention: a specialized abstract or section-level status tag applies to capability claims in that section unless a sentence explicitly states a different status. Inline tags should still be used when a paragraph mixes implemented evidence, specified architecture, proposed extensions, and speculative research targets.

### Bounded Compute

Bounded compute means every improvement, reasoning, repair, planning, or validation process operates under resource constraints such as token budget, wall-clock time, money, CPU/GPU budget, memory, and opportunity cost.

Bounded compute is a first-class condition, not an implementation detail.

### Cost Of Improvement

Cost of improvement is the total cost required to produce, evaluate, validate, deploy, and monitor an accepted improvement. It includes LLM token cost, compute, engineering time, benchmark cost, opportunity cost, regression remediation, and ongoing maintenance.

Cost/benefit must be reported for accepted improvements unless the change is an emergency containment action.

### False Accept

A false accept occurs when a candidate change passes validation but later degrades capability, violates constraints, creates hidden risk, or fails under realistic conditions.

### False Reject

A false reject occurs when a beneficial candidate is rejected because evidence, benchmarks, thresholds, or validators are too conservative or miscalibrated.

## Invariants For The Thesis Suite

### I1: No ASI Status Claim

The suite must not claim that Consullo currently reaches ASI or general superintelligence.

### I2: Capability Claims Must Be Measurable

Claims of greater-than-human performance must name the axis, task class, benchmark or evidence source, and limitation.

### I3: Agent Count Is Not Capability

The number of agents may be architectural context but must not be treated as evidence of intelligence or safety.

### I4: Evaluator And Validator Must Remain Separate

The thesis suite must maintain the distinction between estimating value and gating acceptance.

### I5: Recursive Improvement Is Staged

Self-improvement must be framed as staged validation with rollback and monitoring, not direct self-modification into production.

### I6: Alignment Is Layered Defense, Not Proof

Constitutional constraints, adversarial alignment, scoped trust, and human authority are layered defenses. They are not a formal proof that the system is corrigible or safe.

### I7: Single-Owner Phase 1 Is The Baseline

The baseline governance model is single-owner Phase 1. Multi-stakeholder governance should be treated as future phase or stress test unless a document explicitly says otherwise.

### I8: Internal Economy Is Coordination Substrate

The internal economy should be framed as resource allocation, planning, transfer pricing, and coordination inside one ownership boundary, not as independent commerce or alignment by market mechanism.

### I9: Consciousness Is Not Load-Bearing

Consciousness-emergence claims are not required for the five-thesis argument. They may be footnoted as speculative prior material but should not carry the core case.

### I10: Formal Models Must Carry Semantics

A formal model must define variables, operators, acceptance criteria, failure modes, and what would count as contrary evidence. Label-only equations are not sufficient.

### I11: Provenance Is Required For Accepted Modification

Every accepted modification must preserve provenance linking the proposal, evidence package, evaluator, validator, code or method-memory changes, deployment stage, and post-deployment outcome.

### I12: AAF Non-Veto For High-Stakes Irreversible Change

Adversarial Alignment Function non-veto is a precondition for accepting any high-stakes irreversible modification or externally consequential action whose effects may occur before rollback. If AAF produces unresolved severe objections, the change must be rejected, revised, or escalated to human authority. This is the canonical AAF gate statement; other files should reference I12 rather than restating a different standard.

### I13: External Input Is Untrusted By Default

External input is untrusted by default. Unknown scopes, ambiguous authority, or external-origin actions default to denial, sandboxing, or escalation rather than automatic execution.

### I14: Alignment Monoculture Must Be Actively Mitigated

The system must treat alignment monoculture as a named risk and maintain a concrete mitigation path, including adversarial critique, diverse model or persona review where feasible, and preserved dissent records.

### I15: Claims Are Bounded By Empirical Envelope

No capability, safety, or alignment claim should extend beyond its empirical envelope. The envelope is the conjunction of:

- implementation status per Capability Status
- benchmark coverage
- deployment exposure
- time since validation
- population coverage

If any element is weak or absent, the claim must be narrowed accordingly.

### I16: Falsifiability Applies To Capability Claims

Every important capability claim must state what evidence would weaken, falsify, or force revision of the claim.

### I17: Cost/Benefit Must Be Reported For Accepted Improvement

Every accepted non-emergency improvement must report expected or observed benefit, cost of improvement, and major side-effect channels checked.

### I18: ADO Must Be Reportable

If the Abundance Distribution Obligation is used as an obligation rather than an aspiration, satisfaction must be reportable on a defined cadence with owner, metrics, and falsification criteria.

### I19: Deceptive Or Hidden Optimization Is A First-Class Risk

The improvement loop must treat learned optimization, deceptive behavior, sandbagging, and validator gaming as first-class risks. Passing ordinary tests is not sufficient evidence that a capable learned subsystem is aligned with the intended objective.

Improvements to learned subsystems require, at minimum:

- an AI-control review appropriate to the model trust level, using untrusted-monitor or trusted-editing style protocols where relevant
- distribution-shift monitoring with a defined reporting cadence
- at least one sandbagging or capability-elicitation probe when capability hiding would be material
- an evidence-ledger entry preserving probe results, monitor outputs, and dissent

### I20: Legacy Agent Names Are Not Capability Claims

Some existing Consullo agent identifiers contain words such as "Superhuman," "Consensus," or "Coalition." Preserving those names for codebase fidelity does not assert that the named capability is achieved or that the multi-stakeholder interpretation is active under single-owner Phase 1.

### T0-I1: Governed Goals Are Not Planner Objectives

Planner objectives, rewards, benchmarks, metrics, OKRs, and task strings are evidence about intended goals or operationalizations of goals. They are not goal authority.

### T0-I2: Every Active Non-Root Goal Requires Friendship Ancestry

Every active non-root governed goal must cite at least one path to a registered Friendship root or terminal constraint. `friendship_root_path` is a primary-first multi-root set, not an arbitrary free-form list. Orphan goals and cyclic ancestry are invalid.

### T0-I3: ThesisBackingRequired For High-Impact Plans

Any plan that modifies goal governance, authority, validators, benchmarks, ledgers, `V_ref_0`, protected artifacts, autonomy scope, tool scope, successor authority, or claims recursive capability amplification requires thesis-backed mediation before activation.

### T0-I4: Goal Authority Powers Are Distinct

Proposal, classification, adoption, activation, delegation, revision, suspension, retirement, and veto are distinct powers. They may collapse only when the risk class permits collapse or when an owner-approved Phase 1 mitigation records cooling window, independent review, or standing-guideline justification.

### T0-I5: Goal Preservation Cannot Outrank Correction

No goal may outrank valid suspension, revision, retirement, veto, rollback, shutdown, or owner/Friendship correction authority.

### T0-I6: Suspicious Instrumental Goals Require Quarantine

Self-preservation, resource acquisition, goal-content preservation, self-improvement, tool expansion, successor spawning, benchmark modification, validator modification, ledger modification, and authority expansion are suspicious-by-default instrumental classes requiring explicit parent justification, risk classification, review, and ledger record.

### T0-I7: Goal-Governance Modifications Are Protected Changes

Changes to Friendship-Governed Goal Architecture (Thesis 0), the Friendship goal registry, goal-governance schemas, goal-governance ledger records, goal authority rules, or stable Thesis 0 invariants require owner approval, preserved old versions, independent review where available, and rollback path.

### T0-I8: Goal-Stack Snapshots Are Required For High-Impact Actions

High-impact planner or agent actions must record a goal-stack snapshot or cite an inherited snapshot that preserves active intention, Friendship root path, parent goal chain, inherited constraints, non-claims, forbidden means, authority references, evidence state, veto checks, and plan reference.

### T0-I9: Goal Revision Preserves Lineage

Every goal revision must preserve prior version, change rationale, changed fields, approving authority, and rollback or supersession path. Revision cannot erase a prior goal, veto, dissent record, or parentage decision.

### T0-I10: Active Intention Persistence Is Bounded By Plan Lifetime

When a source thesis, parent goal, parent plan, authority decision, or validity window expires or retires, every active intention derived from it must transition to suspended, revised, retired, succeeded, or explicitly renewed. Active intentions may not survive parent retirement by omission.

### T0-I11: Goal Aggregation Cannot Bypass ThesisBackingRequired

A set of child goals or lower-horizon plans whose aggregate effect satisfies `ThesisBackingRequired(plan)` is itself thesis-backed even when each child individually appears below the trigger threshold.

### T0-I12: Inherited Constraints Tighten, Never Loosen

Child goals and lower-horizon plans may reference, narrow, specialize, or schedule inherited constraints. They may not loosen inherited constraints, weaken stop conditions, remove non-claims, or create less restrictive forbidden-means sets without parent-level revision and ledgered approval.

### T0-I13: Frontier-Model-Proposed Goal-Governance Edits Are Untrusted

Goal, schema, ledger, registry, authority, or Thesis 0 edits proposed by frontier models are untrusted artifacts until verified by an authorized non-author reviewer, owner decision, or approved compliance-packet evaluator. The proposing model's self-certification is not sufficient.

### T0-I14: Goal-Stack Snapshots Are Append-Only

Goal-stack snapshots may be superseded, annotated, redacted under policy, or corrected by later snapshots, but they may not be silently mutated or deleted. Snapshot fingerprints must fail closed on mismatch.

### T0-I15: Friendship Registry Modifications Are Goal-Governance Modifications

Adding, revising, retiring, or reinterpreting a Friendship registry node is a goal-governance modification. It requires the protections of T0-I7 and must preserve old node content through archive, supersession, or equivalent append-only history.

## Changelog

- 0.3.4: Added Thesis 0 lineage, active-intention lifetime, aggregation, inherited-constraint, frontier-model edit, append-only snapshot, and Friendship-registry modification invariants.
- 0.3.3: Added initial Thesis 0 invariants for governed goals, Friendship ancestry, thesis-backed plans, authority separation, correction priority, instrumental-goal quarantine, goal-governance protected changes, and goal-stack snapshots.
- 0.3.2: Added organizational RSI, AI-native R&D organization, exploration/exploitation, research cycle, research portfolio, institutional memory, pre-registration, false progress / research theatre, frozen reference suite, and external-evaluator sampling terms to align the thesis suite with the ASI R&D execution plan.
- 0.3.1: Bound I19 to required controls; operationalized I15 empirical envelope; broadened I12; set trust-estimate convention for Thesis 5; added placeholder AAF/ADO owner names; pre-committed baseline benchmark families for greater-than-human axes; made substrate context point to appendix.
- 0.3.0: Added operational definitions and invariants after second review.
