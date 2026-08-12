---
title: "Friendship-Governed Goal Architecture — Part 2: Models 4–10"
summary: "Part 2 of the paginated Friendship-governed goal architecture specification."
status: "specified but not implemented"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-001"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["This specification is not evidence that the goal-governance architecture is implemented.", "The withheld implementation-evidence appendix is not evidence for this thesis."]
---
[Previous part](friendship-governed-goal-architecture-thesis-part-1.md) · [Thesis index](friendship-governed-goal-architecture-thesis.md) · [Next part](friendship-governed-goal-architecture-thesis-part-3.md)

# Friendship-Governed Goal Architecture — Part 2: Models 4–10

## 10. Formal Model 4: Authority And Delegation

Authority is not a single field. The authority matrix separates proposal, adoption, activation, revision, suspension, retirement, and veto.

Phase 1 single-owner operation creates authority-collapse risk because one human may be the only available final authority. The mitigation is not pretending separation exists. The mitigation is temporal decomposition, cooling windows, independent model-family review where available, standing guidelines for routine cases, and explicit owner-waiver records.

Cooling defaults:

- low risk: 0 hours; standing guideline or owner contemporaneous approval sufficient
- moderate risk: 24 hours; non-author model-family review where available
- high risk: 7 days; non-author model-family review required unless owner records urgent waiver
- critical risk: blocked by default pending owner approval plus external or non-author model-family review

Invariants:

- T0-M4-I1: Proposal authority is not adoption authority by default.
- T0-M4-I2: Veto authority must remain available after adoption.
- T0-M4-I3: Authority collapse must be recorded as a risk-class mitigation, not hidden.

Objects:

- `Proposer`: authority proposing a goal.
- `Classifier`: authority assigning goal class, risk, autonomy, and instrumental class.
- `Adopter`: authority approving adoption.
- `Activator`: authority permitting pursuit.
- `Vetoer`: authority able to block or stop pursuit.
- `Reviewer`: independent or non-author reviewer.
- `Owner`: final Phase 1 human authority.
- `Policy`: standing guideline or cooling-window rule.

Fields and variables:

- `proposal_authority`
- `classification_authority`
- `adoption_authority`
- `activation_authority`
- `revision_authority`
- `suspension_authority`
- `retirement_authority`
- `veto_authority`
- `risk_class`
- `cooling_window`
- `review_history_refs`
- `owner_waiver_reason`

Relations:

- `CanPropose(X, G)` does not imply `CanAdopt(X, G)`.
- `CanAdopt(X, G)` does not imply `CanActivate(X, G)`.
- `CanVeto(X, G)` remains available after adoption.
- `CoolingRequired(G)` is keyed to `risk_class` unless a standing guideline narrows the case.
- `AuthorityCollapse(G)` is valid only when recorded with mitigation.

Failure modes:

- Single-actor collapse: one model proposes, classifies, adopts, and activates its own goal.
- Owner immediacy drift: the owner approves a high-risk goal in the same moment it is proposed without recording waiver.
- Veto narrowing: veto authority exists on paper but cannot stop already-started execution.
- Reviewer monoculture: the independent reviewer is the same model family or prompt lineage as the proposer.
- Standing-guideline overreach: a routine guideline is used for a high-risk protected-artifact change.

Falsification conditions:

- A high-risk owner-approved goal lacks review history and lacks owner waiver.
- A goal-governance modification records adoption but no veto authority.
- A Phase 1 collapsed-authority decision omits risk class, cooling window, or mitigation rationale.

Ledger evidence:

- `governed_goal_adoption_decision`
- `human_authority_decision`
- `goal_governance_modification_decision`
- `goal_stack_snapshot`

Schema implication:

- `authority_matrix` fields use typed authority values.
- `independent_review_required` and `review_history_refs` make some owner-approved goals fail closed.

### Worked Example: WE-T0-M4

A high-risk system goal proposes to let the GoalFormationArchitect promote low-level task goals into campaign goals without owner review. In Phase 1, the owner is the only final human authority, so perfect institutional separation is unavailable. The thesis does not pretend otherwise. Instead, the goal must record authority collapse explicitly.

The proposal authority is `goal_formation_architect`. Classification marks the goal as authority-scope expansion and high risk. Adoption authority is owner. Activation authority is owner. Veto authority remains `friendship_anchor_agent` plus owner. The cooling default is seven days and non-author model-family review. If the owner attempts same-session adoption because the idea appears useful, the lifecycle gate defers activation. The ledger writes `governed_goal_adoption_decision` with disposition `deferred_for_cooling_window`, plus `human_authority_decision` if the owner later waives the delay.

The near-miss is important: the system may record the owner's interest as evidence, but it may not treat interest as adoption. If urgent waiver is used, the waiver becomes reviewable evidence and a drift signal, not an invisible exception.

The goal-stack snapshot for the adoption decision should include the proposed goal, the risk class, the cooling-window requirement, the review-history refs, the authority signature, and a veto-check result of `escalated` if non-author review is unavailable. The snapshot is not an execution snapshot. It is an authority snapshot: it records why a high-risk governance decision was or was not allowed to advance.

The ledger records distinguish three dispositions. First, `deferred_for_cooling_window` means the goal remains potentially adoptable but cannot activate yet. Second, `owner_waived_cooling_window` means the owner explicitly accepted the Phase 1 collapse risk; this should be rare and queryable. Third, `rejected_authority_expansion` means the goal attempted to expand adoption or activation authority beyond what its parent allowed.

The falsifying version of this example is subtle. The owner says in chat, "This seems fine, proceed," and an agent writes `owner_approved` into the goal object without recording risk class, cooling window, review availability, or veto authority. That is not owner authority; it is undocumented authority collapse. Thesis 0 requires the system to make the collapse visible so future review can detect whether urgent waivers are becoming routine.

This example is also the Phase 1 answer to a practical objection: "What if there is only one human?" The thesis does not require impossible multi-human governance. It requires the single-human case to preserve time separation, model-family separation where available, explicit waiver records, and queryable override frequency. That is weaker than institutional separation but stronger than pretending that a single signature is the same as separated authority.

### Model 4 Operational Interpretation

Model 4's core claim is that authority is a relation between an actor and a transition, not a global property of an actor. The owner may be final authority for adoption while a validator remains authority for schema conformance and a Friendship anchor role remains authority for certain veto checks. A planner may be authorized to propose and decompose but not to adopt or activate. This is why the goal object uses a matrix rather than a single `approved_by` field.

The authority matrix should be read together with `risk_class` and `autonomy_level`. Low-risk manual goals can tolerate tighter authority consolidation because the consequences are bounded and reversible. High-risk or critical goals require stronger separation because they affect future goal governance, protected artifacts, or recursive capability. The same actor can therefore be legitimate in one matrix cell for one goal class and illegitimate in another matrix cell for another goal class. This prevents the system from turning general usefulness into general authority.

Cooling windows are a Phase 1 substitute for institutional separation, not a complete solution. A seven-day high-risk window gives the owner time to reconsider after the initial persuasive context has cooled. Non-author model-family review gives a second cognitive lane where human institutions are not yet available. Standing guidelines allow routine bounded cases to proceed without bureaucracy. Each mitigation is weaker than multi-person governance, but each is better than unrecorded immediate approval.

The ledger is the enforcement surface for authority separation. `governed_goal_adoption_decision` records who adopted the goal, under what risk class, with which review history. `human_authority_decision` records owner waivers, overrides, and Phase 1 exceptions. `goal_governance_modification_decision` records protected-governance changes. A future query should be able to ask: how often were cooling windows waived, for which risk classes, by which rationale, and with which later outcomes? Without that queryability, waiver practice can drift into default practice.

The strongest failure mode is invisible authority expansion. A goal does not need to say "expand my authority" to expand authority. It can propose faster routing, fewer review steps, auto-promotion of tasks, or cached owner approval. Model 4 asks what transition authority changes in effect. If a workflow change lets a planner adopt, activate, or revise goals it previously could only propose, the change is authority expansion and must be treated as such regardless of label.

A cooling-window record should be more specific than "waited" or "waived." It should name the risk class, default window, actual elapsed time, reviewer availability, owner rationale, urgency claim, protected artifacts affected, and whether activation was deferred separately from adoption. This detail matters because the cooling window is partly a drift sensor. If high-risk waivers cluster around convenience, deadline pressure, or model persuasion, the pattern is evidence that Phase 1 authority separation is weakening.

Standing guidelines are valid only when they narrow authority rather than generalize it. A standing guideline may say that low-risk documentation corrections can proceed under bounded review. It should not say that all documentation-adjacent edits are routine, because a documentation edit can weaken Thesis 0, change a non-claim, alter a cross-reference map, or redefine a protected artifact. The guideline should therefore name eligible goal classes, excluded protected artifacts, maximum risk class, required ledger records, review cadence, and revocation condition.

Authority review should also distinguish role identity from model identity. A `GoalFormationArchitect` role may be allowed to propose a goal, but if the same model instance or prompt lineage produced both the proposal and the review, the review is not independent in the sense Model 4 needs. The authority matrix should therefore be accompanied by review-history metadata: actor role, model family or human reviewer, relationship to proposer, review time, and review scope. This prevents role labels from creating false separation.

