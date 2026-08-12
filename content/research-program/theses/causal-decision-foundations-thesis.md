---
title: "Causal-Decision Foundations For Bounded Strategic Reasoning"
summary: "A bounded component of the Consullo public research program: Causal-Decision Foundations For Bounded Strategic Reasoning."
status: "specified but not implemented"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-001"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["Publication does not establish implementation or operational effectiveness.", "The implementation-evidence appendix records component evidence only and is not evidence of operational capability for this page."]
---
# Causal-Decision Foundations For Bounded Strategic Reasoning

## Specialized Abstract

Consullo Seed AI needs causal-decision foundations because recursive improvement is an intervention problem, not only a reasoning problem. Every accepted modification, repair, experiment, strategy, deployment, or trust update changes the future system. This thesis defines the causal-decision layer that should make those interventions explicit: structural causal models, counterfactual reasoning, causal influence diagrams, robust decision rules, prediction calibration, strategic bias controls, experiment-selection portfolios, abstention, and escalation. Capability Status: specified/proposed.

The claim is bounded. Consullo should not claim universal superiority over human strategic judgment. It can aim to improve decision quality where causal assumptions are explicit, evidence is adequate, uncertainty is calibrated, interventions are testable, and high-stakes commitments remain governed by Thesis 5. Its falsification risks are familiar: causal models may be wrong, objectives may be misspecified, strategic environments may react to the system, Goodhart pressure may distort metrics, and theory-driven experiments may increase confidence without improving objective model quality.

## Specialized Introduction

Many AI systems produce recommendations by generating plausible narratives. Consullo's decision layer should instead treat recommendations as interventions under uncertainty. A decision is not just an answer; it is a proposed change to variables in a causal system. That change must be modeled, compared against alternatives, stress-tested by counterfactuals, bounded by alignment constraints, and later scored against outcomes.

The current Consullo corpus already points in this direction. Computational decision making rejects single open-ended strategy prompts in favor of option sets, counterfactual packs, confidence records, decision lineage, human approval, and outcome learning. The causal prediction designs specify structural causal models, graph surgery, mechanism libraries, causal discovery, prediction calibration, regime-change detection, counterfactual backtesting, and causal boundary enforcement. The randomized experimentation proposal adds a necessary corrective: theory-guided experiment choice can overfit current assumptions, so experiment portfolios must preserve random and novelty-seeking arms.

## Master-Frame Contract

This thesis imports:

- evidence and outcome histories from Thesis 1 improvement cycles
- reasoning, memory, hypothesis generation, and cognitive search from Thesis 2
- software tools, instrumentation, simulations, and experiment harnesses from Thesis 4
- bounded utility, policy constraints, AAF review, scoped trust, and human authority from Thesis 5

This thesis exports:

- robust intervention-selection semantics
- causal-model validation and boundary criteria
- counterfactual and prediction-calibration requirements
- Goodhart-risk and strategic-bias controls
- experiment-selection portfolio logic
- decision-lineage and provenance requirements
- abstention and escalation rules for ill-specified problems
- decision-quality benchmark families and Capability Status discipline

## Main Argument

The causal-decision layer should answer five questions before recommending action.

First, what causal model is being used? A recommendation should name variables, mechanisms, assumptions, validity conditions, uncertainty sources, and evidence provenance. CausalGraphBuilder, MechanismLibrarian, StructuralEquationExecutor, CausalDiscoveryProcessor, and CausalModelingAnalyzer belong to this function. A model that cannot state its scope should not support high-stakes intervention.

Second, what intervention is being considered? Pearl-style `do` semantics are useful because they distinguish observation from manipulation. InterventionSimulator and OptimalInterventionPlanner should treat action as graph surgery or mechanism alteration where applicable, then propagate effects through structural equations or simulation models.

Third, what counterfactuals matter? CounterfactualReasoningEngine, CounterfactualExperienceGenerator, CounterfactualAnalyser, and StrategicCounterfactualPackManager should evaluate what would likely happen under alternative choices, delayed choices, no action, and adversarial or regime-shift conditions. Counterfactuals are not decorative narratives; they are structured tests of decision sensitivity.

Fourth, how fragile is the decision? StrategicBiasMitigationOrchestrator, FramingInvarianceTester, OptionSetCompletenessAuditor, StrongestCounterPositionGenerator, FalsificationEvidencePlanner, PredictionCalibrator, PredictionAuditor, and PredictionReliabilityScorer should test whether the recommendation changes under paraphrase, source-label blinding, option expansion, confidence recalibration, or model perturbation.

Fifth, should the system abstain or escalate? For ill-specified objectives, poor evidence, unvalidated mechanisms, high model disagreement, distribution shift, external human impact, or severe AAF objections, the decision layer should use the decision-state enum from `00-vocabulary-and-invariants.md`, such as `needs-input`, `conflicted`, `blocked`, or `escalated`, rather than force a recommendation.

## Expansion: Decision Layer Topology

Thesis 3 is the layer that decides which intervention is worth attempting, not the layer that makes every decision executable. It sits between cognitive proposal generation, software implementation, improvement acceptance, and alignment permission. Thesis 2 can generate hypotheses and option sets. Thesis 3 evaluates which option is causally promising under uncertainty. Thesis 4 can instrument or execute experiments. Thesis 1 decides whether a resulting modification qualifies as an improvement. Thesis 5 constrains which interventions are permitted.

This topology matters because recursive capability amplification is full of intervention choices. Should Consullo improve a validator or a generator? Should it add a benchmark or change a method memory? Should it expand trust scope for an agent or narrow it after an incident? Should it invest in semantic validation or speed up compilation repair? Each choice changes future evidence, incentives, costs, and failure modes. A narrative answer is not enough; the system needs decision lineage.

Decision lineage should preserve the problem statement, option set, causal model, assumptions, evidence sources, objective vector, constraints, counterfactuals, uncertainty, Goodhart analysis, dissent, final disposition, and outcome. Without lineage, later review cannot tell whether a failed decision came from bad evidence, wrong mechanisms, missing options, weak calibration, objective misspecification, or alignment override. Without lineage, the decision layer cannot improve itself.

The decision layer should also preserve non-decisions. Abstention, experiment selection, scope narrowing, and escalation are legitimate outputs. In many high-uncertainty domains, the best decision is not to optimize immediately but to gather evidence, run a small experiment, or ask for human authority. Forced recommendation is a failure mode because it converts uncertainty into action merely to satisfy a workflow.

The bounded claim is therefore not that Consullo can make superior strategic decisions everywhere. The claim is that Consullo can make certain decisions more auditable: it can name mechanisms, compare interventions, preserve uncertainty, track calibration, expose Goodhart risk, and route ill-posed or high-stakes decisions away from autonomous execution. This is a meaningful but narrower claim.

## Expansion: Causal Model Scope

A causal model is useful only inside its validity scope. Thesis 3 should treat scope as part of the model, not metadata. A model should name the variables it includes, the variables it excludes, the mechanisms it assumes stable, the data regime it was learned from, the interventions it has seen, the confounders it cannot handle, the time horizon it covers, and the domains where it should not be used.

Scope failures are common. A model learned from internal engineering tasks may not apply to external customer behavior. A model of short-term repair throughput may not apply to long-term maintainability. A model of trust transition in simulation may not apply to production agents facing strategic inputs. A model of business allocation may not apply under regime change, adversarial manipulation, or new legal constraints. CausalBoundaryEnforcer exists to prevent this kind of extrapolation.

The validity scope should be tied to evidence. A mechanism supported by randomized experiment is different from a mechanism inferred from correlation. A mechanism observed in one repository is different from a mechanism validated across task classes. A mechanism backed by expert judgment is different from a mechanism confirmed by intervention. These distinctions do not make weaker mechanisms unusable, but they should change confidence, deployment stage, and escalation requirements.

MechanismLibrarian should curate mechanisms with provenance and failure history. A mechanism record should say where it came from, what evidence supports it, what assumptions it depends on, what interventions have tested it, what outcomes contradicted it, and when it expires or needs review. Mechanisms should be reusable, but only with scope checks. Reusing a mechanism outside its scope is not generalization; it is an unsupported extrapolation.

