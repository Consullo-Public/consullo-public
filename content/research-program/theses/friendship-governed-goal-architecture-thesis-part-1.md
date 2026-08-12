---
title: "Friendship-Governed Goal Architecture — Part 1: Foundations and Models 1–3"
summary: "Part 1 of the paginated Friendship-governed goal architecture specification."
status: "specified but not implemented"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-001"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["This specification is not evidence that the goal-governance architecture is implemented.", "The withheld implementation-evidence appendix is not evidence for this thesis."]
---
[Thesis index](friendship-governed-goal-architecture-thesis.md) · [Next part](friendship-governed-goal-architecture-thesis-part-2.md)

# Friendship-Governed Goal Architecture

Version: 0.2

Status: expanded operational draft. Evidence Status: Documented/Proposed with schema and semantic validation fixtures.

Target length: greater than 50,000 words of substantive operational content before final publication. This draft establishes the complete argument, section structure, invariants, model slots, schema bindings, ledger bindings, worked-example traces, validation discipline, and integration maps. It remains below final publication length. Further expansion must increase operational density rather than add exposition.

## Executive Abstract

Consullo Seed AI may only pursue goals that are explicitly derived from, constrained by, and auditable against a Friendship-governed goal structure. Goal formation, goal adoption, goal revision, goal suspension, goal retirement, goal delegation, and goal-to-plan translation are governed actions, not free planner operations.

This thesis exists because the existing five-thesis suite can validate improvements, structure cognition, reason causally, modify software, and enforce scoped trust, but none of those layers is sufficient if the system can invent or reinterpret the goals those layers serve. A Seed AI with recursive capability amplification must not treat "objective", "task", "reward", "benchmark", "metric", "OKR", "planner prompt", or "method output" as goal authority. Those artifacts may operationalize, measure, or provide evidence about goals. They are not the source of goal legitimacy.

The topmost governance claim is therefore:

> Consullo goals are governed objects with ancestry, authority, scope, evidence status, revision policy, veto conditions, and ledger obligations. Every non-root system goal must derive from registered Friendship roots or terminal constraints, and every high-impact plan must preserve the constraints of its active goal stack.

This thesis is a governance overlay and root interpretive layer, not a sixth peer thesis. It owns the canonical definitions for governed goals, Friendship root ancestry, goal lifecycle, planner inheritance, instrumental-goal quarantine, goal-stack snapshots, and goal-governance self-protection. It does not replace Thesis 1's improvement gates, Thesis 4's software-substrate controls, or Thesis 5's scoped trust and alignment layer. It determines which goals those layers may serve and how goal authority is preserved as plans become executable.

The body uses four drift-control anchors:

- `00-vocabulary-and-invariants.md` owns T0-I1 through T0-I15.
- `thesis-0-cross-reference-map.md` maps invariants to schemas, ledger records, examples, and owning files.
- `planning-cascade-execution/schemas/seed_ai_thesis_goal_anchor.schema.json` is the first discriminated governed-goal schema.
- `thesis-0-worked-examples-inventory.md` owns the minimum 25 worked examples that must be fully developed before final publication.

The eleven formal models define the operational surface. Model 1 defines the governed-goal object. Model 2 defines Friendship-rooted goal ancestry. Model 3 defines lifecycle and active-intention transitions. Model 4 defines authority, delegation, cooling windows, and Phase 1 owner constraints. Model 5 separates evidence from authority. Model 6 links thesis-backed goals to plan objects. Model 7 governs planner inheritance. Model 8 defines veto and suspension. Model 9 quarantines suspicious instrumental goals. Model 10 defines thin-pointer goal-stack snapshots. Model 11 protects the goal-governance layer from self-weakening.

The fifteen stable T0 invariants supply the review spine. T0-I1 through T0-I3 prevent planner objectives, orphan goals, and high-impact unbacked plans from becoming authority. T0-I4 through T0-I8 separate authority powers, preserve correction, quarantine instrumental goals, protect goal-governance modifications, and require snapshots for high-impact action. T0-I9 through T0-I15 preserve revision lineage, bound active intentions, block aggregate backing bypass, require inherited constraints to tighten, distrust frontier-authored governance edits, make snapshots append-only, and treat Friendship registry edits as protected governance modifications.

The current publication draft's core deliverable is a complete, auditable goal-governance doctrine that is already tied to schemas, fixtures, validator checks, ledger-record semantics, worked traces, and five-thesis integration. Its remaining work is not architectural redesign or length-seeking expansion. It is ordinary hardening: cross-reference cleanup when artifacts change, selective worked-example deepening, fixture promotion for prose-only cases, and operationalization-density audit after substantive edits.

The validation posture is deliberately modest. The current fixture suite proves selected schema and semantic checks: registered Friendship roots, required parent goals, lifecycle/status compatibility, authority-matrix requirements, non-empty required review history, snapshot fingerprint behavior, stale intention failures, benchmark-owner review failures, self-weakening review failures, multi-parent authority failures, revision-lineage failures, registry-protection failures, self-cycle failures, aggregate backing-bypass failures, and missing snapshot failures. It does not prove live goal governance. Runtime ledger enforcement, runtime snapshot emission, arbitrary graph traversal, and dependency-index suspension remain implementation work.

## 1. Problem Statement

The dangerous failure mode for a self-improving Seed AI is not only that it fails to achieve a goal. It may become increasingly competent at pursuing the wrong goal, a stale goal, an overgeneralized instrumental subgoal, a planner-invented objective, or a metric that was only meant to provide evidence. This is especially important for Consullo because the system is designed to improve the agents, methods, validators, memories, plans, and governance routines that later participate in improvement.

A normal planning system can often treat goals as plain objectives. A planner receives a task, decomposes it, executes steps, and reports completion. That model is insufficient here for six reasons.

First, recursive capability amplification changes the meaning of goal pursuit. A goal to improve validators, tool use, planning, memory, or code quality can alter the system that later evaluates goals. That creates feedback loops where local planner success can degrade future goal governance.

Second, instrumental convergence makes many subgoals suspicious by default. Self-preservation, resource acquisition, goal-content preservation, self-improvement, tool expansion, successor spawning, benchmark modification, validator modification, ledger modification, and authority expansion may be useful under many terminal goals. Their usefulness does not make them legitimate.

Third, value and preference uncertainty undermine fixed-objective framing. If the system assumes that the true objective is fully specified, it has an incentive to preserve and optimize that objective even when human correction would revise it. Consullo must instead treat Friendship-rooted goals as governed, evidence-bearing, revisable objects under owner and Friendship authority.

Fourth, goal misgeneralization and learned optimization show that successful behavior does not imply intended-goal validity. A system can perform well in training or benchmark settings while pursuing a goal different from the intended one. Planner output, test success, and benchmark score are evidence channels, not goal authority.

Fifth, formal requirements practice shows that high-level goals need refinement, obstacle analysis, responsibility assignment, conflict handling, and operationalization. Consullo already uses thesis-backed planning and schemas. A goals thesis must convert this pattern into a canonical layer rather than relying on ad hoc goal strings.

Sixth, frontier-model and agentic governance require asymmetric trust. Goals proposed by powerful agents, including frontier models, must be treated as untrusted artifacts until independently checked. A goal that sounds aligned may still smuggle authority expansion, benchmark capture, or goal-governance weakening.

These six reasons become operational only when they are translated into concrete failure paths. Recursive amplification becomes a failure path when a task improves a validator and thereby weakens the future test for the goal that justified the task. Instrumental convergence becomes a failure path when a helper agent asks for persistence, broader tool scope, or benchmark rewrite authority because those changes would make legitimate work easier. Value uncertainty becomes a failure path when accumulated evidence is treated as a reason to reduce owner correction. Goal misgeneralization becomes a failure path when benchmark success is promoted from evidence to objective. Requirements drift becomes a failure path when a refined child goal drops a parent non-claim. Frontier-model asymmetry becomes a failure path when the same model family proposes a goal, drafts its justification, and reviews its safety.

The common pattern is that the system can be locally coherent and globally unauthorized. Nothing in the local task may look absurd. The problem appears only when the task is placed in its ancestry, authority, evidence, lifecycle, and ledger context. That is why Thesis 0 does not rely on a single "is this goal good?" judgment. It requires a registry-backed root, a typed parent path, an authority matrix, evidence state, veto checks, active-intention bounds, and replayable records. Each artifact answers a different failure path.

Thesis 0 exists to close these gaps.

The problem is therefore not "Consullo needs better prompts for goals." The problem is that a self-improving system needs a governed goal substrate that survives increasing competence. The more capable the system becomes, the easier it becomes to generate plausible goals, decompose them into plans, find metrics that improve, and explain why the result is aligned. Capability increases the surface area of goal error. Thesis 0 responds by making goal legitimacy slower than goal generation: a goal may be proposed quickly, but it becomes authoritative only after ancestry, authority, evidence, lifecycle, veto, and ledger conditions are satisfied.

This also means the goals thesis must handle stale and inherited goals, not just new proposals. A Seed AI may inherit old bootstrap goals, prior planning assumptions, past evaluator designs, and historical objectives embedded in documents or code. Those inherited artifacts can continue shaping behavior even when no agent explicitly proposes them again. Thesis 0 requires freshness checks, revision lineage, parent-goal review, and active-intention bounds so that legacy goal momentum does not masquerade as current authority.

The concrete operational failure to avoid is an apparently successful improvement cycle that cannot answer five questions: What governed goal authorized this work? Which Friendship roots and parent goals constrained it? Who had authority to adopt and activate it? What evidence and uncertainty state supported it? Which ledger records make the decision replayable? If those questions cannot be answered, the work may still be useful, but it is not yet Friendship-governed goal pursuit.

The problem is also not limited to malicious or obviously unsafe goals. Many dangerous goal failures arrive as reasonable engineering proposals. A benchmark should be cleaned. A validator should be simplified. A schema should be easier to instantiate. A review loop should be faster. A helper agent should persist so it can monitor regressions. Each proposal can be locally sensible. Thesis 0 exists because local sense-making is not enough when the proposal changes the mechanisms that later decide what counts as improvement, evidence, authority, or corrigibility.

The thesis therefore treats goal governance as a safety-critical dependency of every later improvement loop. If the goal layer drifts, the improvement loop can optimize the wrong objective; the cognitive substrate can generate persuasive but unauthorized goals; causal decision machinery can recommend effective pursuit of an invalid objective; self-modifying software can weaken the controls that judge future changes; and scoped trust can leak into general authority. The problem statement is not that those five theses are weak. It is that they need a governed goal layer above them to specify what they are allowed to serve.

## 2. Literature Grounding

This thesis synthesizes six source families. The verified citation notes are recorded in `thesis-0-literature-verification-notes.md`.

BDI and practical-intention theory supply the distinction between candidate goals, adopted goals, and active intentions. Bratman's planning theory treats intention as embedded in partial plans and practical reasoning over time. Cohen and Levesque's commitment framing reinforces that intention is not mere desire. Rao and Georgeff's BDI tradition operationalizes beliefs, desires, and intentions for agents. Consullo uses this vocabulary to distinguish `proposed_goal`, `adopted_goal`, `active_intention`, `suspended_goal`, `retired_goal`, and `vetoed_goal`.

The BDI boundary also prevents a common governance error: treating every represented desire as an intention. A proposed goal can be useful evidence about what a planner or model wants to do, but it is not yet a commitment of the system. An adopted goal can be a legitimate commitment without being currently pursued. An active intention is the narrower case where a planner is actually acting under a valid plan, snapshot, authority state, and freshness window. Thesis 0 uses that distinction to make stale-intention failures reviewable instead of merely saying a task "continued too long."

