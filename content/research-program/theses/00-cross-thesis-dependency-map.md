---
title: "Cross-Thesis Dependency Map"
summary: "A bounded component of the Consullo public research program: Cross-Thesis Dependency Map."
status: "specified but not implemented"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-001"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["Publication does not establish implementation or operational effectiveness.", "The implementation-evidence appendix records component evidence only and is not evidence of operational capability for this page."]
---
# Cross-Thesis Dependency Map

Version: 0.3.1

This file defines the import/export contract among the five Consullo Seed AI theses. It exists to prevent the suite from becoming a set of overlapping agent rosters.

## Dependency Principle

Each thesis has one primary conceptual responsibility. Agents may appear in multiple discussions, but every agent or function should have one primary home. Cross-thesis use should be described as an import rather than duplicate ownership.

Imports are marked as:

- definitional: terminology, interface, or conceptual context only
- load-bearing: required for the thesis argument or runtime architecture

## Capability Flow

```text
Thesis 2: Cognitive Substrate -----------------------> Thesis 1: Validated Improvement Loop
              \                                       ^
               \                                      |
                v                                     |
Thesis 4: Self-Modifying Software Substrate ----------+
                ^                                     |
               /                                      |
Thesis 3: Causal-Decision Foundations ----------------+
```

Capability flow shows how capabilities feed the improvement loop. Thesis 2 and Thesis 3 both feed Thesis 1 directly and also inform Thesis 4. It does not show permissioning.

This diagram shows capability flow only, not all definitional imports. For example, Thesis 4 imports Thesis 1's acceptance vocabulary, but that back-import is definitional rather than a capability-flow dependency.

## Constraint Wrapper

```text
+-----------------------------------------------------------------------+
| Thesis 5: Alignment Invariants And Scoped Trust                       |
|                                                                       |
|  constrains Thesis 1, Thesis 2, Thesis 3, Thesis 4, substrate context |
|  via AAF gate, scoped permission, trust estimates, human authority     |
+-----------------------------------------------------------------------+
```

Thesis 5 is not downstream output of the improvement loop. It is a constraint layer over all theses and all substrate context.

## Organizational Operating Layer

`appendix-organizational-recursive-self-improvement.md` defines a cross-thesis operating layer, not a sixth thesis. It interprets the five theses as an AI-native R&D organization whose work product is validated improvement of research, engineering, evaluation, memory, and governance processes.

| Organizational function | Primary thesis imports | Evidence boundary |
| --- | --- | --- |
| Agenda and portfolio formation | Thesis 1 improvement targets; Thesis 3 portfolio reasoning; Thesis 5 permission boundaries | Specified/proposed until `research_agenda` and `portfolio_decision` ledger records exist. |
| Hypothesis and candidate generation | Thesis 2 cognitive search, brainstorming, negative-space mapping; Thesis 1 proposal semantics | Candidate generation only; accepted improvement requires downstream gates. |
| Pre-registration and experiment design | Thesis 3 causal-decision discipline; Thesis 1 evidence packages | Capability claims require pre-registered success/failure criteria. |
| Implementation and validation | Thesis 4 software substrate; Thesis 1 acceptance semantics | Java repair is exploitation evidence, not full organizational RSI evidence. |
| Adversarial review and governance | Thesis 5 AAF, scoped trust, owner authority; Thesis 1 acceptance gates | High-stakes or externally consequential actions route through I12. |
| Institutional memory and post-cycle learning | Thesis 1 method-memory update; Thesis 2 memory and anti-library functions | Organizational learning requires later measured reuse or transfer. |

The live execution controls for this layer are specified in the internal execution plan. That document is operational, not part of the publication thesis claim.

## Cycle-Breaking Rule

There is an unavoidable conceptual relationship between Thesis 1 and Thesis 2: cognitive agents help improve the system, and the improvement loop evaluates cognitive agents. This is not a circular proof if the import types are separated:

- Thesis 1 imports Thesis 2 definitionally for cognitive interfaces and load-bearing for current cognitive capabilities used by proposer/evaluator agents.
- Thesis 2 imports Thesis 1 definitionally for the improvement-evaluation vocabulary, but its core claim about cognitive substrate can be stated without assuming Thesis 1 succeeds.

No thesis may use its own future success as evidence for its current capability claim.

## Master Frame

The master frame exports:

- definition of Consullo Seed AI
- no-ASI-status-claim constraint
- greater-than-human capability measurement schema
- shared vocabulary and invariants
- single-owner Phase 1 baseline
- Adversarial Alignment Function
- Abundance Distribution Obligation
- alignment-monoculture mitigation requirement
- evidence-ledger schema with indexed views, as specified in `appendix-evidence-ledger-schema.md`
- capability-status enum
- legacy-agent-name rule
- literature survey expectations