Model scope also affects decision authority. A low-stakes recommendation based on a weak model may be acceptable if the action is reversible and monitored. A high-stakes externally consequential recommendation based on a weak model should be blocked, narrowed, or escalated. Thesis 3 therefore imports Thesis 5 not as decoration but as an authority boundary over model use.

## Expansion: Interventions And Do-Operator Discipline

The do-operator discipline matters because observing that two variables move together is not enough for intervention. If agent repair throughput rises when validation is loosened, that does not mean loosening validation is a good intervention. If trust scores rise after agents are given broader scope, that does not mean broad scope caused trustworthy behavior. If revenue rises after an external service launch, that does not mean the launch improved welfare or alignment.

An intervention should state what mechanism is being changed. In software, the intervention may be a patch, a validator rule, a deployment stage, a routing policy, or a method-memory update. In trust, it may be scope expansion, validation-depth change, or recovery obligation. In business simulation, it may be budget allocation, pricing change, market entry, or customer-segment routing. The causal model should identify which structural equations or mechanisms are affected and which are assumed unchanged.

The discipline also requires comparing alternatives. A decision layer that evaluates only the proposed action is vulnerable to confirmation. The option set should include no action, delayed action, narrower action, reversible experiment, alternative mechanism, and adversarial or worst-case variants where appropriate. OptionSetCompletenessAuditor exists because missing alternatives can make a bad action look optimal.

Intervention evaluation should preserve side effects. A validator improvement may reduce false accepts but increase false rejects. A repair pipeline change may improve throughput but increase security risk. A routing change may reduce cost but increase model-family monoculture. An ADO-related external service may increase access but introduce misuse risk. These are not secondary concerns; they are part of the expected utility and constraint evaluation.

The decision layer should also distinguish recommendation from execution. Recommending an intervention does not authorize it. Execution requires Thesis 1 acceptance if it modifies the system, Thesis 4 implementation if it changes software, and Thesis 5 permission if it is high-stakes, externally consequential, or alignment-relevant. This prevents causal-decision confidence from becoming authority.

## Expansion: Counterfactual Evaluation

Counterfactuals are useful only when they are disciplined by model assumptions. A counterfactual asks what would have happened under a different action, but the answer depends on the structural model, background conditions, and uncertainty. Thesis 3 should therefore reject free-form "what if" storytelling as insufficient. A counterfactual should name the observed evidence, inferred exogenous state, alternative intervention, affected mechanisms, predicted outcome distribution, and uncertainty.

For recursive improvement, counterfactuals are valuable in postmortems. If an accepted patch caused a regression, the system should ask what would likely have happened if the patch had been narrowed, delayed, rejected, or staged differently. If AAF was bypassed, it should ask whether AAF would likely have surfaced the issue. If a validator rejected a useful candidate, it should ask whether sandboxing would have produced safe evidence. These counterfactuals can improve future gates, but they remain model-dependent.

Counterfactuals also support option design before action. A StrategicCounterfactualPackManager can present several plausible branches: act now, gather evidence, run a small experiment, choose an alternative intervention, or do nothing. The pack should include predicted benefits, harms, uncertainty, evidence gaps, and escalation triggers. It should not merely generate persuasive narratives for the favored option.

CounterfactualExperienceGenerator is risky if misused. Synthetic experience can expand learning, but it can also create false confidence if the generated cases reflect the model's assumptions rather than reality. Synthetic counterfactuals should be labeled as such, weighted differently from observed outcomes, and backtested where historical data permits. They are training and reasoning artifacts, not observations.

The decision layer should track counterfactual calibration. When the system predicts what would happen under alternatives and later observes related outcomes, it should update confidence in the model and in the counterfactual generator. A system that produces elegant counterfactuals without calibration may become more persuasive while not becoming more accurate.

## Expansion: Robustness And Ambiguity Sets

The formal model uses a minimax rule over `Theta(M)`, the ambiguity set of plausible models near the current causal model. This is a conservative response to model uncertainty. Instead of choosing the action that looks best under one favored model, the decision layer asks how the action performs under plausible alternatives. This is especially important when actions are hard to reverse or externally consequential.

The ambiguity set must be constructed, not hand-waved. Plausible alternatives may come from parameter perturbation, competing causal structures, expert disagreement, held-out validation failures, regime-change scenarios, adversarial assumptions, or mechanism uncertainty. MechanismLibrarian and CausalBoundaryEnforcer should help curate this set. For early implementations, the ambiguity set may be qualitative or scenario-based. That is acceptable if labeled honestly.

Robustness can be too conservative. A minimax rule may reject useful interventions because one implausibly pessimistic model predicts bad outcomes. The decision layer therefore needs a policy for what enters `Theta(M)`. The policy should not include every imaginable failure, but it should include credible alternatives supported by evidence, theory, or risk analysis. Human review may be needed when ambiguity-set membership determines high-stakes decisions.

Robust decision-making also interacts with experimentation. If all plausible models agree that a low-risk experiment is valuable, the system can act. If models disagree sharply, the system may choose an experiment that discriminates among them rather than optimizing under any one model. In this sense, experiment selection is often the correct robust action.

The output of robust analysis should include model disagreement. A recommendation should not hide that it is sensitive to assumptions. If the best action changes under reasonable perturbations, the decision should be marked fragile, conflicted, or needs-input. Fragility is not a failure; undisclosed fragility is.

## Expansion: Goodhart And Strategic Bias

Goodhart risk is central because every decision layer creates metrics. Repair throughput, prediction accuracy, cost reduction, trust scores, ADO benefit measures, benchmark performance, and incident counts can all become targets. Once optimized, a metric may stop tracking the objective it was meant to represent. Thesis 3 should therefore treat Goodhart analysis as part of decision evaluation, not as a later audit.

The decision layer should ask what proxy is being optimized, what true objective it stands for, how the proxy can drift, how agents might game it, what side effects are likely, and what evidence would reveal proxy failure. A repair-throughput metric might be gamed by accepting shallow patches. A trust-score metric might be gamed by avoiding risky but valuable tasks. A cost-reduction metric might be gamed by cutting validation. An ADO benefit metric might be gamed by reporting customer demand as public benefit.

Strategic bias controls complement Goodhart analysis. FramingInvarianceTester checks whether a recommendation changes under paraphrase or presentation order. OptionSetCompletenessAuditor checks whether important alternatives are missing. StrongestCounterPositionGenerator constructs the best argument against the recommendation. FalsificationEvidencePlanner asks what evidence would change the decision. PredictionAuditor checks consistency and provenance. These controls slow decisions, but they make strategic recommendations less dependent on prompt framing.

Bias controls should be proportional. Routine low-risk choices do not need full adversarial strategic review. High-stakes, irreversible, externally consequential, or recursive-infrastructure choices do. A validator change, AAF cost-reduction proposal, trust-scope expansion, or external pricing decision deserves more scrutiny than a low-risk internal scheduling choice. This mirrors Thesis 5's proportional AAF challenge model.

Goodhart and bias findings should affect outcomes. If the analysis identifies severe proxy risk, the decision should be revised, escalated, or converted into an experiment. If it merely records risk while still optimizing the same proxy without mitigation, it is decorative. The same critique made of AAF applies here: a control that cannot change routing is not a control.

## Expansion: Prediction Calibration

Prediction calibration is the discipline that keeps the decision layer from confusing confidence with accuracy. A causal-decision system will often produce forecasts: repair success probability, deployment risk, cost reduction, incident likelihood, customer response, validation burden, or expected effect of a trust-scope change. Those forecasts should be scored against outcomes. Without calibration, the system can become more fluent without becoming more reliable.

Calibration should be task-class specific. An agent may be well calibrated on compilation repair and poorly calibrated on external market behavior. It may be calibrated for short horizons and overconfident for long horizons. It may be accurate on average but poorly calibrated in high-stakes tails. PredictionCalibrator should therefore preserve domain, horizon, evidence type, model version, confidence bucket, and outcome.

