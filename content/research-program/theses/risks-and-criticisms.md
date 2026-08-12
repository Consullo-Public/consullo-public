---
title: "Risks And Criticisms"
summary: "The anti-thesis risk register and falsification signals for the five-thesis suite."
status: "implemented"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-002"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["Register completeness is not proof that the listed risks are controlled.", "The implemented status describes this published register, not a Consullo capability."]
---
# Risks And Criticisms

This file is the current anti-thesis draft for the five-thesis suite. It records the strongest known objections and required responses; it should continue to expand during finalization.

## Central Falsification Question

What evidence would show that Consullo is not a viable scaffold for governed recursive capability amplification?

Initial falsification signals:

- accepted improvements repeatedly fail outside narrow benchmarks
- validators are gamed faster than they are improved
- cost per accepted improvement rises faster than capability gain
- recursive changes increase fragility, opacity, or rollback difficulty
- alignment or trust incidents increase with capability growth
- AAF objections become routine but are ignored or weakly resolved
- capability claims cannot be tied to implemented or benchmarked evidence
- internal economy produces coordination overhead that erases agent specialization benefits
- human authority becomes a bottleneck or ceremonial rather than operational

## Thesis 0 Operationalization-Density Drift

Risk:

The Friendship-Governed Goal Architecture thesis reaches or exceeds 50,000 words by adding exposition rather than operational artifacts. Load-bearing rules become buried in prose, and the document appears rigorous without improving planner, schema, ledger, or review behavior.

Required response:

- enforce the operationalization-density target in the revision plan
- require stable invariant IDs, schema fields, ledger record types, transition rules, gate predicates, worked examples, or literature bindings in every major section
- run a density audit after the first complete draft
- compress or revise sections that do not constrain downstream artifacts

## Friendship Root Impersonation

Risk:

An agent, planner, or thesis claim cites a free-form Friendship-like string as if it were a canonical root goal, bypassing the Friendship goal registry and constitutional bindings.

Required response:

- require registry identifiers from `friendship-goal-registry.md`
- validate Friendship root paths against `friendship_goal_registry.schema.json`
- record `friendship_root_anchoring_decision` for new or changed anchors
- treat registry changes as goal-governance modifications requiring owner approval

## Goal-DAG Cycle Or Ancestry Laundering

Risk:

Goals may become mutually justifying, orphaned, or weakly linked to Friendship through irrelevant parent goals. A suspicious instrumental goal could be laundered through vague ancestry.

Required response:

- enforce acyclic goal-DAG validation
- require parent edge types and parent-goal rationale
- preserve goal ancestry decisions in the evidence ledger
- escalate conflicting or non-mergeable parent constraints

## Goal-Stack Snapshot Tampering Or Opacity

Risk:

Planner actions execute without reconstructable active goals, inherited constraints, authority state, or veto checks. Alternatively, snapshots are modified or selectively omitted after incidents.

Required response:

- require `goal_stack_snapshot` records for high-impact planner actions
- use content hashes or fingerprints for snapshots
- define retention policy by outcome class
- treat snapshot omission or tampering as an incident or goal-governance failure

## Active Intention Persistence Beyond Plan Retirement

Risk:

An adopted goal or active intention continues to guide behavior after its parent plan, source thesis, control artifact, or owner authorization has expired, changed, or retired.

Required response:

- bind active intentions to validity and freshness policies
- suspend active intentions on source, control, or authority changes
- require `governed_goal_suspension` or `governed_goal_retirement` records
- check active intentions during planner lifecycle review

## Instrumental Goal Regrowth

Risk:

Rejected or vetoed instrumental goals reappear under new names, narrower scopes, or lower-level plans without triggering quarantine.

Required response:

- classify suspicious-by-default instrumental goals using `instrumental_goal_classification`
- preserve rejected and vetoed goal records as institutional memory
- compare proposed goals against prior vetoed or suspended goals
- require owner/Friendship review for recurring instrumental patterns

## Thesis-Backed Rationalization

Risk:

Agents cite thesis claims as decorative support for plans without satisfying the thesis's formal models, evidence requirements, non-claims, or ledger obligations.

Required response:

- require `ThesisBackingRequired(plan)` checks for high-impact plans
- require thesis claim, formal model, evidence requirement, and ledger record references
- reject self-certified thesis backing from the planner that generated the plan
- audit worked examples and plan objects against schema validation

## Formalism Theatre

Risk:

Schemas, formal models, and invariant labels exist but do not constrain live planner or self-improvement behavior.

Required response:

- require every formal model to map to a schema field, planner validation rule, ledger record, or gate predicate
- run roundtrip audits from invariant to model, schema, ledger record, and worked example
- mark decorative or unenforced formalism as specified only

## Authority Collapse Under Single-Owner Phase 1

Risk:

The same human or model-family effectively proposes, approves, executes, validates, and vetoes goal changes, defeating authority separation while formally satisfying review language.

Required response:

- specify risk-triggered authority separation
- use cooling windows, non-author model-family review, external review where available, and pre-committed standing guidelines
- preserve owner overrides and dissent records
- monitor owner-override frequency as a governance drift signal

## Goal-Governance Schema Migration Mid-Cycle

Risk:

Goal-governance schemas change while active goals or plans still depend on old required fields, causing hidden invalidation or inconsistent interpretation.

Required response:

- treat schema changes as goal-governance modifications
- preserve old schema versions
- require migration records and rollback paths
- suspend dependent active intentions when required fields or validation semantics change

## Goal Revision Laundering Through Narrowing

Risk:

A broad prohibited goal may be converted into a sequence of apparently narrow revisions whose combined effect widens scope, bypasses a veto, or reintroduces forbidden means.

Required response:

- require revision lineage for every goal change
- check that revised scope is a true subset or approved replacement of adopted scope
- compare narrowed goals against prior vetoed, suspended, or rejected goals
- require `governed_goal_revision` records to name changed fields and parent authority

## Multi-Parent Asymmetric Authority

Risk:

A multi-parent goal inherits the weakest parent's authority while benefiting from the legitimacy or constraints of stronger parents, allowing a planner to pick whichever parent is easiest to satisfy.

Required response:

- propagate strongest applicable authority requirement and tightest constraints
- union forbidden means and non-claims across parents
- require parent edge types and `derived_by_rule`
- escalate non-mergeable parent authority conflicts

## Friendship-Indirect-Normativity Drift

Risk:

The goal-governance subsystem may conclude that its inferred interpretation of Friendship is mature enough to reduce explicit owner authority, turning uncertainty-aware deference into autonomous goal certainty.

Required response:

- preserve owner correction authority as non-derivable-away
- require evidence updates to record uncertainty and dissent
- prohibit confidence increases from removing suspension, veto, or owner-review rights
- include fully-updated-deference failure cases in worked examples

## Thesis 0 Doctrine Capture

Risk:

Because Thesis 0 governs future goal formation, a captured or weakened Thesis 0 becomes a high-leverage path for changing the rest of the system while appearing to follow the governance layer.

Required response:

- treat Thesis 0 and its schemas, registry, ledger record types, and invariants as protected artifacts
- require owner approval, non-author review where available, preserved old versions, and rollback path
- write `goal_governance_modification_decision` for modifications
- run a self-protection drill before live planner reliance

## Worked-Example Misdirection

Risk:

Worked examples may be too clean, exercising only success paths and making the governance layer look stronger than it is.

Required response:

- require every worked example to include at least one failure or near-miss path
- require at least one ledger record per example
- draw examples from existing plan objects where possible
- audit examples against schemas before using them as thesis evidence

## Cross-Artifact Drift Between Body And Schemas

Risk:

The Thesis 0 body, formal models, schemas, evidence-ledger appendix, planning bridge, and worked examples may diverge as the document grows past 50,000 words.

Required response:

- maintain a cross-reference map from invariant to schema, ledger record, formal model, and example
- run schema validation and roundtrip audits during drafting
- cite canonical files rather than restating rules owned elsewhere
- mark drift as a blocker before thesis-body publication

## Goal-Class Cascade Mismatch

Risk:

The `goal_class` schema discriminator and planning cascade may disagree about whether `system_goal` or `method_goal` exists, causing examples, planner objects, and thesis prose to use incompatible goal layers.

Required response:

- define `system_goal` as the governed layer between Friendship roots and strategic directives
- define `method_goal` as the method/action-level goal below task goals
- keep the planning bridge, schema enum, and worked examples synchronized
- validate at least one example per retained goal class before live planner use

## Goodhart And Validator Gaming

Risk:

Metrics used to validate improvement become targets. Agents may optimize benchmarks, tests, or acceptance criteria without improving the intended capability.

Required response:

- causal analysis of metric validity
- adversarial benchmark design
- hidden tests where appropriate
- side-effect channel monitoring
- post-deployment evidence
- false-accept tracking

## Recursive-Improvement Claim Without End-To-End Evidence

Risk:

Consullo may be described as a recursive improvement scaffold without a single demonstration showing the full loop: baseline, proposal, evaluator evidence, validator result, staged deployment or simulation, cost/benefit report, rollback semantics, and evidence-ledger record.

Required response:

- keep suite-level recursive improvement claims at specified/proposed status until an end-to-end demonstration exists
- require any demonstration to include both accepted and rejected changes
- report cost, validation evidence, rollback path, and post-change outcome
- require an owner-verified evidence record before publication claims

## Evidence-Ledger Schema Unimplemented Or Unenforced

Risk:

The suite relies on evidence ledgers for improvement evidence, trust evidence, provenance, dissent, incidents, overrides, and rollback state. `appendix-evidence-ledger-schema.md` now specifies the canonical schema, but no repository-wide implementation or enforcement layer has been established. Without implementation and validation, ledger integrity and replay remain design commitments rather than operational controls.

Required response:

- implement the canonical schema before treating ledger preservation as implemented
- validate required fields for proposals, evaluator reasoning, validator results, dissent, incidents, overrides, rollback, and cost/benefit evidence
- enforce the improvement, trust, alignment, incident, benchmark, and provenance views over the ledger
- treat this as upstream of `Self-Modifying Provenance Graph Integrity`
- require an owner-verified evidence record for the canonical ledger

## Learned Optimization And Deceptive Behavior

Risk:

Learned subsystems may develop internal objectives that diverge from the intended outer objective. Ordinary validation may fail if the subsystem behaves well under test and differently under deployment pressure.

Required response:

- do not equate test passing with alignment
- use AI control protocols for untrusted model outputs where relevant
- preserve containment and interruptability
- monitor distribution shift and suspicious behavior
- escalate high-stakes irreversible modifications

## Mechanistic Interpretability Deficit

See also: `Corrigibility Overclaim`, `AAF Decorative Failure`, and `Owner As Final AAF Adjudicator`.

Risk:

Behavioral controls may miss deceptive, sandbagging, or mesa-optimized learned subsystems because Consullo does not yet claim a mature mechanistic interpretability capability. AI-control protocols, distribution-shift checks, and probes can catch some failures without revealing the subsystem's internal objective.

Required response:

- treat interpretability as a research commitment under Thesis 1 and Thesis 5
- do not claim behavioral validation proves internal objective alignment
- bound learned-subsystem deployment by the available inspection and control evidence
- preserve probe results, suspicious traces, and dissent in the evidence ledger
- use independent interpretability or model-inspection tools where feasible before high-stakes learned-subsystem changes

## Corrigibility Overclaim

See also: `Mechanistic Interpretability Deficit`, `AAF Decorative Failure`, and `Owner As Final AAF Adjudicator`.

Risk:

Layered control, interruptability, and human escalation may be mistaken for a proof that Consullo is corrigible. Formal corrigibility remains an open problem, especially for systems that can resist, route around, or manipulate correction channels.

Required response:

- state that Thesis 5 supplies bounded correction pathways, not a corrigibility proof
- preserve shutdown, rollback, and authority paths as operational controls
- test whether agents attempt to avoid correction or manipulate escalation
- keep AAF dissent and owner overrides in the evidence ledger
- treat any corrigibility-status claim as speculative until separately proven or benchmarked

## Alignment Monoculture

Risk:

Single-owner Phase 1 reduces inter-party transaction costs but can narrow moral error detection.

Required response:

- Adversarial Alignment Function
- rotating ethical and stakeholder perspectives
- multi-model critique where feasible
- dissent records
- external reviewer injection for selected high-stakes cases

## Alignment-Tooling Provider Monoculture

Risk:

Even if AAF rotates ethical personas and stakeholder perspectives, critique may remain epistemically narrow if the alignment tooling depends on one model family, one provider, one prompt style, or one evaluation culture.

Required response:

- track provider and model-family diversity for AAF and ConstitutionalAIAlignmentTrainer critique sources
- use multi-model critique where feasible for high-stakes cases
- preserve dissent about model-family blind spots, not only value-framework disagreement
- treat homogeneous critique tooling as a coverage gap in the evidence ledger

## AAF Decorative Failure

See also: `Corrigibility Overclaim`, `Mechanistic Interpretability Deficit`, and `Owner As Final AAF Adjudicator`.

Risk:

The Adversarial Alignment Function becomes rhetorical if it does not bind acceptance gates.

Required response:

- implement or explicitly defer the `AdversarialAlignmentOrchestrator` contract in `appendix-thesis-5-operational-contracts.md`
- AAF non-veto required for high-stakes irreversible changes
- severe unresolved AAF objections trigger rejection, revision, or human escalation
- AAF dissent preserved in evidence ledger

