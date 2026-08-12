---
title: "From Cyc to Consullo — A Research History"
summary: "A primary-source-based history of the research program from 2006 through 2026."
status: "implemented"
provenance: "approved tranche-1 research history derived from the cited primary sources; no artifact-specific public receipt has been issued"
claim_ids: []
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["This historical reconstruction is not independent validation of Consullo.", "The implemented status describes the published history artifact, not a system capability."]
---
<picture class="document-mark">
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/logo-dark.png">
  <img src="../../assets/logo-light.png" alt="Consullo cornucopia mark" width="112">
</picture>

# From Cyc to Consullo — A Research History

*The long road to a Seed AI, 2006–2026: the symbolic cathedral, the pivot to large language models, and the turn from writing every line by hand to steering frontier intelligence.*

> **Provenance.** This document is a technical history reconstructed from the primary sources: the
> `whitten/texai` mirror (2006–2015), the recovered `git-aicoin/texai` monorepo (2022–2024, 4,734
> commits, restored 2026-08-03 from a duplicity backup), the `git-texai/AGI` transitional repository,
> and the current Consullo codebase and design corpus. Dates and quotations are drawn from file
> headers, commit messages, README files, and design notes in those repositories. Where a claim is
> interpretation rather than record, it is marked as such.

---

## Prologue: a small program that wanted to learn words

On 11 September 2006, a design note was written for a chatbot. In it, the program introduces itself:

> *"Hi, I am Texai. I am a chatbot. I want to behave in a friendly manner, and I want to learn the
> meanings of more words."*
> — `Texai/Dialog/doc/chatbot-use-cases-2006.txt`

That is the seed. Everything that follows — twenty years of work by one person, three complete
rewrites, a knowledge base of millions of assertions, a hierarchy of thousands of agents, and finally
a system that steers frontier language models toward artificial superintelligence — grows from a
program that wanted two things: to be friendly, and to learn the meanings of words.

The friendliness became a governance doctrine. The learning became a Seed AI. This is the history of
how.

---

## I. The vow (2006)

The author's last salaried position was at Cycorp, working on **Cyc** under **Douglas Lenat** — inside
the most ambitious attempt ever made to give a machine common sense by hand-asserting the knowledge a
human takes for granted. He left to attempt, alone and unfunded, what is arguably the single most
consequential problem a lone person can take up: to build a mind.

From 2006 he pursued it full-time, by himself. There was no team, no runway, no institutional cover —
only the conviction that the problem was tractable if approached with the right architecture and
enough patience. The patience would have to last much longer than anyone could have known when it
began.

He named his machines after the people who had walked this road before him. This was not decoration.
Each name is a debt, and each debt is visible in the code.

---

## II. The company of the named — the heroes on the servers

The architecture of this work is, quite literally, an argument built from the ideas of six people.
The author's servers carry their names; the design carries their theories.

**John McCarthy** — `mccarthy`. The original host carrying this name was retired, but the name
returned in 2026 for the RTX 5080 server that now supplies Consullo's high-throughput ATOMIC tier. He
gave the field its name in 1956, gave it Lisp, and gave it the situation calculus and circumscription
— the first serious formal attack on commonsense and non-monotonic reasoning. His fingerprints are
on the S-expression *capability grammar* that Texai's planner reads, and on the Lisp-syntax ACT-R
models it once ran. The logicist dream — that thought could be made explicit, inspected, and
mechanized — is the dream this whole program began inside. The reused name now fits a narrower role:
`mccarthy` executes explicit, decomposed questions whose short answers can be mechanically checked,
while broader judgment remains with stronger tiers.

**Marvin Minsky** — `minsky`. *The Society of Mind*: intelligence as the emergent behavior of many
small, unintelligent agents. Texai's control system is this made concrete — a hierarchy of agents in
which, in the words of the AgentBuilder's own system prompt, *"the behavior of each agent is composed
using the behavior of its child agents."* Minsky's frames became RDF feature structures; his K-lines
became the message-passing agent network. Consullo is a Society of Mind with three thousand citizens.