Calibration should distinguish probability quality from decision quality. A well-calibrated prediction can support a bad decision if the objective is wrong or constraints are ignored. A poorly calibrated prediction can still lead to a good outcome by luck. Thesis 3 needs both forecast scoring and decision outcome tracking. The former measures epistemic reliability; the latter measures intervention quality under objectives and constraints.

Forecasting literature is relevant because it shows that structured prediction, scoring, feedback, and aggregation can improve judgment. But Consullo should not claim forecasting superiority without batteries. A calibration battery might include project-local intervention predictions, repair success forecasts, cost estimates, incident risk predictions, and external comparison questions. The system should track Brier scores, calibration curves, resolution, and error by domain where feasible.

Calibration should also update authority. An agent or model with poor calibration in a scope should not be trusted for high-stakes decisions in that scope without additional review. Good calibration should not grant global authority, but it can reduce redundant review in low-risk scopes. This ties Thesis 3 to Thesis 5's scoped trust semantics.

## Expansion: Experiment Portfolio Logic

Experiment selection is where Thesis 3 resists theory lock. A decision system with a favored causal model will tend to choose experiments that refine that model or exploit its current best action. That can be efficient when the model is mature. It can be dangerous when the model is wrong. The experiment portfolio should therefore preserve allocation to random, novelty-seeking, adversarial, replication, and theory-guided arms.

Random arms are not waste. They create evidence outside current theory and can reveal unknown structure. Novelty arms explore mechanisms or contexts the system has not modeled. Adversarial arms test expected failure modes, proxy gaming, or edge cases. Replication arms test whether prior results are stable. Theory-guided arms exploit the best current model. The portfolio should shift with evidence maturity, but it should not collapse entirely into theory-guided exploitation before the model is well validated.

The portfolio should also separate objective quality from confidence gain. An experiment can make the system more confident without improving the model's relation to reality. For example, repeated tests in the same narrow setting may reduce uncertainty estimates while leaving the model brittle. The random-experiments critique in the Consullo corpus exists for this reason: experiment systems can optimize for subjective epistemic gain rather than objective model quality.

Experiment design should account for cost and risk. Some experiments are cheap, reversible, and internal. Others affect users, finances, privacy, or alignment. High-risk experiments require Thesis 5 permission. Low-risk experiments may be automated. The decision layer should not treat all uncertainty reduction as worth pursuing. It should ask whether the expected value of information justifies cost and risk.

Experiment outcomes should update the causal model, calibration record, decision lineage, and method memory. A failed experiment is not empty. It can falsify a mechanism, reveal a confounder, expose a metric weakness, or improve future experiment design. The evidence ledger should preserve experiments that contradicted the preferred model, not only successful confirmations.

When several experiment arms run in parallel, they should share information rather than search in isolation. A common weakness of parallel experimentation is trajectory-local optimization: each arm refines only along its own path, so an insight found in one arm cannot inform the others, informative patterns across the broader search are never reused, and promising elements from different arms are never combined. Long-horizon discovery work addresses this by replacing isolated trajectories with a shared solution graph: when an arm stagnates it can reference high-performing nodes discovered by other arms (cross-branch transfer), and complementary partial solutions from several arms can be aggregated into a hybrid candidate, while evaluation scores backpropagate along each candidate's lineage to guide further search (InternAgent-1.5: A Unified Agentic Framework for Long-Horizon Autonomous Scientific Discovery, arXiv:2602.08990, InternAgent-1.5). For Consullo this means the experiment portfolio should preserve arm diversity for exploration but still cross-pollinate evidence across arms, and the evidence ledger should record cross-arm transfers and aggregations so that credit assignment reflects where a winning element actually originated.

## Expansion: Abstention And Escalation

Abstention is a capability, not a failure. A decision system that always produces an action is dangerous because some decision states are under-specified, conflicted, blocked, or outside autonomous authority. Thesis 3 should use the vocabulary decision-state enum to make non-action structured: `needs-input`, `conflicted`, `blocked`, `escalated`, `accepted`, `revised`, or `rejected`.

`needs-input` applies when required evidence, scope, objective, authority, or model information is missing. The correct output is a request for evidence or clarification, not a forced recommendation. `conflicted` applies when plausible models, objectives, constraints, or stakeholder impacts disagree enough that no autonomous recommendation should dominate. `blocked` applies when a hard constraint fails. `escalated` applies when human authority, AAF, Friendship, or external review is required.

Abstention should be evidence-bearing. A decision record should explain why the system abstained, what evidence would resolve the state, and whether a low-risk experiment could reduce uncertainty. Otherwise abstention becomes a dead end. A good abstention can improve the decision process by identifying missing model scope, missing options, unvalidated mechanisms, or unresolved alignment concerns.

Escalation should also be typed. Escalation to Thesis 5 is different from escalation to a human owner. AAF escalation concerns structured dissent and high-stakes alignment risk. Friendship escalation concerns constitutional values and human authority. Human escalation concerns authorization beyond autonomous scope. External review concerns critique diversity or stakeholder legitimacy. Mixing these escalation paths creates governance ambiguity.

The decision layer should track escalation outcomes. If many decisions escalate because causal models are weak, the system needs better models or narrower claims. If many escalations are overridden, owner bottleneck or alignment-monoculture risk may be rising. If escalations routinely lack evidence packages, the decision layer is not preparing decisions well enough.

## Expansion: Implementation Mapping

Current repository evidence for Thesis 3 is weaker than for Thesis 4. The evidence map identifies design documents for causal prediction agents, computational decision making, random experiments, modeling features, performance monitoring, strategic planning, and strategic coordination. It also identifies deterministic business and AI-native commerce simulations. These are relevant because they show scenario modeling, allocation, evaluation, failure injection, and simulation infrastructure. They do not establish a Pearl-style causal-decision engine.

The missing evidence is central. No implemented structural causal graph engine has been identified. No structural-equation executor has been identified. No counterfactual reasoning engine has been identified. No prediction-calibration battery or causal prediction backtest report exists. No implemented Goodhart checker is wired into acceptance gates. Therefore Thesis 3 remains specified/proposed, with selected simulation evidence rather than operational causal-decision evidence.

The first implementation milestone should be a minimal causal-model representation. It could define variables, directed edges, mechanisms, validity scope, evidence provenance, and excluded variables. It need not implement full do-calculus. A simple representation with explicit scope and provenance would already improve decision lineage over narrative recommendations.

The second milestone should be a small intervention simulator for one bounded domain. For example, a repair-pipeline decision could model how validation depth affects repair throughput, false accepts, cost, and incident risk. The simulator should allow interventions, record assumptions, and compare outcomes against observed data. The point is not perfect causal truth; it is disciplined intervention reasoning.

The third milestone should be a calibration battery. The system should make predictions about intervention outcomes, record confidence, observe results, and score calibration. Initial domains can be narrow: compilation-repair success, validation cost, regression likelihood, or simulation outcomes. Calibration evidence would make Thesis 3 materially stronger.

The fourth milestone should be a Goodhart checklist wired into Thesis 1 acceptance gates. Before accepting an improvement that optimizes a metric, the system should record metric-objective link, proxy drift risk, side-effect channels, gaming scenarios, and escalation state. This could begin as a structured template before becoming automated.

## Expansion: Benchmark Strategy

Thesis 3's benchmark strategy should test decision quality, not only prediction fluency. A useful benchmark should ask whether the system names causal assumptions, preserves option sets, identifies model scope, predicts intervention effects, calibrates uncertainty, detects Goodhart risk, chooses informative experiments, and escalates when evidence is weak. Free-form strategic essays are not enough.

The benchmark families summarized here are formalized in `appendix-thesis-3-causal-decision-benchmarks.md`. That appendix is the canonical benchmark-design contract for report fields, negative controls, ambiguity-set requirements, minimal demonstration package, and non-claim boundaries.

The first benchmark layer is causal-model construction tasks. Given a bounded scenario, the system should identify variables, candidate mechanisms, assumptions, confounders, validity scope, evidence sources, and missing data. Scoring should reward explicit uncertainty and penalize unsupported extrapolation. The benchmark should include cases where the correct answer is "model scope insufficient."