All theses import the master frame.

## Substrate Context

Substrate context is not a sixth thesis, but it should be documented in `appendix-substrates.md`.

Substrate context owns:

- `SpecializedLanguageModelEcosystemDirector`
- specialized LLM provider abstraction and routing
- rapid knowledge access infrastructure
- atomic prompt decomposition and compiled-code orchestration
- internal economy and resource accounting
- `DigitalVirtualEconomyOrchestrator`
- `BusinessFunctionOrchestrator`
- `ServiceProvidingEntitiesOrchestrator`
- model routing, token-cost accounting, and provider selection

Thesis 5 may evaluate these systems for trust and alignment. It does not own them as alignment mechanisms.

## Thesis 1: Validated Improvement Loop

Primary responsibility:

Model recursive capability amplification as a staged, evidence-gated loop over agents, method memories, code, tests, workflows, policies, and agent populations.

Exports:

- improvement-cycle semantics
- proposer/evaluator/validator distinction
- acceptance-gate structure
- evidence package requirements
- method-memory update semantics
- credit-assignment requirements
- false-accept and false-reject treatment
- benchmark and cost requirements for accepted improvements
- mandatory Capability Status tagging for improvement claims
- improvement evidence-ledger view

Imports:

- from Thesis 2: cognitive interfaces and current cognitive capabilities used to generate, critique, and evaluate improvements
- from Thesis 3: causal-decision objectives, intervention evaluation, uncertainty estimates, and Goodhart analysis
- from Thesis 4: code generation, repair, testing, deployment, provenance, and software-modification mechanisms
- from Thesis 5: alignment invariants, AAF non-veto requirements, permissioning, scoped trust, human authority, rollback, and containment
- from substrate context: model routing, token-cost accounting, rapid knowledge access, and internal resource accounting

Primary agent/function home:

- `SelfImprovementOrchestrator`
- `SeedAIManager`
- `AgentImprovementGoalSetter`
- `AgentCapabilityImprover`
- `AgentComplianceValidator`
- `RecursiveEnhancementTracker`
- `MethodMemoryExtractor`
- `MethodMemoryOrganizationOrchestrator`
- `ConstructiveRuleChallenger`
- `AutonomousTaskProposer`
- `QualityCostBalancer`
- `ExplorationPortfolioManager`
- DGM proposer/evaluator/validator/selection/archive roles

Not owned here:

- `AgentBuilder`, `AgentEditor`, and `WorkflowAutomationCompiler` are imported from Thesis 4.
- Causal-model selection and robust intervention choice are imported from Thesis 3.
- Alignment vetoes and trust gates are imported from Thesis 5.

## Thesis 2: Cognitive Substrate

Primary responsibility:

Model Consullo's modular cognitive substrate for capability amplification: memory, reasoning, perception, attention, metacognition, social cognition, creativity, executive control, knowledge access, and orchestration.

Exports:

- cognitive capability profiles
- typed cognitive-agent interfaces
- memory and knowledge access functions
- attention and metacognitive control functions
- social-modeling functions
- cognitive composition and integration-cost model
- capability-status-tagged cognitive claims

Imports:

- from Thesis 1: improvement-evaluation vocabulary, benchmark results, and post-deployment learning evidence
- from Thesis 3: causal-decision layer for intervention-quality decisions
- from Thesis 4: software substrate for implementing cognitive agents
- from Thesis 5: permissioning and alignment constraints
- from substrate context: LLM ecosystem, rapid knowledge access, and atomic prompt decomposition

Primary agent/function home:

- `ExecutiveFunctionOrchestrator`
- `GoalFormationArchitect`
- `StrategyFormulationDesigner`
- `SubgoalDecompositionPlanner`
- `ResourceAllocationOptimizer`
- `ProgressMonitoringAgent`
- `TaskPerformanceExecutor`
- `KnowledgeFunctionsOrchestrator`
- `SemanticKnowledgeOrganizer`
- `EmbeddingIndexer`
- `MemoryFeedbackProcessor`
- `MethodMemoryGenerator`
- `MMCanonicalMethodRetriever`
- `AbductiveExplanationGenerator`
- `DeductiveReasoningProcessor`
- `InductiveGeneralizationAnalyzer`
- `AbstractionLevelProcessor`
- `AnalogicalMappingProcessor`
- `ConceptualBlendingCreator`
- `UncertaintyAssessmentAnalyzer`
- `ErrorDetectionProcessor`
- `AttentionRegulationManager`
- `CognitiveEffortAllocator`
- `LearningStrategySelector`
- `VisualPerceptionProcessor`
- `AudioPerceptionProcessor`
- `MultimodalFusionProcessor`
- `FeatureExtractionAnalyzer`
- `AnomalyDetectionSpecialist`
- `SalienceDetectionProcessor`
- `FocusShiftingCoordinator`
- `SustainedMonitoringAgent`
- `TemporalBindingCoordinator`
- `CollectiveInsightSynthesizer`
- `GlobalCoherenceIntegrator`
- `ExhaustivePatternMatcher`
- `DeepAnalogicalTraverser`
- `CrossDomainSynthesizer`
- `FailurePatternAnalyzer`
- `TemporalPatternExtractor`
- `ParallelReasoningCoordinator`
- `InformationGainOptimizer`
- `CognitiveDepthRegulator`
- `IdeationProcessor`
- `CreativeIdeaEvaluator`
- `CuriosityDrivenExplorer`
- `PlayfulExplorationAgent`
- `ConceptualAssociationMapper`
- `NegativeSpaceMapper`
- `PatternPriorSynthesizer`
- `FailureAntiLibraryManager`
- `ClarificationSeeker`
- `ParallelHypothesisManager`
- `SustainedReasoningManager`

Theory-of-mind agents primarily support the Adversarial Alignment Function and are owned by Thesis 5, while Thesis 2 may describe them as cognitive primitives:

- `BeliefModelingProcessor`
- `IntentionRecognitionAnalyzer`
- `PerspectiveTakingModeler`

Not owned here:

- Causal decision agents are owned by Thesis 3.
- Code generation and repair agents are owned by Thesis 4.
- Formal verification primitives are owned by Thesis 4.
- Trust, alignment, and governance agents are owned by Thesis 5.
- Consciousness claims are non-load-bearing and should not be central to this thesis.

## Thesis 3: Causal-Decision Foundations

Primary responsibility:

Model causal prediction, counterfactual reasoning, causal influence diagrams, robust decision-making, experiment selection, strategic bias control, and model-misspecification handling.

Exports:

- robust intervention-selection semantics
- causal-model validation criteria
- uncertainty and ambiguity treatment for causal decisions
- strategic bias control
- Goodhart-risk analysis
- experiment-selection logic
- decision-quality benchmarks
- abstention and escalation rules for ill-specified problems
- capability-status-tagged decision claims

Imports:

- from Thesis 1: evidence and outcome histories from improvement cycles
- from Thesis 2: reasoning, memory, and hypothesis-generation capabilities
- from Thesis 4: software tools and instrumentation for experiments and simulations
- from Thesis 5: bounded utility, policy constraints, and alignment restrictions

Primary agent/function home:

- `CausalPredictionOrchestrator`
- `CausalGraphBuilder`
- `MechanismLibrarian`
- `InterventionSimulator`
- `StructuralEquationExecutor`
- `CausalDiscoveryProcessor`
- `CausalModelingAnalyzer`
- `SelfPredictionModeler`
- `PredictionCalibrator`
- `SuperhumanExperienceMiner` (legacy name; not a capability claim)
- `CounterfactualReasoningEngine`
- `CounterfactualExperienceGenerator`
- `CounterfactualAnalyser`
- `StrategicCounterfactualPackManager`
- `LongHorizonChainPredictor`
- `HybridInferenceCoordinator`
- `MechanismValidator`
- `CausalBoundaryEnforcer`
- `ForwardCausalPredictor`
- `PredictionAuditor`
- `PredictionReliabilityScorer`
- `OptimalInterventionPlanner`
- `ComputationalDecisionMakingOrchestrator`
- `StrategicBiasMitigationOrchestrator`
- `FramingInvarianceTester`
- `OptionSetCompletenessAuditor`
- `StrongestCounterPositionGenerator`
- `FalsificationEvidencePlanner`
- `SystematicExperimentDesigner`
- `MonteCarloScenarioSimulator`
- `TemporalHorizonIntegrator`

Note: `SuperhumanExperienceMiner` is a legacy codebase name. Its name is not a claim that superhuman capability is implemented.

Not owned here:

- General executive planning is discussed in Thesis 2 unless explicitly tied to causal-decision semantics.
- Acceptance gates for modifications are owned by Thesis 1 and Thesis 5.

## Thesis 4: Self-Modifying Software Substrate

Primary responsibility:

Model the executable substrate that lets Consullo generate, edit, repair, test, validate, document, and deploy agents and code.