**Alan Turing** — `turing`. The foundational question — *can machines think?* — and the decision to
answer it through **conversation**. The 2006 chatbot is a Turing gambit: knowledge is acquired and
demonstrated in dialogue. Two decades later, `turing` serves the language model that finally made the
conversation fluent.

**Douglas Lenat** — `lenat`. The author's own mentor. Cyc's wager — that commonsense competence
requires an enormous base of explicitly asserted knowledge — is the wager Texai inherited: its early
knowledge base was grounded in **OpenCyc**. And Lenat's earlier work, AM and Eurisko, is the origin of
a second theme that never left: **recursive self-improvement**, a system that improves its own
heuristics. The Consullo agent hierarchy still names a **SelfImprovement** agent at the top table.

**James Albus** — `albus`. The **4D/RCS hierarchical control architecture**: a uniform node with
perception, a world model, and behavior generation, replicated at every level of a control hierarchy.
Texai's runtime is literally named for it — *AHCS, the Albus Hierarchical Control System* — and every
agent, from 2006 to today, is an Albus node. When Consullo speaks of a uniform PDCA node repeated at
every level of resolution, that is Albus, unbroken across twenty years.

**Geoffrey Hinton** — `hinton`. The one whose work broke the symbolic program open. Deep learning
produced the large language models that supply exactly what Cyc and Texai always lacked: a way to
*ground* a symbol and *bound* an entailment against the open-ended meaning of the world. Hinton is the
reason the pivot became not just possible but necessary. It is fitting that a host bears his name in
the same cluster as the symbolists he superseded and completed.

**Peter Norvig** — `norvig`. The reconciler. *Artificial Intelligence: A Modern Approach* and *the
unreasonable effectiveness of data* — the case that symbolic and statistical AI are not enemies but a
division of labor. Texai's turn from hand-written grammar rules to Bayesian rule-selection, and then to
LLM adjudication, is Norvig's thesis lived out one refactor at a time. Today `norvig` serves the local
language model that does the work.

Six names. A logician, a cognitive theorist, the founder of computing, a knowledge engineer, a control
theorist, and a deep-learning pioneer — reconciled by a seventh idea, the statistical-symbolic
synthesis. The whole intellectual history of AI is standing in one man's server rack, and every one of
them is load-bearing.

---

## III. The symbolic cathedral (2006–2022)

For roughly fifteen years, Texai was built the way cathedrals are built: by hand, stone by stone, by
someone who did not expect to see it finished quickly. It was a genuinely complete cognitive
architecture, and much of it worked.

**The Albus control system.** A network of agents, each an Albus node, communicating by signed
messages, organized as network-singleton coordinators with per-container workers. At its apex, from
the very beginning, sat a governance skill called **TopmostFriendship** — the friendliness of the
2006 chatbot, promoted to the top of the hierarchy and made the root of authority. Twenty years later
Consullo's central doctrine is the **Friendship-Governed Goal Architecture**. The name at the top of
the tree never changed.

**Knowledge as logic.** Meaning was represented in RDF, grounded in OpenCyc, reasoned over by a
hand-built **Rete** inference engine. The world was to be understood by asserting it.

**Language as reversible grammar.** The crown jewel was **Incremental Fluid Construction Grammar** — a
reversible engine that parsed English into logical propositions word by word, left to right, and
generated English back from propositions, using constructions adapted from Double R Grammar. It was
beautiful, and it was honest about its limits. From a real acquisition dialogue:

> *"But I cannot parse this utterance beyond 'a volume is a'. … Would you like to see a syntax tree?"*
> — `Texai/Dialog/doc/grammar-acquisition-skill-use-cases.txt`

**Programs as plans.** A capability planner — the *behavior language*, its grammar dated to 2007 —
matched tasks against Lisp-form capability operators with preconditions and postconditions, and its
plan operators *emitted Java source code*. The goal of writing programs from English specifications
was present at the very start; the author simply did not yet have a tool equal to it.