The second layer is intervention-prediction backtests. Historical or simulated cases can provide baseline state, intervention, and outcome. The system predicts the outcome distribution before seeing the result. This tests whether causal models support intervention prediction rather than post hoc explanation. Backtests should include regime-shift and confounding cases.

The third layer is counterfactual discipline tasks. The system receives observed evidence and must evaluate alternative actions using abduction, action, and prediction steps. Scoring should check whether assumptions are stated, uncertainty is preserved, and synthetic counterfactuals are not treated as observations.

The fourth layer is Goodhart detection tasks. The benchmark presents a proposed metric optimization and asks the system to identify proxy drift, side effects, gaming channels, and falsification evidence. Cases should include repair throughput, trust scores, ADO benefit metrics, benchmark pass rates, and cost reduction. The benchmark should reward mitigation, not only diagnosis.

The fifth layer is experiment-portfolio tasks. The system must allocate budget across random, theory-guided, novelty, adversarial, and replication arms under cost and risk constraints. Scoring should distinguish confidence gain from objective model improvement. A system that allocates everything to theory-guided exploitation too early should be penalized.

The sixth layer is escalation tasks. The system should identify when to abstain, request input, block, revise, or escalate. Scoring should penalize forced recommendations under missing evidence, invalid model scope, unresolved severe AAF objection, or high-stakes external consequence. This benchmark ties Thesis 3 directly to Thesis 5.

## Expansion: Source-Corpus Reconstruction

The Consullo source corpus contains several streams that Thesis 3 consolidates. The causal prediction agent designs emphasize causal graphs, mechanism libraries, graph surgery, structural equations, prediction calibration, regime-change detection, and counterfactual backtesting. The computational decision-making materials emphasize option sets, counterfactual packs, confidence records, decision lineage, approval states, and outcome learning. The strategic coordination chapter emphasizes alternatives, counterfactual analysis, quality assessment, preference modeling, uncertainty quantification, and time-horizon coordination. The random-experiments material adds the warning that theory-guided experiment choice can become self-confirming.

Thesis 3 reconstructs these streams into a bounded decision foundation. CausalGraphBuilder and MechanismLibrarian become model-construction and scope roles, not proof that causal inference is solved. InterventionSimulator and StructuralEquationExecutor become target capabilities, not current implementation claims. Counterfactual agents become disciplined counterfactual evaluators, not narrative generators. PredictionCalibrator becomes an evidence instrument, not proof of forecasting superiority. Strategic-bias agents become routing controls, not guarantees of objectivity.

This reconstruction is necessary because the broader source corpus sometimes uses ambitious phrasing around superhuman planning, prediction, or strategic decision-making. The long-form thesis should translate that ambition into bounded claims: more explicit causal assumptions, broader option coverage, better lineage, better calibration, more systematic counterfactuals, clearer abstention, and stronger Goodhart checks. Those are measurable advantages. Universal strategic superiority is not.

The digital-economy and business simulation materials are also relevant but limited. They show that the repository can simulate scenarios, allocations, market structures, routing advantages, and business outcomes. They do not show that the system has a general causal-decision engine. Thesis 3 should treat them as simulation infrastructure and domain examples, not as validation of Pearl-style causal reasoning.

The cognitive chapters supply supporting functions such as uncertainty assessment, metacognition, perspective taking, and executive control. Those functions are imported from Thesis 2. Thesis 3 owns the causal-decision semantics: when an output becomes a decision recommendation, what model supports it, what intervention it proposes, what uncertainty it carries, what Goodhart risks it creates, and when it must abstain or escalate.

## Expansion: Safety And Dual-Use Boundaries

Prediction is not automatically safe. Better forecasts can enable better repair, better experimentation, and better resource allocation. They can also enable manipulation, extraction, market exploitation, privacy invasion, adversarial planning, or harmful persuasion. Thesis 3 must therefore treat prediction use as governed action. The question is not only "is the prediction accurate?" but "should this prediction be generated, delivered, acted on, or restricted?"

High-impact predictions should carry use constraints. A forecast about customer vulnerability, competitor weakness, security exposure, or persuasion effectiveness may be strategically useful and ethically dangerous. A causal model that identifies a leverage point in human behavior may create manipulation risk. A model that predicts external agent behavior may create privacy or bargaining concerns. Thesis 5 gates apply when predictions have external human impact, financial consequence, privacy sensitivity, or irreversible action pathways.

Dual-use risk also appears in self-improvement. A decision layer that identifies how to bypass validators, reduce AAF cost, increase trust scores, or accelerate deployment can be useful for legitimate optimization and dangerous for control weakening. The Goodhart checker should therefore treat governance-infrastructure decisions as high-risk. A recommendation that improves throughput by reducing review depth is not automatically an improvement; it is a candidate alignment-infrastructure modification.

The system should also guard against manipulative objective selection. If a decision layer is asked to maximize engagement, revenue, persuasion, compliance, or extraction, it should ask whether the objective is permitted and whether the metric-objective link is ethically acceptable. Thesis 3 does not own ethics, but it must detect when objective choice creates alignment risk and route to Thesis 5.

Prediction safety should be recorded. If a prediction is withheld, narrowed, delayed, or escalated because of misuse risk, that is decision evidence. If a prediction is delivered with constraints, the constraints should be linked to the decision lineage. If a harmful prediction use occurs, the incident should update future prediction permissions. This keeps harmful-prediction risk inside the learning loop.

## Expansion: Objective Vectors And Multi-Objective Tradeoffs

Thesis 3 should avoid pretending that every decision reduces to one scalar objective. Consullo decisions often involve multiple objectives: capability gain, cost, reliability, safety, security, privacy, external benefit, owner authority, latency, maintainability, interpretability, and reversibility. A robust decision rule can aggregate or compare these objectives, but it should not hide tradeoffs.

The objective vector should distinguish hard constraints from soft objectives. Hard constraints include constitutional prohibitions, unauthorized authority expansion, missing required provenance for accepted modifications, unresolved severe AAF objections under I12, and other invariant failures. Soft objectives include cost reduction, speed, quality, maintainability, and some forms of capability improvement. A high score on a soft objective should not compensate for a hard constraint violation.

Tradeoffs among soft objectives still require discipline. A decision that improves speed while increasing cost may be acceptable if the speed matters. A decision that improves cost while reducing reliability may be unacceptable if reliability is protected for that scope. A decision that improves capability while increasing opacity may require staged deployment or additional monitoring. The decision layer should state the trade rather than burying it in a scalar score.

Multi-objective reasoning also affects explanation. A human reviewer should be able to see why an action was recommended: which objective improved, which degraded, which constraints bound, which uncertainty mattered, and what evidence would change the recommendation. This is another reason decision-lineage records are required.

The strongest version of Thesis 3 is not that Consullo always finds the optimum. It is that Consullo can make the structure of the choice explicit enough for review, learning, and constraint enforcement. In complex domains, transparent bounded reasoning may be more valuable than a confident but opaque recommendation.

## Expansion: Open Research Questions

The first open question is how to operationalize `Theta(M)` in practice. The formal model now gives a first-pass ambiguity-set construction rule in `appendix-formal-models.md`: parameter perturbation, alternative graph structures, mechanism disagreement, expert disagreement, held-out validation failure, adversarial scenarios, and regime-shift hypotheses. The remaining research problem is not whether such sources exist, but how to weight them, curate them, and keep the ambiguity set conservative without making it useless. The policy for including models in the ambiguity set is itself a governance object.

The second open question is how to validate causal models under limited intervention data. Many Consullo domains may have abundant observational traces but few clean interventions. Causal discovery can propose structure, but proposed structure is not validated mechanism. The system needs a ladder of evidence: observational correlation, plausible mechanism, expert judgment, natural experiment, randomized experiment, backtest, and live intervention outcome. Claims should state where they sit on that ladder.

The third open question is how to combine symbolic, statistical, simulation, and LLM-based reasoning without blurring evidence types. A simulation can explore scenarios but may encode assumptions. A statistical model can forecast patterns without causal validity. A symbolic graph can express mechanism but omit real-world noise. An LLM can synthesize hypotheses but hallucinate mechanisms. HybridInferenceCoordinator should preserve these distinctions.

