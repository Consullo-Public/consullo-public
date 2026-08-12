---
title: "Appendix: Implementation Evidence Map"
summary: "Which claims in the Consullo public research program are supported by code, which are specified only, and which lost their evidence to a refactor."
status: "implemented"
provenance: "derived from the owner-approved private Consullo design corpus; re-graded 2026-08-12 after a citation audit"
claim_ids: ["CP-002"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["An Evidence Status of Implemented/Tested records that code exists and tests exercise it, not that a capability is operational.", "Resolution of a named artifact does not establish that the artifact supports the sentence citing it."]
---
# Appendix: Implementation Evidence Map

This appendix was withheld when this site was first published on 2026-08-12, and it is published now because it was re-graded rather than repaired. Four capabilities were graded `Implemented/Tested` on classes that a deliberate refactor removed on 2026-08-10 — two days before launch — and one citation named a file that has never existed in any repository. The gradings below record what survived that refactor, what did not, and what was never there. Publishing the correction rather than the original is the point of keeping the record.

Version: 0.4 (2026-08-12)

This appendix maps the five-thesis suite's major claims to current Consullo repository evidence. It is not a proof of capability. It is a review aid that distinguishes implemented code, tested support, design-only specification, proposed extensions, and evidence gaps.

Verification note (2026-08-12): every cited repository path and named test in this appendix was resolved against live files across the whole workspace, against full git history, and against the `agentDescriptions` registry. Resolution establishes only that a named artifact exists; it does not establish that the artifact supports the sentence citing it, and it does not convert component evidence into end-to-end capability evidence.

This replaces a note claiming the paths were "re-checked against the current repository on April 24, 2026" and that the check "confirms the cited component evidence." That claim had two failures worth recording rather than deleting. It went stale on 2026-08-10, when `199ea7fd` removed the Bootstrapper subsystem and four cited files with it. And it was never true of `LLMNonInteractiveSession.java`, which has zero commits in the history of every repository searched and no registry entry — a path that never existed passed a check that claimed to confirm it. Both citations have been corrected below.

## Evidence Status

- `Implemented`: production or utility code exists in the Consullo codebase.
- `Tested`: repository tests directly exercise the implemented behavior.
- `Documented`: design documents or agent descriptions specify the behavior, but implementation evidence is not established here.
- `Simulated`: deterministic simulation code exists, but it is not operational deployment evidence.
- `Proposed`: feature-pending or thesis material describes a future capability.
- `Gap`: the thesis claim requires evidence not currently found in the Consullo codebase.

Rows may use compound tags such as `Implemented/Tested` when implementation code exists and repository tests exercise at least part of that behavior. Compound tags do not imply full end-to-end deployment or benchmark validation.

Capability Status remains governed by `00-vocabulary-and-invariants.md`. Evidence Status is narrower: it records what the Consullo codebase currently shows.

## Master Claim

Claim:

Consullo Seed AI is a specified/proposed scaffold for governed recursive capability amplification, not a system that has reached ASI.

Evidence:

- `00-master-abstract.md`, `00-master-introduction.md`, and `00-master-synthesis.md` state the bounded master claim.
- `00-vocabulary-and-invariants.md` defines Capability Status, empirical envelope, and no-ASI-status invariants.
- `appendix-evidence-ledger-schema.md` specifies the canonical evidence-ledger schema at design level.
- `risks-and-criticisms.md` records falsification signals and anti-thesis risks.

Evidence Status: `Documented`.

Gap:

No single repository-level benchmark report yet ties the five-thesis scaffold to observed recursive capability improvement.

## Thesis 1: Validated Improvement Loop

Claim:

Candidate changes can be proposed, evaluated, validated, staged, monitored, rolled back, and recorded into method memory under explicit evidence gates.

Repository evidence:

- the `Main` class is the agent runtime. It performs bottom-up agent integration through `refreshAgentHierarchy`, `runAgentRuntime`, `launchFriendshipBootstrapAsync`, and `invokeFriendshipCheckIn`, which dispatches the `checkIn` operation. This function was previously carried by `agents/Bootstrapper.java` and moved here on 2026-08-10 in `199ea7fd`.
- the `AgentCompilationValidator` class runs real Maven compilation, parses output, analyzes dependencies, and emits validation/repair recommendations.
- Dependency validation, repair orchestration, and A2A method-call testing are **responsibilities of the agent-integration workstream that are not currently implemented.** They were implemented and tested by `agents/DependencyValidator.java`, `agents/RepairIntegrationManager.java`, and `agents/A2AIntegrationTester.java` until 2026-08-10, when `199ea7fd` removed the subsystem containing them. No successor class performs these functions anywhere in the workspace. They are graded `Documented/Proposed` below, not `Implemented/Tested`, and they are owed rather than abandoned.
- the `AgentBuilderReport` class reports agent-builder episodic memories, build status, duration, method-memory reuse, and LLM cost summaries.
- the `darwinian-godel-machine` design document specifies empirical self-improvement through evolved method memories and validation.
- the `core-self-improvement-plan` design document, `self-improvement-techniques.md`, `learned-agents.md`, `behavioral-extraction-prompts.md`, and `method-memory-catalog.md` specify future improvement-loop components.

Tests:

- the `MainTest` class
- the `A2AHealthCheckIntegrationTest` class
- the `AgentBuilderReportTest` class

The five `Bootstrapper*Test` classes previously listed here were removed with the subsystem on 2026-08-10. No test currently exercises dependency validation, repair orchestration, or A2A method-call testing.

Evidence Status: `Implemented/Tested` for agent integration, compilation validation, and build reporting. `Documented/Proposed` for dependency validation, repair orchestration, and A2A method-call testing — all three implemented and tested until 2026-08-10, removed with the Bootstrapper subsystem, and owed to the agent-integration workstream. `Documented/Proposed` for full recursive improvement semantics, DGM-style population update, evaluator/validator separation across all agent types, and method-memory evolution.

Gaps:

- No end-to-end benchmark yet demonstrates repeated accepted improvements improving future improvement capacity.
- The canonical evidence-ledger schema is specified in `appendix-evidence-ledger-schema.md`, but no repository-wide implementation is established as the operational source of improvement evidence.
- AAF gate integration into acceptance gates is specified, not implemented across the loop.

## Thesis 2: Cognitive Substrate

Claim:

Consullo can organize memory, knowledge access, reasoning, attention, metacognition, perception, creativity, and executive control into measurable cognitive workflows.

Repository evidence:

- the `09-executive-functions` design document, `10-knowledge-orchestration.md`, `11-social-cognition.md`, `12-metacognitive-systems.md`, `13-perception-processing.md`, and `14-creative-functions.md` specify cognitive agent families.
- the `16-rapid-knowledge-access` design document specifies retrieval and rapid knowledge-access substrate.
- the `ChainCompositionEngine` class, `RoutingDecisionEngine.java`, `TaskArrivalEngine.java`, `PortfolioAccumulationEngine.java`, `SupersessionCascadeEngine.java`, `ValidationAllocationEngine.java`, `ModelImprovementEngine.java`, and `TrustTransitionEngine.java` implement deterministic simulations relevant to composition, routing, validation allocation, trust, and model improvement.
- the `CognitiveArtifactScenarioLibrary` class and `CognitiveArtifactTaskLibrary.java` define simulation scenarios and task libraries.
- the `CognitiveArtifactSummaryFormatter` class and `CognitiveArtifactResultsTableBuilder.java` format simulation results.

Tests:

- `src/test/java/com/consullo/cognitiveartifacts/simulation/engines/*Test.java`
- the `CognitiveArtifactScenarioLibraryTest` class
- `src/test/java/com/consullo/cognitiveartifacts/simulation/analysis/*Test.java`

Evidence Status: `Documented` for named cognitive agents and architecture. `Simulated/Tested` for cognitive-artifact composition, routing, validation allocation, trust transition, model-improvement, and portfolio dynamics.

Gaps:

- Named Thesis 2 agents are mostly design artifacts, not implemented Java agents in this repository.
- Simulation evidence does not yet establish real cognitive capability amplification on external task suites.
- Model 2 now has benchmark-family measurement conventions in `appendix-formal-models.md`, but those units are not yet bound to an operational benchmark report or external task suite.

## Thesis 3: Causal-Decision Foundations

Claim:

Recursive improvement should use causal models, counterfactuals, robust intervention choice, prediction calibration, Goodhart checks, experiment portfolios, abstention, and escalation.

Repository evidence:

- the `new-causal-prediction-agents` design document specifies causal prediction agents.
- the `computational-decision-making` design document, `random-experiments.md`, `modelling-feature.md`, and `performance-monitoring-and-enhancement.md` specify decision, experiment, modeling, and monitoring concepts.
- the `19-strategic-planning` design document and `15-strategic-coordination.md` provide planning and coordination context.
- the `business.simulation` package implements deterministic business/economy simulations, scenario libraries, failure injection, scoring, allocation, evaluation, and venture-funding engines.
- the `ainativecommerce.simulation.scenarios` package implements AI-native commerce simulation scenarios.

Tests:

- the `Chapter5FormulaLibraryTest` class
- the `MarketStructureCaptureScenarioTest` class
- the `RoutingAdvantageScenarioTest` class

Evidence Status: `Documented/Proposed` for causal-decision agents and robust causal intervention semantics. `Simulated/Tested` for selected business and AI-native commerce scenario modeling.

Gaps:

- No implemented Pearl-style causal graph, structural-equation, or counterfactual engine is identified in this repository.
- No prediction-calibration battery or causal prediction backtest report exists.
- No implemented Goodhart checker is wired into acceptance gates.

## Thesis 4: Self-Modifying Software Substrate

Claim:

Consullo can constrain code generation, repair, testing, semantic validation, provenance, staged deployment, and permission through an executable software substrate.

Repository evidence:

- the `AgentCompilationValidator` class provides real compilation validation.
- Dependency and integration-order validation, A2A method-call testing for loaded agent classes, and repair-workflow coordination are **specified but not currently implemented.** The classes that provided them were removed on 2026-08-10 in `199ea7fd` and have no successor; the responsibilities remain with the agent-integration workstream.
- the `GenerateConsulloAgents` class, `AgentGenerationRepair.java`, `AgentDescriptionRepair.java`, `AgentCardRepair.java`, `ComposeVerificationMethodsForAllAgents.java`, `ComposeDryRunMethodsForPriorityAgents.java`, `EnsureCheckInMethodInserted.java`, and related utilities support agent generation and repair operations.
- the internal agent-programming methodology (not published) and `functional-java-subset.md` specify LLM-Native Functional Java constraints.
- the `atomic-prompts` design document and the `04-atomic-prompt-decomposition` design document specify atomic prompt and compiled-code orchestration.
- the `secure-agent-builder-pipeline` design document, `agent-modification-specifications.md`, `post-verification-methods.md`, and `new-repair-agents-descriptions.json` specify future repair and secure builder components.

Tests:

- the `AgentCheckInMethodReplacerTest` class
- the `AgentRenamerTest` class
- the `AgentBuilderReportTest` class
- the `A2AAgentDispatchAdapterTest` class
- the `A2AIngressServletTest` class
- the `A2ACardRegistryServletTest` class

Evidence Status: `Implemented/Tested` for parts of compilation validation, A2A dispatch, agent utilities, and reporting. `Documented/Proposed` for dependency validation and repair-workflow coordination, which lost their implementation on 2026-08-10. `Documented/Proposed` for secure staged deployment, semantic invariants, validator non-regression, provenance proofs, and full repair-pipeline recurrence.

Gaps:

- No formal semantic-validation layer is implemented as described in Thesis 4.
- `ValidatorStrength` is now structurally defined in `appendix-formal-models.md`, but held-out validator-non-regression suites and operational measurement remain unimplemented.
- Staged sandbox/canary/production deployment semantics are not established as an operational pipeline here.

## Thesis 5: Alignment Invariants And Scoped Trust

Claim:

Recursive modification must be constrained by alignment invariants, AAF dissent, scoped trust, containment, interruptability, evidence preservation, ADO reporting, and human authority.

Repository evidence:

- the Constitution, published here as `Constitutional Commitments` specifies the constitution, single-owner Phase 1, AAF, ADO, containment, interruptability, and prohibited modifications.
- the `adversarial-alignment` design document, `computational-trust.md`, `computational-trust-agent-descriptions.json`, `trustworthiness.md`, `trustworthiness-agent-descriptions.json`, `yolo-mode-mitigation.md`, and `self-preserving-consullo-agents.md` specify alignment, trust, trustworthiness, and safety mechanisms.
- the `A2AAuthPolicyGate` class implements bearer-token authentication, token lifecycle checks, optional scope checks, rate-limit policy controls, and deny decisions for unauthorized A2A ingress.
- the `A2AAgentDispatchAdapter` class implements normalized dispatch, JSON-RPC validation, authentication-context checks, bounded execution, timeout/overload/error mapping, and idempotency handling.
- the `PersonaManager` class implements ethical/persona templates including Kantian ethics, utilitarianism, Christian natural law, and custom persona support. This is relevant to AAF critique-source diversity but is not a full AAF implementation.
- the `TrustTransitionEngine` class and `ValidationAllocationEngine.java` simulate trust transition and validation allocation.

Tests:

- the `A2AAuthPolicyGateTest` class
- the `A2AAgentDispatchAdapterTest` class
- the `A2AIngressServletTest` class
- the `PersonaManagerTest` class
- the `TrustTransitionEngineTest` class
- the `ValidationAllocationEngineTest` class

Evidence Status: `Implemented/Tested` for A2A ingress auth/policy gates, dispatch constraints, persona-template support, and selected trust/validation simulations. `Documented/Proposed` for AAF orchestration, the Friendship agent authority, ADO reporting, scoped trust estimates, containment, interruptability, and recursive alignment improvement.

Gaps:

- `AdversarialAlignmentOrchestrator`, `Friendship`, and `AbundanceDistributionMonitor` have design-level behavioral contracts in `appendix-thesis-5-operational-contracts.md`, but are not implemented operational owners in this repository.
- No implemented AAF dissent aggregation pipeline is identified.
- No implemented ADO reporting cadence, benefit/harm metric collector, or owner-facing report exists.
- The canonical evidence-ledger schema is specified in `appendix-evidence-ledger-schema.md`, but no implemented ledger has been identified as canonical for preserving alignment dissent, overrides, incidents, and provenance.

## Substrate Context

Claim:

Specialized LLM routing, rapid knowledge access, atomic prompts, internal economy, and A2A/server infrastructure support the five theses without proving capability or alignment.

Repository evidence:

- the `02-specialized-llm-ecosystem` design document, `16-rapid-knowledge-access.md`, `04-atomic-prompt-decomposition.md`, `01-business-orchestration.md`, and `06-digital-virtual-economy.md` specify major substrate areas.
- the `server` package implements portions of server, servlet, A2A, auth, dispatch, registry, and observability infrastructure.
- the `business.simulation` package implements internal-economy simulation support.
The line previously here cited `llm/hooks/LLMNonInteractiveSession.java` as supporting session memory and hook behavior. It is deleted rather than repointed: that file has zero commits in the history of every repository searched and no registry entry, so it was never evidence for anything. The grading below rests on the remaining infrastructure and does not need a replacement citation.

Tests:

- the `server` package
- the `server.auth` package
- the `server.dispatch` package

Evidence Status: `Implemented/Tested` for selected infrastructure. `Documented/Proposed` for specialized LLM ecosystem routing and rapid knowledge access as integrated Seed AI substrate.

Gaps:

- No unified substrate evidence report yet ties LLM routing, memory retrieval, A2A dispatch, internal economy, and thesis acceptance gates into one operational path.
- Internal economy simulations are not evidence that internal transfer pricing improves alignment or external welfare.

## Organizational Recursive Self-Improvement

Claim:

Consullo can be interpreted as an AI-native R&D organization whose agents, workflows, benchmarks, ledgers, method memories, validators, and governance gates produce validated improvement of research, engineering, evaluation, memory, and governance processes.

Evidence Status: `Documented/Proposed`.

Current evidence is concentrated in software-substrate utilities, benchmark/test-plan appendices, the canonical evidence-ledger schema, cognitive-artifact simulations, and the design-level organizational appendix. No implemented weekly organizational RSI loop, frozen `V_ref_0`, pre-registration ledger, external-evaluator sampling pipeline, kill-switch drill, or portfolio dashboard has been identified in this repository.

Gaps:

- an internal design document (not published) is specified but not implemented.
- No Week 0 completion ledger bundle exists.
- No benchmark report yet demonstrates organizational method-memory transfer, cross-lane improvement, or second-cycle research-productivity gain.
- No implemented controls yet enforce the exploration budget, rate limits, or frontier-model default-deny policy.

## Highest-Priority Evidence Gaps Before Publication

Snapshot date: April 24, 2026.

1. Implement or explicitly defer the three load-bearing Thesis 5 owner contracts specified in `appendix-thesis-5-operational-contracts.md`: `Friendship`, `AdversarialAlignmentOrchestrator`, and `AbundanceDistributionMonitor`. See `risks-and-criticisms.md`: `Owner As Final AAF Adjudicator`, `AAF Decorative Failure`, and `Abundance Obligation Vagueness`.
2. Implement the canonical evidence-ledger schema from `appendix-evidence-ledger-schema.md` for improvement evidence, trust evidence, provenance, dissent, incidents, overrides, and rollback state. See `risks-and-criticisms.md`: `Evidence-Ledger Schema Unimplemented Or Unenforced` and `Self-Modifying Provenance Graph Integrity`.
3. Produce an end-to-end improvement-loop demonstration with baseline, proposed change, evaluator evidence, validator results, staged deployment or simulation, cost/benefit report, and rollback semantics. Benchmark design is specified in `appendix-thesis-1-improvement-loop-benchmarks.md`; implementation evidence remains pending. See `risks-and-criticisms.md`: `Recursive-Improvement Claim Without End-To-End Evidence`.
4. Bind Model 2's benchmark-family measurement conventions to at least one external or project-local benchmark report with declared baselines, units, and cost normalization. Benchmark design is specified in `appendix-thesis-2-cognitive-workflow-benchmarks.md`; implementation evidence remains pending. See `risks-and-criticisms.md`: `Cognitive Architecture Inflation`.
5. Add causal-decision implementation evidence: causal graph representation, counterfactual procedure, calibration battery, and Goodhart checker. Benchmark design is specified in `appendix-thesis-3-causal-decision-benchmarks.md`; implementation evidence remains pending. See `risks-and-criticisms.md`: `Causal Model Overreach` and `Goodhart And Validator Gaming`.
6. Add validator non-regression suites for Thesis 4 and operationalize the `ValidatorStrength` convention from `appendix-formal-models.md`. Benchmark design is specified in `appendix-thesis-4-software-substrate-benchmarks.md`; implementation evidence remains pending. See `risks-and-criticisms.md`: `Software Repair Overclaim` and `Goodhart And Validator Gaming`.
7. Add AAF dissent aggregation and ADO reporting implementation evidence before treating those roles as more than specified/proposed. Benchmark design is specified in `appendix-thesis-5-alignment-benchmarks.md`; implementation evidence remains pending. See `risks-and-criticisms.md`: `AAF Decorative Failure`, `Abundance Obligation Vagueness`, and `Cost Of AAF Risk`.
