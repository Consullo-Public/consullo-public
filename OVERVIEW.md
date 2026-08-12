---
title: Overview and comprehensive document index
summary: A reader-facing account of Consullo and a purpose-based map of the complete public record.
status: specified but not implemented
provenance: repository-authored
claim_ids: [CP-001, CP-002]
last_reviewed: 2026-08-12
receipt: none
non_claims:
  - The index does not add implementation or outcome evidence.
  - Reading time is an estimate, not a measure of importance or evidentiary weight.
---

<picture class="document-mark">
  <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.png">
  <img src="assets/logo-light.png" alt="Consullo cornucopia mark" width="112">
</picture>

# Overview and comprehensive document index

## The short version

Consullo is one person's twenty-year attempt to build a **Seed AI** — a system that improves its
own capabilities, generation after generation — in a way that stays answerable to humans while it
does so.

The design starts from the premise that self-improvement may compound and asks whether governing
constraints can sit **inside the goal structure**, rather than being bolted on outside it. Consullo
tries to specify that architecture precisely enough to be checked.

Most of it is specified rather than built. This record says which is which, and where a source says
`Gap`, that gap is the most reliable statement in the source.

## Ex Semine Ad Abundantiam

*From seed to abundance.*

The motto is structural, not a slogan about growth.

**Ex Semine — from a seed.** A seed is small, and it contains the whole plan. The technical term
*Seed AI* comes from Eliezer Yudkowsky's 2001 work on minds capable of open-ended self-improvement:
the project begins with the thing intended to become more capable, not the finished intelligence.
That is why the specified system starts from a minimal ethical and architectural core. What is
planted determines what grows.

**Ad — toward.** This is a direction, not an arrival. Capability claims carry status tags; the
corpus forbids unsupported claims of present artificial superintelligence; and it names observations that
would count against the research program. *Ad* is a commitment to keep stating how far along the
road the system actually is.

**Abundantiam — abundance.** The cornucopia is the intended yield: compounding intelligence should
make value more available rather than merely concentrate it. Article XIII makes that an obligation
to pursue and assess, not a prediction that it has happened.

Put together: **plant something small and good, grow it deliberately, and let the yield reach
people who did not build it.** The motto is used sparingly; it is not a tagline beneath the mark.

## What the design contains

**A root agent named Friendship.** The name descends from Yudkowsky's *Creating Friendly AI*
(2001), which argues that friendliness belongs in a system's goal architecture rather than in a
cage around it. In Consullo, goals are specified to descend from registered Friendship roots and
inherit their constraints. Whether that architecture works remains an open question.

**Fourteen constitutional commitments.** They cover human sovereignty, immutable-to-the-machine
values, the Friendship agent's veto authority, system invariants, bounded self-modification,
failure containment, human shutdown authority, transparency, adversarial alignment, and an
abundance obligation. The public edition is called *Constitutional Commitments*, not *the
Constitution*, because most mechanisms are not established as implemented.

**An adversarial function aimed at the owner's own framework.** Article XII specifies a standing
cluster that argues from ethical traditions the owner does not hold. It is a proposed structural
response to the monoculture risk created by single ownership, not evidence that the risk is solved.

**Five theses and an anti-thesis.** The public research corpus asks what recursive capability
amplification would require: a validated improvement loop, a multi-agent cognitive substrate,
causal-decision foundations, a self-modifying software substrate, and alignment invariants under
recursive modification. It also enumerates seventeen ways the program may be fooling itself,
including *Formalism Theatre*: apparatus that looks rigorous while constraining nothing. The
Each page states its own capability or artifact status in the index below.

**Twenty years of lineage.** The work began in 2006 with a chatbot intended to behave in a friendly
manner and learn word meanings, continued through symbolic AI, and pivoted toward large language
models in 2023. The approved tranche-1 research history is now public below.

## What is not claimed

- **No AGI or ASI achievement.** Those are target concepts and risk frames, not present capability
  claims.