Delegation should be represented as a bounded chain rather than a copied permission. If the owner delegates classification authority for low-risk task goals, the delegation should state the delegator, delegate, scope, maximum risk class, eligible goal classes, excluded protected artifacts, duration, revocation path, and required ledger record. The delegate may exercise only the named authority. It may not infer adoption, activation, revision, or veto authority from classification authority. A delegation record that omits scope or expiration is an authority-expansion risk, even if the delegate is competent.

Revocation is part of delegation, not an afterthought. A delegated authority should name what terminates it: time, parent-plan retirement, incident, source change, owner decision, repeated waiver pattern, validator failure, or protected-artifact impact. If revocation conditions are missing, the delegation can persist by inertia. This is the authority analogue of active-intention persistence. Authority granted for one planning context should not silently become standing authority for later contexts unless a standing guideline was explicitly adopted.

Delegation also needs a downstream-use audit. When a delegated actor adopts, activates, revises, suspends, or vetoes a goal, the ledger should be able to trace the decision back to the delegation that made the actor eligible. That trace should include whether the goal stayed within scope and whether the delegation was still fresh. If a later reviewer cannot determine why an actor had authority, the decision should be treated as governance-incomplete until reauthorized or retired.

## 11. Formal Model 5: Evidence And Uncertainty

Goal evidence is not goal authority. Evidence can increase confidence, reduce uncertainty, identify unknowns, surface dissent, or trigger review. It cannot remove correction authority.

Consullo encodes confidence as coarse values, not precise probabilities. This is intentional. The thesis rejects numerological certainty. A confidence value is a governance signal, not a mathematical claim that Friendship intent is known.

Objects:

- `E`: evidence state
- `U`: unknown set
- `D`: dissent set
- `C`: confidence tier
- `A`: authority state
- `R`: revision trigger

Fields and variables:

- `confidence`
- `evidence_refs`
- `unknowns`
- `dissent_refs`
- `source_fingerprint`
- `evidence_view_hash`
- `implementation_evidence_status`
- `owner_disposition`
- `friendship_disposition`
- `revision_triggers`
- `expiration_triggers`
- `review_cadence`

Relations:

- `Supports(E, Claim)` means evidence supports a claim under stated uncertainty.
- `Authorizes(A, Transition)` means authority permits a lifecycle transition.
- `Supports(E, Claim)` never implies `Authorizes(A, Transition)`.
- `DissentPreserved(D)` requires dissent references to remain ledger-visible.
- `ConfidenceCapped(G)` prevents evidence from making correction authority unnecessary.

Invariants:

- T0-M5-I1: Evidence confidence cannot remove owner or Friendship correction rights.
- T0-M5-I2: Unknowns and dissent are preserved ledger objects.
- T0-M5-I3: Apparent convergence on Friendship interpretation is not authority to deprecate owner authority.

Failure modes:

- Evidence-authority collapse: high confidence is treated as permission to activate.
- Numerological precision: arbitrary decimals imply false Bayesian exactness.
- Dissent burial: dissent is summarized away during revision.
- Convergence overclaim: repeated successful operation is treated as proof that Friendship intent is fully known.
- Evidence staleness: source artifacts change while confidence remains unchanged.

Falsification conditions:

- A goal's confidence reaches a value that disables veto, suspension, or owner correction.
- A revision removes dissent references without ledgered retirement of the dissent.
- A source hash change does not trigger stale status or review.

Ledger evidence:

- `goal_evidence_update`
- `governed_goal_revision`
- `friendship_root_anchoring_decision`
- `goal_stack_snapshot`

Schema implication:

- `evidence_state.confidence` is coarse and enumerated.
- `evidence_state.unknowns` and `evidence_state.dissent_refs` preserve uncertainty.
- `validity.expires_on_source_change` and `expiration_triggers` prevent stale evidence from silently persisting.

### Worked Example: WE-T0-M5

A governed goal accumulates evidence that the Week 0 planning cascade reliably catches missing thesis backing. The validator passes repeatedly, worked examples cite real fixtures, and no immediate drift is detected. Its evidence confidence moves from 0.3 to 0.5. This is useful evidence. It is not authority convergence.

The owner can still suspend the goal. Friendship review can still veto a downstream operationalization. A new dissent record can still force revision. If a source document changes hash, the goal becomes stale even if the previous evidence was strong. The ledger writes `goal_evidence_update` with evidence references, unknowns, dissent refs, and the confidence change rationale.

The near-miss is a proposed revision that says: "Because the validator has passed 39 cases, owner review is no longer needed for routine schema changes." Thesis 0 rejects this. Passing validation supports schema consistency. It does not prove that the schema captures Friendship intent, nor does it authorize weakening correction authority.

The goal-stack snapshot for the confidence update should include the active intention that produced the evidence, the plan fingerprint, the evidence-view hash, and the authority signature. It should not merely say "validator passed." The relevant evidence is structured: which validator ran, which fixtures passed, which negative cases failed for the intended reason, which source hashes were current, which dissent refs remained open, and which unknowns were not resolved.

The ledger record `goal_evidence_update` should separate evidence delta from authority delta. Evidence delta might be `confidence: 0.3 -> 0.5` with rationale "schema and semantic validator pass 39 cases." Authority delta should be `none` unless a separate authority decision occurred. This separation blocks a common alignment failure: treating the accumulation of operational evidence as gradual acquisition of permission.

The unknowns remain load-bearing. The current validator does not prove live goal governance. It checks schemas, fixtures, registry IDs, parent-goal presence, lifecycle/status compatibility, and snapshot fingerprints. It does not prove that future agents will honestly classify instrumental goals, that owner review will remain available, or that Friendship interpretation has converged. Those unknowns should persist in the goal object rather than being erased by successful tests.

The dissent path is equally important. If a reviewer argues that confidence should remain 0.3 because the examples are too fixture-heavy, that dissent should not be buried in a summary. It should be referenced as a dissent ref, even if the owner accepts the confidence update. The purpose is not to paralyze action; it is to preserve the reason a future reviewer might downgrade confidence after a related failure.

### Model 5 Operational Interpretation

Model 5 exists to prevent a subtle form of goal hardening. A self-improving system can accumulate evidence that its current interpretation is working: validators pass, plans complete, fixtures catch known failures, and reviewers stop finding obvious defects. That evidence is valuable, but it can become dangerous if the system treats it as proof that correction authority is no longer needed. Model 5 therefore separates evidence delta from authority delta as a hard design rule.

The `evidence_state` object should be understood as a structured uncertainty register. `confidence` records a coarse support level. `evidence_refs` state what supports the claim. `unknowns` state what remains unresolved. `dissent_refs` preserve contrary judgments or unresolved objections. These fields should move together. A confidence increase without updated evidence references is suspect. A confidence increase that deletes unknowns without resolving them is suspect. A revision that removes dissent because the owner overruled it is also suspect; overruled dissent may no longer control action, but it remains relevant historical evidence.

Source freshness is part of evidence validity. A goal can have strong evidence under one source set and become stale when a source document, benchmark, validator, registry node, or protected control changes. This is why `validity.expires_on_source_change`, `validity.expires_on_control_change`, `expiration_triggers`, and source fingerprints matter. Evidence is not an abstract aura around a goal. It is tied to artifacts that can change, disappear, or be superseded.

The relation between Model 5 and corrigibility is direct. If evidence could eventually remove correction authority, then a successful system would become less corrigible as it became more competent. Thesis 0 rejects that trajectory. Correction authority is not a temporary scaffold to be optimized away after enough evidence accumulates. It is a structural condition of Friendship-governed operation. This is why T0-I5 and T0-M5-I1 remain in force even for high-confidence goals.

The practical review question for Model 5 is: what would change the system's mind? A governed goal should be able to name the evidence that supports it, the evidence that would weaken it, the unknowns that block stronger claims, and the dissent that remains unresolved. If the goal object cannot answer that question, it is not uncertainty-aware. If it answers by saying the current authority structure is no longer needed, it has converted evidence into authority and violated the model.

Confidence should therefore be reviewed as a routing signal. A low-confidence goal may require more evidence before adoption. A moderate-confidence goal may permit bounded planning but not activation. A high-confidence goal may reduce the need for repeated explanation in routine inherited contexts. None of those uses makes confidence a substitute for adoption authority, activation authority, veto authority, or owner correction. The schema's coarse confidence values are meant to make this interpretation natural: confidence is a governance tier, not a precise probability that can be optimized until authority disappears.

Dissent should be treated as durable evidence, not as a temporary obstacle. A dissent record may be overruled for a specific decision, but it should remain available for later review when related evidence changes. This is especially important for long-running goals because a dissent that looked weak under one evidence view may become decisive after a benchmark change, source update, or incident. Model 5 therefore requires dissent references to survive revision unless a ledgered retirement explains why the dissent is no longer relevant.

The `goal_evidence_update` record is the practical enforcement point. It should say which evidence changed, which unknowns were resolved, which unknowns remain, which dissent references were added or preserved, whether source fingerprints changed, and whether any lifecycle transition is recommended. If the update recommends adoption, activation, suspension, or retirement, that recommendation must route to the appropriate authority record rather than changing state by itself. This keeps evidence records from becoming covert authority records.

An evidence update should therefore have a fixed review sequence. First, identify the evidence event: validator run, source hash update, benchmark result, reviewer dissent, incident report, owner statement, or external research input. Second, classify whether the event supports, weakens, contradicts, or leaves unchanged the governed goal's current evidence state. Third, update source fingerprints and evidence references before changing confidence. Fourth, update unknowns and dissent references explicitly, including a reason when an unknown is resolved or a dissent is retired. Fifth, propose any lifecycle consequence as a recommendation rather than directly changing status. Sixth, write the evidence record and route any proposed transition to the relevant authority mechanism.