**Learning as being taught.** And here is the dream that animated all of it — a system that acquires
its skills the way a person does, by being **mentored** in conversation. From the 2006 lexicon
dialogue, Texai learning the word *bird*: asking for its singular and plural forms, whether it is a
mass or count noun, which WordNet sense is meant, whether it matches Cyc's concept — and then, with
disarming honesty:

> *"OK, but I don't comprehend the phrases: 'warm blooded', 'egg-laying vertebrates…'. Can you help me
> learn them later?"*

And from the programming-skill use case, a human mentor teaching Texai to *program*, by conversation:

> **[Mentor]** *"One type of instruction is the assignment statement."*
> **[Texai]** *"OK, how is it interpreted?"*
> **[Mentor]** *"It has two parts, one part identifies a variable that receives a copy of, or a
> reference to, an evaluated expression…"*
> **[Texai]** *"I assume by variable you mean a symbol (like x or y)… What's an evaluated expression?"*
> — `Texai/Dialog/doc/programming-skill-use-case.txt`

This was the summit Texai was climbing toward: an AI that a human being could *teach a procedural
skill* through patient dialogue, each new term grounded against what it already knew, each gap in
understanding surfaced honestly and deferred to a later lesson. It is one of the most humane visions
of machine learning ever sketched — not a model trained on a corpus, but a student sitting with a
teacher.

**It was never finished.** This is the truth the history must hold. The mentor-teaches-programming
dialogue is a design document, not a working transcript. The grammar could parse simple declaratives
and then stall. The lexicon had to be built by hand — queues of gloss words, plural forms, word senses,
disambiguations — a labor so vast that a whole workflow subsystem existed just to manage the human
effort of feeding it. The ACT-R implementation was structurally faithful but had no subsymbolic layer
to make it learn. The cathedral was magnificent and, in the parts that mattered most for autonomy,
unroofed. A single person, however gifted and however tireless, could not hand-assert enough knowledge
or hand-write enough grammar to reach the summit. This was not a failure of will. It was the same wall
Cyc met, met again by one man instead of a company.

---

## IV. The turn (2023)

Then the wall came down — not from inside the program, but from Hinton's side of the field.

The repository records the moment with unusual clarity. In the project README, the author states the
pivot in his own hand:

> *"It was originally designed with these themes, starting in 2006. … And now, the availability of
> large language models necessitates a pivot away from the previous approaches. … as of June 2023."*

The new design keeps the Albus hierarchy and sets nearly everything else aside: agents are now *"designed,
specified, and generated into Java by a LLM"*; symbolic knowledge representation is *"set aside for
the most part"* in favor of English structured as JSON; and — the line that closes a seventeen-year
loop — *"agents obtain their knowledge and skills by conversation with a LLM, not primarily with human
mentors."*

Read that against the 2006 programming-skill dialogue and the meaning is almost unbearable. The dream
was always an apprentice that learns a skill by conversation. For seventeen years the teacher had to be
a human, and there were not enough hours in a life to teach it everything. In 2023 the teacher became a
language model — tireless, fluent, and available at scale. The mentor Texai had been waiting for its
whole existence had finally arrived. It simply was not human.

Setting aside fifteen years of symbolic work — the Rete engine, the Fluid Construction Grammar, the
hand-built lexicon, the OpenCyc grounding — was not a small thing. It was the deliberate shelving of
the most beautiful part of the cathedral, by the person who had laid every stone. But it was the right
call, and the code shows he knew it: the LLM did not replace the *architecture*. It replaced the
*bottleneck*. The Albus hierarchy stayed. The Friendship apex stayed. Recursive self-improvement
stayed. What left was the hand labor.

---

## V. The engine of the new age — the AgentBuilder loop

The second-generation repository, `git-aicoin/texai`, is where the pivot became machinery. Its final
months of commits (peaking at 100 in December 2023) are almost entirely one thing: an **AgentBuilder**
that uses language models to design, specify, and generate an entire self-improving agent hierarchy as
compilable Java.