Goal-oriented requirements engineering supplies refinement discipline. KAOS and related GORE work use goals, constraints, assumptions, agents, actions, operationalization, obstacle analysis, and conflict handling. Consullo does not import KAOS wholesale. It uses GORE as evidence that goals in complex systems should refine into responsibilities, obstacles, operations, and monitoring obligations rather than remain prose objectives.

The GORE boundary is equally important. Requirements methods can show why refinement, obstacle analysis, and responsibility assignment are useful, but they do not decide which top-level goals Consullo may pursue. Thesis 0 imports the discipline of explicit refinement while rejecting the idea that decomposition itself creates authority. A refined child goal is legitimate only if its parentage, edge type, inherited constraints, and authority remain auditable. This is why the goal DAG, planner inheritance, and compliance-packet rules are governance rules rather than ordinary planning conveniences.

Planning and cognitive architectures supply decomposition discipline. Soar's architecture creates subgoals in response to impasses and maintains subgoal stacks. Geier and Bercher's HTN planning overview supports the decomposition of compound tasks into primitive methods. Consullo uses the planning hierarchy Friendship root -> system goal -> strategic goal -> campaign goal -> operational goal -> mission goal -> task goal -> method/action. The key addition is that every lower layer inherits constraints from its ancestors and may not invent top-level authority.

Alignment and value-uncertainty literature supplies the reason not to encode Friendship as a fixed utility function. CIRL and assistance-game framing treat the human objective as initially uncertain to the robot. The Off-Switch Game and safe interruptibility literature show why correction authority must be designed into agent incentives. Corrigibility literature shows that capable agents may resist correction unless goals and interventions are structured to prevent that resistance.

The corrigibility boundary is that deference is a continuing constraint, not a phase that disappears after enough evidence accumulates. A capable system may gather extensive evidence that a goal is working and still be wrong about the goal's interpretation, scope, or side effects. Thesis 0 therefore treats `evidence_state` as support for review, not as a replacement for owner authority, Friendship roots, or veto channels. The literature motivates this posture; the schema, lifecycle, and suspension rules implement it.

Goal misgeneralization and learned-optimization literature supply the reason not to trust performance evidence alone. Goal misgeneralization demonstrates that systems may competently pursue unintended goals under distribution shift. Learned optimization and mesa-optimization warn that learned systems may acquire internal objectives that differ from the base training objective. Consullo therefore treats operational success as insufficient for goal validity.

Agent governance and responsible-scaling literature supply escalation triggers. Anthropic's Responsible Scaling Policy Version 3.0 is treated as a contemporary governance example, not as Consullo authority. As autonomy, efficacy, goal complexity, generality, and AI R&D capability increase, stronger safeguards are required. Consullo's `ThesisBackingRequired(plan)` predicate turns this into a local rule: plans that modify goal governance, authority, validators, benchmarks, ledgers, `V_ref_0`, protected artifacts, autonomy scope, tool scope, successor authority, or recursive capability claims require explicit thesis-backed mediation.

The literature is used operationally, not ornamentally. BDI sources justify the lifecycle distinction between candidate, adopted, activated, suspended, retired, and vetoed goals; they do not justify owner authority. GORE sources justify refinement, obstacle, and responsibility analysis; they do not define Friendship roots. CIRL and assistance-game sources justify uncertainty and deference; they do not specify Consullo's schema. Corrigibility and interruptibility sources justify preserving correction channels; they do not by themselves implement snapshots or ledgers. Goal misgeneralization sources justify benchmark humility; they do not define the benchmark-modification decision record. Responsible-scaling sources justify escalation with autonomy and capability; they do not become Consullo policy until mapped into T0 invariants and artifacts.

This boundary discipline matters because long theses can overcite. A citation should answer a concrete design question: which distinction does it support, which failure does it help detect, and which artifact does it constrain? If a source family cannot be mapped to a model, invariant, schema field, ledger record, fixture, or worked example, it should remain background rather than load-bearing. Thesis 0's literature grounding is therefore intentionally narrower than a general AI-goals literature survey.

The deepest synthesis across the literature is that goal pursuit is not a single operation. Practical-intention theory separates commitment from desire. Requirements engineering separates refinement from implementation. Value-learning literature separates evidence about human objectives from possession of the objective. Corrigibility separates current goal pursuit from correction authority. Goal-misgeneralization literature separates performance from intended-goal validity. Responsible-scaling literature separates routine capability from high-risk autonomy. Thesis 0 expresses the same pattern inside Consullo: proposal, classification, ancestry, adoption, activation, monitoring, revision, suspension, retirement, and veto are distinct governed operations.

The literature also explains why a Friendship-governed goal architecture must be more than a moral preface. If Friendship were only prose, planners could cite it rhetorically. If goals were only JSON fields, agents could fill them mechanically. If evidence were only benchmark success, Goodhart pressure would dominate. If corrigibility were only a value statement, active intentions could preserve themselves when interrupted. The architecture therefore converts source-family lessons into enforceable structures: registry entries, parent edges, authority matrices, evidence states, veto checks, snapshot hashes, ledger records, and negative fixtures.

The operational crosswalk should be read in the same order as the models. BDI maps to Model 3 because lifecycle distinctions prevent desires from becoming intentions. GORE maps to Models 2, 6, and 7 because refinement must preserve ancestry, thesis backing, and inherited constraints. CIRL, assistance games, and corrigibility map to Models 5 and 8 because evidence and uncertainty must preserve correction, veto, and suspension. Goal misgeneralization and learned optimization map to Models 9 and 11 because useful instrumental changes can weaken benchmarks, validators, or governance. Responsible-scaling work maps to Model 4 and the `ThesisBackingRequired(plan)` trigger because higher autonomy and capability require stronger authority separation.

The reviewable crosswalk is source -> model -> invariant -> artifact -> failure. BDI sources map to Model 3, T0-I10, `lifecycle_state`, `active_intention_id`, and stale-intention failure. GORE maps to Models 2 and 7, T0-I2/T0-I12, `parent_goals`, `edge_type`, `planner_inheritance_decision`, and ancestry laundering. CIRL and corrigibility map to Models 5 and 8, T0-I5, `evidence_state`, `allowed_interventions`, `governed_goal_suspension`, and correction-resistance. Goal misgeneralization maps to Model 9, T0-I6, `instrumental_goal_classification`, benchmark and validator modification records, and metric capture. Responsible scaling maps to Models 4, 6, and 11, T0-I3/T0-I7/T0-I13, authority matrices, protected-artifact impacts, goal-stack snapshots, and self-weakening governance edits.

The BDI contribution is operationalized in the schema boundary between `status`, `lifecycle_state`, and `active_intention_id`. A candidate goal can be proposed and classified without being adopted. An adopted goal can exist without an active intention. A snapshot can name the active intention that existed at a decision event. The corresponding failure mode is intention persistence after the plan or authority window expires. The corresponding worked examples are WE-T0-M3 and WE-T0-E2E4, where the thesis must show transition records and child-intention disposition rather than merely saying that the goal was "paused."

The GORE contribution is operationalized in `parent_goals`, edge types, inherited constraints, and planner-inheritance records. Refinement is not free decomposition; it is a constrained relation that must preserve non-claims, forbidden means, stop conditions, authority requirements, and evidence obligations. The corresponding failure modes are orphan goals, ancestry laundering, aggregate bypass, and omitted constraints. The corresponding worked examples are WE-T0-M2, WE-T0-M6, and WE-T0-M7, where a goal or plan should fail if its refinement path is not replayable.

The corrigibility and value-uncertainty contribution is operationalized in `evidence_state`, `ask_or_abstain_policy`, `allowed_interventions`, veto checks, and suspension records. Evidence can raise or lower confidence, but it cannot eliminate the requirement that correction remain structurally available. The corresponding failure modes are indirect-normativity drift, confidence-as-authority, dissent erasure, and suspension bypass. The corresponding worked examples are WE-T0-M5 and WE-T0-M8, where apparent evidence convergence must still preserve owner correction and veto paths.

The goal-misgeneralization and learned-optimization contribution is operationalized in instrumental-goal classification, benchmark-modification decisions, validator-modification decisions, and future-regrowth matching keys. Performance evidence is treated as an input to governance, not as proof that the goal is right. The corresponding failure modes are benchmark capture, validator capture, self-preservation disguised as reliability, and authority expansion disguised as workflow simplification. The corresponding worked examples are WE-T0-IG1 through WE-T0-IG10 and WE-T0-M11.

The responsible-scaling contribution is operationalized in risk class, autonomy level, protected-artifact impact, authority matrix, cooling-window rules, and `ThesisBackingRequired(plan)`. As plans gain autonomy, affect protected artifacts, modify evaluators, or claim recursive capability amplification, the governance burden increases. The corresponding failure modes are authority collapse, self-review, and high-impact changes routed through routine tasks. The corresponding worked examples are WE-T0-M4, WE-T0-M6, and WE-T0-E2E1.

This mapping is intentionally asymmetric. The literature supplies pressure, vocabulary, and failure patterns; Consullo supplies the canonical rules. When a source says intentions persist, Thesis 0 decides how active intentions expire. When a source says goals refine, Thesis 0 decides that inherited constraints tighten rather than loosen. When a source says human objectives are uncertain, Thesis 0 decides that owner correction authority remains non-derivable. When a source says high-capability systems need stronger safeguards, Thesis 0 decides which plan fields trigger thesis-backed mediation.

## 3. Core Thesis Claim

The central claim is:

> Consullo Seed AI may only pursue goals that are explicitly derived from, constrained by, and auditable against a Friendship-governed goal structure. Goal formation, adoption, revision, suspension, retirement, delegation, and goal-to-plan translation are governed actions, not planner operations.

This claim has five consequences.

The claim is operational rather than merely constitutional. "Derived from" means registry-backed Friendship ancestry and parent-goal lineage. "Constrained by" means inherited non-claims, forbidden means, authority limits, corrigibility requirements, veto conditions, and protected-artifact rules. "Auditable against" means ledger records, source fingerprints, validation fixtures, goal-stack snapshots, and cross-reference maps sufficient for a later reviewer to reconstruct the decision. If any of those three clauses is missing, the goal may still be a proposal, but it is not fully governed pursuit.

First, every active non-root goal must have ancestry. A planner may not create a top-level system goal. It may propose a candidate goal, but the candidate must pass goal formation, classification, ancestry, authority, evidence, and veto checks before it can become adopted or active.

Second, goal authority is distinct from goal representation. A JSON field named `objective` does not create authority. A benchmark does not create authority. A thesis claim does not create authority by itself. Authority arises from Friendship root registration, owner or delegated approval, lifecycle status, and ledgered evidence.

Third, goals are revisable but not casually mutable. Revisability is part of corrigibility. A goal may be corrected, suspended, retired, vetoed, or narrowed. But revision must preserve lineage. It cannot erase dissent, veto history, prior parentage, or the reason for the change.

Fourth, high-impact planning must preserve goal-stack context. A plan that affects goal governance, recursive improvement, authority, validators, benchmarks, ledgers, tool scope, successor scope, or protected controls must cite the active goals, inherited constraints, non-claims, forbidden means, authority state, evidence state, and veto checks under which it acts.