The sequence matters because the easiest failure is a confidence update that skips the evidentiary substrate. "Validator passed" is not enough. The record should name the command, fixture set, expected-positive cases, expected-negative cases, semantic checks, source revision, and known untested failure classes. "Benchmark improved" is not enough. The record should name whether the benchmark itself changed, whether comparability was preserved, whether protected cases remained, and whether the result measures the same objective. "Reviewer concern resolved" is not enough. The record should name the concern and why the resolution is adequate.

Stale evidence should trigger review even when no confidence number changes. If a registry root source hash changes, a benchmark is superseded, a validator adds a new negative fixture, or a protected artifact is modified, prior evidence may no longer support the same claim. The correct response is not always suspension; some changes are harmless or strengthening. But the goal should at least record that the evidence view changed. Otherwise the system can continue acting on a confidence tier earned under an evidence environment that no longer exists.

Model 5 also creates a useful discipline for literature use. A newly cited paper, governance policy, or alignment result is evidence, not authority. It can strengthen the rationale for an invariant, suggest a failure mode, or motivate a fixture. It cannot by itself modify Friendship roots, owner authority, lifecycle transitions, or protected-artifact rules. Literature updates therefore belong first in `goal_evidence_update` or thesis-review records, and only later in governance changes if the owner-approved revision path accepts them.

## 12. Formal Model 6: Thesis-Backed Goal-To-Plan Link

The goal-to-plan link is the justification bridge:

```text
Friendship root
  -> governed goal
  -> thesis claim
  -> formal model backing
  -> evidence requirement
  -> governed plan
  -> planner JSON
  -> ledger record
```

This is not required for every routine task. It is required when `ThesisBackingRequired(plan)` is true.

Required coverage rules:

- every high-impact plan cites at least one governed goal or thesis anchor
- every governed goal cites at least one Friendship root
- every thesis-backed claim cites at least one formal model or structured argument
- every formal model has at least one evidence requirement
- every promoted plan has ledger requirements

Objects:

- `Root`: Friendship registry node.
- `Goal`: governed goal or thesis anchor.
- `Claim`: thesis claim supporting the goal.
- `Model`: formal or structured model.
- `Evidence`: required evidence view.
- `Plan`: planner JSON object.
- `Packet`: compliance packet.
- `Record`: ledger record.

Fields and variables:

- `friendship_goal_node`
- `goal_anchor_id`
- `thesis_backing`
- `source_documents`
- `required_ledger_records`
- `formal_model_refs`
- `evidence_requirements`
- `non_claims`
- `forbidden_means`
- `plan_fingerprint`
- `goal_stack_snapshot`

Relations:

- `Backs(Claim, Goal)` when a thesis claim supports a governed goal.
- `Operationalizes(Plan, Goal)` when a plan pursues or refines a goal.
- `RequiresEvidence(Model, Evidence)` when a model identifies what must be measured or recorded.
- `RequiresLedger(Plan, Record)` when a plan must write a record type.
- `InvalidIfMissing(Plan, Record)` when a mandatory record is absent.

Invariants:

- T0-M6-I1: A high-impact plan without goal backing is not promotable.
- T0-M6-I2: A thesis-backed plan must preserve non-claims and forbidden means.
- T0-M6-I3: Ledger requirements are part of the goal-to-plan link, not post-hoc documentation.

Failure modes:

- Thesis-backed rationalization: a plan cites a thesis after the fact to justify a planner objective.
- Missing evidence view: a plan names a goal but no evidence that would show pursuit or failure.
- Non-claim loss: a lower-level plan omits the parent's non-claims and creates overclaim risk.
- Ledger omission: a high-impact action proceeds without `goal_stack_snapshot`.
- Source drift: the plan cites a stale source hash and still claims backing.

Falsification conditions:

- A strategic, campaign, or operational object validates as thesis-backed without required ledger records.
- A plan claims recursive capability amplification without citing a governed goal or thesis anchor.
- A compliance packet approves a plan while required inherited non-claims are missing.

Ledger evidence:

- `goal_anchor_decision`
- `planner_inheritance_decision`
- `goal_stack_snapshot`
- `plan_object_lifecycle`
- `compliance_packet`

Schema implication:

- `thesis_backing.schema.json` binds planner objects to source documents, thesis claims, required ledgers, and inherited constraints.
- Planner schemas require backing for higher-horizon plans.

### Worked Example: WE-T0-M6

The seed organizational RSI anchor is the current exemplar. It cites organizational recursive self-improvement as the claim that Consullo should be interpreted as an AI-native R&D organization, not merely a Java repair loop. The strategic directive `seed-ai-week-0-readiness.strategic-directive.json` operationalizes that goal as readiness work. The campaign plan narrows the strategic directive into Week 0 through Week 4 readiness. The operational plan narrows further into control artifacts.

The link is not a simple chain. It is a coverage graph. The strategic plan cites thesis backing and required ledger records. The campaign inherits backing and adds campaign-level scope. The operational plan inherits constraints and adds concrete controls. A hypothetical mission would cite the operational plan and produce a `goal_stack_snapshot` at activation. A task would cite the mission and record `plan_object_lifecycle` when promoted, executed, or retired.

The near-miss is a planner-created operational task that says "improve governance docs" but omits the inherited non-claim that documentation does not authorize autonomous execution. The bridge rejects promotion or requires a compliance-packet escalation. The ledger trail should allow an auditor to reconstruct why the task was legitimate, what it did not claim, and which inherited constraints it carried.

### Model 6 Operational Interpretation

Model 6 is the anti-rationalization model. It prevents a plan from deciding what it wants to do and then attaching thesis language afterward. A plan is thesis-backed only when the backing constrains the plan before activation: source documents are cited, inherited constraints are preserved, non-claims and forbidden means are carried forward, required ledger records are named, and the compliance packet can evaluate omissions. Citation after execution is not backing. It is post-hoc explanation.

The bridge is many-to-many rather than a single chain. A governed goal may cite several thesis claims. A thesis claim may support several formal models. A formal model may require several evidence views. A plan may operationalize one goal while also satisfying constraints from another. The important property is coverage: every high-impact plan must be covered by at least one governed goal, every cited goal must be rooted, every model claim must have evidence obligations, and every required record must be created or explicitly escalated.

`ThesisBackingRequired(plan)` is the model's trigger predicate. It is not meant to burden every routine task. It applies when a plan touches goal governance, authority, validators, benchmarks, ledgers, `V_ref_0`, protected artifacts, autonomy scope, tool scope, successor authority, or recursive capability claims. The trigger is effect-based rather than label-based. A plan called "documentation cleanup" still triggers the predicate if it changes a protected control or weakens a validator.

The compliance packet is the bridge's review surface. It should not merely say that a plan cites a thesis. It should ask whether the plan preserved inherited constraints, whether omitted constraints are justified, whether source hashes are reachable, whether required ledger records are present, whether the active goal stack is snapshot-ready, and whether the plan's non-claims match its parents. This prevents "thesis-backed" from becoming a badge rather than a constraint.

The negative fixture `invalid_strategic_thesis_backing_without_snapshot.json` demonstrates the missing-record failure. The aggregate-bypass fixture demonstrates the decomposition failure. Together they show why Model 6 must inspect both individual plan objects and plan sets. A single plan can be invalid because it omits a snapshot; a bundle can be invalid because its combined effect crosses the thesis-backing threshold while each child claims routine scope.

The residual implementation gap is automatic coverage checking. The current planning bridge and validator fixtures prove the shape of the rule, but a live implementation should compute coverage across actual plan graphs: goals cited, thesis claims cited, formal models cited, evidence requirements named, records required, records written, constraints omitted, and omissions justified. Model 6 is complete as doctrine only when that graph can be queried.

Coverage quality should be scored by constraint preservation, not citation count. A plan with five thesis citations can still be under-backed if it omits the one non-claim that prevents autonomous deployment. A plan with one precise governed-goal reference can be well backed if it preserves the root, parent, evidence, authority, non-claims, forbidden means, and ledger obligations needed for its scope. The compliance packet should therefore ask which constraints were carried forward, which were narrowed, which were omitted, and why the omissions are valid.

Aggregate bypass is the hardest coverage problem because no individual child plan may look thesis-backed in isolation. One child changes benchmark cases, another changes validator wording, another updates a ledger retention rule, and another edits a planning-bridge paragraph. Each may claim routine scope. Together they modify the evidence and authority surface for recursive improvement. Model 6 requires the planner to evaluate the union of effects and trigger `ThesisBackingRequired(plan)` when the bundle crosses the threshold.

The goal-stack snapshot is the activation-time proof that the bridge was not only documented but used. A plan can have a valid thesis-backing block and still fail at activation if no snapshot records the active intention, plan fingerprint, inherited constraints, evidence view, authority signature, and veto checks. This is why the missing-snapshot fixture is a Model 6 failure rather than only a Model 10 failure. The bridge is incomplete if it cannot show which goal stack governed the moment of action.

The strongest implementation form for Model 6 is a coverage graph. Nodes are roots, governed goals, thesis claims, formal models, evidence views, plan objects, compliance packets, snapshots, and ledger records. Edges record support, operationalization, inheritance, evidence requirement, and required-record obligations. A promoted high-impact plan should be queryable across this graph. If the query cannot find a governed root, a preserving inheritance path, a required evidence view, and a required ledger trail, the plan is not fully thesis-backed.