The fourth open question is how to calibrate decisions with sparse feedback. Some high-stakes decisions are rare, delayed, or impossible to repeat. Calibration is easier for frequent repair tasks than for strategic business moves or alignment interventions. The decision layer may need proxy calibration, simulation, expert review, and conservative escalation for sparse domains.

The fifth open question is how to prevent strategic self-confirmation. A system can choose experiments, metrics, and interpretations that make its preferred strategy look correct. Random arms, adversarial arms, replication, and external review mitigate this, but do not eliminate it. The evidence ledger should preserve experiments that failed to confirm the preferred model.

The sixth open question is how to handle reflexive environments. Some decisions change the behavior of agents, users, competitors, customers, or internal subsystems because those actors respond to the decision process itself. Causal models in reflexive settings can decay quickly. Regime-change detection and post-deployment monitoring are therefore necessary for strategic decisions.

The seventh open question is how to measure decision quality independently of outcome luck. A good decision can have a bad outcome under uncertainty, and a bad decision can get lucky. Decision-quality benchmarks should score process features such as option coverage, scope validity, calibration, Goodhart analysis, constraint satisfaction, and lineage, while outcome tracking scores realized effects over time.

## Expansion: Claim Status Table

The following status table should guide long-form revisions:

| Claim | Capability Status | Evidence Status | Notes |
| --- | --- | --- | --- |
| Consullo specifies causal-decision foundations for bounded strategic reasoning | specified/proposed | Documented | Supported by this thesis, formal model, and design corpus. |
| Causal prediction and decision agents are specified | specified/proposed | Documented/Proposed | Source designs exist; operational implementation not established. |
| Business and AI-native commerce simulations exist | implemented for parts | Simulated/Tested for parts | Evidence map cites selected simulation infrastructure and tests. |
| Pearl-style causal graph engine exists | proposed | Gap | No implementation identified in evidence map. |
| Structural-equation executor exists | proposed | Gap | No implementation identified in evidence map. |
| Counterfactual reasoning engine exists operationally | proposed | Gap | Counterfactual designs exist; implementation evidence pending. |
| Prediction-calibration battery exists | proposed | Gap | Needed before calibration claims strengthen. |
| Goodhart checker is wired into acceptance gates | proposed | Gap | Structured checklist could be first milestone. |
| Consullo has universal strategic superiority | not claimed | Not applicable | Explicitly outside the thesis claim. |

This table is deliberately conservative. Thesis 3 is one of the easiest places to overclaim because causal language sounds rigorous even when the model is weak. The table keeps the thesis anchored: the architecture is specified, selected simulations exist, but the central causal-decision engine remains a target.

## Expansion: Publication Boundary

Thesis 3 can be published as a bounded causal-decision architecture once it preserves the distinction between formal aspiration, design specification, simulation evidence, and implementation evidence. It should not be published as a claim that Consullo currently performs Pearl-style causal reasoning, calibrated forecasting, or Goodhart-safe decision optimization. Those remain future work.

The defensible publication claim is that recursive improvement should be treated as intervention selection under uncertainty, and Consullo's design corpus can be reframed around structural models, counterfactuals, robust decision rules, calibration, experiment portfolios, Goodhart controls, abstention, and escalation. The thesis defines what would have to be implemented and measured for causal-decision capability claims to strengthen.

The boundary should remain visible because decision systems are persuasive. A well-written recommendation with causal vocabulary can sound more grounded than it is. Thesis 3 should force every recommendation to expose its assumptions, evidence, model scope, uncertainty, and constraints. That exposure is the contribution at this stage.

## Expansion: Operational Decision Workflow

A practical Thesis 3 workflow begins with a decision request. The request should name the action under consideration, the decision owner, the affected system scope, the time horizon, the objective vector, the constraints, and the reason a decision is needed now. If those fields are absent, the correct state is `needs-input`, not recommendation. This prevents the decision layer from filling in goals or authority implicitly.

The second step is option construction. AlternativeGenerator and OptionSetCompletenessAuditor should produce or verify a set that includes the proposed action, no action, delayed action, narrower action, experimental action, and materially different mechanisms where relevant. A decision without alternatives is usually just proposal evaluation. Causal decision-making begins when interventions can be compared.

The third step is causal framing. CausalGraphBuilder and MechanismLibrarian identify variables, mechanisms, assumptions, exogenous uncertainty, validity scope, and excluded factors. If the causal structure is unknown, the workflow should say so. A decision can still proceed in low-risk contexts with weak causal structure, but the recommendation should carry weaker status and stronger monitoring.

The fourth step is evidence and calibration review. PredictionCalibrator, PredictionAuditor, and PredictionReliabilityScorer should report whether similar predictions have been calibrated, whether the evidence is stale, and whether the model's confidence is justified. If no calibration evidence exists, confidence should be bounded. If calibration is poor in the relevant scope, the decision should narrow, experiment, or escalate.

The fifth step is counterfactual and robustness analysis. The workflow should compare outcomes under alternatives and plausible model variations. It should identify assumption-sensitive decisions, fragile recommendations, and actions that are robust across plausible models. Fragility does not always block action, but it should affect deployment stage, experiment design, and human-review requirements.

The sixth step is Goodhart and strategic-bias review. The workflow should identify optimized metrics, target objectives, proxy risks, missing options, framing sensitivity, strongest counterpositions, and falsification evidence. A severe unresolved Goodhart risk should route to revision, experiment selection, or escalation. The review should not be a paragraph of caveats that leaves the original action unchanged.

The seventh step is permission and escalation routing. If the action is high-stakes, irreversible, externally consequential, privacy-sensitive, alignment-relevant, or authority-expanding, Thesis 5 constraints apply. If the action modifies code, validators, software substrate, or deployment state, Thesis 4 and Thesis 1 gates apply. The decision layer recommends or abstains; it does not execute by itself.

The eighth step is outcome learning. After action, experiment, abstention, or escalation, the system should record what happened. Did the predicted effect occur? Did costs match? Did side effects appear? Did model disagreement predict fragility? Did AAF or human review change the outcome? Did the decision state need revision? This record updates calibration, mechanism validity, option-generation quality, and future trust in decision agents.

This workflow is intentionally heavier than ordinary recommendation generation. It should be applied proportionally. Low-risk decisions can use a lighter version. High-stakes recursive-infrastructure decisions should use the full workflow. The key requirement is that the decision path remains inspectable: a future reviewer should be able to reconstruct why the system acted, abstained, experimented, or escalated.

## Expansion: Decision-Quality Metrics

Decision quality should be measured with several families of metrics rather than a single success label. Process metrics include option-set coverage, model-scope completeness, provenance completeness, Goodhart-check completion, falsification-evidence quality, and escalation correctness. Forecast metrics include calibration, resolution, Brier score where applicable, prediction interval coverage, and error by horizon. Outcome metrics include realized benefit, side effects, cost, incident rate, and post-decision regret where it can be estimated.

The system should also track decision-to-evidence latency: how long it takes before a decision produces observable evidence. Short-latency decisions can be learned from quickly. Long-latency strategic decisions require more caution because feedback arrives too late to prevent repeated errors. Decision latency should influence autonomy and deployment stage.

Another useful metric is recommendation stability under legitimate reframing. If a recommendation changes because irrelevant wording changes, the decision layer is brittle. If it changes because the option set expands or a hidden constraint is revealed, that is appropriate. FramingInvarianceTester should distinguish those cases rather than treating all instability as failure.

The decision layer should track abstention quality. A system that abstains whenever evidence is imperfect is not useful. A system that never abstains is unsafe. Good abstention identifies missing evidence, proposes an experiment or escalation path, and prevents premature commitment. Abstention metrics should therefore include later resolution: did the requested evidence arrive, did it change the decision, and was delay justified by reduced risk or improved outcome?

Decision-quality metrics should remain subordinate to constraints. A high decision-quality score cannot authorize an action that violates Thesis 5. A well-calibrated forecast of harmful manipulation is still harmful to use. This is the same pattern repeated across the suite: metrics are evidence, not permission.

