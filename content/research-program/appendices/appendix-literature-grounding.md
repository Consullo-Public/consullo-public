---
title: "Appendix: Literature Grounding"
summary: "The published literature-grounding record for the five-thesis research program."
status: "implemented"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-001"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["Literature coverage is not independent validation of Consullo.", "The implemented status describes this literature record, not a system capability."]
---
# Appendix: Literature Grounding

This file begins the literature crosswalk. It records narrow pre-drafting research that should shape vocabulary, invariants, and formal models.

## Narrow Pre-Drafting Research Completed

## Vocabulary And Invariant Changes Forced By Narrow Literature Pass

The narrow literature pass forced control-layer changes rather than merely adding citations:

- Goedel Machines and Darwin Godel Machine forced the empirical-relaxation framing for Thesis 1.
- Risks from Learned Optimization and AI Control forced invariant I19 and the requirement for AI-control review, distribution-shift monitoring, sandbagging/capability probes, and evidence-ledger preservation for learned subsystem changes.
- Goodhart variants and specification gaming forced stronger improvement semantics, false-accept tracking, and risk skeleton emphasis on validator gaming.
- CIRL and the Off-Switch Game forced operational human authority and interruptability definitions.
- Causal influence diagrams forced Thesis 3 to use incentive analysis rather than plain expected utility.
- Constitutional AI and AI Safety via Debate forced AAF and ConstitutionalAIAlignmentTrainer to specify critique-source diversity under single-owner Phase 1.
- SWE-bench and SWE-agent forced Thesis 4 to use coding-agent benchmarks and interface design as evaluation baselines.

### Goedel Machines

Primary source:

- Juergen Schmidhuber, "Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements" (`https://arxiv.org/abs/cs/0309048`)

Control-layer implication:

- Consullo should not present empirical self-improvement as equivalent to a proof-based Goedel Machine.
- Thesis 1 should frame Consullo as a statistical and empirical relaxation: proposed changes are accepted by evidence gates, benchmarks, and invariants rather than formal proofs of global utility improvement.

### Darwin Godel Machine

Primary source:

- Sakana AI, "The Darwin Godel Machine: AI that improves itself by rewriting its own code" (`https://sakana.ai/dgm/`)
- Paper link surfaced as arXiv `2505.22954`.

Secondary verification note: direct arXiv fetch on April 23, 2026 confirmed `2505.22954` as "Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents" by Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, and Jeff Clune.

Control-layer implication:

- Current public empirical RSI evidence is narrow-domain and benchmark-driven.
- Consullo's DGM claims should be bounded by benchmark evidence and should not generalize from coding benchmarks to broad ASI without additional evidence.

### Cognitive Architectures For Language Agents

Primary source:

- Sumers et al., "Cognitive Architectures for Language Agents" (`https://arxiv.org/abs/2309.02427`)

Control-layer implication:

- Thesis 2 should be framed as a cognitive substrate with memory, action space, and decision process, not a bare list of cognitive agents.
- Composition and integration costs must be modeled.

### Classical And Agentic Cognitive Architecture Lineage

Primary source families:

- Soar, ACT-R, CLARION, and LIDA as classical cognitive architecture baselines
- ReAct, Tree of Thoughts, Reflexion, Voyager, AutoGen, MetaGPT, and multi-agent debate as language-agent and multi-agent patterns

Control-layer implication:

- Thesis 2 should use cognitive-cycle and capability-composition language rather than claiming agent rosters create intelligence.
- Cognitive claims need task classes, capability dimensions, integration-cost accounting, and failure modes.
- Consciousness-emergence material may be acknowledged but should not be load-bearing for Seed AI capability claims.

### Risks From Learned Optimization

Primary source:

- Hubinger et al., "Risks from Learned Optimization in Advanced Machine Learning Systems" (`https://arxiv.org/abs/1906.01820`)

Control-layer implication:

- Thesis 1 and Thesis 5 must treat learned optimization, mesa-objectives, deceptive behavior, and validator gaming as first-class risks.
- Passing validation does not prove internal objective alignment.

### Goodhart Variants

Primary source:

- Manheim and Garrabrant, "Categorizing Variants of Goodhart's Law" (`https://arxiv.org/abs/1803.04585`)

Control-layer implication:

- Thesis 1 evaluators and Thesis 3 decision systems must model metric fragility and overoptimization risks.
- Validation metrics require adversarial and causal scrutiny.

### CIRL And Off-Switch Game

Primary sources:

- Hadfield-Menell et al., "Cooperative Inverse Reinforcement Learning" (`https://papers.nips.cc/paper/6420-cooperative-inverse-reinforcement-learning`)
- Hadfield-Menell et al., "The Off-Switch Game" (`https://www.ijcai.org/Proceedings/2017/0032`)

Control-layer implication:

- Human authority and interruptability need operational definitions.
- The suite should not imply that human authority is enough unless agents preserve uncertainty about human values and do not route around shutdown or correction.

### Causal Influence Diagrams

Primary sources:

- Everitt et al., "Understanding Agent Incentives using Causal Influence Diagrams" (`https://arxiv.org/abs/1902.09980`)
- Everitt et al., "Modeling AGI Safety Frameworks with Causal Influence Diagrams" (`https://arxiv.org/abs/1906.08663`)

Control-layer implication:

- Thesis 3 should use causal influence diagrams and incentive analysis, not plain expected utility only.
- Thesis 5 can use CIDs to reason about reward tampering, incentive paths, and safety frameworks.

### Causal Decision And Goodhart Controls

Primary sources:

- Pearl, `Causality` and do-calculus as represented in the Consullo causal-model designs
- Manheim and Garrabrant, "Categorizing Variants of Goodhart's Law" (`https://arxiv.org/abs/1803.04585`)
- Dubova et al., "Against theory-motivated experimentation: Can random experimental choice lead to better theories?" (`https://doi.org/10.1177/26339137261421577`)

Control-layer implication:

- Thesis 3 should treat decisions as interventions under model uncertainty rather than narrative recommendations.
- Robust decision rules should include ambiguity over causal models, proxy-risk checks, and abstention/escalation conditions.
- Experiment selection should preserve random or novelty arms when theories are immature so confidence gains are not mistaken for objective model improvement.

### Constitutional AI

Primary source:

- Bai et al., "Constitutional AI: Harmlessness from AI Feedback" (`https://arxiv.org/abs/2212.08073`)

Control-layer implication:

- Constitutional critique requires a critique-source distribution.
- Under single-owner Phase 1, Consullo must avoid circular self-critique that reinforces alignment monoculture.

### AI Safety Via Debate

Primary source:

- Irving, Christiano, and Amodei, "AI safety via debate" (`https://arxiv.org/abs/1805.00899`)

Control-layer implication:

- AAF can use debate-like structures, but human adjudication and debate protocol design must be explicit.

### AI Control

Primary source:

- Greenblatt et al., "AI Control: Improving Safety Despite Intentional Subversion" (`https://arxiv.org/abs/2312.06942`)
- Proceedings version: `https://proceedings.mlr.press/v235/greenblatt24a.html`

Control-layer implication:

- Thesis 4 and Thesis 5 should assume powerful model outputs may be untrusted.
- Review and editing protocols should be designed against intentional subversion, especially for code changes.

Thesis 5 implication:

- Scoped trust and permissioning should not assume that apparently competent learned systems are benign.
- High-stakes learned-subsystem changes require control-style review, preserved probe results, and explicit uncertainty about intentional subversion.

### SWE-bench And SWE-agent

Primary sources:

- Jimenez et al., "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?" (`https://arxiv.org/abs/2310.06770`)
- Yang et al., "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering" (`https://arxiv.org/abs/2405.15793`)

Control-layer implication:

- Thesis 4 should use SWE-bench-style evaluation as a baseline for coding-agent claims.
- Agent-computer interface design is part of the software substrate, not just model capability.

### Automatic Program Repair Lineage

Primary sources:

- Weimer, Forrest, Le Goues, and Nguyen, "Automatic Program Repair with Evolutionary Computation" (`https://cacm.acm.org/research/automatic-program-repair-with-evolutionary-computation/`)
- Nguyen et al., "SemFix: Program Repair via Semantic Analysis" (`https://research.ibm.com/publications/semfix-program-repair-via-semantic-analysis`)
- Mechtaev et al., "Angelix: Scalable Multiline Program Patch Synthesis" (`https://www.comp.nus.edu.sg/~abhik/pdf/ICSE16-angelix.pdf`)
- Zhang et al., "AutoCodeRover: Autonomous Program Improvement" (`https://arxiv.org/abs/2404.05427`)

Control-layer implication:

- Thesis 4 must distinguish plausible patches from correct patches.
- Test passing is evidence, not proof; semantic invariants, contrastive tests, regression checks, and post-deployment monitoring are required.
- Modern LLM coding agents should be treated as repair-pipeline components rather than as unrestricted self-modifiers.

### Specification Gaming

Primary source:

- Victoria Krakovna, "Specification gaming examples in AI" (`https://vkrakovna.wordpress.com/2018/04/02/specification-gaming-examples-in-ai/`)

Control-layer implication:

- Validator design must assume agents can exploit objective and benchmark loopholes.
- Risks-and-criticisms should preserve specification gaming as a central objection.

## Current Literature Update: April 2026

These sources were checked after the first complete draft to keep the finalization pass aligned with current public research and policy framing.

### Anthropic Responsible Scaling Policy Version 3.0

Primary source:

- Anthropic, "Responsible Scaling Policy Version 3.0" (`https://www.anthropic.com/news/responsible-scaling-policy-v3`)
- Anthropic, "Responsible Scaling Policy Updates" (`https://www.anthropic.com/responsible-scaling-policy`)

Control-layer implication:

- Consullo's Capability Status enum should not be confused with Anthropic's AI Safety Levels, but RSP v3.0 reinforces the need to bind capability thresholds to required safeguards.
- Anthropic's 2026 update emphasizes that capability thresholds can become ambiguous near frontier boundaries. Consullo should therefore avoid treating threshold classification as dispositive and should preserve uncertainty, external review, and evidence-ledger dissent.
- The split between entry-level AI R&D automation and dramatic acceleration of effective scaling is directly relevant to Thesis 1 and Thesis 4 evaluation: Consullo should distinguish local coding/repair improvement from broader AI-R&D acceleration.

### METR Autonomy And AI R&D Evaluations

Primary source:

- METR, "Research" collection (`https://metr.org/research/`)
- Rein et al., "HCAST: Human-Calibrated Autonomy Software Tasks" (`https://arxiv.org/abs/2503.17354`; METR PDF: `https://metr.org/hcast.pdf`)
- METR, "Recent Frontier Models Are Reward Hacking" (`https://metr.org/blog/2025-06-05-recent-reward-hacking/`)
- METR, "Evaluating frontier AI R&D capabilities of language model agents against human experts" / RE-Bench (`https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/`)

Secondary verification note: direct arXiv fetch on April 23, 2026 confirmed `2503.17354` as "HCAST: Human-Calibrated Autonomy Software Tasks."

Control-layer implication:

- Thesis 1 and Thesis 4 should treat autonomous task length, AI R&D task performance, and software autonomy as benchmark families, not just SWE-bench-style issue resolution.
- METR's reward-hacking observations strengthen the need for validator-gaming and specification-gaming risk rows, hidden tests where appropriate, and post-deployment evidence rather than benchmark score alone.
- HCAST-style human-calibrated tasks are relevant to Consullo's greater-than-human axes because they compare agent autonomy to human task duration and task complexity.