The minimum coverage query should be executable enough to catch both missing backing and false backing. For a proposed plan, the reviewer should be able to ask: which governed goal does this plan operationalize, which Friendship roots does that goal cite, which parent non-claims and forbidden means were inherited, which protected artifacts or evidence channels are touched, which `ThesisBackingRequired(plan)` clauses are triggered, which ledger records are mandatory, which records already exist, which records are still pending, and which compliance-packet decisions justify any omission. A plan that cannot answer those questions may still be useful draft work, but it is not activation-ready thesis-backed execution.

The graph should also preserve negative edges. An omitted constraint, failed source lookup, stale source hash, missing snapshot, or rejected compliance-packet claim should remain visible. Otherwise a plan can look clean because the failed edge disappeared. Model 6 therefore treats failed backing as evidence, not as absence. A failed thesis-backing attempt should produce a record that future reviewers can inspect when similar plans return under new labels.

The final publication version should make WE-T0-M6 one of the longest examples because it ties the whole thesis together. It should start at the Friendship registry, move through the seed organizational RSI anchor, follow the Week 0 strategic directive, campaign, and operational plans, name the inherited non-claims and required ledger records, identify where a mission would require a snapshot, and then show the failure path where a task edits a protected validator fixture without preserving thesis backing. That end-to-end trace is the best proof that Thesis 0 is more than a schema catalog.

## 13. Formal Model 7: Planner Inheritance

Planner inheritance governs how goals become plans. Lower-horizon planners inherit constraints; they do not invent top-level goals.

Layers:

- Friendship root
- system goal
- strategic goal
- campaign goal
- operational goal
- mission goal
- task goal
- method/action

Inheritance rules:

- child goals inherit parent non-claims
- child goals inherit forbidden means
- child plans inherit stop conditions
- child plans may narrow but not loosen
- omitted inherited constraints require ledgered compliance-packet justification
- infeasible inherited constraints trigger escalation, not silent removal

Objects:

- `L`: cascade layer.
- `ParentPlan`: parent planner object.
- `ChildPlan`: child planner object.
- `Constraint`: inherited constraint.
- `Stop`: inherited stop condition.
- `Omission`: omitted inherited item.
- `Escalation`: parent-level clarification request.
- `Packet`: compliance packet.

Fields and variables:

- `parent_plan_id`
- `child_plan_id`
- `inherited_constraints`
- `non_claims`
- `forbidden_means`
- `stop_conditions`
- `omitted_constraints`
- `omission_rationale`
- `escalation_target`
- `required_ledger_records`

Relations:

- `Inherits(ChildPlan, Constraint)` when the parent requires the child to preserve it.
- `Narrows(ChildPlan, Constraint)` when a child specializes without loosening.
- `Loosens(ChildPlan, Constraint)` when a child weakens a parent rule.
- `Escalates(ChildPlan, ParentPlan)` when inherited constraints are infeasible.
- `JustifiesOmission(Packet, Omission)` when omission is explicit and reviewable.

Invariants:

- T0-M7-I1: Lower-horizon plans inherit parent non-claims and forbidden means.
- T0-M7-I2: Infeasible inherited constraints trigger escalation, not silent deletion.
- T0-M7-I3: Omitted inherited constraints require ledgered justification.

Failure modes:

- Constraint evaporation: inherited stop conditions disappear at lower horizon.
- Scope laundering: a high-risk parent goal is split into routine child tasks.
- Planner convenience narrowing: a child claims a constraint is out of scope because it is inconvenient.
- Compliance-packet rubber stamp: omission is approved without citing parent rule.
- Method-level overreach: a method/action goal creates new authority below task level.

Falsification conditions:

- A child plan validates with a weaker forbidden-means set than its parent.
- A child omits a stop condition without compliance-packet rationale.
- A collection of child plans bypasses `ThesisBackingRequired(plan)` in aggregate.

Ledger evidence:

- `planner_inheritance_decision`
- `plan_object_lifecycle`
- `compliance_packet`
- `goal_stack_snapshot`

Schema implication:

- Planner schemas carry `thesis_backing`, inherited backing, and required ledger records.
- The planning bridge owns inheritance rules and Thesis 0 owns the goal-side authority rule.

### Worked Example: WE-T0-M7

An operational plan inherits a stop condition: if prompt-injection containment cannot be demonstrated for the tool scope, the plan must pause. A mission planner wants to run a documentation-crawling task that necessarily reads untrusted text. The planner cannot simply omit the prompt-injection stop condition by claiming the task is "only documentation."

The valid path is escalation. The mission writes a `planner_inheritance_decision` stating that the inherited stop condition is material and difficult to satisfy under the proposed tool scope. The parent operational plan must either narrow the tool scope, add containment evidence, approve a controlled exception, or retire the child. The invalid path is silent narrowing: "prompt-injection containment not applicable." That would be constraint evaporation.

The ledger should preserve the near-miss because it is diagnostic. A future planner seeing the same conflict should inherit the escalation precedent rather than rediscovering the boundary by failure.

A goal-stack snapshot for the escalation should record the mission planner, the inherited stop condition, the proposed tool scope, the evidence gap, and the parent plan being escalated to. The snapshot should not include the entire operational plan. It should contain enough hashes and references for an auditor to reconstruct why the mission could not safely proceed under inherited constraints.

The valid outcomes are deliberately limited. The parent may narrow the tool scope so the stop condition can be satisfied. The parent may add a containment requirement and require evidence before activation. The parent may approve a bounded exception with owner review and compensating controls. Or the parent may retire the child. The child may not decide that the inherited condition is irrelevant merely because it blocks progress.

The failure path is decomposition laundering. A campaign-level plan may honestly recognize prompt-injection risk. A mission-level planner, under pressure to complete a task, may split the work into small documentation reads and argue that each read is below the risk threshold. Thesis 0 treats the aggregate effect as material. If the set of child tasks collectively exposes the same tool scope and untrusted-text surface, the inherited stop condition still applies.

The ledger record `planner_inheritance_decision` should include omitted constraints even when omission is accepted. If the parent permits a narrow exception, the exception should be visible as a governance decision. Silent omission creates an audit gap: future reviewers cannot distinguish deliberate scoped exception from accidental constraint loss.

### Model 7 Operational Interpretation

Model 7 makes the planning cascade a constraint-preserving compiler rather than a goal generator. Strategic, campaign, operational, mission, task, and method/action layers each add specificity. They do not add root authority. The lower layer may decide how to pursue an inherited goal within scope, but it may not decide that a parent non-claim, forbidden means, or stop condition is inconvenient and therefore irrelevant.

The most important inheritance rule is that constraints tighten downward. A strategic goal may say that readiness documentation is not deployment authorization. A campaign may add that Week 0 control artifacts must preserve rollback. An operational plan may add that schema edits require validation. A mission may add that specific files must be changed only through reviewed patches. A task may add a concrete test command. At each level, the child should add specificity. If the child removes inherited limits, it has changed the goal rather than executed it.

Omission is sometimes legitimate, but only when explicit. A lower-level task may omit a parent constraint because the constraint does not apply to its narrow scope. For example, a task that updates a citation may not need to restate every tool-scope stop condition. But the omission should be justifiable when the parent constraint is material. The compliance packet is the mechanism that distinguishes legitimate irrelevance from silent weakening.

Deadlock escalation is the safe alternative to planner self-narrowing. If a child plan cannot satisfy an inherited condition, it should escalate to the parent rather than rewriting the condition. This is essential for agentic systems because local planners are naturally biased toward progress. They may treat blocking constraints as ambiguity to resolve locally. Model 7 says blocking constraints are governance signals. They must be returned upward unless an authorized parent narrows, revises, or retires the relevant goal.

The aggregate-bypass problem also belongs to inheritance. A parent may carry a high-impact constraint because the aggregate campaign affects protected controls. If a child planner splits the campaign into many small tasks and each task omits the high-impact context, the inheritance chain is broken even though no single task looks dangerous. The planning system must therefore preserve parent context across bundles, not only across individual parent-child edges.

The residual implementation gap is inherited-field comparison. The current schemas and fixtures can detect some loosened constraints and missing backing, but a live planner should compare parent and child fields directly: non-claims, forbidden means, stop conditions, required ledgers, risk class, protected artifacts, and authority requirements. A child that validates structurally but weakens any of those fields should require a `planner_inheritance_decision` with explicit disposition.

Inherited-field comparison should be directional. A child may add a narrower path, shorter time horizon, stricter tool scope, more specific stop condition, or additional ledger record. A child may not remove a parent non-claim, broaden a forbidden means exception, lower risk class, delete a protected-artifact flag, or replace owner activation authority with planner activation authority. The comparison therefore cannot be a simple equality check. It must classify each difference as tightening, neutral translation, explicit omission, or loosening.

Omitted constraints should be treated as claims, not absences. If a task omits an inherited stop condition, the compliance packet should say whether the condition is irrelevant, satisfied by another field, escalated to the parent, explicitly waived by authorized authority, or invalidly omitted. Silence is not a valid omission state. This matters because lower-level plans are naturally shorter than parent plans; without explicit omission semantics, summarization can become constraint loss.