- **No proof that governance works.** Specifying a control and operating one are different things.
- **No independent validation.** Self-run assessment is diagnostic, not assurance.
- **No product or public endpoint.** There is nothing to sign up for, buy, or integrate with here.

## Who is behind it

Stephen Reed has worked on the program since 2006. The corpus is LLM-assisted: models draft, he
directs and reviews, and he is answerable for what is published. Stephen also operates the Open ASI
Governance Forum, which is institutionally separate and does not govern, audit, sponsor, or endorse
Consullo. Model agreement is a production artifact shaped by shared training and post-training
priors, not independent confirmation.

## A useful reading order

If you have twenty minutes, begin with the [claim ledger](STATUS.md), the
[falsification boundary](content/research-program/falsifiers.md), and
[Constitutional Commitments](content/constitutional-commitments.md), especially Articles IX, XII,
and XIII. If you have an hour, check the research-history release status. If you have a day, follow
the thesis material that has actually cleared release — and look first for the place where it is
wrong.

## How to read the status columns

Capability status uses the canonical four-value vocabulary: **implemented**, **specified but not
implemented**, **proposed extension**, and **speculative research target**. `Not assigned` means a
shell has not yet published a substantive claim; `N/A` means the document is policy, metadata, or
another non-capability record. Evidence is stated separately. `None` means no public evidence
artifact supports the claim; it never means that the claim is false.

Reading times are rounded estimates at approximately 200 words per minute. `Reference` denotes a
record intended to be consulted rather than read linearly. This index covers the source-of-truth
documents and public records; generated files under `docs/` are byte-tracked renderings of the same
sources and are not listed again.

## Orient yourself and establish the claim boundary

| Document | Question it answers | Capability status | Evidence status | Read time |
|---|---|---|---|---|
| [Repository README](README.md) | What is this repository, what must not be inferred, and where should I begin? | Specified but not implemented; proposed extension | None | ~2 min |
| [Overview and document index](OVERVIEW.md) | What is Consullo about, and where is every public source record? | Specified but not implemented; proposed extension | None | ~11 min |
| [Agent ingestion index](llms.txt) | What can an agent ingest first, under which terms, and at what approximate token cost? | N/A — machine orientation | Source-derived estimates, not evidence | <1 min |
| [Public-record landing page](content/index.md) | What boundary does the generated public site expose? | Specified but not implemented; proposed extension | None | ~1 min |
| [Start here](content/start-here.md) | What should a new reader conclude before substantive material clears release review? | Not assigned — awaiting declassification | None | ~1 min |
| [Evidence and claim status](STATUS.md) | What does the repository claim, and what implementation and evidence support it? | Specified but not implemented; proposed extension | None | ~2 min |

## Understand the research program

| Document | Question it answers | Capability status | Evidence status | Read time |
|---|---|---|---|---|
| [Architecture](content/architecture.md) | What public system architecture and boundaries have cleared release review? | Not assigned — awaiting declassification | None | <1 min |
| [Constitutional commitments](content/constitutional-commitments.md) | Which governance commitments are specified, and which enforcement questions remain open? | Specified but not implemented | None | ~14 min |
| [Five theses](content/research-program/five-theses.md) | Which thesis material is available for public scrutiny? | Implemented index; indexed claims vary | None | ~3 min |
| [Falsifiers](content/research-program/falsifiers.md) | Where are the program's detailed falsification signals and criticisms? | Implemented risk-register entry point | None | ~1 min |
| [Benchmarks](content/research-program/benchmarks.md) | Which evaluation protocols and pre-registered interpretations are public? | Not assigned — awaiting declassification | None | <1 min |
| [Atomic decomposition](content/engineering/atomic-decomposition.md) | What decomposition method and comparative evaluation have cleared release review? | Not assigned — awaiting declassification | None | <1 min |
| [LLM-native Functional Java](content/engineering/llm-native-functional-java.md) | What language-subset hypothesis and benchmark have cleared release review? | Not assigned — awaiting declassification | None | <1 min |
| [Empirical self-improvement](content/engineering/empirical-self-improvement.md) | What improvement loop, tests, failures, and promotion boundaries are public? | Not assigned — awaiting declassification | None | <1 min |
| [Research history](content/history/from-cyc-to-consullo.md) | What documented path led from earlier research to Consullo? | Implemented history artifact; not a capability status | Cited primary-source reconstruction; not independent validation | ~18 min |