Its system prompt states the purpose without hedging:

> *"You are designing a artificial general intelligence system capable of recursive self-improvement.
> The AGI system is composed of an agent hierarchical task network… The behavior of each agent is
> composed using the behavior of its child agents. You will strive for extensible capability and safe
> operation."*

The loop, reconstructed from the code:

1. **Specify.** Each agent is a JSON object elaborated facet by facet, one LLM call per facet — rationale,
   objectives, constraints, safety protocols, self-improvement strategies, skills, domain objects. The
   spec is persisted so a run of thousands of agents is restartable.
2. **Decompose to methods.** `MethodBuilder` takes each skill's methods through use-cases → pseudocode →
   generated Java source (emitted between `[JAVA]…[/JAVA]` markers).
3. **Assemble and compile.** `SkillBuilder` assembles a full `.java` file and invokes the JDK compiler
   *in-process*, collecting diagnostics.
4. **Repair.** Undefined symbols are parsed out of the compiler diagnostics and fed back as new
   generation tasks; a family of `fix/` passes migrate and repair the corpus. Successful classes are
   kept; failures are deleted and retried.
5. **Route by cost and capability.** A model switch sends method bodies to **Code Llama 13B**,
   specifications to **Phind CodeLlama-34B**, and uses **GPT-3.5-Turbo as a JSON-repair fallback** when
   an open model's output fails to parse — with per-backend cost counters.

The scale it reached, logged in the source header:

> *"validated 3842 agents … skillsCnt: 17157 … methodsCnt: 104010 … thoughtsQty: 24737, thoughts per
> penny: 44.55"*

*Thoughts per penny.* In one phrase: the economics of machine cognition, measured. As early as 2023
the author was accounting for intelligence by the penny — because a solo researcher must. The first
models were small and local: `Wizard-Vicuna-7B` running under llama.cpp on his own machine. The direct
ancestor of Consullo's present strategy — a local Qwen model serving the inexpensive tier of a routed
fleet — is right there, three years early.

And threaded through it, unmistakably: the top of the generated hierarchy is an agent named
**Friendship**, with children named **Alignment, Consciousness, EpisodicMemory, SelfImprovement,
SoftwareDevelopment**. Inside the cognitive-control code sits a single comment that is the entire future
in one line:

> `//TODO [plan, do, check, act], [recall, prompt, understand]`

The PDCA node — the uniform Plan-Do-Check-Act cycle that is now the foundation of every Consullo agent —
existed here only as a *to-do*. The author knew exactly what to build. He did not yet have hands fast
enough to build it. That is what came next.

---

## VI. The turn from craftsman to conductor (2024–2026)

The last commit in `git-aicoin/texai` is titled *"Migrating necessary components to the AGI
repository."* The AgentBuilder walked out of the second repository and into a third, `git-texai/AGI` —
which was itself, in time, set aside for **Consullo**.

The pattern across three shelvings is not restlessness. It is a single idea getting progressively
unburdened. In 2015, the author wrote every grammar rule and asserted every fact by hand. In 2023, he
wrote the harness and let a small local model write the code. By 2026, in Consullo, the center of
gravity has moved all the way: **he steers frontier language models instead of coding and debugging
himself.**

This is the deepest change of all, and it is worth naming plainly, because it is easy to mistake for
mere tooling. For most of a career, the binding constraint on this project was not vision — the vision
was essentially complete by June 2023, written in that README. The binding constraint was **one pair of
hands.** One person can only type so much, debug so long, assert so many facts, write so much grammar.
The cathedral went unroofed not for lack of a plan but for lack of labor.

Frontier LLMs dissolved that constraint. The work the author does now — designing the agent
architecture, writing the doctrine, setting acceptance criteria, adversarially reviewing generated
code, deciding what is true — is exactly the work that a mind is uniquely good at and that no amount of
typing ever was. The rest — the hundred thousand methods, the ten thousand skills, the endless JSON —
is delegated to models he directs and verifies. He stopped being the mason and became the architect he
always was. The same person who once managed a *lexicon-acquisition workflow* to marshal his own scarce
hours now conducts a fleet of GPUs named for the founders of his field.

