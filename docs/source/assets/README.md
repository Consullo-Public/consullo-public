# Brand assets

The committed assets are deterministic derivatives of the approved Consullo cornucopia mark. The
large original is retained in the private brand archive rather than duplicated in this repository.

| Asset | Use | Treatment |
|---|---|---|
| `logo-light.png` | Light-theme README and site | Black ink on transparent background |
| `logo-dark.png` | Dark-theme README and site | Near-white ink on transparent background |
| `favicon.png` | Small square site icon | Black ink on a warm-white square canvas |

The source measured 2048 × 2080 pixels and 5,959,742 bytes. It was fully opaque, had an off-white
background, and carried substantial dead margin. Derivation removes the background by measuring
pixel distance from the sampled border color, preserves the original ink shape, trims to the mark,
adds restrained transparent padding, and resamples to the delivery sizes. No text, motto, new glyph,
or stylistic element is embedded in the illustration.

The README and generated site select light and dark assets with `prefers-color-scheme`. The visible
name is typeset outside the mark, preserving the lockup boundary.

The favicon uses an opaque primary lockup because browser chrome does not consistently honor
theme-specific favicon selection; the light field preserves legibility in both light and dark tabs.

The measured source digest is
`cc0880d5c3c51b94304d078e19bbdaa81af648f4892046a2aae5f8075fb61632`. Run
`python3 tools/derive_logo.py --source PATH` only against a source whose digest matches that value.