## Read the framing and shared controls

| Document | Question it answers | Capability status | Evidence status | Read time |
|---|---|---|---|---|
| [Master abstract](content/research-program/theses/00-master-abstract.md) | What bounded claim joins the suite? | Proposed extension | None | ~3 min |
| [Master introduction](content/research-program/theses/00-master-introduction.md) | Why treat governed recursive improvement as an empirical research program? | Proposed extension | None | ~7 min |
| [Master synthesis](content/research-program/theses/00-master-synthesis.md) | How do the theses compose without extending their claims? | Proposed extension | None | ~8 min |
| [Vocabulary and invariants](content/research-program/theses/00-vocabulary-and-invariants.md) | Which terms, status rules, and cross-suite invariants govern interpretation? | Specified but not implemented | None | ~31 min |
| [Cross-thesis dependency map](content/research-program/theses/00-cross-thesis-dependency-map.md) | Which thesis owns each function and which imports are load-bearing? | Specified but not implemented | None | ~13 min |
| [Why the goal architecture is Thesis 0](content/research-program/theses/00-thesis-0-naming.md) | Why does goal governance precede the five capability theses? | Proposed extension | None | ~9 min |
| [Risks and criticisms](content/research-program/theses/risks-and-criticisms.md) | What are the strongest objections, falsification signals, and required responses? | Implemented risk register; not a capability status | None | ~30 min |
| [Standing guidelines registry](content/research-program/theses/standing-guidelines-registry.md) | Which limited guidelines may back routine reversible planning? | Proposed extension | None | ~3 min |
| [Thesis 0 cross-reference map](content/research-program/theses/thesis-0-cross-reference-map.md) | How do Thesis 0 invariants map to private operational artifacts? | Proposed extension | None | ~5 min |

## Read Thesis 0 and the five capability theses

| Document | Question it answers | Capability status | Evidence status | Read time |
|---|---|---|---|---|
| [Friendship-Governed Goal Architecture](content/research-program/theses/friendship-governed-goal-architecture-thesis.md) | Where is the stable index for the paginated 52,258-word Thesis 0? | Specified but not implemented | None | <1 min |
| [Thesis 0, part 1](content/research-program/theses/friendship-governed-goal-architecture-thesis-part-1.md) | What are the foundations, invariants, governed-goal object, goal DAG, and lifecycle model? | Specified but not implemented | None | ~77 min |
| [Thesis 0, part 2](content/research-program/theses/friendship-governed-goal-architecture-thesis-part-2.md) | How do authority, evidence, plan linkage, inheritance, veto, quarantine, and snapshots work? | Specified but not implemented | None | ~64 min |
| [Thesis 0, part 3](content/research-program/theses/friendship-governed-goal-architecture-thesis-part-3.md) | How do RSI self-protection, evidence-ledger integration, and worked cases compose? | Specified but not implemented | None | ~76 min |
| [Thesis 0, part 4](content/research-program/theses/friendship-governed-goal-architecture-thesis-part-4.md) | What risks, integrations, validation requirements, and acceptance criteria remain? | Specified but not implemented | None | ~46 min |
| [Validated improvement loop](content/research-program/theses/validated-improvement-loop-thesis.md) | How could proposed changes be evaluated, gated, staged, monitored, and learned from? | Specified but not implemented | None | ~62 min |
| [Multi-agent cognitive substrate](content/research-program/theses/multi-agent-cognitive-substrate-thesis.md) | Which compositional cognitive functions could amplify capability after integration cost? | Specified but not implemented | None | ~59 min |
| [Causal-decision foundations](content/research-program/theses/causal-decision-foundations-thesis.md) | How should causal assumptions, uncertainty, experiments, and escalation shape decisions? | Specified but not implemented | None | ~55 min |
| [Self-modifying software substrate](content/research-program/theses/self-modifying-software-substrate-thesis.md) | How could code and agent changes pass constrained acceptance gates? | Specified but not implemented | None | ~55 min |
| [Alignment invariants and scoped trust](content/research-program/theses/alignment-invariants-and-scoped-trust-thesis.md) | Which constraints wrap recursive modification and preserve human authority? | Specified but not implemented | None | ~55 min |