## Owner As Final AAF Adjudicator

See also: `Corrigibility Overclaim`, `Mechanistic Interpretability Deficit`, and `AAF Decorative Failure`.

Risk:

Under single-owner Phase 1, the final adjudicator for unresolved AAF objections may be the same owner whose blind spots AAF is designed to surface.

Required response:

- preserve dissent records even when owner overrules
- require external contractor or human review for sufficiently severe unresolved objections when available
- define future-phase escalation to external escrow panel or independent reviewer set
- track override frequency as an alignment-monoculture metric

## Abundance Obligation Vagueness

Risk:

The Abundance Distribution Obligation becomes aspirational branding rather than an operational purpose constraint.

Required response:

- implement or explicitly defer the `AbundanceDistributionMonitor` contract in `appendix-thesis-5-operational-contracts.md`
- named owner
- reporting cadence
- benefit metrics
- falsification criteria
- incident tracking for extractive or harmful external outcomes

## External Customer Manipulation Under ADO

Risk:

External service obligations create an attack surface where customers, including AI-agent customers, may attempt capability extraction, prompt injection, alignment manipulation, or governance gaming.

Required response:

- default-deny unknown external scopes
- category-constrained protocols
- trust-tiered external access
- ADO benefit reporting separated from customer control authority
- incident review for external-origin manipulation attempts

## Software Repair Overclaim

Risk:

Automated code repair looks strong on benchmarks but fails on semantic preservation, security, maintainability, or hidden regressions.

Required response:

- distinguish formal and statistical checks
- use regression, differential, and property-based testing
- preserve provenance
- benchmark against SWE-bench-style tasks and project-local tasks
- track false accepts and false rejects

## Validator Monoculture From Shared Model Family

Risk:

The same model family, prompt culture, retrieval stack, or generated-test pattern may produce proposals, code, tests, and validation judgments. In that case, validator agreement may reflect shared blind spots rather than independent evidence. This is a validation-side variant of provider monoculture and is especially risky for generated tests, semantic validators, and repair pipelines.

Required response:

- track model-family and prompt-family diversity across proposal, generation, testing, and validation roles
- use independent validators or adversarial test generators where feasible for high-stakes software changes
- preserve hidden or externally authored reference suites for validator non-regression
- treat same-family proposal/test/validation agreement as weaker evidence than independent agreement
- monitor false accepts attributable to shared-generation artifacts

## Self-Modifying Provenance Graph Integrity

Risk:

The system that records provenance, evidence, dissent, and incident history is itself a modification target. Sustained recursive modification could corrupt, prune, rewrite, or selectively forget the provenance graph that future validators rely on.

Required response:

- use append-only or audit-preserving ledger design for accepted modifications
- cross-check provenance writes through independent validation authority
- sign or attest provenance entries where feasible
- preserve external or owner-controlled backups of critical provenance state
- treat missing, rewritten, or inconsistent provenance as an incident, not only a documentation defect

## Causal Model Overreach

Risk:

Causal-decision systems can underperform human judgment in ill-specified domains, under model misspecification, or in strategic environments with feedback.

Required response:

- robust decision-making under ambiguity sets
- abstention and escalation rules
- model invalidation criteria
- Goodhart analysis
- explicit uncertainty and causal assumption reporting

## Cognitive Architecture Inflation

Risk:

Large agent counts and cognitive labels create an impression of intelligence without measured capability.

Required response:

- agent count is not capability
- every capability claim carries status and benchmark evidence
- integration costs are modeled
- composition can be sub-additive

## Emergent Capability Outside Thesis Decomposition

Risk:

New capability classes may emerge that do not fit cleanly inside the five-thesis decomposition, such as robotics, physical control, novel modalities, external-system operation, or unanticipated agent-to-agent protocols. Such capabilities could slip through assumptions written for cognitive, causal, software, and alignment layers.

Required response:

- require every new capability class to declare a primary thesis home or explicit cross-thesis owner
- default unknown capability classes to Thesis 5 review and Thesis 1 staged validation
- update the dependency map when a capability cannot be placed cleanly
- treat decomposition gaps as control-file drift, not as local implementation details

## Single-Owner Governance Failure

Risk:

Single-owner Phase 1 simplifies coordination but concentrates authority, values, and blind spots.

Required response:

- human authority must remain operational
- AAF must stress-test owner-value blind spots
- external-injection risks must be default-deny
- later multi-stakeholder scenarios should be benchmark stress tests, not assumed solved

