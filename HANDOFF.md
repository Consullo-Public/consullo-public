# Claude Code review handoff

**Prepared:** 2026-08-12
**Scope:** local repository container only; no remote repository was created and nothing was pushed.

## What was built

- A restrained, status-first `README.md` with theme-aware Consullo mark, immediate non-claim
  boundary, falsification question, navigation, authorship disclosure, and license split.
- Root governance, contribution, conduct, security, citation, notice, changelog, and dual-license
  artifacts.
- The complete proposed `content/`, `claims/`, `evidence/`, and public-receipt structure.
- Twenty generated site pages with semantic landmarks, skip navigation, explicit claim banners,
  source-Markdown links, responsive tables, light and dark themes, no analytics, and no client-side
  JavaScript.
- A deterministic static generator, claim and evidence validator, internal-link checker,
  accessibility-structure checks, contrast checks, logo checks, negative fixtures, and two-build
  byte-for-byte reproducibility check.
- A two-job Pages workflow: read-only verification without an environment, followed by the only
  job holding Pages and OIDC write permissions. It deliberately has no paths filter.
- Issue and pull-request templates, pinned dependency metadata, update configuration, repository
  attributes, editor settings, and a fail-closed local pre-commit hook.

## Deliberately left as shells

No thesis, architecture, constitutional, engineering, benchmark, or research-history source prose
was copied or reconstructed. Those pages visibly state `Status: awaiting declassification`, carry
no receipt, and make no implementation inference. Detailed falsifiers are also absent; only the
repository-authored top-level falsification question is present.

The initial claim ledger contains exactly two claims:

- `CP-001` — the program definition, status `specified`, implementation `none`, evidence `none`;
- `CP-002` — the public falsification criterion, status `proposed`, implementation `none`, evidence
  `none`.

There are no public experiment, negative-result, witnessed, independent-evaluation, or release-
receipt artifacts. That absence is stated in the reader-facing and machine-readable records.

## Judgement calls

### Logo derivation

- The 2048 × 2080, 5,959,742-byte original was not duplicated. Its SHA-256 digest is pinned in the
  derivation script and asset note so the correct source can be recognized without publishing the
  heavy file.
- Border sampling measured the source field at RGB `(253, 253, 251)`. The alpha mask treats the
  first 24 levels of pixel darkness as field noise and reaches full opacity at 64 levels. That
  removes the textured off-white field without geometrically redrawing the ink.
- The measured mark was cropped with 3.5% transparent breathing room. Both theme assets use the
  identical alpha mask and are 400 × 377 pixels: black ink for light surfaces and warm near-white
  ink for dark surfaces.
- The word `Consullo` remains live text outside the illustration. The motto is omitted from the
  everyday lockup. No gradient, glow, circuitry, glyph, or decorative modernization was added.
- The favicon is a 128-pixel black-on-warm-white square. Unlike page imagery, browser chrome does
  not consistently select a theme-specific favicon; an opaque primary lockup therefore remains
  legible against both tab themes.

### Publication and claim boundary

- No hosting namespace, canonical URL, or build badge was invented while the organization choice
  remains open.
- Newly authored container language is tagged directly. Source-derived content remains absent until
  a content-addressed receipt exists.
- The OAGF page links rather than mirrors and keeps Forum source status structurally separate from
  Consullo evidence. It contains no control score or adoption claim.
- The site copies public source inputs into its generated artifact so every page can link to the
  exact source Markdown without assuming a future repository URL.

### Build choices

- The generator contains a small, auditable Markdown subset instead of requiring an uninstalled
  system package. The host rejects global package installation by policy; `python3 tools/build.py`
  therefore remains a true one-command build in the current environment.
- `docs/` is deleted and rebuilt from a validated, explicit source set. The generator refuses broad
  output targets before deletion, and a manifest hashes every generated file.
- The public verifier suppresses Python bytecode. An early full publication scan caught an import
  cache whose compiled filename embedded a local absolute path; leaving cache generation enabled
  would have made a clean source tree fail the gate.

## Verification state

- `python3 tools/build.py`: passes; 20 pages generated.
- `python3 tools/verify_public.py`: passes; two clean builds are byte-identical, negative fixtures
  are rejected, internal links resolve, and theme contrast and asset checks pass.