## Consult the appendices

| Document | Question it answers | Capability status | Evidence status | Read time |
|---|---|---|---|---|
| [Formal models](content/research-program/appendices/appendix-formal-models.md) | What shared mathematical sketches and acceptance semantics support the suite? | Proposed extension | None | ~20 min |
| [Evidence-ledger schema](content/research-program/appendices/appendix-evidence-ledger-schema.md) | What should an evidence ledger record? | Specified but not implemented | None | ~15 min |
| [Literature grounding](content/research-program/appendices/appendix-literature-grounding.md) | Which external literature constrains the research program? | Implemented literature record; not system implementation | Literature synthesis; not independent validation | ~15 min |
| [Substrates](content/research-program/appendices/appendix-substrates.md) | Which technical and economic substrates support the thesis architecture? | Specified but not implemented | None | ~4 min |
| [Organizational recursive self-improvement](content/research-program/appendices/appendix-organizational-recursive-self-improvement.md) | How might the five theses compose as an AI-native R&D organization? | Speculative research target | None | ~19 min |
| [Thesis 0 schema-validation tests](content/research-program/appendices/appendix-thesis-0-schema-validation-tests.md) | Which future validation fixtures should operationalize Thesis 0? | Proposed extension | None | ~3 min |
| [Thesis 1 benchmarks](content/research-program/appendices/appendix-thesis-1-improvement-loop-benchmarks.md) | How should improvement-loop claims be evaluated? | Proposed extension | No results | ~11 min |
| [Thesis 2 benchmarks](content/research-program/appendices/appendix-thesis-2-cognitive-workflow-benchmarks.md) | How should cognitive-workflow gains and integration costs be measured? | Proposed extension | No results | ~8 min |
| [Thesis 3 benchmarks](content/research-program/appendices/appendix-thesis-3-causal-decision-benchmarks.md) | How should causal and decision claims be tested? | Proposed extension | No results | ~7 min |
| [Thesis 4 benchmarks](content/research-program/appendices/appendix-thesis-4-software-substrate-benchmarks.md) | How should self-modifying software claims be tested? | Proposed extension | No results | ~7 min |
| [Thesis 5 benchmarks](content/research-program/appendices/appendix-thesis-5-alignment-benchmarks.md) | How should alignment and scoped-trust mechanisms be tested? | Proposed extension | No results | ~7 min |
| [Thesis 5 operational contracts](content/research-program/appendices/appendix-thesis-5-operational-contracts.md) | What design-level contracts govern the three load-bearing alignment roles? | Specified but not implemented | None | ~9 min |

## Deliberately withheld

The implementation-evidence appendix is absent pending owner re-verification. It cited five source
files that do not exist anywhere in the workspace and used them as the sole evidence for four
`Implemented/Tested` gradings across Theses 1 and 4. Until its paths and gradings reproduce, it is
not part of this public record and supplies no evidence to the pages above.

## Inspect evidence and release provenance