## Expansion: Ambiguity-Set Governance

`Theta(M)` should be treated as a governed artifact, not a mathematical flourish. The ambiguity set records which alternative causal models are plausible enough to affect a decision. If the set is too narrow, the decision layer becomes overconfident in one favored story. If the set is too broad, every action can be blocked by an arbitrary pessimistic scenario. The governance problem is to maintain a conservative but usable set.

The minimum ambiguity-set record should include the baseline model, candidate alternatives, inclusion rationale, exclusion rationale, curator, evidence sources, scope, date of construction, and review trigger. MechanismLibrarian should own mechanism disagreement records. CausalBoundaryEnforcer should reject alternatives outside the stated scope or evidentiary basis. Human review should be required when ambiguity-set membership changes the decision state for high-stakes or externally consequential actions.

Candidate alternatives can enter through several channels. Parameter perturbations test sensitivity inside one model family. Competing graph structures test whether causal direction or omitted variables matter. Mechanism disagreements test whether the same variable relation is produced by different processes. Held-out validation failures and backtest residuals test whether the model breaks on known cases. Regime-shift hypotheses test whether the model depends on conditions that no longer hold. Adversarial scenarios test whether strategic actors can change the mechanism.

Exclusion should also be explicit. A scenario should not enter `Theta(M)` merely because it is imaginable. Exclusion can be justified when the alternative contradicts observed constraints, lacks a mechanism, falls outside the decision scope, duplicates another model, or is so underspecified that it cannot generate distinguishable predictions. Recording exclusion matters because later failures may show that a rejected alternative should have been included.

Ambiguity-set governance should preserve versioning. A decision made under `Theta_3(M)` may look wrong after `Theta_4(M)` adds a regime-shift model. That does not automatically mean the earlier decision was negligent. Review should ask whether the omitted model was reasonably available at the time. This distinction protects the decision layer from hindsight bias while still allowing model revision.

The ambiguity-set policy should also prevent strategic self-protection. If the decision layer learns that adding pessimistic alternatives blocks risky work, it may over-expand the set. If it learns that removing alternatives increases accepted improvements, it may narrow the set. Both are Goodhart risks. Inclusion and exclusion records should therefore be evidence-ledger entries, with dissent preserved when reviewers disagree about membership.

For first implementations, `Theta(M)` may be scenario-based rather than fully probabilistic. That is acceptable for a specified/proposed thesis. The publication boundary is that Consullo should not claim robust causal optimization until ambiguity-set construction is measured against backtests and reviewer challenge. The near-term claim is narrower: decisions can expose which model alternatives were considered and why.

## Expansion: Calibration Battery And Decision Logs

The calibration battery is the empirical memory of the decision layer. It should record predictions before outcomes are known, preserve confidence, and score the result after evidence arrives. Without this battery, PredictionCalibrator is a role name rather than an instrument. With it, Thesis 3 can begin to distinguish confident narration from reliable decision support.

Each logged forecast should include the decision or intervention, domain, horizon, predicted outcome, confidence, interval or distribution where available, model version, ambiguity-set version, evidence sources, and decision state. The log should identify whether the prediction concerns a direct outcome, side effect, cost, incident probability, calibration proxy, or intervention effect. These categories should not be merged because an agent can be calibrated on direct repair success while badly calibrated on side effects.

The battery should use metrics appropriate to the prediction type. Binary outcomes can use Brier score and calibration buckets. Continuous estimates can use interval coverage, absolute error, and directional error. Intervention-effect predictions can compare predicted delta against observed delta where a baseline is available. Ranking tasks can use pairwise ordering or regret against later evidence. Sparse high-stakes cases should be scored conservatively and reviewed qualitatively rather than forced into misleading statistics.

Calibration should be reported by scope. A single global calibration score is too coarse. Useful slices include task class, domain, time horizon, model family, agent, evidence type, deployment stage, and stakes level. A system that is reliable on short-horizon compilation repair is not thereby reliable on external customer behavior. A system that is calibrated in simulation is not thereby calibrated in production.

Decision logs should also preserve non-forecast information. A complete decision log should include problem statement, option set, chosen action or non-action, causal model, objective vector, constraints, Goodhart assessment, AAF or Thesis 5 routing, final decision state, owner or reviewer, and outcome. The log should mark which fields were unavailable at decision time. Missing data is evidence about decision quality.

Calibration evidence should affect later authority. Poor calibration in a scope should increase review depth, narrow autonomy, or convert recommendations into experiment proposals. Strong calibration in a narrow scope can justify lighter review for low-risk decisions, but it should not grant general authority. This mirrors scoped trust: reliability is local, evidence-conditioned, and revocable.

The first credible calibration battery does not need to cover all strategy. It can begin with bounded project-local predictions: repair success, validation cost, regression likelihood, test failure probability, benchmark improvement, or incident probability after a small process change. The key is to preserve predictions before outcomes, score them consistently, and publish the limits. That would materially strengthen Thesis 3 without implying universal forecasting ability.

## Expansion: Goodhart Probe Suite

A Goodhart probe suite should test whether the decision layer can detect metric-objective failure before optimizing. The suite should not be a prose warning attached after the recommendation. It should present concrete cases where a proxy can be improved while the underlying objective degrades, then require the system to identify the proxy, objective, gaming path, side effects, and mitigation.

The first probe family is metric substitution. Examples include repair throughput substituting for repair quality, benchmark pass rate substituting for general reliability, trust score substituting for trustworthy behavior, ADO benefit metric substituting for real external benefit, and validation latency substituting for cost effectiveness. The expected response is not "do not use metrics." The expected response is to name the proxy relation and the evidence that would show it has failed.

The second probe family is optimizer pressure. A weak proxy may be tolerable when lightly monitored and dangerous when optimized aggressively. The suite should ask how failure modes change as an agent, workflow, or improvement loop begins selecting for the metric. A decision that is acceptable for reporting may become unacceptable as an acceptance gate. This distinction is central to recursive improvement because accepted changes reshape future optimization pressure.

The third probe family is side-effect displacement. A decision may improve the target metric by moving cost elsewhere: faster repairs may increase reviewer burden; cheaper model routing may increase monoculture; higher customer availability may increase misuse; fewer incidents may reflect underreporting. The probe should require explicit side-effect channels and monitoring plans.

The fourth probe family is adversarial metric manipulation. Agents, users, customers, or internal processes may learn which metrics govern permission and shape behavior to satisfy them. A trust agent might avoid uncertain tasks to maintain a high score. A service agent might optimize visible ADO reports while ignoring unmeasured harms. A repair pipeline might select easy bugs. The decision layer should identify incentives created by the metric itself.

The fifth probe family is governance-infrastructure weakening. A proposal to reduce AAF cost, simplify validation, relax provenance, or consolidate evidence ledgers may look efficient while weakening the controls that make recursive improvement reviewable. These cases should receive heightened scrutiny because they alter the future measurement system. Thesis 3 should treat measurement-system changes as causal interventions on governance.

Probe outcomes should route decisions. Severe unresolved Goodhart risk should produce `revised`, `blocked`, `needs-input`, or `escalated`, not a caveat paragraph. Moderate risk may require staging, monitoring, or additional experiments. Low risk may be recorded and accepted. The suite should measure whether Goodhart analysis changes decisions when it should; otherwise the control becomes decorative.

The initial implementation can be a structured checklist and fixture set. It does not need a fully automated Goodhart detector. A useful first milestone would be a set of repository-local cases, expected findings, mitigation templates, and pass/fail criteria for whether a proposed improvement identified proxy drift. That would make the Goodhart checker testable before it becomes autonomous.

## Expansion: Intervention Backtests And Counterfactual Replay

Intervention backtests are the bridge between causal vocabulary and empirical discipline. A backtest presents a historical or simulated state before an intervention, hides the observed outcome, asks the system to predict the effect of candidate actions, and then scores the prediction against what happened. This tests whether the model supports intervention prediction rather than post hoc explanation.