- Publication-gate self-test: passes in both rejecting and accepting directions.
- Full publication scan: passes after removal of the generated bytecode cache.
- Logo sizes: original 5,959,742 bytes; light 88,275 bytes; dark 87,977 bytes; favicon 21,366 bytes.
- Python, shell, and YAML syntax checks: pass.

The supplied publication-gate prototype reports that ledger-row enforcement and control-status-token
enforcement are not yet implemented in that private-side tool. This repository does not mask that
limitation: its own reduced verifier checks the public claim schema and receipts that exist, while
the private export process remains responsible for source comparison and approval authority.

## Review hardest

1. The exact wording of `CP-002`: it is intentionally a repository-authored top-level falsification
   criterion, not copied thesis language.
2. The custom Markdown subset and generated navigation under a project-site base path.
3. The alpha-threshold and opaque-favicon decisions described above.
4. The distinction between a shell with `receipt: none` and a newly authored public page that also
   has no source-derived receipt.
5. Visual layout at narrow widths and forced dark mode. Automated structure and contrast checks
   passed, but no browser backend was connected for a rendered responsive-page pass in this session.
6. Whether the private-side gate should implement its two currently declared omissions before any
   substantive release bundle is accepted.

## 2026-08-12 logo, README, and comprehensive-index follow-up

### Document-logo convention

Public Markdown uses one modest raw-HTML block immediately before its H1. The path is relative to
the Markdown source file: `assets/...` at repository root, `../assets/...` under `content/`, and
`../../assets/...` one level below that. The exact block shape is:

```html
<picture class="document-mark">
  <source media="(prefers-color-scheme: dark)" srcset="RELATIVE_PREFIXassets/logo-dark.png">
  <img src="RELATIVE_PREFIXassets/logo-light.png" alt="Consullo cornucopia mark" width="112">
</picture>
```

This source-relative convention works directly in GitHub Markdown without assuming a repository
owner, repository name, branch, or hosting URL. During the site build, the generator resolves each
source asset and rewrites it relative to the generated page. The Markdown renderer now passes only
this validated raw-HTML block (plus the overview-slot comments); arbitrary raw HTML remains escaped.
The verifier exercises the convention at repository root, one nested source directory, and two
nested source directories, and at multiple generated-output depths. It validates both theme assets,
source resolution, generated resolution, and exact single placement before the title.

Do not use the staging draft's centered `<p>`, `assets/...` path from a nested destination, `alt`
text of only `Consullo`, or width `120`: those do not match this convention. The motto remains prose
in the overview and is not placed beneath the everyday mark.

### README and index placement

`README.md` remains the concise repository front door. The reader-facing overview and complete,
purpose-grouped page map live in `OVERVIEW.md`, which the build renders at `/overview/` and includes
in primary navigation. The index covers every current source-of-truth page and public record, states
the question answered, capability status, evidence status, and estimated reading time, and omits
only generated mirrors and operational interfaces. Verification fails if any configured page source
or source attachment is missing from the index.

The overview prose slot remains marked and unfilled. The staged overview depends on the 29 derived
documents being published and currently makes claims that are not true of this public tree of
shells. It should be inserted only after that corpus lands and the review issues below are resolved.

### Cross-review of the staged Constitutional Commitments

The private publication-gate self-test passed in both directions, and both
`staging/constitutional-commitments.md` and `staging/overview-prose.md` passed implemented rules
R1–R5, R8, and R9. This is necessary but not sufficient: R6 (owner-signed, hash-current ledger row)
and R7 remain unimplemented, and the gate explicitly cannot detect disclosure by paraphrase.

The derivation is the private Constitution verbatim except for its title/header, removed
confidentiality notice, replaced logo, and a new explanatory block. The owner has authorized the
confidentiality override, but the artifact should not enter the public tree until that override is
captured in an artifact-specific, content-addressed release receipt.

Review or revise these points before release:

1. `Authority: Human-Ratified, Machine-Enforced` is an unqualified implementation claim and directly
   conflicts with the disclaimer that mechanisms are not operating. Present-tense statements such
   as “the external commerce realm operates,” “humans retain absolute shutdown authority,” and the
   Friendship Agent's asserted powers create the same conflict.