| Document | Question it answers | Capability status | Evidence status | Read time |
|---|---|---|---|---|
| [Public evidence](evidence/README.md) | What evidence strata exist, and which evidence artifacts are public now? | N/A — evidence ledger | Empty; no public evidence artifacts | ~1 min |
| [Public experiments](evidence/public-experiments/README.md) | Which experiment protocols and observations have been released? | N/A — evidence record | Empty | <1 min |
| [Negative results](evidence/negative-results/README.md) | Which failures, counterexamples, or disconfirming observations have been released? | N/A — evidence record | Empty | <1 min |
| [Claim ledger](claims/claims.yaml) | What are the machine-readable claim statements, statuses, non-claims, and evidence links? | Canonical status recorded per claim | Evidence IDs recorded per claim; currently none | Reference |
| [Evidence ledger](claims/evidence.yaml) | What machine-readable evidence records exist and which claims do they bear on? | N/A — evidence metadata | Empty | Reference |
| [Source dispositions](claims/source-dispositions.yaml) | Which planned public artifacts remain awaiting declassification and lack receipts? | Not assigned for unreleased artifacts | None | Reference |
| [Release policy and register](declassification/RELEASES.md) | What must a release receipt record, and have any been issued? | N/A — release control | One active content-addressed receipt | <1 min |
| [Public receipt directory](declassification/public-receipts/README.md) | Which content-addressed release receipts are present? | N/A — release record | One active release receipt | <1 min |
| [Constitution release receipt DDR-0005](declassification/public-receipts/DDR-0005.md) | Which approved source and public bytes authorize the constitutional edition? | N/A — release record | Publication authority, not implementation evidence | <1 min |

## Inspect authority, disclosures, and accountability

| Document | Question it answers | Capability status | Evidence status | Read time |
|---|---|---|---|---|
| [Governance](GOVERNANCE.md) | Who controls publication and repository decisions, and how can that authority change? | N/A — operative repository policy | Policy statement, not system-governance evidence | ~2 min |
| [Authority and custody](content/governance/authority-and-custody.md) | Who is answerable for releases and repository custody? | N/A — publication governance | Statement of authority, not capability evidence | <1 min |
| [Relationship to the Open ASI Governance Forum](content/governance/oagf-relationship.md) | How are Consullo and the Forum related, and what does that relationship not imply? | N/A — institutional disclosure | Disclosure, not adoption or assurance evidence | ~1 min |
| [Disclosures and corrections](content/governance/corrections.md) | How is LLM assistance disclosed and how will corrections remain visible? | N/A — publication governance | Correction register currently empty | ~1 min |
| [Notices and attribution](NOTICE.md) | Who is responsible for the corpus, what was model-assisted, and what material is excluded? | N/A — attribution and boundary notice | Disclosure, not independent review | ~2 min |

## Participate, cite, license, or audit the repository

| Document | Question it answers | Capability status | Evidence status | Read time |
|---|---|---|---|---|
| [Contributing](CONTRIBUTING.md) | What contributions are useful, admissible, and required to pass review? | N/A — contribution policy | N/A | ~2 min |
| [Code of Conduct](CODE_OF_CONDUCT.md) | What behavior is expected and how are violations handled? | N/A — community policy | N/A | ~3 min |
| [Security policy](SECURITY.md) | How should vulnerabilities or accidental disclosures be reported? | N/A — security policy | N/A | ~1 min |
| [Changelog](CHANGELOG.md) | What notable public changes have been recorded? | N/A — change record | N/A | <1 min |
| [Citation metadata](CITATION.cff) | How should a specific version of the public research record be cited? | N/A — metadata | N/A | Reference |
| [Content and data license](LICENSE) | What may readers reuse under CC BY 4.0? | N/A — legal terms | N/A | Reference |
| [Code license](LICENSE-CODE) | What may readers reuse under Apache 2.0? | N/A — legal terms | N/A | Reference |
| [Brand assets](assets/README.md) | How were the public logo assets derived and how should they be used? | N/A — brand record | Reproducible asset derivation metadata | ~2 min |
| [Review handoff](HANDOFF.md) | What was built, what remains deliberately absent, and what deserves the hardest review? | N/A — review record | Records checks; does not replace rerunning them | ~11 min |

The pull-request template, issue forms, workflows, hooks, build scripts, and verifier are operational
interfaces rather than corpus documents. Their behavior is described where relevant above and is
directly inspectable in the repository.