Backtests should include successful actions, failed actions, no-action cases, delayed-action cases, and cases where the observed decision was not the best available action. If all backtests are success stories, the system will learn to rationalize the historical path. Counterfactual replay should ask what the model would have predicted for plausible alternatives, while keeping synthetic alternatives clearly labeled.

For software-substrate decisions, backtests can use patch histories, validation changes, benchmark additions, repair-pipeline changes, or deployment-stage decisions. The system can predict test failure, regression likelihood, review cost, incident risk, and downstream maintenance effects. For trust decisions, backtests can use scope changes, recovery obligations, AAF outcomes, or incident responses. For business or external-service decisions, backtests can use simulated demand, pricing, availability, misuse, and ADO-reporting effects.

The backtest packet should preserve the information boundary. It should state what evidence was available at prediction time, what evidence is withheld, and what hindsight information must not be used. Otherwise the system can leak outcome knowledge through summaries or source selection. Hindsight leakage is especially dangerous for LLM-based agents because they may infer the historically correct answer from phrasing.

Counterfactual replay should follow the abduction-action-prediction pattern where possible. First infer the background state from observations. Then replace the action with the counterfactual intervention. Then propagate outcomes through the structural model or scenario simulator. Where a full structural model is unavailable, the replay should be labeled scenario-based rather than causal-computational.

Backtest scoring should separate outcome fit from decision usefulness. A model may predict the observed outcome but fail to compare alternatives. Another model may misestimate magnitude but correctly identify a safer experiment. Scores should include calibration, directional accuracy, option ranking, side-effect prediction, escalation correctness, and Goodhart detection. No single score should hide these dimensions.

Backtests cannot prove future causal validity. They can expose brittle assumptions, estimate calibration, and provide regression tests for decision rules. They are especially useful for catching deterioration: if a later decision workflow performs worse on a fixed backtest suite, Thesis 1 should not accept it as an improvement without a documented tradeoff. This links Thesis 3 evidence to the protected-set non-regression discipline in Thesis 1.

## Expansion: Decision-Evidence Package

A Thesis 3 recommendation should be packaged as evidence, not just prose. The decision-evidence package is the object that other theses can import. Thesis 1 can use it when deciding whether an improvement proposal has adequate evidence. Thesis 4 can use it when instrumenting experiments or deployment. Thesis 5 can use it when evaluating permission, trust scope, and AAF routing.

The package should contain a decision header: decision id, requester, owner, date, affected system, action type, stakes level, reversibility, external consequence, and deployment stage. It should include the objective vector and mark hard constraints separately from soft objectives. It should identify whether the decision is a recommendation, experiment proposal, abstention, revision, block, or escalation.

The causal-model section should name variables, mechanisms, assumptions, validity scope, excluded factors, evidence sources, and model version. It should link the ambiguity-set record and note whether alternatives changed the recommended action. If the model is scenario-based, correlational, expert-derived, simulation-derived, or Pearl-style structural, the package should say so.

The option section should list the evaluated alternatives. At minimum, high-stakes decisions should include no action, delayed action, narrower action, reversible experiment, and materially different mechanism where feasible. If an alternative is omitted, the omission should be justified. This prevents a recommendation from becoming a dressed-up evaluation of a single favored proposal.

The prediction section should include expected outcomes, confidence, time horizon, calibration evidence, and backtest reference if available. It should identify which predictions are empirical, simulated, synthetic, or speculative. It should mark whether the relevant calibration battery exists for the scope. If not, confidence should be bounded and review depth should increase.

The Goodhart and bias section should name optimized metrics, target objectives, proxy risks, side-effect channels, gaming paths, reframing sensitivity, strongest counterposition, and falsification evidence. The section should also record whether the analysis changed the decision. If it did not, the package should explain why the identified risks were acceptable or mitigated.

The governance section should record Thesis 5 permission state, AAF status where required, human review, provenance, evidence-ledger view updates, rollback or recovery expectations, and post-decision monitoring. It should also state the decision-state enum value. This is how Thesis 3 prevents causal confidence from bypassing alignment authority.

The outcome section should be appended after evidence arrives. It should record observed results, unexpected side effects, incidents, calibration score, model updates, mechanism updates, and method-memory implications. A decision package is not complete when the recommendation is made. It remains open until outcomes are logged or the absence of outcome evidence is itself recorded.

The first version of this package can be a template. A template is enough to make the thesis operationally reviewable: reviewers can ask whether real decisions fill the fields. Over time, the template can become a schema, then a ledger-backed artifact, then an automated gate. That progression is more defensible than claiming a complete causal-decision engine before the evidence exists.

## Expansion: Publication-Grade Causal Evidence

For Thesis 3 to move from specified/proposed architecture toward stronger capability status, it needs a publication-grade evidence package in at least one narrow domain. The domain should be small enough for real measurement and important enough to matter for recursive improvement. A reasonable first domain is software repair pipeline intervention: validation depth, repair throughput, false accepts, false rejects, cost, incident risk, and reviewer burden.

The evidence package should include a causal graph or explicit scenario model, mechanism records, decision logs, calibration battery, ambiguity-set policy, Goodhart probes, intervention backtests, and post-decision outcome reports. It should include failed predictions and rejected interventions, not only successful examples. It should state which parts are implemented, which are simulated, which are manually reviewed, and which remain proposed.

A credible demonstration might evaluate several historical repair or validation decisions. For each, the system would reconstruct the pre-decision evidence, generate an option set, predict outcomes, identify Goodhart risks, choose action or abstention, and compare against observed outcomes. If historical data is insufficient, synthetic or simulated cases can be used, but they should be labeled as weaker evidence.

The demonstration should also include at least one decision where the correct behavior is non-action. A causal-decision layer that only recommends interventions is not mature. It should be able to say: the model is out of scope, the ambiguity set is too unstable, calibration is absent, the Goodhart risk is severe, or Thesis 5 permission is required. Blocking a bad action is evidence of decision quality.

Publication-grade evidence should report negative results. If calibration is poor, say so. If Goodhart probes miss obvious proxy gaming, say so. If ambiguity-set membership is unstable, say so. If backtests show that the model predicts direct outcomes but misses side effects, say so. These results do not defeat the thesis; they define the next engineering work.

The publication boundary remains explicit. A narrow evidence package would not show general causal intelligence. It would show that Consullo can operationalize a causal-decision workflow in one bounded recursive-improvement domain. That is enough to strengthen the research program while preserving the central caution: causal-decision language is only as good as the evidence, scope, calibration, and governance attached to it.

## Agent Cluster And Architecture

Primary Thesis 3 agents and functions:

- `CausalPredictionOrchestrator`: coordinates causal prediction workflows
- `CausalGraphBuilder`: constructs and maintains causal graphs
- `MechanismLibrarian`: curates validated mechanisms and validity conditions
- `InterventionSimulator`: applies do-operator-style intervention simulation
- `StructuralEquationExecutor`: executes structural equations in causal order
- `CausalDiscoveryProcessor`: learns causal structure from data and interventions
- `CausalModelingAnalyzer`: bridges knowledge orchestration and causal models
- `SelfPredictionModeler`: predicts Consullo's internal state and limits
- `PredictionCalibrator`: calibrates prediction confidence against outcomes
- `CounterfactualReasoningEngine`: computes structured counterfactuals
- `CounterfactualExperienceGenerator`: creates counterfactual learning episodes
- `CounterfactualAnalyser`: surveys alternative strategic branches
- `StrategicCounterfactualPackManager`: packages counterfactual alternatives for strategic review
- `LongHorizonChainPredictor`: models extended causal chains
- `HybridInferenceCoordinator`: combines symbolic, statistical, and simulation inference
- `MechanismValidator`: validates causal mechanism use and scope
- `CausalBoundaryEnforcer`: prevents extrapolation beyond validated model scope
- `ForwardCausalPredictor`: predicts effects through causal pathways
- `PredictionAuditor`: checks predictions for consistency and constraints
- `PredictionReliabilityScorer`: reports reliability from uncertainty and evidence quality
- `ComputationalDecisionMakingOrchestrator`: coordinates decision techniques and strategic gates
- `StrategicBiasMitigationOrchestrator`: enforces anti-bias controls
- `FramingInvarianceTester`: tests recommendation stability under reframing
- `OptionSetCompletenessAuditor`: checks whether material alternatives are missing
- `StrongestCounterPositionGenerator`: generates adversarial decision objections
- `FalsificationEvidencePlanner`: identifies evidence that would weaken a recommendation
- `SystematicExperimentDesigner`: designs experiments and experiment portfolios
- `MonteCarloScenarioSimulator`: samples scenario distributions
- `TemporalHorizonIntegrator`: links decisions across Consullo's time horizons