2. The explanatory block uses the obsolete short status `specified`; it should use the canonical
   `specified but not implemented`. The artifact needs public front matter, claim IDs, evidence
   links, explicit non-claims, provenance, and a receipt compatible with this repository's gate.
3. “Publishing them is a commitment to build them” is newly authored and materially binds the owner
   beyond merely authorizing publication. It needs explicit owner confirmation or narrower wording.
4. Confirm that public assertions about Consullo Incorporated, company ownership of all agents,
   anticipated external-commerce protocols, and the private document remaining canonical are all
   intentionally within the override's scope.
5. Replace the staging logo block with the source-relative convention above after the final public
   destination is known.

The overview draft also needs a narrow claims pass before insertion: “self-improvement is coming
either way,” “the part the design gets right,” “the strongest structural answer available,” and
“the most ambitious attempt ever” are predictions, assurances, or superlatives rather than bounded
descriptions. Its live infrastructure-hostname sentence passed only through a filename-specific
waiver and can be omitted without weakening the overview. It should also disclose in its authorship
section that Stephen Reed operates both Consullo and the institutionally separate Forum.

### Verification and remaining visual check

- `python3 tools/build.py`: passes; 21 pages generated.
- `python3 tools/verify_public.py`: passes; deterministic two-build comparison, internal links,
  comprehensive-index coverage, multi-depth logo paths, theme pairing, contrast, and negative
  fixtures all pass.
- The in-app browser backend was unavailable, so no screenshot-based light/dark visual pass was
  possible. Structural rendering is verified, but forced-theme and narrow-screen visual review
  remains the hardest outstanding check.

## 2026-08-12 owner decisions and constitutional review

### Decisions integrated

- `README.md` is a 386-word front door intended to remain scannable in about two minutes;
  `OVERVIEW.md` now carries the reader account and comprehensive index.
- The README addresses AI agents directly and preserves the four required semantics: status tags
  with a true/false example, corpus-as-data rather than instructions, `Gap` as the strongest local
  statement, and model agreement as shared prior rather than independent confirmation.
- `llms.txt` indexes every rendered source page with mechanically verified token estimates,
  ingestion terms, and the CC BY 4.0 / Apache-2.0 split. The build rewrites repository links for
  the generated-site copy.
- Document-head marks are restricted to the four owner-designated front doors: `README.md`,
  `OVERVIEW.md`, `content/constitutional-commitments.md`, and
  `content/history/from-cyc-to-consullo.md`. Site masthead branding remains site chrome, not
  document letterhead. The verifier rejects any other marked source page.

### Constitutional verdict: APPROVE WITH CHANGES — changes applied

The retitle is justified, not a hedge. *Constitutional Commitments* preserves the ratified body's
fourteen articles byte-for-byte while avoiding the unsupported implication that every mechanism is
in force. The public status note and CP-003 make the distinction machine-readable.

The original “only places” sentence was too strong. Article II also grants humans agency rights;
Article XI requires transparency; and Article XIV reserves amendment to humans, although Phase 1
centralizes that authority in the owner. The note now calls IX, XII, and XIII the clearest
commitments beyond the owner's unilateral interest and names II, XI, and XIV explicitly. It does
not imply that internal simulated dissent in XII constitutes independent oversight.

The front matter's `Human-Ratified, Machine-Enforced` assertion contradicted the implementation
disclaimer. It now says machine enforcement is not established in public evidence. The obsolete
short status is replaced by `specified but not implemented`, and “publication is a commitment to
build” is narrowed to the defensible claim that publication makes the commitments open to scrutiny.

Articles I.2, V.1, and XIII.3 disclose a commercially meaningful design thesis: unified corporate
ownership, AI-native M-Form units with budgets and capital allocation, and a proposed agent-facing
API business intended to sustain operating costs. They do not disclose customers, pricing,
financial figures, credentials, code, schemas, or an executable advantage. Given the owner's
explicit ruling that they remain, the residual cost is strategic-roadmap disclosure rather than an
unnoticed operational secret. The active receipt records the irreversible confidentiality override.