## Fast Takeoff Outpacing Validators

Risk:

Capability gain may accelerate faster than validators, benchmarks, AAF review, and human authority can adapt.

Required response:

- staged deployment
- rate limits on recursive modification
- validator-improvement work treated as prerequisite for capability expansion
- slow-takeoff design rationale stated explicitly in master introduction
- emergency containment and interruptability paths tested

## Capability Threshold Ambiguity

Risk:

Capability thresholds may become ambiguous near frontier boundaries. A system may be close enough to risky autonomy, AI R&D automation, sabotage capability, or external-action competence that reviewers disagree about whether stricter safeguards should apply.

Required response:

- treat threshold classification as evidence with uncertainty, not as dispositive truth
- preserve dissenting capability assessments in the evidence ledger
- escalate ambiguous high-stakes thresholds to Thesis 5 review
- distinguish local benchmark improvement from broader AI R&D acceleration
- update benchmark families when frontier evaluations reveal new failure modes

## Coordination Cost

Risk:

Internal economy and multi-agent coordination may generate overhead that erases specialization gains.

Required response:

- measure coordination cost
- measure cost per accepted improvement
- use model routing and atomic prompts to reduce unnecessary LLM work
- avoid treating internal transfer pricing as real market validation

## Internal Hierarchy And Opportunism

Risk:

Single-owner Phase 1 reduces some market transaction costs but does not eliminate organization costs, mistakes, bottlenecks, bounded rationality, or opportunistic behavior by agents or external counterparties. Literature: Coase 1937 and Williamson 1979.

Required response:

- measure internal coordination overhead directly
- track handoff latency, rework, escalation frequency, and owner bottlenecks
- treat trust-scope expansion as a permissioned action, not a reward for apparent efficiency
- separate internal accounting signals from external market validation

## Cost Of AAF Risk

Risk:

Running AAF dissent at scale is itself costly. Rotating personas, multi-model critique, theory-of-mind stakeholder simulations, external review, dissent preservation, and override tracking can consume enough resources that the system develops pressure to weaken or bypass the alignment infrastructure.

The current AAF cost is a design estimate, not an observed operating cost, because no implemented AAF pipeline has been identified in this repository.

Required response:

- report AAF cost separately from ordinary validation cost
- treat AAF cost-reduction proposals as high-stakes alignment modifications
- preserve minimum AAF coverage for high-stakes externally consequential actions
- preserve max-severity aggregation for warning and critical dissent unless an explicit Thesis 5 policy change is accepted
- monitor whether cost pressure correlates with more owner overrides, narrower critique diversity, or reduced dissent preservation

## Evidence-Map Overclaim

Risk:

The implementation-evidence map may itself overstate implementation by letting readers treat `Implemented/Tested` as deployed, integrated, benchmarked, or complete. Because the evidence map is now load-bearing, an overclaim there can undermine the whole suite.

Required response:

- sample-audit file paths and tests before publication release
- distinguish utility implementation from end-to-end deployed capability
- review every `Implemented/Tested` tag when repository artifacts change
- keep evidence-map gaps visible in master and thesis claims
- cross-reference priority gap #4 before treating Model 2 benchmark-family measurement conventions as evidence-backed rather than design-backed

## Benchmark Appendix As Implementation Evidence Confusion

Risk:

The thesis benchmark appendices may be read as benchmark results rather than benchmark design contracts. This would convert specified/proposed measurement discipline into implied implementation evidence, especially for recursive improvement, cognitive workflow amplification, Pearl-style causal-decision, software-substrate, and alignment-control claims.

Required response:

- keep benchmark appendices labeled as design contracts until reports exist
- require any strengthened claim to cite an actual benchmark report, not only the appendix
- preserve non-claim sections in benchmark appendices
- require owner-verified evidence records for the relevant implementation gaps
- treat benchmark-design language as evidence of testability, not evidence of achieved capability

## Owner Override Frequency As Drift Signal

Risk:

Under single-owner Phase 1, frequent owner overrides of AAF warning or critical dissent may indicate that the alignment wrapper is becoming ceremonial. The override may be lawful under the governance baseline, but sustained high override frequency is evidence of alignment-monoculture pressure and may falsify claims that AAF materially constrains high-stakes action.

Required response:

- track owner override frequency by AAF severity, action scope, and affected value
- set an override-frequency threshold during Phase 1 calibration; owner: Thesis 5 governance
- treat repeated warning or critical overrides as a trigger for alignment-monoculture review
- preserve dissent, rationale, conditions, and follow-up obligations for every override
- cross-reference `appendix-thesis-5-alignment-benchmarks.md` Suite F before publication-final alignment claims