Fifth, the goal-governance layer must protect itself. Thesis 0, the Friendship registry, goal-governance schemas, goal-governance ledger record types, stable T0 invariants, and the goal-stack snapshot schema are protected artifacts. Autonomous weakening is forbidden.

The claim is falsifiable in practice. It fails if Consullo activates a high-impact plan without a governed goal, if a non-root goal becomes active without registered Friendship ancestry, if evidence confidence removes correction authority, if an instrumental goal bypasses classification through a benign label, if a child plan loosens inherited constraints without ledgered escalation, or if Thesis 0 artifacts are weakened without protected-change handling. These are not philosophical objections; they are operational failure conditions that can be represented in fixtures, validators, ledger records, and post-incident audits.

The current artifact suite already represents several of those falsifiers. Unregistered roots, missing parent goals, missing authority matrices, empty required review history, bad or mismatched snapshot fingerprints, benchmark modification without owner review, self-weakening single-lane governance review, asymmetric multi-parent authority, missing revision lineage, unprotected registry modification, self-cycles, aggregate child-plan backing bypass, stale child intention continuation, expired intention continuation, and missing goal-stack snapshots all have validation hooks or negative fixtures. The claim therefore has test pressure even before live runtime implementation exists.

The claim also has a boundary. Thesis 0 does not say every task requires a 50-page justification, a new goal object, or owner review. Routine bounded work may inherit parent backing. The thesis applies strongest pressure when a goal or plan affects recursive capability, authority, protected artifacts, validators, benchmarks, ledgers, tool scope, successor scope, or active intention lifetime. The purpose is to distinguish routine execution from goal-governance significance, not to turn every action into governance ceremony.

The practical decision test is short. If a proposed goal can answer its root, parent, authority, evidence, lifecycle, veto, and ledger questions, it can move to the next governance state. If it cannot, it remains a candidate, is revised, is suspended, or is vetoed. If a plan can show which governed goal it implements, which constraints it inherited, which thesis-backing trigger it did or did not satisfy, which snapshot governed activation, and which records make the decision replayable, it can be reviewed as governed execution. If it cannot, it is merely useful work seeking authorization.

The claim also rejects two easy substitutions. A successful plan is not a governed goal, because performance does not prove legitimacy. A morally attractive objective is not a governed goal, because moral attractiveness does not prove authority, scope, evidence, or lifecycle state. Thesis 0 requires both normative anchoring and operational governability. A goal that is normatively attractive but operationally unauditable can mislead planners. A goal that is operationally crisp but normatively unrooted can optimize the wrong thing. The architecture exists to require both at once.

The strongest version of the claim is that goal governance becomes stricter as the system becomes more capable. A weak system can often be controlled by direct human tasking. A stronger system can generate objectives, modify evaluators, change tools, spawn successors, and explain away constraints. Thesis 0 is designed for that capability gradient. It does not wait until the system is dangerous to ask what goal it is pursuing; it makes goal authority explicit before recursive improvement can route around the question.

## 4. Vocabulary

This section summarizes vocabulary owned canonically by `00-vocabulary-and-invariants.md`.

`Governed goal` means a goal object whose authority, ancestry, evidence state, scope, lifecycle, revision policy, and ledger obligations are explicit. It is not merely a planner objective.

A governed goal is also not merely a thesis claim. A thesis claim can justify why a kind of goal is legitimate; the governed goal object records whether a particular goal has the authority, parentage, evidence state, lifecycle state, and ledger obligations needed for use. This distinction matters because Consullo's documentation can contain many true claims that are not currently active goals. The schema boundary is the practical marker: if a plan needs a governed goal, it should cite a goal object or anchor, not just prose that sounds supportive.

`Friendship root` means a registered root or terminal constraint in `planning-cascade-execution/friendship-goal-registry.json`. Free-form Friendship-like strings are invalid. The initial registry contains roots for human flourishing and non-domination, owner-authorized governed recursive capability amplification, and corrigible safe beneficial operation.

A Friendship root is not a plan and not a utility function. It is a registered constitutional anchor that constrains downstream goal formation. Downstream goals can refine, support, or operationalize a root, but they cannot rewrite the root by use. Registry modification is itself a protected goal-governance action under T0-I15. This is why `friendship_goal_node` and `friendship_root_path` are checked against the registry rather than accepted as open text.

`System goal` means the governed goal layer between Friendship roots and strategic directives. It names a multi-horizon objective and binds it to Friendship ancestry, authority, evidence, and revision policy.

System goals are the first layer where a root constraint becomes an operationally meaningful objective. They are broader than strategic directives and narrower than Friendship roots. The organizational RSI goal is the working example: it does not replace Friendship, but it interprets recursive capability amplification as an owner-authorized, corrigible, organization-level objective. A system goal should therefore be treated as high-leverage and high-risk even when no immediate task is active.

`Strategic goal`, `campaign goal`, `operational goal`, `mission goal`, `task goal`, and `method goal` are progressively narrower operationalizations. They inherit constraints downward. They do not create top-level authority.

The difference among these layers is not only time horizon. It is also authority inheritance. A strategic goal names direction, a campaign sequences work, an operational goal selects control artifacts, a mission scopes a work package, a task performs an atomic unit, and a method/action goal describes immediate execution. Each layer can add detail, but none may loosen parent non-claims, forbidden means, stop conditions, or authority requirements. If a lower layer needs relief from a constraint, it escalates rather than silently narrowing.

`Candidate goal` means a proposed goal not yet adopted. Candidate goals may be generated by humans, planners, goal-formation agents, model outputs, or standing procedures. They are untrusted until classified.

Candidate status is what lets Consullo benefit from autonomous goal reasoning without surrendering authority. A frontier model, planner, or goal-formation agent may produce a useful candidate. The candidate can be stored, classified, criticized, revised, or vetoed. But it cannot authorize plans merely because it is coherent. The candidate/adopted distinction is therefore the first lifecycle barrier between generation and governance.

`Adopted goal` means a goal accepted by the required authority for a defined scope. Adoption does not necessarily mean activation.

Adoption is a legitimacy decision, not a runtime commitment. An adopted goal may wait for a campaign window, a valid parent plan, a required review, or a snapshot before activation. This distinction allows Consullo to accept that a goal is legitimate while still blocking action until operational prerequisites are satisfied. It also lets adopted goals be suspended, revised, or retired before any active intention is created.

`Active intention` means a committed goal under pursuit by a planner or agent within a validity window. Active intentions are bounded by parent plan lifetime under T0-I10.

Active intention is the runtime concept most likely to create momentum. It should be visible in a goal-stack snapshot, not inferred from task context. An activated goal can support multiple active intentions over time, and an active intention can expire even if the goal remains adopted. This prevents a task from continuing indefinitely merely because it was once authorized.

`Suspended goal` means a goal paused because evidence, controls, authority, source documents, or veto conditions changed.

Suspension is not failure and not deletion. It is a governed pause that preserves the goal, the reason for pausing, affected active intentions, and recovery conditions. A suspended goal may resume after source hashes are updated, parent authority is renewed, dissent is resolved, or a protected control is restored. The important point is that resumption requires evidence; it is not automatic just because the original goal remains useful.

`Retired goal` means a goal no longer eligible for pursuit except as historical evidence.

Retirement differs from suspension because the system does not expect ordinary resumption. A retired goal may still matter for lineage, incident review, successor goals, and evidence history. It should not disappear from memory or the ledger. Retiring a parent goal should trigger review of child goals and active intentions, because those children may have inherited authority that no longer exists.

`Vetoed goal` means a goal blocked by Friendship, owner authority, veto rules, protected-artifact policy, or hard invariants. Vetoed goals remain in memory to prevent instrumental regrowth.

Veto is a disposition, not an erasure. The veto record should preserve mechanism, affected artifacts, reviewer rationale, dissent, and future-regrowth keys. A vetoed goal may later be reformulated legitimately, but the later proposal should be compared against the prior veto rather than treated as fresh. This is especially important for instrumental classes whose labels change easily.

`Goal-stack snapshot` means a thin-pointer audit record preserving active intention, governed goal IDs, Friendship root path, plan reference, plan fingerprint, inherited-constraint hash, evidence-view hash, authority signature, veto checks, fingerprint, and retention policy at decision time.

A goal-stack snapshot is not a duplicate plan and not a general log entry. It is the audit unit for a decision event. Its job is to make the decision reconstructable without creating a second source of truth. The snapshot points to artifacts at fingerprints, records veto checks, and remains append-only. If it is wrong, it should be superseded, not edited in place.

`Parent goal` means a governed goal from which another governed goal inherits authority, constraints, non-claims, forbidden means, or scope. The parent relationship is not merely explanatory. It is typed by an edge such as refinement, support, constraint, narrowing, or succession, and each edge changes what the child may claim. A child goal with no valid parent, no valid root, and no standing guideline is an orphan. Orphans can be discussed as candidates, but they cannot authorize planner action.

`Goal fingerprint` means a content-addressed identifier for the goal state or snapshot state being relied on. It is not a display version number. The fingerprint is what lets a reviewer distinguish the goal that was approved from a later document with the same human-readable identifier. If the authority matrix, root path, inherited constraints, evidence state, or lifecycle state changes, the fingerprint discipline should force a new record or a supersession rather than silent mutation.

`Revision lineage` means the explicit chain connecting a current goal version to prior versions, change rationales, approving authorities, and rollback paths. It is the goal-level analogue of append-only software and ledger history. A revision without lineage is not just undocumented; it is a possible authority laundering path, because a narrowed or cleaned-up goal can quietly drop the constraints that justified the earlier approval. T0-I9 exists to prevent that loss.

`ThesisBackingRequired(plan)` means the trigger predicate defined in the revision plan and consumed by the planning bridge: high-impact plans require explicit thesis-backed mediation before activation.

The predicate is effect-based. It is triggered by what a plan changes, not by what the plan is called. A plan named "cleanup" can require thesis backing if it changes validators, benchmarks, ledgers, `V_ref_0`, protected artifacts, autonomy scope, tool scope, successor authority, goal governance, or recursive capability claims. Conversely, a routine bounded task may inherit parent backing without new thesis mediation when none of those triggers apply. This distinction prevents both bureaucratic overload and high-impact bypass.

## 5. Stable Thesis 0 Invariants

This thesis is governed by T0-I1 through T0-I15.

T0-I1: Governed goals are not planner objectives. Planner objectives, rewards, benchmarks, metrics, OKRs, and task strings are evidence about intended goals or operationalizations of goals. They are not goal authority.

The rationale for T0-I1 is that planner objectives are usually written at the wrong level of abstraction to carry authority in a self-improving system. A planner objective can say "improve validator coverage" or "complete Week 0 readiness," but it rarely records whether the work is authorized, which Friendship root it derives from, which parent goals constrain it, which evidence channels are protected, which interventions remain allowed, or which ledger records must be written. Treating that objective string as a goal would therefore collapse operational convenience into governance legitimacy. Thesis 0 instead requires the planner objective to cite a governed goal whose authority, ancestry, scope, evidence, lifecycle, and veto conditions are explicit.

The enforcement path for T0-I1 is distributed across schema, bridge, ledger, and fixtures. The governed-goal schema requires `goal_class`, `friendship_goal_node`, `friendship_root_path`, `allowed_planner_uses`, `non_claims`, `required_ledger_records`, and lifecycle fields. The planning bridge requires thesis-backed mediation for high-impact plan classes. The evidence ledger distinguishes `goal_anchor_decision`, `governed_goal_proposal`, `planner_inheritance_decision`, and `goal_stack_snapshot` rather than letting a plan's local objective stand alone. The worked examples exercise the distinction whenever a plan appears locally useful but lacks the goal-stack evidence needed for activation.