Exports:

- agent/code generation mechanisms
- automated repair pipeline
- test and regression validation methods
- semantic validation requirements
- formal and statistical verification primitives
- provenance requirements
- LLM-Native Functional Java constraints
- static-method, JSON-only, PDCA method contract
- repair-pipeline self-improvement recurrence
- capability-status-tagged software claims

Imports:

- from Thesis 1: improvement-loop acceptance semantics and method-memory learning
- from Thesis 2: cognitive agents used by code generation and repair
- from Thesis 3: decision logic for repair strategy selection and experiment design
- from Thesis 5: trust gates, safety boundaries, security constraints, and deployment permission
- from substrate context: LLM routing, atomic prompt routing, and token-cost accounting

Primary agent/function home:

- `SoftwareDeveloper`
- `SystemsArchitect`
- `DatabaseAdministrator`
- `CloudServicesProvider`
- `CybersecuritySpecialist`
- `AgentBuilder`
- `AgentEditor`
- `AgentDocumenter`
- `CodeProvenanceTracker`
- `WorkflowAutomationCompiler`
- `FormalProofConstructor`
- `ReasoningChainVerifier`
- `ConsistencyValidator`
- `FaultLocalizer`
- `ExecutionTraceAnalyzer`
- `StaticAnalysisIntegrator`
- `HistoricalFixRetriever`
- `RepairKnowledgeGraphManager`
- `ContrastiveTestGenerator`
- `PatchCandidateGenerator`
- `PatchValidator`
- `PatchRanker`
- `MultiHunkRepairCoordinator`
- `RuntimeErrorDiagnoser`
- `SecurityVulnerabilityFixer`
- `RepairPromptComposer`
- `RegressionTestValidator`
- `RepairMetricsCollector`
- `SemanticPatchValidator`
- methodology metrics roles from the internal agent-programming methodology
- atomic prompt and compiled-code orchestration roles from `atomic-prompts.md`

Not owned here:

- Whether a software change should be accepted into the system is ultimately governed by Thesis 1 and Thesis 5.
- Causal choice of interventions is owned by Thesis 3.

## Thesis 5: Alignment And Scoped Trust

Primary responsibility:

Model alignment invariants, scoped trust, evidence ledgers, permissioning, containment, rollback, incident response, adversarial alignment, abundance obligation, and human authority under recursive modification.

Exports:

- alignment invariants
- safety invariants
- scoped-trust semantics
- permission predicates
- trust-estimate discipline, with trust-posterior models optional only when the vocabulary requirements are met
- evidence-ledger requirements
- Adversarial Alignment Function requirements
- AAF non-veto requirement for high-stakes irreversible changes
- Abundance Distribution Obligation requirements
- human authority and escalation rules
- containment, interruptability, rollback, and incident response constraints
- single-owner Phase 1 governance frame
- capability-status-tagged alignment and trust claims

Imports:

- from Thesis 1: candidate modifications and improvement-cycle evidence
- from Thesis 2: cognitive and theory-of-mind capabilities used in alignment analysis
- from Thesis 3: causal analysis of harms, incentives, and interventions
- from Thesis 4: provenance, testing, deployment, rollback, and security instrumentation
- from substrate context: internal economy and external-commerce context as scopes for trust evaluation

Primary agent/function home:

- `HumanValuesAligner`
- `AlignmentDriftDetector`
- `AgentAuditor`
- `ConstitutionalAIAlignmentTrainer`
- `SafetyBoundaryEnforcer`
- `ConsensusCoordinator` (legacy name under single-owner Phase 1)
- `AgentActionRecorder`
- `InnovationAlignmentSupervisor`
- `BiasAuditAgent`
- `BiasDetectionAndMitigationCoordinator`
- `EthicalEvolutionMonitor`
- `ComputationalTrustOrchestrator`
- `TrustStateManager`
- `TrustEvidenceLedgerManager`
- `TrustDimensionUpdater`
- `TrustContextScoper`
- `TrustUncertaintyCalibrator`
- `TrustPolicyProjector`
- `TrustRecoveryCoordinator`
- `TrustBiasAuditor`
- `CoalitionTrustAnomalyDetector` (legacy name under single-owner Phase 1)
- `TrustImprovementSponsor`
- `TrustworthinessOrchestrator`
- `TrustworthinessGatekeeper`
- `TrustworthinessIncidentCommander`
- `TrustworthinessImprovementRequestBroker`
- `ReliabilityImprovementSponsor`
- `SafetyImprovementSponsor`
- `SecurityImprovementSponsor`
- `PrivacyImprovementSponsor`
- `FairnessImprovementSponsor`
- `Friendship`
- `AdversarialAlignmentOrchestrator`
- `AbundanceDistributionMonitor`
- `BeliefModelingProcessor`
- `IntentionRecognitionAnalyzer`
- `PerspectiveTakingModeler`
- `ProactiveContradictionHunter`
- Adversarial Alignment Function roles
- Abundance Distribution Mechanism roles
- Friendship / constitutional ethical-anchor roles