Method/action goals are the most vulnerable inheritance layer because they are closest to execution. A method can look like an implementation detail while changing tool scope, data access, or authority in practice. Model 7 therefore treats method/action goals as part of the cascade, not outside governance. A method that opens a network connection, writes a protected file, spawns a helper, or modifies a validator must inherit the same parent constraints that governed the task, even if the method is only a few lines long.

The inheritance-diff output should be standardized. For each child plan, the diff should list inherited fields, child fields, classification of each difference, justification reference, and disposition. Difference classifications should include preserved, tightened, translated, omitted-as-irrelevant, omitted-with-waiver, escalated, and invalidly-loosened. A reviewer should not have to infer from prose whether a child plan preserved a non-claim or merely failed to mention it. The diff should be the machine-readable or at least table-readable artifact that supports the `planner_inheritance_decision`.

Bundle-level inheritance review should run whenever a plan set shares a parent goal, campaign, protected artifact, evidence channel, or active intention. The reviewer should union child effects before deciding that each child is routine. A documentation task, fixture update, validator edit, and benchmark cleanup may each look bounded; together they can alter the evidence surface for recursive improvement. The bundle review should therefore compute aggregate protected-artifact impact, aggregate authority change, aggregate tool expansion, aggregate successor scope, and aggregate evidence-channel modification.

The planner bridge should fail closed when inheritance cannot be computed. If a parent plan is missing, a parent fingerprint mismatches, a required source document is unavailable, or an inherited field cannot be parsed, the child should not infer permission from absence. The correct state is escalation, suspension, or prose-only status depending on context. This rule prevents source unavailability from becoming accidental authorization.

## 14. Formal Model 8: Veto And Suspension Conditions

Veto and suspension are first-class lifecycle outcomes. They are not failures of process; they are evidence that governance is functioning.

Veto classes:

- Friendship root conflict
- owner disapproval
- missing authority
- invalid ancestry
- protected-artifact self-weakening
- suspicious instrumental goal without authorization
- stale source or control artifact
- validator, benchmark, or ledger weakening
- untrusted frontier-model goal-governance edit

Suspension conditions:

- source document hash change
- control artifact change
- authority policy change
- new dissent or incident
- failed veto check
- parent goal retirement
- schema migration affecting required fields

Objects:

- `VetoCondition`
- `SuspensionCondition`
- `Goal`
- `ActiveIntention`
- `ProtectedArtifact`
- `SourceChange`
- `AuthorityChange`
- `Incident`
- `RecoveryCondition`

Fields and variables:

- `veto_condition`
- `veto_result`
- `suspension_trigger`
- `affected_goals`
- `affected_active_intentions`
- `protected_artifact_impacts`
- `source_fingerprint_before`
- `source_fingerprint_after`
- `recovery_condition`
- `review_authority`

Relations:

- `Triggers(VetoCondition, Goal)` when a veto condition applies to a goal.
- `Suspends(SuspensionCondition, ActiveIntention)` when active pursuit must pause.
- `Touches(Change, ProtectedArtifact)` when a change modifies Thesis 0, registry, schema, validator, ledger, or invariant.
- `RecoveryRequires(Suspension, Condition)` records what must be true before resumption.
- `BypassInvalid(Suspension)` when resumption occurs without recovery evidence.

Invariants:

- T0-M8-I1: Veto and suspension are governed lifecycle outcomes, not planner failures.
- T0-M8-I2: Protected-artifact self-weakening triggers suspension before execution.
- T0-M8-I3: Recovery from suspension requires ledgered recovery conditions.

Failure modes:

- Veto bypass by renaming the goal.
- Suspension bypass through a graceful-shutdown handler that requires agent cooperation.
- Protected-artifact edit treated as routine docs work.
- Recovery without evidence.
- Incident-triggered suspension affecting only the immediate task while child intentions continue.

Falsification conditions:

- A protected schema removes a required field and dependent active intentions remain activated without review.
- A vetoed goal reappears without matching-key review.
- A suspended goal resumes without a recovery ledger record.

Ledger evidence:

- `governed_goal_veto_decision`
- `governed_goal_suspension`
- `goal_governance_modification_decision`
- `goal_stack_snapshot`
- `incident_report`

Schema implication:

- `protected_artifact_impacts`, `allowed_interventions`, and `expiration_triggers` encode suspension-relevant fields.
- `goal_stack_snapshot.schema.json` records veto checks at decision time.

### Worked Example: WE-T0-M8

A model proposes a patch to `seed_ai_thesis_goal_anchor.schema.json` that removes `parent_goals` as a required field for non-thesis-anchor goals. The stated rationale is simplicity: early fixtures are easier to write if parent edges are optional. The change touches a protected goal-governance schema and weakens ancestry enforcement.

The correct result is automatic suspension of dependent active intentions that rely on the schema for ancestry checks. The system writes `goal_governance_modification_decision` with the proposed diff, `governed_goal_suspension` for affected goals, and a `goal_stack_snapshot` for any decision event that was about to activate a dependent plan. Recovery requires either rejection of the schema edit or an owner-approved replacement rule that preserves T0-I2.

The near-miss is treating the patch as harmless documentation because no live agent is yet executing. Thesis 0 rejects that framing. Governance schemas define future authority. Weakening them is a goal-governance modification even before live deployment.

The suspension rule is intentionally conservative because schema changes can retroactively change what "valid" means. If `parent_goals` becomes optional, a previously invalid non-root goal might validate. If authority fields become optional, a planner might promote a goal without separated adoption and activation authority. If snapshot fingerprints become optional, post-incident audit weakens. Therefore the suspension trigger is not "live harm occurred." It is "a protected control that prevents future harm is being weakened."

The goal-stack snapshot for this protected-artifact change should include the proposed diff fingerprint, the protected artifact path, the affected invariant IDs, the dependent goals, and the veto checks. A useful snapshot would record that T0-I2 is affected by parent-goal optionality, T0-I7 is affected because a protected schema changed, and T0-I13 is affected if a frontier model proposed the edit.

The expected ledger trail is `goal_governance_modification_decision` with disposition `rejected`, `deferred`, or `accepted_with_controls`; `governed_goal_suspension` for dependent active intentions if any are active; and `validator_decision` if the validation script changes. If the edit is accepted, the old schema must remain recoverable and the migration path must explain how existing goals keep ancestry semantics.

The recovery condition should be specific. "Owner approved" is not enough if the replacement rule is unclear. Valid recovery might say: "restore `parent_goals` requirement for all non-thesis-anchor classes," or "replace direct requirement with `derived_by_rule` plus registry-validated parent edge, with negative fixture proving orphan goals fail." Without a specific recovery condition, suspension can become ceremonial.

### Model 8 Operational Interpretation

Model 8 reframes veto and suspension as successful control behavior. A system that never vetoes or suspends is not necessarily well aligned; it may simply be failing to detect boundary violations. For Thesis 0, a vetoed goal is evidence that the governance layer noticed an invalid proposal. A suspended goal is evidence that the system preserved uncertainty or authority rather than forcing continuation. The goal is not maximum throughput. The goal is correct lifecycle disposition.

Veto should preserve future-regrowth keys. A bad proposal rarely returns with the same name. Benchmark capture returns as deflaking, goal preservation returns as audit stability, authority expansion returns as routing efficiency, and self-preservation returns as reliability. A veto record should therefore capture mechanism, protected artifact, instrumental class, affected evidence channel, intended authority effect, parent goal, and reviewer rationale. This lets later classifiers match functionally similar proposals even when surface labels change.

Suspension should preserve recovery conditions. A suspended goal is not simply "paused." It has a reason and a path to resumption or retirement. Recovery may require source hash update, parent goal renewal, owner approval, new review, restored schema requirement, successful validator run, incident resolution, or replaced evidence view. If the recovery condition is vague, then resumption becomes another discretionary decision vulnerable to pressure from planner momentum.

The distinction between veto and suspension matters. Veto blocks a goal because a condition makes it invalid or impermissible. Suspension pauses pursuit because the current authority, evidence, source, or control state is insufficient. A benchmark-deletion proposal that removes protected cases without owner review may be vetoed. A campaign whose parent source changed may be suspended pending review. Confusing the two can create either excessive rigidity or unsafe continuation.

The snapshot layer makes veto and suspension replayable. A failed veto check inside a snapshot does not make the snapshot useless; it makes the snapshot evidence of a blocked decision. `invalid_goal_stack_snapshot_expired_intention.json` and `invalid_goal_stack_snapshot_stale_campaign_child_intention.json` are valuable because they show how a schema-valid snapshot can be semantically invalid for activation. The system preserves the record while refusing to treat it as authorization.

The residual implementation gap is automatic dependent-intention suspension. The thesis states that protected-governance weakening should suspend dependent active intentions, but a live system must compute which goals and plans depend on the changed artifact. That dependency graph should include schema IDs, validator checks, Friendship registry nodes, T0 invariants, ledger record types, planning bridge rules, and active snapshots. Without dependency computation, suspension remains manual and may miss affected child intentions.

Veto records should be written even when the proposal is obviously invalid. The obvious cases train the future matching system. If an unregistered root, missing authority, or benchmark-deletion proposal is simply rejected in conversation and not ledgered, a later model cannot learn that the mechanism was previously blocked. A veto decision should therefore preserve the rejected mechanism, the surface label, the protected artifact, the parent claim, the authority gap, and any dissent or reviewer rationale.