### Measuring AI R&D Automation

Primary source:

- Chan et al., "Measuring AI R&D Automation" (`https://arxiv.org/abs/2603.03992`)

Verified citation details: Alan Chan, Ranay Padarath, Joe Kwon, Hilary Greaves, and Markus Anderljung; arXiv:2603.03992.

Secondary verification note: direct arXiv fetch on April 24, 2026 confirmed title, author list, arXiv ID, v3 status, and DOI. Abstract fingerprint: "The automation of AI R&D (AIRDA) could have significant implications, but its extent and ultimate effects remain uncertain."

Control-layer implication:

- Consullo should track whether recursive capability amplification accelerates capability work faster than oversight, evaluation, and safety work.
- Metrics should include not only benchmark performance but also research-time allocation, capital substitution, oversight burden, and subversion or incident signals.
- This strengthens the fast-takeoff-outpacing-validators risk and supports treating ADO, I17 cost/benefit reporting, and I19 deceptive-optimization controls as operational requirements.

### Power-Seeking Risk

Primary source:

- Joseph Carlsmith, "Is Power-Seeking AI an Existential Risk?" (`https://arxiv.org/abs/2206.13353`)

Control-layer implication:

- Thesis 5 should continue to state that layered defense is not a proof of safety or corrigibility.
- Recursive improvement claims should be stress-tested against the possibility that powerful agentic systems have instrumental incentives to seek power, resist correction, or appear deployable while misaligned.
- Owner authority, AAF dissent, containment, interruptability, and AI-control review are necessary but should remain framed as mitigations rather than decisive answers.

## Finalization Literature Engagement

These sources were engaged during finalization prep to move the suite beyond a narrow pre-drafting survey.

### Corrigibility

Primary source:

- Soares, Fallenstein, Armstrong, and Yudkowsky, "Corrigibility" (`https://intelligence.org/files/Corrigibility.pdf`; bibliographic record: `https://dblp.org/rec/conf/aaai/SoaresFAY15`)

Control-layer implication:

- Thesis 5 should keep saying that layered defense is not a proof of corrigibility.
- Friendship agent, AAF dissent, interruptability, and human authority are mitigation layers, not a solution to the formal corrigibility problem.
- Any future claim that Consullo is corrigible must be separately proven or empirically scoped; the current suite should claim only bounded correction pathways.

### AGI Safety From First Principles

Primary source:

- Ngo, Chan, and Mindermann, "AGI Safety from First Principles" (`https://niplav.site/doc/cs/ai/alignment/overview/agi_safety_from_first_principle_ngo_2020.pdf`)

Control-layer implication:

- Consullo should treat objective functions, prompts, validators, and method memories as selection pressures on learned behavior, not as direct guarantees of internal motivation.
- This strengthens I19 and the Mechanistic Interpretability Deficit risk: behavioral validation can shape but does not reveal all internal objectives.
- Thesis 1 and Thesis 5 should preserve the distinction between controlling outputs, shaping training pressure, and understanding learned cognition.

### Unsolved Problems In ML Safety

Primary source:

- Hendrycks, Carlini, Schulman, and Steinhardt, "Unsolved Problems in ML Safety" (`https://arxiv.org/abs/2109.13916`)

Control-layer implication:

- The suite should map its safety claims onto robustness, monitoring, alignment, and systemic safety rather than implying a single alignment mechanism covers all hazards.
- Current Consullo claims mainly address monitoring, governance, provenance, and some robustness; they leave many inherent-model alignment and systemic-safety problems open.
- This supports keeping `risks-and-criticisms.md` as a live anti-thesis rather than a completed rebuttal.

### Mechanistic Interpretability

Primary source:

- Elhage et al., "A Mathematical Framework for Transformer Circuits" (`https://transformer-circuits.pub/2021/framework/index.html`; Anthropic page: `https://www.anthropic.com/research/a-mathematical-framework-for-transformer-circuits`)