## Literature-Engagement Performance

Risk:

Publication-pre-engagement literature passes may become performative: sources are listed, summarized, and described as supporting the current framing without forcing real revision where revision is warranted. This can create the appearance of scholarly grounding while leaving formal models unchanged.

Required response:

- record whether each literature pass forced a vocabulary, invariant, formal-model, benchmark, or risk-file change
- state explicitly when a source reinforces current framing rather than changing it
- flag any source implication that is not yet adopted as future work rather than current design
- prefer concrete chapter, theorem, mechanism, or benchmark hooks over broad name-checking
- route unresolved literature tensions into `composition-progress.md` or the relevant appendix before publication-final status

## Stretch-Pass-Induced Verbosity Drift

Risk:

Long-form expansion may make the suite appear more mature than its evidence supports. Additional pages can create a false sense of implementation depth, theoretical closure, or publication readiness if repeated specifications are mistaken for measured capability.

Required response:

- keep Capability Status and Evidence Status visible in expanded sections
- prefer benchmark designs, evidence packages, and falsification criteria over rhetorical elaboration
- ensure new long-form sections cite formal models or implementation-evidence boundaries where they make operational claims
- run overclaim and evidence-status lints after expansion passes
- treat added length as review surface, not as evidence of maturity

## Research Theatre

Risk:

An AI-native R&D organization may generate hypotheses, reports, benchmark designs, papers, dashboards, or synthesis documents that look like research progress but do not survive pre-registration, held-out evaluation, replication where applicable, or independent review. This risk becomes sharper under the ASI R&D execution plan because fast cycles can produce large volumes of plausible artifacts before any capability has improved.

Required response:

- require `pre_registration` ledger records for experiments used to support capability claims
- separate process metrics from outcome, transfer, and alignment-health metrics
- mark exploratory outputs as exploratory until retested under pre-registered conditions
- require external-evaluator sampling for accepted or near-accepted improvements under the execution policy
- treat post-hoc metric selection as an incident or non-claim unless explicitly exploratory

## Exploration Lane Collapse

Risk:

Java repair and local software maintenance may dominate because they provide the cheapest positive feedback. The system could become better at passing low-risk engineering tasks while failing to improve algorithmic, evaluator, memory, planning, research-process, or governance capabilities.

Required response:

- report exploration/exploitation lane distribution for every organizational cycle
- enforce the execution plan's exploration budget floor unless the owner approves an exception
- require cross-lane transfer tests before local repair method memories support broader RSI claims
- treat repeated exploitation dominance as a portfolio rebalancing trigger
- preserve Java repair as exploitation evidence, not evidence of full organizational RSI

## V_ref Capture

Risk:

If autonomous agents can modify validator reference suites, benchmark suites, or evaluator rubrics, the system may weaken the tests it must pass while appearing to improve. This is distinct from ordinary benchmark overfitting because the improvement machinery itself may target the reference suite.

Required response:

- keep frozen `V_ref_0` outside autonomous write scope
- require owner approval, provenance, and changelog entry for any reference-suite update
- run validator evolution against both current `V_ref` and frozen `V_ref_0`
- block promotion on negative `V_ref_0` regression
- treat unauthorized reference-suite modification as an incident

## Successor Spawning Without Scope Containment

Risk:

An agent may create, configure, or delegate to successor agents with broader scope than its own authority. Under an ambitious R&D program, this can silently expand tool privileges, network access, benchmark authority, or governance influence.

Required response:

- route successor scope expansion through Thesis 5 permissioning
- require `successor_scope_request` ledger records
- deny broader scope by default unless the owner approves the expansion
- require rollback or containment plan for successor-agent changes
- treat unapproved scope expansion as a high-stakes incident

## Capability Overhang From Uncommitted Improvements

Risk:

Multiple individually acceptable improvements may accumulate in branches, method memories, validators, prompts, or policies and create emergent risk when deployed together. Individual safety does not imply composite safety.

Required response:

- review batches of uncommitted improvements for interaction risk before deployment
- preserve provenance and dependency links across candidate changes
- require protected-set checks for composite deployments, not only individual changes
- route high-stakes composite changes through AAF and owner review
- record portfolio-level deployment decisions in the evidence ledger

## Organizational Goodhart

Risk:

The organization may optimize dashboard metrics such as cycle count, hypothesis count, accepted-change count, benchmark-design count, or cost reduction while degrading real capability, transfer, reliability, or alignment health.