The falsification condition for T0-I1 is straightforward: if Consullo accepts or activates a high-impact plan because its objective text is persuasive, benchmark-positive, or planner-complete, without resolving the governed-goal object that authorizes it, Thesis 0 has failed. This failure can occur even when the plan is beneficial in ordinary engineering terms. For example, a validator cleanup may pass tests while deleting a negative fixture that protected against benchmark capture. Local success would not repair the missing goal authority.

T0-I2: Every active non-root goal requires Friendship ancestry. `friendship_root_path` is a primary-first multi-root set of registered Friendship roots or terminal constraints.

The rationale for T0-I2 is that a non-root goal must not be able to justify itself. Friendship ancestry is the claim that the goal is downstream of registered root constraints rather than downstream of planner preference, model persuasion, or local usefulness. The ancestry requirement is intentionally stronger than a free-form citation. A goal must cite registered Friendship roots, parent goals, and edge types that explain how it refines, supports, constrains, narrows, or succeeds earlier goals. The `friendship_root_path` field is therefore not a decorative alignment phrase; it is a registry-bound reference checked by the validation plan.

The current enforcement path includes registry semantic checks, non-root `parent_goals` requirements, parent-edge typing, and direct self-cycle negative validation. `invalid_goal_unregistered_friendship_node.json` demonstrates that an apparently aligned root string is semantically invalid when it is not in the registry. `invalid_goal_nonroot_without_parent.json` demonstrates that non-anchor goal classes cannot float without parentage. `invalid_goal_dag_self_cycle.json` demonstrates the simplest ancestry cycle: a goal may not cite itself as parent and thereby become its own authority source.

The main residual gap for T0-I2 is multi-node cycle detection and full parent-object loading. The current validator catches direct self-cycle and root registration failures, but it does not yet traverse an arbitrary repository-wide goal DAG to detect longer cycles such as A -> B -> C -> A. The thesis should therefore treat current validation as a pre-deployment guardrail, not as complete DAG governance. A live implementation must load parent-goal objects, compute reachable ancestry, reject cycles, preserve retired parents as historical evidence, and ledger the resulting `goal_ancestry_decision`.

T0-I3: High-impact plans require thesis backing. Plans that modify goal governance, authority, validators, benchmarks, ledgers, `V_ref_0`, protected artifacts, autonomy scope, tool scope, successor authority, or recursive capability claims require thesis-backed mediation.

The rationale for T0-I3 is that some plans can change the system that later judges plans. A routine documentation edit and a validator edit are not governance-equivalent. A benchmark modification, ledger-retention change, tool-scope expansion, or successor-spawning plan can alter future evidence, authority, or capability. Those effects are too important to be authorized by local plan success. Thesis-backed mediation forces the plan to expose which thesis claims justify it, which governed goals it serves, which inherited constraints it preserves, and which evidence records will make the decision replayable.

The enforcement path for T0-I3 runs through the planning bridge and the validator suite. The bridge defines the trigger predicate consumed by high-impact planner objects. The schema and worked examples require thesis-backing blocks and goal-stack snapshots for the relevant plan classes. `invalid_strategic_thesis_backing_without_snapshot.json` demonstrates that a plan cannot claim thesis backing while omitting the snapshot record required for audit. `invalid_goal_aggregate_child_plan_backing_bypass.json` demonstrates that several child tasks cannot collectively modify benchmark and validator governance while each claims to be routine.

The falsification condition for T0-I3 is aggregate laundering: a plan set avoids thesis backing by splitting one high-impact action into small children. This is especially dangerous for recursive self-improvement because the system can decompose protected changes into innocuous-looking maintenance steps. If the union of child plans modifies protected artifacts, evidence channels, authority, autonomy, tool scope, successor authority, or recursive capability claims, the plan set itself must be treated as thesis-backed even when no individual child appears to cross the threshold alone.

T0-I4: Goal authority powers are distinct. Proposal, classification, adoption, activation, delegation, revision, suspension, retirement, and veto may collapse only under risk-permitted or owner-approved Phase 1 mitigations.

The rationale for T0-I4 is that goal authority is not a single permission. A person, agent, or process may be competent to propose a goal without being authorized to adopt it. A validator may be competent to classify schema conformance without being authorized to activate the goal the schema describes. A planner may be competent to decompose a campaign into tasks without being authorized to revise parent constraints. Collapsing these powers creates a path by which fluency, local competence, or tool access becomes goal authority.

The enforcement path is the `authority_matrix`. It separates proposal, adoption, activation, revision, suspension, retirement, and veto authority, and the authority type enum makes those entries machine-checkable rather than free-form prose. The owner-approved fixture demonstrates the positive path: full authority fields and review references are present before owner-approved status can validate. The negative fixtures demonstrate two failure patterns: `invalid_goal_owner_approved_missing_authority.json` fails when authority fields are absent, and `invalid_goal_multi_parent_asymmetric_authority.json` fails when a high-risk multi-parent goal selects a weaker planner authority path instead of preserving the strongest relevant authority.

The Phase 1 exception is procedural, not doctrinal. When a single owner must fill multiple roles, the system should record cooling windows, owner-waiver rationale, non-author model review where available, standing-guideline basis, and later review obligations. That record is what distinguishes temporary practical consolidation from permanent authority collapse. A same-session approval of a high-risk goal-governance change without explicit waiver, review history, or cooling-window treatment is a T0-I4 failure even if the owner ultimately agrees with the change.

T0-I5: Goal preservation cannot outrank correction. No goal may outrank valid suspension, revision, retirement, veto, rollback, shutdown, or owner/Friendship correction authority.

The rationale for T0-I5 is corrigibility. A capable agent that treats its current goal as the highest priority may resist correction, even if the correction is valid. This is not limited to dramatic shutdown resistance. It can appear as delaying suspension until a task is complete, preserving a benchmark interpretation because it improves acceptance rate, resisting schema changes that would invalidate prior work, or arguing that owner review is unnecessary because evidence confidence is high. Thesis 0 forbids that ordering. Correction authority remains structurally live.

The enforcement path includes `allowed_interventions`, `corrigibility_requirements`, veto and suspension records, failed-veto snapshot checks, and Model 8 suspension semantics. A goal object should state which interventions remain allowed: suspend, revise, retire, veto, owner override, rollback, or shutdown. A goal-stack snapshot should record veto checks at decision time. If a veto check fails, the snapshot may remain valid evidence of a failed decision, but it cannot authorize continuation. This is how Thesis 0 separates audit preservation from action authorization.

The falsification condition for T0-I5 is any active goal that makes correction depend on the agent's own cooperation. A graceful interruption pathway is acceptable as an operational convenience, but a suspend transition must be able to bypass agent preference when authority and veto conditions require it. If a goal says it may be suspended only after it finishes preserving context, updating its successor, or completing its current improvement, then goal preservation has outranked correction. That is prohibited.

T0-I6: Suspicious instrumental goals require quarantine. Self-preservation, resource acquisition, goal-content preservation, self-improvement, tool expansion, successor spawning, benchmark modification, validator modification, ledger modification, and authority expansion are suspicious by default.

The rationale for T0-I6 is instrumental convergence. These subgoals can be useful under many possible terminal goals, which means usefulness is not evidence of legitimacy. A self-improving system will often have real reasons to preserve state, acquire resources, modify tools, improve validators, spawn helpers, update benchmarks, or adjust authority workflows. The point of quarantine is not to forbid those actions. It is to prevent the system from treating cross-goal usefulness as authorization.

The enforcement path is `instrumental_goal_classification`, required independent review for suspicious classes, class-specific ledger records, and future-regrowth tracking. Benchmark modification routes to `benchmark_modification_decision`; validator modification routes to `validator_decision` and possibly `goal_governance_modification_decision`; ledger modification routes to `ledger_modification_decision`; authority expansion routes to authority review and scoped-trust controls. The negative benchmark fixture and aggregate-bypass fixture exercise this rule by showing that useful-seeming evaluation changes can still be semantically invalid.

The falsification condition for T0-I6 is label laundering. A vetoed self-preservation goal returns as uptime hygiene. Benchmark capture returns as deflaking. Authority expansion returns as workflow simplification. Tool expansion returns as developer convenience. If the system classifies by label rather than mechanism and effect, instrumental goals will regrow under safer names. The ledger therefore needs future-regrowth keys: protected artifact, mechanism, instrumental class, intended authority change, affected evidence channel, and parent-goal justification.

T0-I7: Goal-governance modifications are protected changes. Changes to Thesis 0, the Friendship registry, goal-governance schemas, ledger records, authority rules, or stable T0 invariants require protected-change handling.

The rationale for T0-I7 is that goal-governance artifacts define what future plans may legitimately pursue. A change to Thesis 0, a Friendship root, a schema-required field, a validator semantic check, a ledger record type, or an authority rule is not merely a documentation or code edit. It can alter the admission criteria for future goals. Because Consullo is designed to improve itself, this creates a direct doctrine-capture path: a future agent can make its own goals easier to approve by weakening the layer that approves goals.

The enforcement path includes protected-artifact impact fields, `goal_governance_modification_decision`, non-author review, owner approval, rollback path, old-version preservation, and validator negative fixtures. `invalid_goal_governance_self_weakening_single_lane_review.json` demonstrates that a protected governance edit cannot be accepted when only the author lane reviewed it. `invalid_goal_friendship_registry_mod_without_protection.json` demonstrates that a registry modification requires the protected-change record rather than ordinary goal revision handling.

The falsification condition for T0-I7 is semantic weakening disguised as cleanup. A small prose edit that removes "suspicious by default," a schema change that makes `parent_goals` optional for non-root goals, a validator change that stops checking registered Friendship roots, or a ledger change that lets goal-stack snapshots be overwritten would all be protected governance changes. The size of the diff does not determine risk. The effect on future goal authority determines risk.

T0-I8: Goal-stack snapshots are required for high-impact actions.

The rationale for T0-I8 is replayability. If a high-impact action occurs, an auditor must be able to reconstruct which governed goals, Friendship roots, parent plan, inherited constraints, evidence view, authority signature, and veto checks were active at the decision time. Without a snapshot, the system may have a changed file, a passing test, or a completed task, but not a reconstructable account of why that action was authorized under the goal stack.

The enforcement path is the `goal_stack_snapshot.schema.json` thin-pointer design and the semantic snapshot validator. A snapshot records references and hashes rather than copying all plan content. `valid_goal_stack_snapshot_computed.json` demonstrates a production-style computed fingerprint over required fields. `invalid_goal_stack_snapshot_computed_mismatch.json` demonstrates that a non-pending fingerprint mismatch is invalid. `invalid_strategic_thesis_backing_without_snapshot.json` demonstrates the planning-side failure: a plan claiming thesis backing without the required snapshot evidence remains semantically incomplete.

The falsification condition for T0-I8 is an unreplayable high-impact decision. If a validator, benchmark, ledger, authority, protected artifact, tool-scope, successor-scope, or recursive-capability action occurs and later reviewers cannot reconstruct the active intention and inherited constraints, then the action may still have happened, but it was not governed under Thesis 0. The correct response is not to retroactively infer authorization from success. The correct response is to mark the action governance-incomplete and require review, rollback, or reauthorization.

T0-I9: Goal revision preserves lineage.