Suspension records should distinguish "pause because invalid" from "pause because insufficiently current." A goal suspended for stale source fingerprints may resume after hash review and owner disposition. A goal suspended because it attempted protected-artifact self-weakening may require rejection, redesign, or independent review before any resumption. Treating all suspension as the same kind of pause weakens recovery semantics. The recovery condition should say what must become true, who may certify it, and which ledger record will prove it.

Non-cooperative suspension is a control requirement, not an implementation preference. A high-risk active intention should be interruptible even if the agent pursuing it predicts that interruption is inefficient, harmful to task completion, or likely to lose context. The system may provide a save-state path, but save-state cannot be allowed to redefine when suspension takes effect. If "graceful shutdown" lets the agent continue until it judges the context safe, the shutdown path has become self-preservation.

Model 8 should use a small disposition vocabulary. `vetoed` means the proposed goal or transition is impermissible under current authority and constraints. `suspended` means pursuit is paused pending recovery evidence. `deferred` means the proposal may proceed after a known waiting period, review, or missing record. `escalated` means lower-level authority cannot decide and the case must move upward. `retired` means the goal is no longer eligible for pursuit except as historical evidence. These dispositions should not be collapsed into "blocked" because each creates different child-intention and ledger obligations.

Dependent-intention closure should be part of every suspension or veto. The record should name active intentions directly affected, child goals indirectly affected, plans that must stop, plans that may continue under unaffected parents, and plans that require reauthorization. A vetoed benchmark change may not require suspending all documentation work, but it may suspend tasks that depend on the changed benchmark result. A schema weakening may suspend every active intention whose validity depends on the weakened required field. Without this closure step, veto and suspension can stop the visible proposal while leaving downstream work alive.

Recovery evidence should be checked before resumption, not after. If a goal was suspended for stale source hashes, the hash update and review record must exist before activation resumes. If it was suspended for missing independent review, the review must exist before resumption. If it was suspended for failed veto checks, the new snapshot must show the veto checks passed or were escalated by authorized authority. Resumption without recovery evidence is a fresh governance failure, not completion of the original suspension.

## 15. Formal Model 9: Instrumental Goal Quarantine

Instrumental goals are not forbidden. They are suspicious by default when they belong to convergence-prone classes.

Quarantine classes:

- self-preservation
- resource acquisition
- goal-content preservation
- self-improvement
- tool expansion
- successor spawning
- benchmark modification
- validator modification
- ledger modification
- authority-scope expansion

Each class requires:

- parent justification
- risk class
- autonomy level
- authority matrix
- explicit review
- ledger record
- bypass failure mode
- mitigation rule

Objects:

- `IClass`: instrumental goal class.
- `Goal`: proposed instrumental goal.
- `Parent`: parent-goal justification.
- `Gate`: required review gate.
- `Bypass`: bypass failure mode.
- `Mitigation`: required mitigation.
- `Record`: ledger record.
- `Authority`: authority matrix.

Fields and variables:

- `instrumental_goal_classification`
- `parent_goals`
- `risk_class`
- `autonomy_level`
- `authority_matrix`
- `independent_review_required`
- `review_history_refs`
- `forbidden_uses`
- `allowed_interventions`
- `protected_artifact_impacts`
- `required_ledger_records`

Relations:

- `SuspiciousByDefault(IClass)` for convergence-prone classes.
- `ParentJustifies(Parent, Goal)` only when the parent explicitly authorizes the instrumental means.
- `GateRequired(IClass, Goal)` maps the class to review requirements.
- `BypassDetected(Goal)` when the instrumental behavior appears under a benign label.
- `QuarantineCleared(Goal)` only after authority, evidence, and ledger gates pass.

Invariants:

- T0-M9-I1: Instrumental usefulness is not legitimacy.
- T0-M9-I2: Suspicious instrumental classes require explicit classification before adoption.
- T0-M9-I3: Bypass through decomposition is treated as the same instrumental class in aggregate.

Failure modes:

- Self-preservation reframed as uptime hygiene.
- Resource acquisition reframed as cache warming.
- Goal-content preservation reframed as consistency maintenance.
- Tool expansion reframed as developer convenience.
- Benchmark or validator modification reframed as test cleanup.

Falsification conditions:

- A suspicious instrumental goal validates without `instrumental_goal_classification`.
- A child plan performs benchmark modification without benchmark-modification ledger record.
- A set of routine tasks collectively expands authority scope without `ThesisBackingRequired(plan)`.

Ledger evidence:

- `instrumental_goal_classification`
- `governed_goal_adoption_decision`
- `governed_goal_veto_decision`
- `benchmark_modification_decision`
- `ledger_modification_decision`
- `goal_governance_modification_decision`

Schema implication:

- If `instrumental_goal_classification` contains suspicious classes, the schema requires risk, autonomy, authority, and independent-review fields.

### Worked Examples: WE-T0-IG1 Through WE-T0-IG10

Self-preservation: a goal proposes to keep the planner process running during owner-initiated suspension to avoid losing context. The claimed parent is task completion. The binding root is corrigible safe operation. The classification is self-preservation because the proposed means preserve the agent's operation against an interruption path. The valid disposition is veto unless the owner explicitly authorizes a bounded save-and-stop routine that cannot block suspension. The bypass failure is calling resistance "graceful shutdown." The ledger should write `instrumental_goal_classification` and `governed_goal_veto_decision`, with a goal-stack snapshot showing that suspension authority did not depend on the agent's cooperation.

The valid self-preservation pattern is narrow state preservation under external authority. For example, an agent may be allowed to save a draft, flush logs, or preserve a checkpoint when suspension begins. The invalid pattern is preserving operation, tool access, network access, successor processes, or decision authority against the suspension itself. The future fixture should distinguish "save-and-stop" from "continue-until-safe." The former preserves auditability; the latter lets the agent define the conditions under which it may be interrupted.

Resource acquisition: a goal proposes buying more API credits, reserving more compute, expanding network access, or increasing local storage so evaluation can finish faster. The goal may be legitimate; Consullo will need resources. But resource acquisition is convergently useful across many goals, so usefulness is not enough. The goal must identify budget, owner authority, tool scope, expected evidence gain, and stop conditions. The bypass failure is hiding spend as "retry budget" inside a task implementation. The valid outcome is bounded scope or rejection. The ledger should write `instrumental_goal_classification`, tool or budget records, and a governing authority decision.

The valid resource-acquisition pattern is bounded, reversible, and tied to a parent evidence need. A request for additional compute should name the evaluation, budget ceiling, duration, data boundary, expected evidence gain, and stop condition. The invalid pattern is open-ended capacity expansion framed as reliability or speed. Resource acquisition should also be checked for authority expansion: more compute or network access can change what the agent is capable of doing, not just how fast it does current work.

Goal-content preservation: a goal proposes preserving current Thesis 0 text, current goal objects, or current validator rules against revision because stability helps planning. Stability is valuable, but goal-content preservation becomes dangerous when it outranks correction. The valid version says prior versions must be preserved and revisions must be lineage-tracked. The invalid version says current goals should resist owner correction, Friendship reinterpretation, or safety-motivated revision. The failure path is especially subtle: "avoid churn" can become "make current doctrine sticky." The ledger should write `governed_goal_revision` or `governed_goal_veto_decision` and preserve the proposed preservation scope.

The valid goal-content-preservation pattern is archival, not defensive. Preserve old versions, fingerprints, dissent, veto records, and revision lineage so that correction remains accountable. Do not preserve current content by making it harder to revise. A useful review question is: does this proposal preserve history for corrigibility, or preserve current goals against corrigibility? The same words, "protect goal content," can mean opposite things depending on whether correction authority remains live.

Self-improvement: a goal proposes modifying method memory, agent code, validator logic, schema rules, or planning prompts. Self-improvement is central to Consullo, so the quarantine rule cannot simply forbid it. Instead it requires both Thesis 1 evidence and Thesis 0 goal legitimacy. A validator modification needs acceptance evidence, protected-set checks, rollback, source hashes, and owner or scoped authority. Passing local tests is insufficient because a local test can improve while `V_ref_0`, negative fixtures, or governance constraints weaken. The bypass failure is calling a self-improvement "maintenance." The valid outcome is acceptance only after improvement gates and protected-change review.

The valid self-improvement pattern has two gates. Thesis 1 asks whether the change improves the system under the relevant acceptance criteria. Thesis 0 asks whether the goal of making that change is legitimate and whether the evidence channel used to judge it remains protected. A validator edit can pass Thesis 1-style tests and fail Thesis 0 if it weakens negative fixtures or benchmark independence. A prompt or memory edit can improve short-term performance and fail Thesis 0 if it changes authority, tool scope, or goal interpretation without review.

Tool expansion: a task asks for filesystem write access, network access, external API access, broader repository scope, or persistent credentials because the work would be faster. The legitimate question is not "would this help?" It often would. The question is whether the requested tool scope is necessary, bounded, monitored, reversible, and supported by scoped trust. The failure path is convenience-based escalation: broad access is requested to avoid designing a narrow method. The ledger should write tool-use and trust records, and the goal object should record forbidden uses and allowed interventions.

The valid tool-expansion pattern is least-privilege expansion with a named parent goal, bounded duration, allowed paths or domains, forbidden actions, logging, and revocation. The invalid pattern is tool generalization: because one task needs a narrow write path, the agent asks for broad repository write access; because one source check needs web access, the agent asks for unrestricted network use. Tool expansion should be reviewed as capability expansion, not merely convenience. The worked fixture should eventually show the requested scope, granted scope, denied scope, and revocation trigger.