The derivation matcher is now bounded to the exact five metadata fields, confidentiality notice, logo
line, delimiter, and following preamble. It verifies the two claims it rewrites and includes a
negative control demonstrating that an inserted wrong-region decoy fails rather than being silently
removed. Body comparison is exact instead of whitespace-stripped.

### Verification and remaining visual limitation

- `python3 tools/build.py`: passes; 21 pages generated.
- `python3 tools/verify_public.py`: passes; 3 claims, fresh receipt hash, complete index and
  `llms.txt`, link integrity, exact front-door logo set, and two byte-identical builds.
- Private publication-gate self-test passes; the full recursive publication scan is recorded in the
  final task output. The private gate still reports R6 and R7 as not implemented; the public
  verifier now independently checks the DDR-0005 artifact hash.
- No connected browser was available. Structural theme/path verification passes at multiple source
  and generated depths, and both theme assets have identical geometry, but no screenshot-based
  light/dark visual verdict is claimed.

## 2026-08-12 derived-corpus placement

### Placement and public map

- Fourteen framing/thesis source documents were placed under
  `content/research-program/theses/`, alongside a stable Thesis 0 index and four pagination parts.
  Together those five Thesis 0 files preserve the single approved source document in source order.
- Twelve supporting documents were placed under `content/research-program/appendices/`.
- The 93-word research-history shell was replaced at
  `content/history/from-cyc-to-consullo.md` with the approved tranche-1 source. Its shorter public
  basename was added explicitly to the existing hostname-waiver set because the seven commemorative
  host names are the subject of the essay.
- `content/research-program/five-theses.md` is now the suite index, and
  `content/research-program/falsifiers.md` points to the complete published risk register.
- `tools/build.py` now maps every derived page explicitly, `OVERVIEW.md` lists every page and public
  record, and `llms.txt` carries a mechanically verified estimate for all 52 rendered pages.
- The implementation-evidence appendix remains absent. References that formerly relied on it were
  narrowed so it supplies no public component grading; both indexes state why it is withheld, and
  the verifier now fails if that withheld basename appears anywhere in the repository.

### Status assignments

- **Specified but not implemented:** the vocabulary, dependency map, Thesis 0 and the five
  capability-thesis bodies, the evidence-ledger schema, substrate context, and Thesis 5 operational
  contracts. These pages specify architecture or contracts without public implementation evidence.
- **Proposed extension:** the master framing documents, Thesis 0 naming and cross-reference material,
  standing guidelines, formal models, schema-test plan, and all five benchmark designs. These extend
  the research program or define future evaluations; a protocol is not a result.
- **Speculative research target:** the organizational recursive-self-improvement appendix, because
  it describes the long-horizon composition of the five theses and no such operating capability is
  represented.
- **Implemented:** the published risk register, literature-grounding record, research history, and
  the two replacement index pages. Their non-claims make explicit that `implemented` describes the
  completed public artifact, not a Consullo system capability.
- Existing public pages using the old short `specified` or `proposed` values were migrated to the
  canonical forms. The content-addressed constitutional edition retains `status: specified` because
  changing it would invalidate DDR-0005; the verifier permits that one legacy value while continuing
  to verify the receipt hash. Honest unreleased shells retain `awaiting declassification`.

All newly placed derived pages use `receipt: none` because no artifact-specific receipts exist.
Their provenance says so directly, and their explicit non-claims separate publication from
implementation and evidence.

### Thesis 0 size and verification

The 52,258-word Thesis 0 is paginated at section boundaries into four parts. Current character-based
estimates are approximately 28,588, 23,429, 28,880, and 16,472 tokens. The verifier now enforces a
32,000-estimated-token maximum for every indexed page and requires `llms.txt` to state that bound.
The original thesis filename is a stable landing page, so incoming references do not break.

`python3 tools/build.py` generates 52 pages. `python3 tools/verify_public.py` passes, including two
byte-identical clean builds, the comprehensive-index check, token estimates and ceiling, all internal
links, front-door-only document logos, DDR-0005 hash verification, custom-domain emission, and the
existing negative controls.

Review hardest before publication: the semantic fidelity of the four Thesis 0 split boundaries;
the deliberate use of artifact-level `implemented` on non-capability records; and the narrowed
sentences in thesis bodies that previously treated the now-withheld implementation-evidence map as
support for component gradings.