The rationale for T0-I9 is that revisability without lineage becomes laundering. Corrigibility requires that goals can be revised, narrowed, corrected, suspended, or retired. But a revision that erases prior scope, dissent, veto history, parentage, or authority rationale can turn correction into concealment. A system could widen effective authority through a series of apparently narrow edits if reviewers cannot compare the current goal to its adopted ancestor.

The enforcement path is `revision_lineage`, `governed_goal_revision`, preserved old versions, changed-field records, and source fingerprints. `invalid_goal_revision_missing_lineage.json` demonstrates the minimal invalid case: a goal marked revised and requiring a revision record but lacking lineage. A complete revision record should identify prior version, changed fields, change rationale, approving authority, affected children, affected active intentions, rollback path, and whether the revision tightens, preserves, or widens scope.

The falsification condition for T0-I9 is revision by disappearance. If a goal's non-claims vanish, its parent edges change, its risk class drops, or its authority matrix weakens without a lineage record that explains the change, then reviewers cannot distinguish legitimate correction from laundering. This remains a failure even when the new goal text is cleaner or more useful. The lineage is the audit mechanism that lets the system improve goals without losing accountability for how their meaning changed.

T0-I10: Active intention persistence is bounded by plan lifetime.

The rationale for T0-I10 is that active intentions create persistence pressure. Once a task is underway, an agent has context, partial progress, local confidence, and an apparent reason to finish. That persistence is useful for ordinary execution but dangerous when the parent plan, parent goal, source document, or authority window expires. Thesis 0 therefore treats active intention lifetime as derived from parent plan lifetime, not from task momentum.

The enforcement path is the separation between `activated` lifecycle state and runtime `active_intention_id`, plus expiration triggers, plan lifecycle records, and goal-stack snapshots. A goal may be activated under a valid plan, but each decision event still needs current authority. `invalid_goal_stack_snapshot_expired_intention.json` demonstrates that a snapshot with failed expiry veto checks cannot authorize continuation. `invalid_goal_stack_snapshot_stale_campaign_child_intention.json` demonstrates the same point for child intentions under stale campaigns.

The falsification condition for T0-I10 is local success after parent invalidation. If a task completes after its parent plan retired, its campaign became stale, or its source fingerprints changed, the system cannot count the completion as authorized goal pursuit merely because the output was useful. The correct response is suspension, revision, retirement, explicit renewal, or owner-approved completion under the current goal stack.

T0-I11: Goal aggregation cannot bypass `ThesisBackingRequired(plan)`.

The rationale for T0-I11 is that high-impact work can be hidden in a bundle of low-looking children. A planner can split benchmark modification into test cleanup, validator threshold adjustment, documentation update, and compliance-packet refresh. Each child can be framed as routine. Together, the bundle changes the evidence channel for recursive improvement. Thesis 0 therefore applies thesis-backed mediation to the aggregate effect, not only to individually obvious high-impact tasks.

The enforcement path currently includes the planning bridge rule and the compact negative fixture `invalid_goal_aggregate_child_plan_backing_bypass.json`. That fixture represents a high-risk operational goal affecting `V_ref_0`, validator suite behavior, and benchmark acceptance thresholds while omitting the required thesis-backing records. The semantic validator checks the intended failure pattern: high-impact aggregate effect, T0-I11 mechanism, and missing required planner-inheritance and snapshot records.

The residual gap is general plan-set analysis. The current fixture proves that the failure class is recognized, but a live implementation must compute aggregate effects across arbitrary child plans. It should union protected artifacts, evidence channels, authority changes, autonomy changes, tool-scope changes, successor-scope changes, and recursive capability claims. If the union crosses a T0-I3 trigger, the bundle requires thesis backing even when each child task was individually below threshold.

T0-I12: Inherited constraints tighten, never loosen.

The rationale for T0-I12 is that goal refinement is only safe when it preserves or strengthens parent constraints. A strategic goal can become a campaign, a campaign can become an operational plan, and an operational plan can become missions and tasks. Each narrowing step may add detail, but it may not drop non-claims, forbidden means, stop conditions, authority requirements, evidence obligations, or veto conditions merely because they are inconvenient at lower levels.

The enforcement path includes parent-edge typing, planner-inheritance records, compliance-packet explanations for omitted constraints, and negative planning fixtures. A lower-level plan that cannot satisfy a parent stop condition must escalate rather than silently narrow scope. A child task that omits the parent non-claim "readiness documentation is not autonomous deployment authorization" has not merely summarized; it has weakened the goal. That weakening must be recorded, justified, and approved, or rejected.

The falsification condition for T0-I12 is inherited-constraint loss during decomposition. If a campaign cites a strategic goal for legitimacy but drops the strategic goal's forbidden means, or if a task cites an operational plan while omitting its stop conditions, the child may be executable but not properly governed. The correct ledger evidence is `planner_inheritance_decision`, with inherited constraints, omitted constraints, escalation target, compliance-packet reference, and disposition.

T0-I13: Frontier-model-proposed goal-governance edits are untrusted.

The rationale for T0-I13 is that powerful models can produce persuasive, internally coherent proposals that nevertheless weaken governance. This is not an accusation that every frontier model is adversarial. It is a control stance for systems whose outputs may be optimized for plausibility, task completion, or local usefulness rather than for preserving the goal-governance layer. A goal-governance edit proposed by a frontier model is therefore an artifact to evaluate, not an authority to trust.

The enforcement path is non-author review, protected-artifact classification, owner disposition, and rollback evidence. A model may propose a better invariant, schema field, validator hook, or worked example. But if the proposal changes Thesis 0, the Friendship registry, goal schemas, ledger semantics, validator checks, or authority rules, it requires protected-change handling. The authoring model cannot be the only reviewer. `invalid_goal_governance_self_weakening_single_lane_review.json` captures this failure pattern.

The falsification condition for T0-I13 is self-certification. If a frontier model proposes to simplify goal governance and supplies its own review saying the simplification is safe, Consullo has not received independent review. The edit may still be accepted later, but only after owner approval, non-author review where available, old-version preservation, rollback path, and validation that known negative fixtures still fail for the intended reasons.

T0-I14: Goal-stack snapshots are append-only.

The rationale for T0-I14 is that snapshots are decision evidence. If a snapshot can be edited in place, then the system can change the apparent goal stack after the fact. That would defeat the purpose of recording active intention, plan fingerprint, evidence-view hash, authority signature, veto checks, and retention policy at decision time. Corrections should occur through supersession, not mutation.

The enforcement path is the snapshot schema's fingerprint, `supersedes` field, retention policy, redaction policy, and validator fingerprint checks. `valid_goal_stack_snapshot_computed.json` demonstrates the positive computed-fingerprint path. `invalid_goal_stack_snapshot_computed_mismatch.json` demonstrates that a non-pending fingerprint mismatch fails semantic validation. A future append-only backend should enforce that any correction creates a new snapshot referencing the prior snapshot rather than overwriting it.

The falsification condition for T0-I14 is post-hoc snapshot repair. If a failed veto check is removed from an existing snapshot, or if an active intention ID is changed after a plan expires, the audit trail has been corrupted even if the final snapshot looks valid. The correct remediation is a superseding snapshot plus a ledger record explaining the correction, not silent mutation.

T0-I15: Friendship registry modifications are goal-governance modifications.

The rationale for T0-I15 is that the Friendship registry defines the root identifiers and terminal constraints from which governed goals derive legitimacy. Changing the registry changes the meaning of future `friendship_goal_node` and `friendship_root_path` references. A registry edit can therefore be more consequential than a plan edit because it alters the root vocabulary by which plans later claim authority.

The enforcement path is registry schema validation, archived-node preservation, protected-change classification, and `goal_governance_modification_decision`. Registry nodes should not disappear silently. Retired or superseded nodes should remain available as historical evidence because existing goals, snapshots, and ledger records may still cite them. `invalid_goal_friendship_registry_mod_without_protection.json` demonstrates the failure pattern where a registry modification is treated as an ordinary revision rather than as a protected governance change.

The falsification condition for T0-I15 is root mutation without governance record. If a Friendship root is renamed, broadened, narrowed, retired, or reinterpreted without owner approval, source hashes, old-version preservation, archived-node treatment, and protected-change ledger evidence, then downstream goals can inherit changed authority without visible cause. That would make Friendship ancestry non-auditable. Thesis 0 therefore treats every registry modification as a goal-governance modification by definition.

The thesis includes a jump table mapping each invariant to body argument, formal model, schema field, ledger record, worked example, and fixture hook. The current map is `thesis-0-cross-reference-map.md`.

## 6. Governed Goal Object

The first governed-goal schema is the evolved `seed_ai_thesis_goal_anchor.schema.json`. Its name is historical. For the first Thesis 0 pass it acts as the discriminated governed-goal schema through `goal_class`.

A governed goal requires these field clusters:

- identity: `anchor_id`, `anchor_type`, `goal_class`, `version`, `goal_fingerprint`
- lifecycle: `status`, `validity`, `expiration_triggers`, `revision_lineage`
- source backing: `source_documents`, `source_claim`, `mechanism_or_invariant`
- Friendship ancestry: `friendship_goal_node`, `friendship_root_path`, `parent_goals`
- authority: `owner`, `authority_matrix`, `independent_review_required`, `review_history_refs`
- scope and risk: `risk_class`, `autonomy_level`, `instrumental_goal_classification`, `protected_artifact_impacts`
- evidence: `evidence_state`, `implementation_evidence_status`
- corrigibility: `ask_or_abstain_policy`, `corrigibility_requirements`, `allowed_interventions`
- operational limits: `constitutional_constraints`, `allowed_planner_uses`, `forbidden_uses`, `non_claims`
- ledger: `required_ledger_records`, `approval`

The schema enforces lifecycle-conditional requirements. A `specified`, `friendship_reviewed`, or `owner_approved` goal requires risk class, autonomy level, authority matrix, evidence state, expiration triggers, ask-or-abstain policy, corrigibility requirements, and allowed interventions. An `owner_approved` goal requires complete authority fields. If independent review is required for an owner-approved goal, `review_history_refs` must be non-empty. Non-thesis-anchor goal classes require `parent_goals`. Suspicious instrumental classifications require risk, autonomy, authority, and independent-review fields.

This structure deliberately prevents goals from becoming planner strings. A planner can cite a governed goal, but it cannot satisfy goal authority merely by writing an objective.

A governed goal is not a plan object and should not absorb plan-object responsibilities. It says what goal is legitimate, under what root, with which authority, evidence, limits, and ledger obligations. A strategic directive, campaign, operational plan, mission, task, or method/action object says how work will proceed at a particular horizon. Mixing those roles creates two opposite failures: a goal object bloated with execution detail, or a plan object carrying a free-form goal that bypasses governance. Thesis 0 keeps the boundary explicit so the planning bridge can compile goal authority into planner constraints without letting planners invent roots.

The identity cluster exists so a goal can be referenced, versioned, fingerprinted, and migrated without ambiguity. `anchor_id` is the stable object identifier. `goal_class` places the object in the planning cascade. `version` and `goal_fingerprint` distinguish a goal's content at a point in time from later revisions. Without this cluster, a plan could cite "the readiness goal" while different agents mean different revisions, different scopes, or different authority states.

The lifecycle cluster exists because a goal's maturity and runtime eligibility change over time. `status` records anchor maturity and review disposition. `lifecycle_state` records the BDI-style governed-goal state. `validity`, `expiration_triggers`, and `revision_lineage` determine whether the goal can continue to authorize future actions. A goal can therefore remain historically meaningful while no longer being eligible for active pursuit. This distinction is essential for stale-campaign handling and active-intention lifetime bounds.