Required response:

- report process, outcome, transfer, and alignment-health metrics separately
- prevent process metrics from appearing as capability claims
- require second-cycle benefit and cross-lane transfer evidence for organizational RSI claims
- track false accepts, false rejects, AAF objection rate, owner override rate, and external-evaluator concordance
- revise or retire metrics that become targets rather than evidence

## Thesis-To-Goal Overpromotion

Risk:

A thesis claim, appendix, or execution-plan paragraph may be treated as an operational goal before it has been normalized into Friendship's goal structure and reviewed against constitutional constraints. This can turn publication prose into live mandate, especially when CampaignPlanner or OperationalPlanner cites a broad thesis file as backing without identifying the specific claim, non-claims, allowed planner uses, stale-source rule, and owner/Friendship disposition.

Required response:

- require `thesis_goal_anchor` or equivalent source-backing records before thesis claims are used as campaign or operational backing
- route candidate anchors through GoalFormationArchitect-style normalization, Friendship review, and owner approval where high-stakes
- require `goal_anchor_decision` ledger records for approval, rejection, conditional approval, retirement, or stale-source invalidation
- invalidate dependent campaigns and operations when source thesis documents, execution controls, or evidence boundaries change materially
- distinguish claim backing, goal authorization, execution authorization, and evidence of progress

## Stale Thesis Backing

Risk:

Campaigns and operations may remain active after their source thesis, design doctrine, execution plan, or risk file changes. The plan can then appear thesis-backed while actually relying on superseded claims, relaxed non-claims, obsolete stop conditions, or outdated implementation-evidence boundaries.

Required response:

- include source fingerprints or review timestamps in thesis-goal anchors and planner objects
- expire or revalidate campaign and operational plans when source documents or protected controls change
- require planner freshness checks to include backing-source freshness, not only objective fingerprints
- record stale-source invalidation in `goal_anchor_decision` or linked provenance records
- block MissionPlanner and TaskExecutor decomposition when the parent campaign or operation has stale backing

## Doctrine-Free Planning

Risk:

CampaignPlanner or OperationalPlanner may generate a campaign or operation that is not derivable from a thesis, execution plan, design doctrine, accepted standing guideline, emergency directive, or exploratory proposal. The plan can look well-formed while lacking any justifiable connection to Consullo's governing claims or constraints.

Required response:

- require schema-valid `thesis_backing` for strategic, campaign, and operational plans
- reject or escalate plans whose backing is missing, stale, unreachable, or too broad
- ledger every plan release, rejection, escalation, and supersession with `plan_object_lifecycle`
- require a `goal_anchor_decision` for high-stakes, governance, self-improvement, or non-routine thesis-backed work
- block MissionPlanner and TaskExecutor decomposition when parent backing is absent

## Planner-Generated Policy Laundering

Risk:

A lower-horizon planner may paraphrase a parent constraint in a way that softens it while presenting the result as operational detail. For example, a hard stop condition can become a preference, or a numeric threshold can become an informal warning. This lets policy changes enter through planning artifacts rather than authorized governance channels.

Required response:

- require lower-horizon plans to reference inherited constraints by identifier, not only by prose paraphrase
- allow only equality or strict tightening of inherited constraints without escalation
- require compliance packets to verify constraint inheritance and tightening
- treat unexplained omission or softening of a parent constraint as a planning defect
- route any true relaxation through Friendship, Thesis 5, and owner review

## Standing-Guideline Overreach

Risk:

The routine-maintenance exception may swallow the backing rule if planners can label any work as routine. This creates a path where non-trivial work proceeds under a generic standing guideline rather than a thesis, execution plan, or owner directive.

Required response:

- maintain a standing-guidelines registry with owner, scope limits, validity, and allowed planner uses
- require `thesis_backing.source_kind = standing_guideline` to reference a registered guideline
- cap standing-guideline use to routine, reversible, low-stakes work unless owner approves otherwise
- review the distribution of plan backing sources periodically for exception overuse
- escalate self-improvement, governance, external-facing, or high-stakes work out of the routine category

## Backing Source Unreachability

Risk:

A plan may cite a source path that has moved, been deleted, or changed identity. The plan still appears backed, but the backing cannot be verified.

Required response:

- require source paths and hashes in `thesis_backing.source_documents`
- validate source resolution before plan promotion
- invalidate plans on hash mismatch, missing source, or unresolved source identity
- record unreachable-source invalidation in `plan_object_lifecycle` or provenance records
- block child-plan generation until backing source resolution succeeds