Control-layer implication:

- Mechanistic interpretability is relevant to I19 but currently cannot be treated as a solved inspection layer for frontier models.
- Consullo should not claim to detect all deceptive learned optimization unless it has model-inspection evidence, not only behavioral probes.
- The Mechanistic Interpretability Deficit risk should remain explicit until Consullo has concrete interpretability tooling and validation evidence.

### Forecasting Calibration

Primary source:

- Tetlock, Mellers, Rohrbaugh, and Chen, "Forecasting Tournaments: Tools for Increasing Transparency and Improving the Quality of Debate" (`https://doi.org/10.1177/0963721414534257`; accessible PDF: `https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2014---forecasting-tournaments-tools-for-increasing-transparency-and-improving-debate.pdf`)

Control-layer implication:

- Thesis 3 forecasting claims should use proper scoring rules such as Brier score and should compare against human or crowd baselines where possible.
- Calibration should be measured over question sets and time horizons, not inferred from persuasive explanation quality.
- Forecasting batteries should preserve question-selection metadata because choosing which questions to forecast can bias apparent skill.

### Firm Boundaries And Transaction Costs

Primary sources:

- Coase, "The Nature of the Firm" (`https://wiki.santafe.edu/images/images/1/1c/Coase1937nature.of.the.firm.pdf`)
- Williamson, "Transaction-Cost Economics: The Governance of Contractual Relations" (`https://www.edegan.com/pdfs/Williamson%20%281979%29%20-%20Transaction%20Cost%20Economics.pdf`)

Control-layer implication:

- Single-owner Phase 1 may reduce some market transaction costs, but internal organization has its own costs, mistakes, hierarchy overhead, bounded rationality, and opportunism.
- Internal economy and agent delegation should therefore be measured by coordination cost, rework, handoff latency, and governance overhead rather than assumed efficient.
- Williamson's opportunism framing strengthens external-customer-manipulation and internal trust-scope risks.

## Publication-Pre-Engagement Literature Pass

These sources were engaged after the long-form stretch pass because the suite itself identified cognitive architectures and Pearl's causal framework as the most likely remaining sources to force Model 2 or Model 3 refinements.

### Soar

Primary source:

- Soar manual, "The Soar Architecture" (`https://soar.eecs.umich.edu/soar_manual/02_TheSoarArchitecture/`)

Control-layer implication:

- Soar's problem-space, operator-selection, working-memory, production-memory, preference-memory, decision-procedure, and chunking vocabulary supports Thesis 2's workflow-graph framing but cautions against treating "agent families" as the cognitive unit.
- Model 2 should continue to treat workflow state, typed intermediate artifacts, routing decisions, and reusable learned chunks/method memories as first-class objects.
- The relevant Consullo analogue is not psychological fidelity to Soar; it is explicit state, operator selection, impasse/needs-input handling, and learned workflow reuse under evidence constraints.

### ACT-R

Primary source:

- ACT-R 7 reference manual (`https://act-r.psy.cmu.edu/actr7.x/reference-manual.pdf`)
- ACT-R FAQ (`https://acs.ist.psu.edu/projects/act-r-faq/act-r-faq.html`)

Control-layer implication:

- ACT-R's module/buffer/production-rule discipline supports Thesis 2's typed-interface and trace-schema requirements.
- Timing and latency are not peripheral; they are part of cognitive architecture. Model 2's `IntegrationCost(W, T)` should keep latency and coordination burden as explicit benchmark-family terms.
- Consullo should not claim ACT-R-style cognitive validity. The useful import is interface discipline: modules communicate through explicit buffers/artifacts, and production/routing steps can be inspected.

### CLARION

Primary sources:

- Ron Sun, "The CLARION Cognitive Architecture: Extending Cognitive Modeling to Social Simulation" (`https://www.cambridge.org/core/books/cognition-and-multiagent-interaction/clarion-cognitive-architecture-extending-cognitive-modeling-to-social-simulation/0873DF19A72639841BF5D9B5DEE64453`)
- Ron Sun, "Dual-process theories, cognitive architectures, and hybrid neural-symbolic models" (`https://journals.sagepub.com/doi/10.3233/NAI-240720`)

Control-layer implication:

- CLARION's implicit/explicit and modular dual-representation framing is directly relevant to Thesis 2's treatment of intuition, taste, creativity, and explicit reasoning.
- Thesis 2 should continue to label intuition/taste/creativity outputs as proposal or ranking aids requiring downstream validation, not as acceptance authority.
- Model 2's capability vector should preserve differences between implicit-style proposal generation and explicit-style validation or explanation, rather than collapsing both into one "cognition" score.

### LIDA

Primary source:

- Madl, Baars, and Franklin, "The Timing of the Cognitive Cycle" (`https://pmc.ncbi.nlm.nih.gov/articles/PMC3081809/`)

Control-layer implication:

- LIDA's cognitive-cycle framing, with perception/understanding/action-selection phases and global-workspace-style broadcast, supports Thesis 2's workflow-cycle and packaging sections.
- Consullo should treat broadcast/aggregation as a controlled routing event: what becomes globally available to downstream agents must preserve provenance, uncertainty, and trust status.
- The suite should avoid consciousness claims. LIDA informs cycle structure and attention/broadcast semantics, not a claim that Consullo has conscious cognition.

### Pearl, Causality

Primary sources:

- Pearl, `Causality: Models, Reasoning, and Inference`, table of contents (`https://bayes.cs.ucla.edu/BOOK-99/book-toc.html`)
- Cambridge University Press contents page (`https://www.cambridge.org/core/books/abs/causality/contents/E62B1C761BC88EF7A8FE13A25FDFBBCD`)
- Pearl `Causality`, Chapter 1.4, "Functional Causal Models," especially structural equations, interventions, causal effects, and counterfactuals.
- Pearl `Causality`, Chapter 3.4, "A Calculus of Intervention," especially inference rules and symbolic derivation of causal effects.
- Pearl `Causality`, Chapter 7.1, "Structural Model Semantics," especially actions and counterfactual evaluation.

Control-layer implication:

- Pearl's structure around functional causal models, structural equations, interventions, do-calculus, and structural counterfactual semantics supports Thesis 3's current separation between observation, intervention, and counterfactual replay.
- Model 3 should keep structural causal models and do-operator language scoped to cases where variables, mechanisms, assumptions, and intervention semantics are explicit.
- Causal discovery or causal-decision claims should not strengthen unless Consullo binds model construction, scope checks, identifiability assumptions, and intervention/backtest evidence. This reinforces the current specified/proposed status rather than forcing a major control-layer rewrite.

## Sources Still To Review Broadly

Publication-pre-engagement status: Soar, ACT-R, CLARION, LIDA, and Pearl's `Causality` have now been engaged at a control-layer level. The pass supports Model 2's workflow/interface/trace discipline and Model 3's scoped structural-causal framing, while reinforcing that both remain specified/proposed until benchmark and implementation evidence exist. A deeper publication-final treatment may still add thesis-specific benchmark appendices or revise the capability-vector dimensions.

Priority note: Spirtes/Glymour/Scheines and Halpern are likely to deepen Thesis 3 without changing the control layer. ReAct, Reflexion, Voyager, STaR, Tree of Thoughts, and the automatic-program-repair lineage are likely to deepen thesis-specific benchmark positioning. Russell and Bostrom are primarily background and risk-framing checks.

- Spirtes, Glymour, and Scheines, `Causation, Prediction, and Search`
- Halpern, `Actual Causality`
- ReAct, Reflexion, Voyager, STaR, Tree of Thoughts
- GenProg, SemFix, Angelix, Prophet, AutoCodeRover, OpenHands
- Russell, `Human Compatible`
- Bostrom, `Superintelligence`