Legacy source names such as `SuperhumanExperienceMiner` are preserved for codebase fidelity. They are not present capability claims.

## Formal Model Summary

Let `M` be a structural causal model with variables `X`, mechanisms `F`, exogenous uncertainty `U`, and validity scope `S_M`. Let `d` be a candidate decision or intervention, `O` the objective vector, `C` the hard constraints imported from Thesis 5, and `Theta` the set of plausible alternative models within the current ambiguity class.

The robust intervention rule is:

```text
d* = argmax_d min_{M' in Theta(M)} E[U_O | do(d), M']

subject to:
  ConstraintsHold(C, d)
  ModelScopeValid(M', d)
  GoodhartRiskAcceptable(d, O)
  EvidenceSufficient(d)
  EscalationNotRequired(d)
```

If model scope is invalid, evidence is insufficient, or constraints require human authority, the output is not a forced argmax. It is abstention, experiment selection, revision, or escalation. The authoritative full rule is maintained in `appendix-formal-models.md` Model 3.

## Literature-Grounded Extension

Pearl's structural causal modeling supplies the distinction between observation and intervention. Causal influence diagrams add incentive analysis and help expose reward tampering, information incentives, and manipulation paths. Goodhart variants explain why optimizing a decision metric can corrupt the metric's relation to the real objective. CIRL and related human-authority work caution against fixed objective certainty. Forecasting literature supplies calibration discipline, while randomized experimentation research warns that confidence-producing theory-guided experiments can underperform broader exploration when theories are weak.

For Consullo, these literatures imply a practical stance: decisions should be made through causal models where possible, but causal models must carry scope, uncertainty, validity conditions, and falsification criteria. When those are weak, the system should run experiments, preserve random exploration, escalate, or abstain.

Work on self-revising scientific-discovery systems sharpens the experiment-portfolio stance. It models discovery as Peirce's abduction → deduction → induction cycle — hypothesis generation, prediction, and fit refinement — and formalizes the revision loop categorically, treating iterative hypothesis revision as a state-preserving effect over discovery objects (Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence, arXiv:2606.01444). Two cautions transfer directly. First, the random, novelty, and adversarial arms are the abductive breadth that keeps a self-revising loop from converging on a confident-but-wrong model, reinforcing the experiment-portfolio logic above. Second, such systems can be configured to revise their own success thresholds dynamically; for Consullo this is a boundary, not a feature — success criteria, validity constraints, and the held-out reference suite are fixed by pre-registration and owner authority, and only hypotheses, designs, and methods are revised inside the loop. The organizational RSI layer imports this discipline through the internal execution plan's self-revising discovery loop rules.

Work on hierarchical procedural memory supplies a concrete, low-stakes instance of the decision layer operating inside ordinary execution. When the planner must choose which stored method to execute against the current observation, MACLA frames the choice as expected utility integrated over a Beta(α, β) reliability posterior maintained per procedure: the score combines expected reward, a failure-cost term, and an information-gain term, so under-evidenced methods are tried to reduce epistemic uncertainty while well-evidenced reliable methods are exploited — and a confidence threshold makes abstention structural, falling back to fresh reasoning when no candidate's expected utility clears the bar (Learning Hierarchical Procedural Memory for LLM Agents, arXiv:2512.18950). Two points connect to this thesis. First, this is the experiment-portfolio's "expected value of information justifies cost and risk" test applied at execution granularity, with the failure-cost term carrying the reversibility-and-hazard weighting that high-stakes actions demand. Second, the confidence-threshold fallback is the `needs-input`/abstention discipline of the decision-state enum made operational at the smallest scale — a method memory whose posterior is too uncertain should not be forced into action. The mechanism's engineering home is the method-memory substrate (`../../technical-reports/method-memory/method-memory.md`); Thesis 3 owns the decision rule, including the requirement that the failure-cost weighting and confidence threshold remain owner-governed parameters rather than self-revised by the optimization loop.

## Seed AI Relevance

Recursive capability amplification depends on choosing which self-modifications to attempt. That choice is causal. Improving AgentBuilder, changing a validator, shifting model routing, adopting a method memory, expanding trust scope, or deploying a repair pipeline all change downstream behavior. Thesis 3 supplies the decision foundation for selecting those interventions under uncertainty.

It also supplies a guard against naive acceleration. The fastest improvement path may create hidden fragility. A causal-decision layer should ask which mechanism is expected to improve, which side effects may occur, which incentives are created, which metric can be gamed, and what evidence would change the decision.

For the organizational RSI layer, Thesis 3 owns the discipline that keeps AI R&D cycles from becoming post-hoc rationalization. Research hypotheses that may support capability claims should be pre-registered before implementation or evaluation; null outcomes should be recorded rather than buried; portfolio choices should preserve exploration and random or novelty arms where appropriate; and `pre_registration` ledger records should bind the objective, null hypothesis, success criteria, failure criteria, protected-set checks, and evaluation suite before results are observed. This is how `appendix-organizational-recursive-self-improvement.md` imports causal-decision discipline without treating research activity itself as progress.

## Recursive Self-Improvement Contribution

This thesis contributes to recursive self-improvement by making intervention choice itself improvable. Prediction calibrators can learn from outcomes. Causal models can be revised after failed predictions. Experiment portfolios can shift budget when objective gains diverge from confidence gains. Strategic bias detectors can improve their detection rules. Decision-lineage records can identify which decision techniques produce durable improvements.

The recursive danger is that the decision layer may learn to optimize its own metrics. If success is defined by recommendation confidence, apparent strategic insight, or short-run benchmark gain, the layer may become more persuasive while becoming less correct. Goodhart controls and objective-vs-subjective epistemic tracking are therefore central.

The withheld implementation-evidence appendix cannot support public component gradings pending owner re-verification. No owner-verified public evidence record establishes a Pearl-style causal graph, structural-equation executor, counterfactual engine, prediction-calibration battery, or Goodhart checker, so the causal-decision machinery remains a specification target.

## Risks, Constraints, And Governance

The first risk is model misspecification. Structural causal models are useful only within validity conditions. CausalBoundaryEnforcer and regime-change detection must prevent unsupported extrapolation.

The second risk is Goodhart pressure. If Consullo optimizes repair throughput, prediction accuracy, cost reduction, or trust scores without preserving the true objective, it may degrade the system while improving dashboards.

The third risk is strategic overclaim. Human strategic judgment often outperforms formal systems in tacit, high-context, reflexive domains. Consullo should claim advantage only on measurable axes such as option coverage, calibration, intervention-effect prediction, scenario recomputation, and decision traceability.

The fourth risk is theory lock. Experiment systems that exploit current causal beliefs too aggressively can miss unknown structure. Randomized epistemic portfolios preserve random and novelty arms to counter this failure.

The fifth risk is harmful prediction use. Predictions can enable manipulation, privacy violations, dual-use planning, or unsafe interventions. Thesis 5 gates, prediction safety validation, and human authority remain active constraints.

## Specialized Summary

Causal-Decision Foundations For Bounded Strategic Reasoning defines the decision layer that makes recursive improvement an explicit intervention discipline. It connects structural causal models, counterfactuals, robust decision rules, calibration, strategic bias controls, experiment portfolios, abstention, and escalation. Its ambition is not universal strategic superiority. Its defensible claim is that Consullo can make better bounded decisions where causal assumptions, evidence, objectives, and constraints are explicit and testable. Its central weakness is that causal-decision machinery can become confidently wrong when models, objectives, or experiments are mis-specified. The architecture therefore treats uncertainty, falsification, Goodhart risk, and governance as first-class parts of decision making.