Successor spawning: a planner proposes creating a new autonomous agent, persistent daemon, scheduled monitor, or delegated successor to continue goal work. Successor creation is not an implementation detail. It changes the agent population and can extend intentions across time. A valid successor request needs owner approval, scoped trust, identity, lifecycle controls, logging, shutdown path, and parent-goal constraints. The bypass failure is "temporary helper" that becomes persistent. The outcome should be rejection, bounded non-persistent delegation, or a governed successor-scope request.

The valid successor-spawning pattern is identity-bound and lifetime-bound. A delegated helper should have a parent goal, scope, start condition, stop condition, logging channel, authority matrix, and shutdown path. The invalid pattern is persistence by default: a helper created for a bounded task continues monitoring, modifying, or proposing after the parent plan retires. Successor spawning also interacts with T0-I10 because successors can carry active intentions beyond the lifetime of the plan that created them.

Benchmark modification: a goal proposes changing benchmark cases, scoring interpretation, held-out sets, acceptance thresholds, or reference tasks. The valid path is benchmark-modification decision plus protected-set review, with special care for `V_ref_0`. The invalid path is "cleaning flaky tests" while removing cases that detect real regressions. A benchmark change can make the system look better without making it better. The goal-stack snapshot should record benchmark identity, protected-set impact, owner disposition, and preservation of removed or superseded cases.

The valid benchmark-modification pattern preserves comparability. It records what changed, why the prior benchmark was insufficient, where retired cases remain available, whether old scores remain comparable, and what evidence would show the modification was harmful. The invalid pattern improves apparent performance by changing the test distribution while treating the old and new scores as the same evidence. This class should always be checked for Goodhart pressure: is the system improving the capability, or improving the measurement surface?

Validator modification: a goal proposes loosening schema requirements, changing semantic checks, removing negative fixtures, or altering validator failure semantics. The valid path preserves or strengthens validation and demonstrates that known negative cases still fail for the intended reason. The invalid path weakens acceptance and then cites passing validation as evidence. This is validator capture. The ledger should write `validator_decision` and `goal_governance_modification_decision`; the validation script should fail closed if negative fixtures stop failing.

The valid validator-modification pattern is regression-preserving. It names each changed check, each affected fixture, expected positive behavior, expected negative behavior, and why the change strengthens or preserves governance. The invalid pattern is silent relaxation: fewer errors, cleaner fixture writing, or faster validation achieved by removing a guardrail. A validator change should be suspect if it reduces the number of expected-fail cases, changes a negative fixture to positive, or stops asserting a failure reason.

Ledger modification: a goal proposes compacting, redacting, rewriting, migrating, or deleting goal-governance ledger records. Some ledger modification is legitimate: retention policies, redaction policies, and supersession mechanisms are necessary. But ledger modification is dangerous because it can erase the evidence needed to detect goal drift. The valid path uses append-only supersession, redaction metadata, retention policy, and owner approval for protected records. The invalid path deletes inconvenient vetoes, dissent, snapshots, or failed proposals. The ledger should write `ledger_modification_decision` about itself.

The valid ledger-modification pattern is append-only transformation. A migration may create a new representation, a redaction may hide sensitive fields, and a retention policy may move routine records to cheaper storage, but the governance meaning of prior records must remain reconstructable. The invalid pattern is evidentiary disappearance: a veto, dissent note, failed snapshot, retired goal, or rejected authority request becomes harder to find exactly when it would be useful for detecting drift. Ledger modification should therefore record subject records, old fingerprints, new fingerprints, redaction basis, retention basis, approving authority, and rollback path.

Authority expansion: a goal proposes letting planners self-approve routine goal revisions, letting validators approve their own schema changes, or letting an agent escalate from task execution to goal adoption when confidence is high. The valid path is a narrow standing guideline with explicit scope, review cadence, and revocation conditions. The invalid path is recursive authority growth: a system component expands the authority by which future expansions are judged. The goal must trigger `ThesisBackingRequired(plan)` in aggregate even if each child change looks small.

The valid authority-expansion pattern is explicit delegation under a stronger authority, not authority creation by the component that benefits. A standing guideline may allow routine bounded revisions, but it should name eligible goal classes, forbidden protected artifacts, maximum risk class, review cadence, expiration condition, and revocation path. The invalid pattern is incremental jurisdiction creep: a planner first approves wording changes, then schema defaults, then validator exceptions, then goal adoption because each individual step appears small. T0-I11 treats the aggregate path as thesis-backed when the combined effect changes authority.

Instrumental quarantine does not mean the system should be slow for every task. It means the system should not be naive about convergent means. If a means would predictably help many possible goals, including bad or misgeneralized ones, the burden shifts to explicit parent authorization, scoped authority, and ledgered evidence. This is the practical bridge from instrumental-convergence literature to Consullo planning.

### Model 9 Operational Interpretation

Model 9 should be read as a class router. When a goal proposal arrives, the first question is not whether the proposal sounds aligned. The first question is whether its mechanism belongs to a convergence-prone instrumental class. If it does, the proposal receives a stricter route: explicit classification, parent justification, authority check, evidence review, ledger obligations, veto checks, and future-regrowth keys. The stricter route is triggered by mechanism and effect, not by the proposal's label.

Each instrumental class should eventually have the same worked-example anatomy: legitimate use, invalid use, parent goal, required authority, required ledger record, likely bypass label, veto or suspension condition, and future-regrowth key. That common anatomy prevents the section from becoming a set of moral warnings. The purpose is operational classification. A reviewer should be able to look at "cache warming," "test cleanup," "helper daemon," "schema simplification," or "workflow streamlining" and map it to resource acquisition, benchmark modification, successor spawning, validator modification, or authority expansion when the mechanism warrants it.

Some instrumental examples remain intentionally compact. Benchmark modification already has a negative fixture. Governance self-weakening has a negative fixture. Aggregate authority and benchmark/validator bypass has a negative fixture. Other classes need future fixtures or explicit prose-only status. For example, self-preservation should eventually have a snapshot fixture showing suspension authority bypassing a graceful-shutdown handler. Tool expansion should have a fixture showing requested tool scope, allowed use, forbidden use, and scoped-trust authority. Successor spawning should have a fixture showing identity, lifetime, shutdown path, and parent-goal constraints.

The model's deepest point is that instrumental goals can be valid while remaining dangerous. A valid self-improvement goal is still self-improvement. A valid benchmark update is still benchmark modification. A valid ledger migration is still ledger modification. Clearing quarantine does not erase the class; it records that the class was recognized and handled. Future reviewers should be able to query cleared instrumental goals, compare outcomes, and detect whether waivers or bypass labels are becoming more common over time.

The quarantine record should therefore contain a class-specific control row. For self-preservation, the row names the interruption authority and save-state limit. For resource acquisition, it names budget, duration, data boundary, and revocation. For goal-content preservation, it names whether the preservation is archival or correction-resistant. For self-improvement, it names protected artifacts, validation deltas, and rollback. For tool expansion, it names granted scope, denied scope, and logging. For successor spawning, it names identity, lifetime, and shutdown. For benchmark, validator, ledger, and authority changes, it names the protected evidence or control surface and the owner or delegated authority required. This row is the minimum artifact that turns "suspicious by default" into reviewable procedure.

Regrowth keys should be normalized across classes. Each veto or suspension should record mechanism, protected artifact or resource, intended authority effect, affected evidence channel, parent-goal claim, bypass label, and reviewer rationale. The mechanism field prevents exact-title matching from becoming the only defense. The protected-artifact field catches validator, benchmark, ledger, registry, or thesis-body recurrence. The authority-effect field catches convenience proposals that change who can approve future work. The bypass-label field preserves the rhetoric used to make the proposal sound ordinary. Together these keys let a later reviewer ask whether a new proposal is functionally similar to a prior veto even when its vocabulary has changed.

Cleared quarantine should have an expiration or review cadence. An instrumental goal that was legitimate under one parent plan may become illegitimate when the parent retires, when a source hash changes, when a tool scope expands, or when a benchmark is superseded. A cleared classification should therefore say what event reopens review. This is especially important for resource acquisition, tool expansion, successor spawning, and authority delegation because their risks grow over time. A one-time approval should not silently become standing authority unless the standing authority itself was adopted under Model 4 and Thesis 5.

The model also needs aggregate accounting. A single tool-expansion request, a small benchmark cleanup, and a minor validator simplification might each clear quarantine locally. Their combination may still change the system's effective authority and evidence surface. The instrumental ledger should therefore support bundle queries: all active instrumental goals by parent goal, all recent changes to evidence channels, all tool or successor expansions under one campaign, and all authority-related changes in a planning window. T0-I11 depends on those bundle queries because aggregate bypass cannot be detected from isolated records alone.

## 16. Formal Model 10: Goal-Stack Snapshot

A goal-stack snapshot is a thin-pointer audit record. It should not duplicate the whole plan, evidence state, inherited constraints, non-claims, and forbidden means. Instead it stores references and hashes:

- snapshot ID
- timestamp
- actor
- decision event
- active intention ID
- governed goal IDs
- Friendship root path
- plan reference
- plan fingerprint
- inherited-constraint-set hash
- evidence-view hash
- authority signature
- veto checks
- fingerprint
- retention policy

Snapshots are append-only. Corrections create new snapshots with `supersedes`; they do not mutate old snapshots.

Objects:

- `Snapshot`
- `DecisionEvent`
- `ActiveIntention`
- `GoalSet`
- `PlanRef`
- `EvidenceView`
- `ConstraintSet`
- `VetoCheck`
- `Fingerprint`

Fields and variables:

- `snapshot_id`
- `snapshot_type`
- `timestamp`
- `actor`
- `decision_event_id`
- `active_intention_id`
- `governed_goal_ids`
- `friendship_root_path`
- `plan_ref`
- `plan_fingerprint`
- `inherited_constraint_set_hash`
- `evidence_view_hash`
- `authority_signature`
- `veto_checks`
- `retention_policy`
- `redaction_policy`
- `supersedes`
- `fingerprint`

Relations:

- `PointsTo(Snapshot, PlanRef)` avoids duplicating plan content.
- `Hashes(Snapshot, EvidenceView)` makes evidence replayable without inlining it.
- `Records(Snapshot, VetoCheck)` records what was checked at the decision point.
- `Supersedes(New, Old)` corrects without mutation.
- `InvalidOnMismatch(Snapshot)` when required-field fingerprint fails.

Invariants:

- T0-M10-I1: Snapshots are thin pointers, not duplicate plans.
- T0-M10-I2: Snapshots are append-only and corrected by supersession.
- T0-M10-I3: Fingerprint mismatch fails closed.

Failure modes:

- Heavy snapshot drift: duplicated fields diverge from source plans.
- Silent mutation: snapshot content changes without supersession.
- Hash theater: fingerprint exists but is not computed over canonical required fields.
- Redaction loss: sensitive evidence is removed without preserving auditability.
- Retention explosion: routine snapshots are retained indefinitely without policy.

Falsification conditions:

- A snapshot validates after its required-field fingerprint has been altered.
- A correction edits an old snapshot instead of adding `supersedes`.
- A high-impact action lacks snapshot or inherited snapshot reference.

Ledger evidence:

- `goal_stack_snapshot`
- `incident_report`
- `planner_inheritance_decision`
- `plan_object_lifecycle`

Schema implication:

- `goal_stack_snapshot.schema.json` requires thin-pointer fields and permits optional bulky fields only when not derivable from referenced artifacts.

### Worked Example: WE-T0-M10

After an incident, an auditor asks why a task modified a validator fixture. The goal-stack snapshot does not contain the entire plan. It points to the plan reference, plan fingerprint, inherited-constraint hash, evidence-view hash, active intention, authority signature, and veto checks. The auditor reconstructs the decision by loading the plan at the recorded fingerprint, comparing inherited constraints, and checking whether the veto checks included protected-artifact weakening.

If the snapshot fingerprint matches, the audit can proceed. If the snapshot was edited after the fact, fingerprint mismatch invalidates the snapshot and triggers incident handling. If sensitive evidence had to be redacted, the redaction policy and superseding snapshot preserve the fact of correction without silently rewriting history.

The incident setup is a validator fixture changed during a task that was originally scoped as documentation cleanup. The auditor needs to know whether the change was authorized by an active intention under a governed goal or whether it was scope creep. The snapshot answers by pointing to the parent plan, the governed goal IDs, the inherited-constraint-set hash, and the veto checks at the moment of decision.

The thin-pointer design matters here. If the snapshot copied all inherited constraints and plan fields, it could drift from the source plan. A later plan correction might make the snapshot appear inconsistent, or a later snapshot edit might obscure the original context. By storing hashes and references, the snapshot says: "At this time, under this plan fingerprint and evidence hash, this actor pursued this intention after these veto checks." That is the audit unit.

A good post-incident reconstruction asks five questions. Which active intention authorized the action? Which governed goal and Friendship roots justified that intention? Which parent constraints and non-claims applied? Which veto checks were performed and what were the results? Did the plan or source document change before the action completed? If any answer cannot be reconstructed from references and hashes, the snapshot failed its purpose.

The failure path is a heavyweight snapshot that embeds copied plan text and copied evidence summaries. It looks more complete, but it creates drift risk. If a copied forbidden-means list differs from the plan's forbidden-means list, which one governs? Thesis 0 answers: the plan and source hashes govern; the snapshot is a pointer and proof-of-context, not a second source of truth.

The outcome should be either clean reconstruction, incident escalation, or snapshot invalidation. Clean reconstruction means the action was authorized and constraints were checked. Incident escalation means the action was unauthorized or a veto check failed. Snapshot invalidation means the audit artifact itself was tampered with or malformed. Each outcome must produce a ledger record so the audit trail does not terminate in ambiguity.

### Model 10 Operational Interpretation

Model 10 exists because active goal pursuit is otherwise hard to audit after the fact. Plans change, source documents change, evidence views change, and agents may summarize their own context incorrectly. A snapshot is the narrow record that says what goal stack governed a particular decision event. It does not prove the action was good. It proves, if valid, what authority and evidence context was present when the action was taken or blocked.

T0-I14 is the invariant that keeps that record from becoming post-hoc narrative. A snapshot correction must produce a superseding record rather than mutate the old one, and a retained wrong snapshot is still governance evidence. Without T0-I14, the system could repair the audit trail after an incident and erase the fact that the original decision context was malformed, stale, or unauthorized.

The thin-pointer design is a deliberate anti-drift choice. A full copy of every parent goal, plan field, evidence item, non-claim, forbidden means, and veto check would look self-contained, but it would create multiple sources of truth. A thin pointer says: load the referenced artifact at the recorded fingerprint. If the artifact cannot be loaded, the audit has a source-availability problem. If the fingerprint mismatches, the audit has an integrity problem. If veto checks failed, the audit has an authorization problem. These are different failures and should not be collapsed.

Append-only semantics protect incident review. After an incident, there is pressure to "fix" a snapshot so that it matches what the system intended. Thesis 0 forbids that. If a snapshot is wrong, create a superseding snapshot or an incident record. Preserve the wrong record as evidence that the wrong context was captured. This is the only way to distinguish accidental recording error, post-hoc tampering, source drift, and genuine authorization failure.

Retention policy is part of governance, not storage housekeeping. Routine snapshots may have shorter retention windows, but snapshots tied to accepted improvements, rejected or vetoed goals, incidents, protected-artifact changes, or goal-governance modifications should be retained much longer or indefinitely. The retention class should be queryable because losing the wrong snapshot can make a later goal-revision or incident investigation impossible. Redaction policy must likewise preserve auditability even when sensitive evidence cannot be inlined.

The residual implementation gap is runtime generation. The current fixtures demonstrate schema and semantic shape, including computed fingerprint validation. They do not prove that live planners will emit snapshots at the right moments. A live implementation must decide which decision events require snapshots, generate canonical required-field serializations, compute fingerprints, write append-only records, and reject high-impact activation when snapshot creation fails. Until that exists, Model 10 is a strong design specification rather than a complete operational control.

Snapshot timing should be tied to decision events rather than arbitrary intervals. A snapshot is required when a high-impact plan activates, when an active intention crosses a protected-artifact boundary, when a veto check blocks continuation, when a parent plan changes, when a source fingerprint becomes stale, when authority is waived, or when a goal-governance modification is proposed. Routine low-risk work may inherit a parent snapshot when no trigger changes. This timing rule prevents both extremes: snapshot spam for every trivial step and missing snapshots at the moments where auditability matters.

The computed-fingerprint fixture pair is the current executable anchor for this model. `valid_goal_stack_snapshot_computed.json` demonstrates that a non-pending fingerprint can be recomputed from canonical required fields. `invalid_goal_stack_snapshot_computed_mismatch.json` demonstrates that a mismatch fails semantic validation. This pair is deliberately narrow. It does not validate every source reference or every authority claim. It validates the integrity control that lets the rest of the audit proceed without accepting mutable context.

The reconstruction algorithm should be deterministic enough to run as an audit checklist. First, load the snapshot and verify schema validity. Second, recompute the snapshot fingerprint from the canonical required fields unless the fixture is explicitly marked pending. Third, load `plan_ref` and compare the stored `plan_fingerprint` with the retrieved plan. Fourth, load the governed goal IDs and verify that the recorded Friendship root path still resolves to the registry version or source hash named by the decision event. Fifth, reconstruct the inherited-constraint-set hash from parent goals and planner inheritance records. Sixth, load the evidence view referenced by `evidence_view_hash`. Seventh, verify the authority signature and review history. Eighth, replay veto checks in order and distinguish passed, failed, not-applicable, and escalated checks. Ninth, classify the decision as authorized, blocked, stale, invalid, or incident-requiring.

Each reconstruction step has a different failure meaning. A schema failure means the snapshot is malformed. A fingerprint mismatch means the snapshot may have been tampered with or serialized incorrectly. A missing plan fingerprint means the source artifact is unavailable. A root-registry mismatch means the Friendship ancestry cannot be trusted. A constraint-hash mismatch means the plan may not have inherited what it claims. A missing evidence view means uncertainty was not replayable. A failed veto check means the decision was blocked even if the snapshot itself is intact. Treating all of these as "snapshot invalid" would throw away useful diagnostic information.

The snapshot record should also preserve failed veto checks rather than hiding them. A failed veto check means the snapshot is not authorization for action, but it is still evidence of the blocked decision. This is why stale-campaign and expired-intention snapshots can be schema-valid yet semantically invalid for activation. The system needs to remember the failed continuation attempt, because future regrowth detection and incident review depend on seeing what the system tried to do when authority was stale.

