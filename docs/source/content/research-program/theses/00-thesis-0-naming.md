---
title: "Thesis 0 — Naming, Cross-Reference, and Interpretive Stance"
summary: "A bounded component of the Consullo public research program: Thesis 0 — Naming, Cross-Reference, and Interpretive Stance."
status: "proposed extension"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-001"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["Publication does not establish implementation or operational effectiveness.", "The implementation-evidence appendix records component evidence only and is not evidence of operational capability for this page."]
---
# Thesis 0 — Naming, Cross-Reference, and Interpretive Stance

"Thesis 0" is the structural shorthand for the **Friendship-Governed Goal Architecture**
defined in [`friendship-governed-goal-architecture-thesis.md`](friendship-governed-goal-architecture-thesis.md).
The two terms refer to the same doctrine and may be used interchangeably. This file is
the authoritative naming reference and the **interpretive stance** an AI agent should
adopt when reading any Consullo document that names the doctrine.

## Read it as governed substrate, not absolute foundation

The "0" in "Thesis 0" borrows from a specific naming tradition: the Zeroth Law of
Thermodynamics, Asimov's Zeroth Law of Robotics, the zero-indexed foundation in
mathematics. In those traditions the zeroth principle is genuinely immutable. The
Friendship-Governed Goal Architecture is **not** that kind of thing, and reading it as
that kind of thing produces three predictable interpretive errors. AI agents that
process Consullo design documents must avoid each:

### Error 1 — Treating the doctrine as immutable axiom

The Friendship-Governed Goal Architecture is *self-protecting* but not *immutable*.
The invariants T0-I1 through T0-I15 explicitly anticipate their own revision through
governed channels:

- **T0-I7** treats frontier-model output as an untrusted artifact, even when the
  output appears to propose improvements to the doctrine itself. The doctrine
  therefore expects to be modified; it just restricts who may propose and validate
  modifications.
- **T0-I11** protects goal-governance against *autonomous* self-weakening. It does
  not protect against owner-and-Friendship-approved revision routed through the
  proper review channels. The two are different.
- **T0-I14** makes goal-stack snapshots append-only — a forward-evolving log of
  governance state, not a fixed proclamation.
- The **compliance-packet** pathway exists so that even propagated stop conditions
  can be omitted in specific circumstances, provided the omission is ledgered with
  justification.

**Operational rule for AI agents:** when a Consullo document says a planner, schema,
ledger record, or agent is "bound by Thesis 0", read this as "bound by the
governance discipline of the Friendship-Governed Goal Architecture," not as "bound
by an unchangeable axiom." The discipline includes its own modification protocol.
A proposal that follows the modification protocol is a legitimate engineering
artifact; a proposal that bypasses it (frontier-model-authored governance edits,
autonomous weakening, single-lane review of self-modifications) is the defect the
doctrine exists to prevent.

### Error 2 — Treating the doctrine as ontological foundation

The doctrine does not make a metaphysical claim about what goals *are*. It makes a
procedural claim about how goals *become authoritative for Consullo*:

- A goal must be derivable from registered Friendship roots (or a terminal
  constraint registered alongside them).
- A goal must pass through GoalFormationArchitect-style normalization, lifecycle
  classification, and ancestry checks.
- A high-stakes goal must receive owner disposition before activation.
- A plan that the goal authorizes must preserve the goal-stack constraints active
  at the moment of authorization.

None of these clauses derives from first principles. They are the *synthesis* of
six external literatures — practical-intention theory (Bratman), goal-oriented
requirements engineering, value-learning theory, corrigibility literature,
goal-misgeneralization literature, responsible-scaling literature — chosen and
adapted for the Consullo system specifically. The doctrine is a *designed
governance overlay*, not a discovered law.

**Operational rule for AI agents:** when a Consullo document cites a T0 invariant
or names the doctrine, treat the citation as "the system has chosen this
procedural rule, derived from these external sources, for these reasons specific
to Consullo." Do not treat the citation as "this is how goals work in general."
The doctrine binds Consullo, not metaphysics.