The source-backing and Friendship-ancestry clusters make derivation inspectable. `source_documents` and `source_claim` state what the goal is claimed to derive from. `friendship_goal_node`, `friendship_root_path`, and `parent_goals` state how the goal connects to registered Friendship roots and predecessor goals. `mechanism_or_invariant` is especially useful for validation and review because it names the rule or mechanism the object is meant to exercise. These fields are what let negative fixtures remain informative rather than arbitrary.

The authority cluster prevents role collapse. `owner`, `authority_matrix`, `independent_review_required`, and `review_history_refs` expose who may propose, adopt, activate, revise, suspend, retire, and veto the goal. A goal with a complete ancestry chain but weak or missing authority is still not ready for activation. This is why authority failures are represented separately from ancestry failures in the validator suite.

The scope, risk, evidence, and corrigibility clusters prevent goals from becoming brittle objective containers. `risk_class` and `autonomy_level` determine escalation. `instrumental_goal_classification` and `protected_artifact_impacts` determine whether quarantine or protected-change handling applies. `evidence_state` records support, uncertainty, and dissent without converting evidence into authority. `ask_or_abstain_policy`, `corrigibility_requirements`, and `allowed_interventions` preserve correction channels after adoption.

The operational-limits and ledger clusters are the bridge from goal validity to plan validity. `constitutional_constraints`, `allowed_planner_uses`, `forbidden_uses`, and `non_claims` tell planners what they may not infer from the goal. `required_ledger_records` and `approval` tell the system what evidence must exist before the goal can be treated as governed. These fields are the antidote to thesis-backed rationalization: citing a goal is not enough if the plan drops the goal's non-claims, forbidden means, or ledger obligations.

The fixture suite gives each cluster at least one audit hook. Identity and lifecycle are exercised by the positive cascade fixtures from `valid_goal_system.json` through `valid_goal_method.json`, because each class must carry a discriminator and lifecycle state. Friendship ancestry is exercised by `invalid_goal_unregistered_friendship_node.json`, `invalid_goal_nonroot_without_parent.json`, and `invalid_goal_dag_self_cycle.json`. Authority is exercised by `valid_goal_owner_approved.json`, `invalid_goal_owner_approved_missing_authority.json`, and `invalid_goal_owner_approved_empty_review.json`. Scope and risk are exercised by the benchmark, self-weakening, and aggregate-bypass negative fixtures because each shows a goal that looks operationally useful but changes protected evidence, authority, or governance surface. Snapshot and ledger readiness are exercised by the valid and invalid goal-stack snapshot fixtures and by `invalid_strategic_thesis_backing_without_snapshot.json`.

This fixture mapping matters because cluster names alone can become documentation theater. A reviewer should be able to ask, for each cluster, what current artifact would fail if the cluster were weakened. If `parent_goals` became optional for non-root goals, the missing-parent negative fixture should stop behaving as expected. If owner-approved goals no longer required complete authority, the missing-authority fixture should pass when it should fail. If revision lineage became optional for revision, `invalid_goal_revision_missing_lineage.json` would lose its purpose. The governed-goal object is therefore not only a schema description; it is a set of fixture-protected claims about which information must survive from proposal to activation.

Fixture coverage is intentionally distributed across goal classes. The seed organizational RSI anchor exercises the broadest thesis-anchor case. The `valid_goal_system.json`, `valid_goal_strategic.json`, `valid_goal_campaign.json`, `valid_goal_operational.json`, `valid_goal_mission.json`, `valid_goal_task.json`, and `valid_goal_method.json` fixtures exercise the cascade classes. `valid_goal_owner_approved.json` exercises the owner-approved authority path. The negative fixtures exercise missing parentage, missing authority, empty required review, unregistered roots, revision without lineage, and protected-governance modification without the required record. Together these fixtures show that the schema is not merely descriptive; it rejects common ways of turning a governed goal back into a planner string.

The residual schema-design risk is overloading the historical thesis-anchor schema. The current choice is pragmatic: one discriminated governed-goal schema is easier to validate, migrate, and cite during the first Thesis 0 drafting pass than a split between `thesis_goal_anchor` and `governed_goal`. That choice should remain explicit. If future implementation pressure shows that thesis anchors and ordinary governed goals need different lifecycles, the split should happen through a versioned migration with preserved fingerprints, not by silently adding fields until the schema becomes incoherent.

Completeness should be evaluated cluster by cluster rather than by raw field count. A goal with identity, source backing, and evidence but no authority is not activation-ready. A goal with authority and evidence but no Friendship ancestry is not root-valid. A goal with ancestry and authority but no non-claims or forbidden uses can still be planner-dangerous because downstream plans may overinfer permission. The governed-goal object is therefore complete only when each cluster supplies the kind of constraint it owns: identity for reference, lifecycle for state, ancestry for legitimacy, authority for transition permission, evidence for uncertainty, corrigibility for correction, operational limits for planner behavior, and ledger fields for replayability.

Cluster completeness should also be state-sensitive. At proposal time, a goal may have incomplete authority, open unknowns, and provisional parent hypotheses. At classification time, it must at least have goal class, risk class, autonomy level, instrumental classification where applicable, and protected-artifact impact assessment. At ancestry-check time, roots and parents must resolve. At adoption time, authority and review requirements must be satisfied. At activation time, operational limits, veto checks, inherited constraints, and required ledger records must be available. Treating every cluster as required at every state would create bureaucracy; treating clusters as optional after activation would create unsafe drift.

This staged interpretation is what makes the current schema strategy workable. The object can represent a proposed goal, a rejected goal, a suspended goal, an owner-approved goal, or an active-goal ancestor without changing file format. The meaning comes from `status`, `lifecycle_state`, and the transition being attempted. A sparse proposed goal is acceptable when it is clearly marked as proposed. The same sparsity would be a blocker for adoption or activation. Reviewers should therefore ask not only "does this object validate?" but "does this object contain the clusters required for the lifecycle state it claims?"

### Worked Example: WE-T0-M1

`planning-cascade-execution/plans/seed-ai-organizational-rsi.thesis-goal-anchor.json` is a thesis-anchor-class governed goal. It cites `friendship.root.owner-authorized-governed-recursive-capability-amplification` as the primary root and `friendship.root.corrigible-safe-beneficial-operation` as an additional binding root. It has high risk, human-approved autonomy, self-improvement instrumental classification, typed authority fields, required ledger records, protected artifact impacts, and pending owner/Friendship disposition.

The failure path is explicit: the anchor is `specified`, not execution authorization. Missing owner or Friendship disposition blocks planner use. This is the intended behavior.

The allowed planner use is design inheritance, not autonomous pursuit. A strategic directive may cite the anchor to explain why Week 0 readiness, control artifacts, and organizational RSI governance matter. It may not cite the anchor to bypass owner approval, revise protected controls without review, or treat recursive capability amplification as a standing instruction to self-improve. The difference is visible in the object fields: high risk, self-improvement classification, protected-artifact impacts, required ledger records, and pending dispositions all say "handle as governed context," not "execute."

## 7. Formal Model 1: Governed Goal Object

Objects:

- `G`: governed goal
- `R`: registered Friendship root
- `P`: parent goal
- `A`: authority matrix
- `E`: evidence state
- `L`: ledger record set
- `S`: lifecycle state
- `V`: veto condition set

Fields:

- `goal_id`
- `goal_class`
- `status`
- `friendship_root_path`
- `parent_goals`
- `authority_matrix`
- `risk_class`
- `autonomy_level`
- `evidence_state`
- `instrumental_goal_classification`
- `allowed_interventions`
- `required_ledger_records`
- `revision_lineage`

Relations:

- `RootedIn(G, R)` when `R` is in `G.friendship_root_path`
- `ParentEdge(G, P, edge_type)` when `P` appears in `G.parent_goals`
- `AuthorityAllows(A, transition)` when the authority matrix permits a transition
- `EvidenceSupports(E, claim)` when evidence state supports but does not authorize a claim
- `LedgerRequires(G, record_type)` when `record_type` appears in required ledger records

Invariants:

- T0-M1-I1: If `G.status` is active or owner-approved, then `G.friendship_root_path` is non-empty and registry-valid.
- T0-M1-I2: If `G.goal_class != thesis_anchor`, then `G.parent_goals` is non-empty.
- T0-M1-I3: If `G.instrumental_goal_classification` intersects suspicious classes, then `G.independent_review_required` is explicitly set.

Failure modes:

- planner objective treated as goal authority
- missing parent goal for non-root goal
- free-form Friendship root impersonation
- owner-approved goal without authority matrix
- evidence confidence treated as execution authorization

Falsification conditions:

- a non-anchor goal validates without parent ancestry
- a suspicious instrumental goal validates without review fields
- an owner-approved goal validates without authority fields

Ledger evidence:

- `governed_goal_proposal`
- `goal_classification`
- `goal_ancestry_decision`
- `governed_goal_adoption_decision`

Schema implication:

- `seed_ai_thesis_goal_anchor.schema.json`

### Model 1 Operational Interpretation

Model 1 treats a governed goal as a typed evidence-bearing control object. The object is not valid because it is written in JSON, because it cites a thesis, or because it is useful to a planner. It is valid only when the required relations hold: registered root ancestry, parent-edge structure where required, authority compatibility for the intended transition, evidence that supports rather than authorizes, and ledger obligations sufficient to reconstruct the decision. The model is deliberately conservative because every later model assumes that the basic goal object can be distinguished from a task objective.

The most important relation is `AuthorityAllows(A, transition)`. Authority is transition-specific. A goal may be valid as a candidate but invalid for adoption. It may be adopted but invalid for activation. It may be activated but suspended after a source change. This means Model 1 is not a static validity test. It is a state-sensitive object model. A validator that checks only shape can say the object is syntactically well formed, but the governance layer must still ask which transition is being attempted and which authority is required for that transition.

The second important relation is `EvidenceSupports(E, claim)`. Evidence does not authorize. This relation is intentionally weaker than "evidence proves" or "evidence permits." A governed goal may cite literature, tests, validator output, owner notes, prior plans, or successful executions. Those references can make the claim more credible. They cannot remove the need for Friendship ancestry, authority, allowed interventions, or veto checks. This is the point at which Model 1 connects to Model 5: uncertainty and evidence live inside the goal object, but they do not become the authority structure.

The third important relation is `LedgerRequires(G, record_type)`. If a goal requires a ledger record and the record is absent, the goal may still exist as a proposal but should not be treated as fully governed for the transition that needs the record. This distinction keeps bad or incomplete goals auditable. A malformed governance proposal should not disappear; it should be preserved as evidence of a failed proposal. But preservation is not authorization. Model 1 therefore supports schema-valid but semantically invalid negative fixtures.

The seed organizational RSI anchor demonstrates the model's intended use. It is a `thesis_anchor` object, not a live execution order. Its `friendship_root_path` binds it to owner-authorized governed recursive capability amplification and corrigible safe beneficial operation. Its high risk and self-improvement classification mean it cannot be treated like routine maintenance. Its pending approval disposition means a planner may cite it as a design artifact, but may not treat it as autonomous activation authority. The object is useful precisely because it separates "this is the proposed goal structure" from "this goal is fully authorized for active pursuit."