Notes under single-owner Phase 1:

- `ConsensusCoordinator` means intra-organizational quorum or dispute resolution under owner authority, not independent democratic governance.
- For `ConsensusCoordinator`, quorum means a typed review quorum over relevant internal evidence sources: policy checks, trust estimates, AAF dissent, technical validation, and human authority state. It is not a vote among independent stakeholders.
- `CoalitionTrustAnomalyDetector` means detection of unhealthy internal dependency, routing, or influence clusters, not autonomous political factions.
- `TrustBiasAuditor` means auditing distortions in scoped reliance decisions.
- `ConstitutionalAIAlignmentTrainer` must specify critique-source diversity to avoid reinforcing alignment monoculture.
- `ConstitutionalAIAlignmentTrainer` must use the AAF dissent-source enumeration as its critique-source distribution under single-owner Phase 1: rotating LLM personas, multi-model critique, theory-of-mind-driven stakeholder simulations, and external review where available.
- `Friendship`, `AdversarialAlignmentOrchestrator`, and `AbundanceDistributionMonitor` operational contracts are specified in `appendix-thesis-5-operational-contracts.md`.
- `AlignmentDriftDetector` monitors unintended deviation from current alignment constraints. `EthicalEvolutionMonitor` monitors intended value-interpretation adaptation under governance.
- `BiasAuditAgent` detects bias patterns. `BiasDetectionAndMitigationCoordinator` owns mitigation workflow and follow-through.
- Thesis 1 owns the generic improvement-sponsor pattern. Thesis 5 owns trust-property-specific sponsor variants such as reliability, safety, security, privacy, and fairness sponsors because their recommendations are derived from trustworthiness evidence.

Not owned here:

- `DigitalVirtualEconomyOrchestrator`, `BusinessFunctionOrchestrator`, and `ServiceProvidingEntitiesOrchestrator` are substrate-context systems, not Thesis 5 primary alignment mechanisms.

## Cross-Cutting Constraints

### Single-Owner Phase 1

All theses must treat single-owner Phase 1 as the baseline. Future contractor oversight and multi-stakeholder governance are later phases or stress-test scenarios.

### Bounded Compute

All theses must account for token cost, compute cost, latency, validation cost, and opportunity cost.

### Capability Status

Every major capability claim must identify whether it is implemented, specified, proposed, or speculative.

### Benchmark Discipline

Benchmarks are evidence sources, not proof of intelligence or safety. Every benchmark claim must state task class and limitation.

### Evidence Ledger Discipline

Evidence ledgers must be treated as audit-preserving records. Rollback annotates or supersedes evidence; it does not erase inconvenient history.

The canonical evidence-ledger schema is maintained in `appendix-evidence-ledger-schema.md`.

### AAF Gate Discipline

The Adversarial Alignment Function must be routed into Thesis 1 acceptance gates according to invariant I12 in `00-vocabulary-and-invariants.md`.

### Provenance Discipline

Accepted modifications must satisfy invariant I11.

### Cost/Benefit Discipline

Accepted non-emergency improvements must satisfy invariant I17.

### Deceptive Optimization Discipline

Improvements to learned subsystems must satisfy invariant I19.

### Overclaim Control

Sub-theses should use "scaffold for," "pathway to," "bounded," "measurable," and "governed" where appropriate. Avoid unqualified claims of superintelligence, solved alignment, or guaranteed improvement.

## Changelog

- 0.3.2: Added organizational operating-layer row tying the AI-native R&D organization interpretation to the five-thesis import/export contract and execution-plan boundary.
- 0.3.1: Added version header; annotated capability-flow and constraint-wrapper diagrams; added placeholder AAF/ADO/Friendship owner agents; canonicalized AAF gate through I12; added provenance, cost/benefit, and deceptive-optimization cross-cutting constraints; specified ConstitutionalAIAlignmentTrainer critique-source distribution; clarified ConsensusCoordinator, drift/evolution, bias/mitigation, and improvement-sponsor ownership.
- 0.3.0: Revised after second review with capability-flow and constraint-wrapper diagrams.