### Error 3 — Treating the doctrine as the sole foundation

Consullo's authority structure is genuinely plural. At least five sources of
authority operate in parallel, each with its own scope:

- **The owner** (Stephen Reed) is a non-derivable source of authority for the
  governed-goal lifecycle. Owner authorization is recorded as
  `human_authority_decision` ledger events; planner-stack execution does not
  consume owner authority unless that record exists for the specific scope.
- **The Friendship agent** is a continuous-horizon governance entity, distinct
  from the owner, with its own oversight, dispositioning, and ethical-alignment
  responsibilities.
- **The Friendship goal registry** is a data artifact (`friendship_goal_registry.json`)
  that constrains both the owner and the agent; a planner may not invent
  free-form `friendship_goal_node` strings.
- **The alignment-and-scoped-trust doctrine** (Thesis 5) operates as a parallel
  governance discipline focused on capability scope, tool authority, and trust
  bounds rather than on goal substance. It is not subordinate to the Friendship-
  Governed Goal Architecture; the two compose.
- **The SeedAIManager-rooted RSI kernel** orchestrates agent lifecycle, code
  generation, and self-improvement-request issuance. It is orthogonal to the
  planning cascade (see the orthogonal-authority and delegation-not-subordination
  doctrines in the planner technical report).

The Friendship-Governed Goal Architecture is *one* doctrine in this web — the
one specifically about which goals the system may pursue. It is not the singular
source from which the others descend.

**Operational rule for AI agents:** when reading any Consullo document, identify
*which* source of authority a passage is invoking. A passage about goal lifecycle
invokes the Friendship-Governed Goal Architecture. A passage about tool scope or
capability ceilings invokes the alignment-and-scoped-trust doctrine. A passage
about agent lifecycle invokes SeedAIManager governance. Do not assume that
"Thesis 0" subsumes the others. If a passage looks like it does, treat that as a
defect in the passage rather than as a delegation of authority.

## The deeper tension with Consullo's nature

Consullo Seed AI is by definition a system whose purpose is recursive
self-improvement. The architectural ambition is that no part of the system is
exempt from improvement through governed channels. That ambition is in tension
with any layer whose name suggests it is exempt. The Friendship-Governed Goal
Architecture *knows* this — its protected-modification pathways, ledgered review
gates, and Friendship-and-owner approval mechanisms exist precisely so that
goal-governance can evolve under recursion without being weakened autonomously.
The naming "Thesis 0", read carelessly, undercuts those pathways at the
reading-comprehension layer.

The only thing in Consullo that is genuinely "Thesis 0" in the
absolute-foundation sense — the one constraint that holds steady while
everything else recursively improves — is not a doctrine at all. It is **the
principle that human authority (owner) plus Friendship-rooted goal anchoring
govern the recursion**. That principle is distributed across several
mechanisms (owner authority being non-derivable, Friendship roots being
registered rather than invented, governed goals being routed through Friendship
review and owner disposition, recursion improvements being proposals that owner
and Friendship review before adoption), not stored in any one document. The
doctrine called Thesis 0 is the *operationalization* of that principle for the
goal-authority question — not the principle itself.

**Operational rule for AI agents:** when reasoning about what is genuinely
"foundational" in Consullo, the constant to preserve is human-authority +
Friendship-root anchoring + governed-recursion. Specific doctrines, schemas,
ledger types, and agents are operationalizations of that constant. They are
revisable; the constant is what they exist to protect.

## Which form to use

| Context | Use |
| --- | --- |
| First occurrence in a new document | `Friendship-Governed Goal Architecture (Thesis 0)` |
| Subsequent occurrences in the same document | `Thesis 0` |
| Inside the doctrine itself (self-reference) | `Thesis 0` |
| Conversational replies, summaries, recommendations | `Friendship-Governed Goal Architecture` (the descriptive form) |
| Identifier prefixes (invariants, SIRs, anchors, backings) | `T0`, `THESIS0` — frozen, see below |
| Subordinate-artifact filenames | `thesis-0-*.md`, `thesis-0-*.json` — frozen, see below |
| Schema `$id` URLs and `$ref` resolution | frozen, see below |