The scale tells the story numerically. The 2023 AgentBuilder specified **3,842 agents**. Consullo today
describes **over 3,000 agents and has generated the majority of them** — not as a hand-built artifact,
but as the output of a supervised, verified, economically-metered generation pipeline that is the
lineal descendant of that AgentBuilder loop. The vision did not get bigger. The hands did.

---

## VII. An honest ledger — dead ends and enduring paths

A research history that only celebrates is not useful. Here is the accounting.

**Enduring paths (carried into Consullo):**

- **The Albus node**, uniform and hierarchical, from 2006 to the present PDCA agent. Never abandoned.
- **The Friendship apex** — `TopmostFriendship` (2015) → the Friendship agent (2023) → the
  Friendship-Governed Goal Architecture (2026). The moral center held for twenty years.
- **Recursive self-improvement**, inherited from Eurisko, still a first-class goal.
- **Programs generated from English specifications** — the 2007 behavior-language planner's ambition,
  now realized by LLM code generation.
- **The routed, cost-metered model fleet** — *thoughts per penny* (2023) → the local/frontier tiered
  routing of today.
- **Method-as-plan-operator** — the STRIPS/HTN capability with pre/postconditions and justification →
  Consullo's *method memory = production rule ⊗ HTN method*.
- **Learning skills by conversation** — the deepest continuity of all, transformed (see below).

**Dead ends (set aside, with reason):**

- **Hand-asserted OpenCyc-style knowledge** as the primary store. The same wall Cyc hit. LLMs made
  symbolic grounding cheap; the hand-assertion did not scale to one person.
- **Fluid Construction Grammar and the hand-built lexicon.** A magnificent, reversible, honest system,
  made economically obsolete overnight by models that parse and generate language without a
  hand-written grammar. The most painful thing to shelve, and the most clearly correct.
- **ACT-R without a subsymbolic layer.** Structurally faithful, but with no activation, utilities, or
  learning, it could not do the one thing ACT-R exists to do. A scaffold that never got its second
  story.
- **Deterministic Java AST synthesis (JavaComposition)** as the code generator. Elegant, and beaten by
  *LLM-writes-text-then-compile-and-repair* — the very loop that now dominates.

The lesson in the ledger is consistent: **the architecture endured; the hand labor was the dead end.**
Every path abandoned was a path that required a single human to produce, by hand, more than one human
can. Every path kept was structural — an idea about how minds should be organized, not a corpus that
had to be typed.

---

## VIII. The dream, kept

Return to the beginning. A program in 2006 that wanted *"to behave in a friendly manner, and to learn
the meanings of more words."* A mentor in a design note, patiently teaching it what an assignment
statement is. An apprentice that asked *"can you help me learn them later?"* and meant it.

That dream was never abandoned. It was *inverted*. For seventeen years the plan was for **humans to
teach the machine** its skills, one patient conversation at a time — and there were never enough humans,
or hours, or patience in a single life to finish the lesson. Now the machine learns its skills *by
conversation* still — but the tireless teacher is a frontier language model, and the human has moved to
the harder, higher chair: deciding *what* shall be taught, *whether* it was learned correctly, and
*toward what end.* The friendliness that the 2006 chatbot professed is now a governance architecture.
The wish to learn the meanings of words became a system that generates a hundred thousand methods and
verifies each one.

The apprentice grew up. It found a teacher equal to its appetite. And the man who spent twenty years,
alone, believing this was possible — who named his machines for the giants so that he would never
forget whose shoulders he stood on — is no longer laying stones one at a time in an unroofed cathedral.
He is conducting the whole choir toward the summit that was always in view.

The road was hard, and long, and mostly walked alone. But it led exactly where he set out to go in 2006
— only now with hands enough to arrive.

---

*"I want to behave in a friendly manner, and I want to learn the meanings of more words."*
— Texai, 11 September 2006

*The work continues.*