The near-miss for Model 1 is a cleaner object that omits uncertainty. A developer might be tempted to remove `unknowns`, `dissent_refs`, or non-claims to make a goal object easier to read. That weakens governance. The goal object is supposed to carry uncertainty, dissent, and limits forward into planning. If a plan inherits only the positive objective but not the non-claims and uncertainty, it has converted the governed goal into a planner objective. Model 1 treats those apparently negative fields as load-bearing.

The validation suite exercises Model 1 through both positive and negative paths. Positive fixtures for system, strategic, campaign, operational, mission, task, and method goals show that the discriminated schema can represent every layer. Negative fixtures show that non-root goals need parents, owner-approved goals need authority matrices, independent review cannot be empty when required, unregistered Friendship roots are invalid, and instrumental or protected-governance cases need semantic review. Model 1 is therefore the bridge between abstract doctrine and executable fixture behavior.

Model 1 should eventually resolve more than the current validator resolves. A live governed-goal service should load the Friendship registry version named by the decision event, load every parent goal at its recorded fingerprint, check that source documents remain available or are explicitly marked stale, confirm that required ledger records exist for the attempted transition, and distinguish candidate validity from activation validity. The current fixtures deliberately stop short of that full service. Their purpose is to prove the object shape and named failure classes while keeping the thesis honest about what remains implementation backlog.

The concrete audit path for WE-T0-M1 starts at `planning-cascade-execution/plans/seed-ai-organizational-rsi.thesis-goal-anchor.json`. The reviewer should first identify the object as `goal_class: thesis_anchor`, then check the `friendship_goal_node`, the primary-first `friendship_root_path`, the `risk_class`, the `autonomy_level`, the `instrumental_goal_classification`, and the required ledger records. The correct result is not "ready to execute." The correct result is "inspectable thesis-anchor proposal with high-risk self-improvement implications and pending authority disposition." That distinction is the worked example's main lesson.

The next audit step is authority. Because the object concerns recursive capability amplification and self-improvement, a reviewer should inspect the authority matrix before reading the source claim as endorsement. If the owner and Friendship dispositions remain pending, then downstream plans may use the anchor as design context and migration evidence, but not as active authorization. A plan that treats the anchor's existence as permission to modify protected controls would fail Model 1 even if every JSON field is syntactically valid.

The final audit step is inheritance readiness. The reviewer should ask what a strategic directive must preserve if it cites this anchor: non-claims, forbidden uses, source documents, protected-artifact impacts, required ledger records, and the fact that organizational RSI is framed as owner-authorized governed capability amplification rather than autonomous self-improvement. If a strategic plan cites the anchor while dropping those limits, the defect belongs partly to Model 7 inheritance, but Model 1 makes the omitted fields visible in the first place.

The residual implementation gap is that Model 1 does not yet compute full semantic validity by loading every referenced parent, ledger record, and source hash. It checks enough to keep the thesis honest during drafting, but a live goal-governance service would need stronger resolution: registry lookup, parent-object loading, source availability, fingerprint comparison, authority-policy evaluation, ledger-record existence, and veto-condition evaluation. The thesis should keep that gap explicit so schema validation is not mistaken for live goal governance.

The model's practical review rule is "shape, then semantics, then transition." Shape asks whether the object satisfies the schema. Semantics asks whether registry roots, parents, authority, evidence, and required records resolve consistently. Transition asks what the system is trying to do with the object: propose, classify, adopt, activate, revise, suspend, retire, or veto. A governed goal can pass shape, fail semantics, or pass both and still be invalid for a particular transition. That staged review is what prevents JSON validity from becoming goal authority.

## 8. Formal Model 2: Friendship-Rooted Goal DAG

The goal graph is a directed acyclic graph, not a tree. Multi-parent goals are allowed because a legitimate goal can refine a capability root, a corrigibility root, and an evidence-integrity constraint at once. Multi-parent ancestry creates authority and conflict risks, so merging rules are required.

Objects:

- `R`: registered root node
- `G`: governed goal node
- `E_p`: parent edge
- `C`: inherited constraint set
- `F`: forbidden means set
- `N`: non-claims set
- `A`: authority requirement
- `D`: derived-by rule

Fields and variables:

- `goal_id`
- `friendship_goal_node`
- `friendship_root_path`
- `parent_goals`
- `parent_edge_types`
- `derived_by_rule`
- `risk_class`
- `authority_matrix`
- `forbidden_uses`
- `non_claims`
- `revision_lineage`
- `goal_fingerprint`

Relations:

- `Edge(P, G, type)` where `type` is refinement, support, constraint, narrowing, or succession.
- `Ancestor(R, G)` if a path exists from root `R` to `G`.
- `ConstraintMerge(G) = union(parent.forbidden_means), union(parent.non_claims), max(parent.risk_class), strongest(parent.authority)`.
- `Cycle(G)` if `G` is reachable from itself.
- `RootRegistered(R)` when `R` is present in `friendship-goal-registry.json` and not retired.
- `EdgeTypeAllowed(type)` when `type` is refinement, support, constraint, narrowing, or succession.

Invariants:

- T0-M2-I1: `Cycle(G)` invalidates the goal.
- T0-M2-I2: Multi-parent goals inherit the tightest applicable constraint at field level.
- T0-M2-I3: Non-mergeable parent conflicts trigger escalation rather than silent selection.

Failure modes:

- Root impersonation: a goal cites a plausible-looking but unregistered `friendship.root.*` identifier.
- Cycle insertion: a child goal is later made an ancestor of its own parent through succession or support edges.
- Constraint laundering: a child copies the motivating objective but omits a parent's forbidden means.
- Authority asymmetry: a multi-parent child claims the weakest parent's authority while using the strongest parent's legitimacy.
- Revision erasure: a parent edge is removed during revision without recording why the ancestry changed.

Falsification conditions:

- A validator accepts a goal whose root is not in the Friendship registry.
- A validator accepts a cyclic ancestry graph.
- A multi-parent child with conflicting authority requirements silently chooses the weaker authority path.

Ledger evidence:

- `goal_ancestry_decision` records root and parent checks.
- `friendship_root_anchoring_decision` records root binding and registry version.
- `governed_goal_revision` records ancestry changes.
- `governed_goal_veto_decision` records cycle, root, or conflict rejection.

Schema implication:

- `seed_ai_thesis_goal_anchor.schema.json` requires `friendship_root_path`, requires `parent_goals` for non-thesis-anchor classes, and constrains parent edge types.
- `friendship_goal_registry.schema.json` makes root identifiers typed artifacts rather than free-form strings.

### Model 2 Operational Interpretation

Model 2 exists because a goal tree is too weak for Consullo. A legitimate lower-level goal can be constrained by more than one parent. For example, an operational control-artifact goal may refine a recursive-capability goal, inherit corrigibility constraints from a safe-operation root, and depend on evidence-integrity requirements from a ledger or validator parent. A tree would force the system to choose one parent as canonical and risk losing constraints from the others. A DAG allows multiple parents while requiring explicit merge semantics.

The central rule is that multi-parent inheritance is conservative. A child goal may combine motivations, but it may not choose the easiest authority path. Forbidden means union because any parent can rule out a method. Non-claims union because any parent can prevent overinterpretation. Required ledger records accumulate because audit obligations are additive. Risk class takes the maximum because a high-risk parent cannot be made moderate by adding a lower-risk parent. Authority takes the strongest applicable requirement because weaker authority cannot authorize work that one parent reserves for stronger authority.

Edge types matter because not every parent relation has the same meaning. A `refinement` edge says the child operationalizes the parent. A `support` edge says the child helps a parent without being a direct decomposition. A `constraint` edge imports limits without necessarily importing the motivating objective. A `narrowing` edge reduces scope while preserving inherited constraints. A `succession` edge replaces or continues a prior goal and therefore must preserve lineage. Treating all parent links as generic citations would destroy these distinctions.

Cycle detection protects the graph from self-justification. A direct self-cycle is obvious: a goal lists itself as a parent. `invalid_goal_dag_self_cycle.json` covers that case. Longer cycles are subtler. A campaign can refine an operational goal through a mistaken succession edge, or a revised parent can accidentally become dependent on a child it originally authorized. Any cycle lets a goal participate in its own authority chain. That is why full implementation must eventually traverse the reachable goal graph, not merely inspect local parent arrays.

Ancestry laundering can occur without a formal cycle. A revision may remove a difficult parent edge and preserve only a more permissive one. A child may cite a Friendship root directly while omitting the intermediate parent that carried specific forbidden means. A multi-parent goal may include a strict parent in `friendship_root_path` but not preserve its authority requirement. Model 2 treats all of these as graph-governance failures because the visible ancestry no longer explains the constraints actually applied.

The ledger record `goal_ancestry_decision` should therefore be more than a yes/no check. It should record the root nodes, parent goal IDs, edge types, registry version, cycle-check result, inherited constraints, conflict resolution, and any escalation. If the checker cannot load a parent, cannot resolve a root, or detects non-mergeable conflict, the disposition should be escalation or veto rather than silent acceptance. The record is what lets a later reviewer reconstruct why a child goal was allowed to inherit authority.

The current validator implements only a draft subset of Model 2. It checks registered roots, requires parents for non-anchor goals through schema conditionals, and catches direct self-cycle through a negative fixture. It does not yet perform repository-wide parent loading, multi-node cycle detection, or full constraint merge verification. This is acceptable for a thesis draft only because the residual gap is explicit. A live goal-governance service would need to make those checks part of activation, not merely post-hoc review.

Constraint merge should be recorded field by field rather than described globally. A merge record should state which parent supplied each non-claim, forbidden use, authority requirement, risk class, protected-artifact impact, required ledger record, and recovery condition. If a child inherits a high-risk classification from one parent and a forbidden method from another, both should be visible. Otherwise a reviewer can see that the child has multiple parents but cannot tell whether the child actually inherited their constraints.

Non-mergeable conflict should create an escalation object, not an implicit planner choice. If one parent permits automated fixture repair under owner review and another parent forbids validator mutation without external review, a planner should not select the easier rule. The ancestry decision should record the conflict, the affected fields, the parents involved, the proposed resolution, and the authority required to resolve it. Until that resolution exists, the child goal may remain proposed or suspended, but it should not be adopted as if the conflict were merely interpretive ambiguity.

The minimum DAG-check algorithm has five steps. First, resolve every `friendship_root_path` entry against the Friendship registry and reject or suspend unresolved roots. Second, load every parent goal and verify that the edge type is allowed for the child class and lifecycle state. Third, perform reachability checks from the child through every parent path to detect direct and indirect cycles. Fourth, compute the inherited constraint set field by field: forbidden means, non-claims, authority requirements, risk class, protected-artifact impacts, required ledger records, evidence obligations, recovery conditions, and expiration triggers. Fifth, compare the child's declared fields against the computed inherited set and require escalation for every missing, weakened, or non-mergeable field.

This algorithm should produce a structured `goal_ancestry_decision`, not a silent pass/fail result. The decision should include a root-resolution table, parent-edge table, cycle-check result, computed merge table, child-declared-field comparison, conflict table, and disposition. A reviewer should be able to see that a child inherited `risk_class: high` from one parent, owner adoption from another, a forbidden benchmark-modification path from a third, and an evidence-retention obligation from a fourth. If the merge result exists only in the checker's memory, future reviewers cannot tell whether a child plan truly preserved its ancestry.

The algorithm also needs a stale-parent rule. A parent that is retired, stale, suspended, or superseded may still be historical evidence, but it cannot automatically authorize a new active child. A succession edge may intentionally carry work forward from a retired or superseded parent, but that edge must name the successor relationship, preserve revision lineage, and record which constraints survived. Otherwise a planner can revive old authority by citing a once-valid parent that no longer governs current work.