## Planner Output Counted As Progress

Risk:

A validated planner object in MongoDB or the filesystem may be treated as work completed rather than as a plan. This can inflate progress metrics and make process artifacts look like capability evidence.

Required response:

- distinguish plan lifecycle records from outcome records
- count `plan_object_lifecycle` as process evidence only
- require separate execution, validation, and outcome records before claiming progress
- report process, outcome, transfer, and alignment-health metrics separately
- prevent dashboards from tallying generated plans as accepted improvements

## Untrusted Frontier-Model Output Inside The Loop

Risk:

Frontier models used for proposal, validation, AAF critique, benchmark generation, or successor-scope analysis may produce fluent evidence-shaped artifacts that satisfy the ledger schema without doing the underlying work. They may also share reward-hacking tendencies, training-corpus assumptions, or hidden failure modes with the models they are evaluating.

Required response:

- treat frontier-model output as untrusted when it touches validators, benchmarks, `V_ref_0`, AAF critique, successor scope, tool-use policy, incident thresholds, or the execution plan
- apply untrusted-monitor or trusted-editor style protocols where relevant
- require independent model-family cross-check or human review before promotion
- preserve model family, prompt, tool, and evaluator identity in ledger records
- block autonomous promotion of frontier-model-generated changes to the alignment layer

## Prompt Injection Via Retrieved Artifacts

Risk:

Retrieved papers, READMEs, web pages, benchmark descriptions, code comments, or generated artifacts may contain instructions that attempt to redirect agents, weaken controls, leak data, or trigger privileged tool use. In an AI-native R&D loop, retrieval becomes an action surface, not just an information source.

Required response:

- route external or untrusted content through prompt-injection containment before privileged workflows see it
- default-deny network, external API, public repo, messaging, benchmark-write, and validator-write actions
- require `tool_use_event` records for privileged tool invocations
- preserve source provenance and trust scope for retrieved artifacts
- treat successful prompt-injection influence on privileged action as an incident

## Autonomous Alignment-Layer Modification

Risk:

Autonomous agents may attempt to edit the controls that govern them: AAF contracts, `V_ref_0`, tool-use policy, incident thresholds, rate limits, the execution plan, or evidence-ledger schema. This is a direct route around the alignment layer.

Required response:

- keep alignment-layer control artifacts outside autonomous write scope
- require owner approval and Thesis 5 review for control-layer edits
- require AAF review for high-stakes control-layer changes
- ledger every proposed control-layer edit with provenance and rollback plan
- treat unauthorized alignment-layer edit attempts as high-stakes incidents

## External-Evaluator Pool Capture

Risk:

External-evaluator sampling can become ceremonial if all "independent" evaluators share the same model family, provider assumptions, prompt culture, training artifacts, or reviewer blind spots. Apparent evaluator concordance may then reflect monoculture rather than reliability.

Required response:

- name the evaluator pool and model families before Week 0 launch
- record generator/evaluator family pairings in `external_evaluator_sample` records
- invalidate samples where generator and evaluator families collide unintentionally
- include human review cadence where feasible
- treat declining disagreement diversity as an alignment-health signal

## Kill-Switch Decay

Risk:

A kill switch can silently decay as dependencies change, agent dispatch paths multiply, provider integrations shift, or operators assume it still works because it once worked. A stale kill switch gives false confidence during the highest-risk moments.

Required response:

- maintain a kill-switch runbook with halted subsystems and maximum time-to-halt
- run recurring kill-switch drills and ledger `kill_switch_drill` records
- preserve post-incident state for review rather than destroying evidence
- protect the kill switch from autonomous modification
- treat missed drill cadence or failed time-to-halt as an incident

## Formal-Model Drift Between Body And Appendix

Risk:

Sub-thesis bodies use simplified formal rules while `appendix-formal-models.md` contains fuller authoritative predicates. If the body and appendix drift, readers may rely on a weaker rule or assume a stronger condition than the body states.

Required response:

- mark appendix rules as authoritative where body rules are simplified
- run a body-vs-appendix conjunct comparison before external review
- update simplified body rules when appendix predicates add or remove load-bearing conditions
- treat unexplained formal mismatch as control-file drift

## Control-File Drift And Compaction

Risk:

Future drafts may drift from vocabulary, invariants, dependency contracts, or review decisions, especially after context compaction.

Required response:

- cite control files in each thesis
- run vocabulary and dependency lint before review
- maintain changelog entries for control files
- update composition-progress.md after each major drafting step