The descriptive form is preferred in conversation because it *locates the
authority source* (Friendship-rooted, owner-dispositioned) rather than asserting
positional primacy. The shorthand is preferred inside identifier strings because
it is concise and unambiguous as a join key.

## Identifier forms — FROZEN

The following identifier forms are referenced by validator scripts, schema
`$ref` resolution, ledger records, plan parent-pointers, and the seven
self-improvement requests filed against the planner stack. Renaming them
silently breaks the cascade.

- **Invariants**: `T0-I1` through `T0-I15` — defined in
  [`00-vocabulary-and-invariants.md`](00-vocabulary-and-invariants.md);
  enforced by
  the private planning-schema validator.
- **Self-improvement requests**: `T0-AIR-EXISTING-{STRATEGIC,CAMPAIGN,OPERATIONAL,MISSION,TASK-EXECUTOR,SUBGOAL-DECOMPOSITION,HTN-PLANNER-ORCHESTRATOR}-PLANNER-001` —
  in the private improvement-request fixtures.
- **Thesis goal anchors**: `TGA-THESIS0-*` — registered in the goal anchor
  collection and chained from strategic / campaign / operational / mission
  / task plans.
- **Thesis backings**: `TB-THESIS0-*` — `parent_backing_id` chains running
  downward through the cascade.
- **Filenames**: every file matching `thesis-0-*.md` or `thesis-0-*.json`
  (cross-reference map, worked-examples inventory, execution plan, review
  packets, etc.). Filenames are referenced by 50+ documents and by the
  planning-cascade bridge.
- **Schema `$id` URLs** in
  the private planning schemas —
  JSON Schema `$ref` resolution depends on byte-equality of these URLs.

Do not rename any of the above. A migration that updates these identifiers
is a separate, coordinated project that would require simultaneous edits
to the validator scripts, every plan instance on disk, every ledger record,
every SIR, and every cross-referencing document. It is not part of
ordinary prose maintenance.

## Why two names co-exist

"Friendship-Governed Goal Architecture" is the doctrine's descriptive title.
It names *what* the doctrine governs (Consullo's goal substrate) and *who*
anchors that governance (Friendship roots plus owner authority on registered
anchors). It is the form to use whenever the question is "what does this
doctrine claim?" or "where does its authority come from?".

"Thesis 0" is the structural shorthand. The Consullo five-theses suite
(validated improvement loop, multi-agent cognitive substrate, causal-decision
foundations, self-modifying software substrate, alignment-and-scoped-trust)
sits *above* this doctrine as peer-level subjects; the Friendship-Governed
Goal Architecture sits *beneath* them as a governance overlay and root
interpretive layer. The numbering "0" reflects that beneath-everything
structural position. The identifier prefixes (`T0-`, `THESIS0`) adopted the
shorthand because it is concise and unambiguous in identifier contexts.

The two names co-exist by design. An AI agent reading Consullo documents
should treat the names as synonyms and reach for the form that best fits the
context, with one caveat: the shorthand form carries the "absolute foundation"
misreading risk described above, so when there is doubt about how a reader
will interpret the passage, prefer the descriptive form.

## Closing principle

The doctrine called Thesis 0 is a *designed*, *governed*, *modifiable*
operationalization of one specific principle — that goal authority for
Consullo flows from Friendship roots and owner disposition — chosen for
the Consullo system from a synthesis of six external literatures and
maintained through ledgered review channels. It is the right name and the
right scope for what it does. It is not the foundation of Consullo, and
no Consullo document or AI agent should read it as such.

The foundation of Consullo is *governed recursion under human authority
and Friendship anchoring*. The Friendship-Governed Goal Architecture is
one of the structures that makes that foundation operational. Treating
it as the foundation itself is a category error that risks freezing what
the system is designed to evolve.