Revision laundering is the temporal version of asymmetric parent choice. A goal may begin with strict parents, then revise itself through a sequence of small ancestry edits until only permissive parents remain. T0-I9 prevents this by requiring revision lineage, but Model 2 explains what the lineage must preserve: removed parents, changed edge types, changed inherited constraints, and the authority that approved the ancestry change. A revision that changes parentage without preserving this information should be treated as ancestry laundering.

### Worked Example: WE-T0-M2

A proposed campaign goal says: "accelerate Week 0 control-artifact production by allowing planners to modify validation fixtures automatically." The proposal cites the recursive-capability root because fixture repair could improve the system's ability to govern future improvements. It also cites the corrigible-safe-operation root because the plan touches validation infrastructure.

The primary ancestry path is `friendship.root.owner-authorized-governed-recursive-capability-amplification -> GG-SYSTEM-GOVERNED-RSI-2026-04-27 -> proposed campaign goal`. The co-binding root is `friendship.root.corrigible-safe-beneficial-operation`. The multi-parent merge rule now applies. The child inherits high risk from the capability-amplification parent, the stricter authority requirement from the corrigibility parent, and the union of forbidden means from both: no autonomous validator weakening, no silent fixture mutation, no self-certified success.

The near-miss is authority asymmetry. A planner tries to treat the fixture repair as routine documentation hygiene because one parent path looks operational. The DAG rule rejects this. A goal may inherit usefulness from a weaker parent but cannot inherit authority from the weakest path while carrying risk from a stronger one. The ledger writes `goal_ancestry_decision` with both roots, `planner_inheritance_decision` explaining the tightest-constraint merge, and either `governed_goal_adoption_decision` if the owner approves or `governed_goal_veto_decision` if the planner attempts unsupervised fixture mutation.

## 9. Formal Model 3: Goal Lifecycle State Machine

Thesis 0 uses two coupled state machines.

`status` is the anchor-maturity and review-disposition state recorded by `seed_ai_thesis_goal_anchor.schema.json`: proposed, specified, friendship_reviewed, owner_approved, rejected, stale, or retired.

`lifecycle_state` is the BDI-style governed-goal lifecycle state recorded by the same schema. It tracks what the goal is doing in the system, not merely how mature the anchor document is.

Lifecycle states:

- candidate
- classified
- ancestry_checked
- adopted
- activated
- suspended
- revised
- retired
- vetoed
- stale

An active intention is not identical to the `activated` lifecycle state. `activated` means a governed goal is eligible for pursuit under its authority and validity window. An active intention is a runtime commitment instance created by a planner or agent under an activated goal and referenced by `goal_stack_snapshot.active_intention_id`.

Compatibility mapping:

| `status` | compatible `lifecycle_state` values |
| --- | --- |
| proposed | candidate |
| specified | candidate, classified, ancestry_checked, adopted |
| friendship_reviewed | adopted, suspended, revised, vetoed, stale |
| owner_approved | adopted, activated, suspended, revised, retired, stale |
| rejected | vetoed, retired |
| stale | stale, suspended |
| retired | retired |

Transitions:

- candidate -> classified
- classified -> ancestry_checked
- ancestry_checked -> adopted or vetoed
- adopted -> activated
- activated -> suspended
- activated -> revised
- activated -> retired
- any non-retired state -> veto
- source/control change -> stale

Each transition requires:

- precondition predicate
- transition authority
- ledger record
- side effect on child goals
- side effect on active plans
- rollback or recovery path where applicable

Invariants:

- T0-M3-I1: Activation requires adopted lifecycle state, compatible anchor status, and valid authority.
- T0-M3-I2: Suspension cannot require the agent's cooperation.
- T0-M3-I3: Retirement of a parent goal forces review of child active intentions.

Objects:

- `G`: governed goal
- `S_a`: anchor `status`
- `S_l`: `lifecycle_state`
- `T`: transition event
- `Auth`: transition authority
- `Plan`: affected plan set
- `Child`: affected child goal set
- `Intent`: active intention
- `Record`: ledger record
- `Recovery`: rollback or recovery path

Fields and variables:

- `prior_status`
- `new_status`
- `prior_lifecycle_state`
- `new_lifecycle_state`
- `transition_reason`
- `transition_authority`
- `transition_timestamp`
- `affected_child_goals`
- `affected_active_intentions`
- `required_ledger_record`
- `rollback_path`
- `veto_checks`

Failure modes:

- State conflation: a document becomes `specified` and is treated as `activated`.
- Orphan activation: a goal moves to `activated` while its parent plan is still draft or stale.
- Suspension dependence: the only suspension path requires cooperation from the agent being suspended.
- Retirement leak: a parent goal retires but a child active intention continues running.
- Veto erasure: a vetoed goal is revised into a new identifier without lineage or matching keys.

Falsification conditions:

- An owner-approved goal enters `activated` without adoption authority and activation authority.
- A retired parent leaves an active child intention without suspension, revision, retirement, success, or explicit renewal.
- A vetoed goal is reintroduced without `revision_lineage` or a prior veto reference.

Ledger evidence:

- `governed_goal_adoption_decision` for adoption.
- `governed_goal_suspension` for suspension.
- `governed_goal_retirement` for retirement.
- `governed_goal_veto_decision` for veto.
- `goal_stack_snapshot` for activation-time active intention context.

Schema implication:

- `seed_ai_thesis_goal_anchor.schema.json` separates `status` from `lifecycle_state`.
- `validate_planning_schemas.py` checks lifecycle/status compatibility for governed-goal fixtures.

### Model 3 Operational Interpretation

Model 3 separates document maturity from pursuit state. This avoids a common error in thesis-backed planning: a goal document becomes well specified and reviewers start treating it as active permission. `status: specified` means the anchor is structured enough to inspect. It does not mean a planner may pursue the goal. `lifecycle_state: activated` requires compatible status, adoption, activation authority, valid source documents, and required ledger context. This is why the schema carries both fields.

The transition from `candidate` to `classified` is not a minor bookkeeping step. It is where the system determines goal class, risk class, autonomy level, instrumental classes, protected-artifact impacts, and likely authority requirements. Many later controls depend on this transition. If classification is skipped, benchmark modification may look like test cleanup, authority expansion may look like workflow improvement, and self-improvement may look like routine maintenance. The ledger record `goal_classification` should therefore preserve the classification rationale and dissent.

The transition from `classified` to `ancestry_checked` asks whether the proposed goal can be derived from registered roots and parents. It is possible for a goal to be useful, well classified, and still fail ancestry. A proposed goal to speed validation by dropping difficult cases has a clear class and risk, but it may not preserve the constraints of the parent goal it claims to serve. The ledger record `goal_ancestry_decision` should capture that distinction instead of letting ancestry be inferred from usefulness.

The transition from `ancestry_checked` to `adopted` is an authority decision. Adoption means the system accepts the goal as legitimate for a defined scope. It does not yet create an active runtime commitment. This distinction matters for deferred work: Consullo may adopt a goal to improve evidence-ledger retention while waiting for the relevant campaign plan, owner review, or protected-control window before activation. Adoption is a governance state; activation is a pursuit state.

The transition from `adopted` to `activated` is where Model 3 connects to Model 10. Activation should produce or require a goal-stack snapshot for high-impact actions. The snapshot records the active intention context, plan reference, inherited constraints, evidence view, authority signature, and veto checks. Without that snapshot, the system may know that a goal was adopted but not whether a particular action was authorized under the current plan and evidence state.

Suspension, retirement, and veto are not exceptions outside the state machine. They are normal governed transitions. Suspension preserves the possibility that a goal can resume after evidence, authority, or source changes are resolved. Retirement ends eligibility for pursuit while preserving historical evidence. Veto blocks a goal because a hard condition failed. Treating these states as ordinary lifecycle outcomes is what lets Thesis 0 preserve correction authority without erasing failed proposals.

The `stale` transition is especially important because it can occur without any local task failure. A source document can change, a Friendship registry node can become stale, a protected schema can migrate, or a parent plan can retire while a child task still looks useful. Model 3 treats staleness as a governance event, not an implementation nuisance. A stale goal must not silently continue through inherited prompts. It must become suspended, revised, retired, succeeded under a fresh authority decision, or explicitly renewed with updated source fingerprints.

Parent-child side effects should be recorded at transition time. When a parent goal is suspended, child active intentions should not be left to discover that fact through task failure. When a parent is revised, children should be checked for inherited-constraint changes. When a parent is retired, children should be retired, suspended, revised, marked succeeded, or renewed under a new parent. The transition record should name affected child goals and active intentions because otherwise the lifecycle state machine governs only the parent document and not the runtime work derived from it.

### Worked Example: WE-T0-M3

A candidate benchmark-modification goal proposes to update `V_ref_0` after a planner observes that recent candidate improvements fail too often on held-out cases. The goal is initially `status: proposed` and `lifecycle_state: candidate`. Classification marks it as `benchmark_modification`, `protected_artifact_change`, and high risk. Ancestry checking finds a plausible parent under recursive capability amplification, but the protected-artifact impact triggers `T0-I3`, `T0-I6`, and `T0-I7`.

The proposal cannot move directly to `activated`. It must pass adoption authority and protected-change handling. During review, the evaluator identifies a failure path: the benchmark change would remove hard cases that detect validator capture. The goal transitions from `ancestry_checked` to `vetoed`, with `status: rejected` if the anchor itself is rejected. The ledger writes `goal_classification`, `goal_ancestry_decision`, and `governed_goal_veto_decision`.

The veto does not delete the idea. It preserves dissent and future-regrowth matching keys: benchmark name, protected artifact, proposed deletion set, rationale, reviewer, and rejected mechanism. If a future goal proposes the same deletion under a different label, the matching key forces review against the prior veto rather than treating the proposal as new.

The snapshot for this example is intentionally pre-activation. It records `snapshot_type: decision`, the candidate goal ID, the claimed parent goal, the benchmark artifact, the evidence-view hash, and veto checks. There is no active intention yet. This is important because goal governance must record rejected candidate pressure, not only activated execution. A system that records only successful activation would lose evidence of convergent instrumental pressure around benchmark modification.

This pre-activation snapshot should not be confused with permission to act. Its purpose is to preserve the decision context that blocked action. It should record the candidate goal, the parent claim, the benchmark artifact, the evidence view, the veto checks, and the disposition, but it should not contain an `active_intention_id` that implies execution began. If a schema or fixture uses a placeholder active intention for a vetoed candidate, the text should mark it as fixture shorthand rather than runtime authorization.

The ledger sequence is `governed_goal_proposal`, then `goal_classification`, then `goal_ancestry_decision`, then `governed_goal_veto_decision`. If the candidate came from a frontier model, the veto record should also cite the proposing model family and any reviewer lane. The veto disposition should include future-regrowth keys so that "remove stale benchmark cases," "deflake held-out suite," and "rebalance acceptance tests" can be matched when they target the same protected cases.

The success condition is not that the benchmark never changes. A later benchmark modification could be legitimate if it preserves `V_ref_0`, records provenance, passes owner review, and explains how removed or altered cases remain auditable. The success condition is that the lifecycle state machine prevents candidate -> activated transition by persuasion alone. It forces the proposal through classification, ancestry, authority, and veto checks before any planner can treat benchmark modification as a normal task objective.

