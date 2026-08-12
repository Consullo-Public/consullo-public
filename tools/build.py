#!/usr/bin/env python3
"""Build the Consullo public site deterministically from repository Markdown."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import posixpath
import re
import shutil
from pathlib import Path, PurePosixPath

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "docs"
DERIVED_RESEARCH_SOURCES = (
    Path("content/research-program/theses/00-master-abstract.md"),
    Path("content/research-program/theses/00-master-introduction.md"),
    Path("content/research-program/theses/00-master-synthesis.md"),
    Path("content/research-program/theses/00-vocabulary-and-invariants.md"),
    Path("content/research-program/theses/00-cross-thesis-dependency-map.md"),
    Path("content/research-program/theses/00-thesis-0-naming.md"),
    Path("content/research-program/theses/friendship-governed-goal-architecture-thesis.md"),
    Path("content/research-program/theses/friendship-governed-goal-architecture-thesis-part-1.md"),
    Path("content/research-program/theses/friendship-governed-goal-architecture-thesis-part-2.md"),
    Path("content/research-program/theses/friendship-governed-goal-architecture-thesis-part-3.md"),
    Path("content/research-program/theses/friendship-governed-goal-architecture-thesis-part-4.md"),
    Path("content/research-program/theses/validated-improvement-loop-thesis.md"),
    Path("content/research-program/theses/multi-agent-cognitive-substrate-thesis.md"),
    Path("content/research-program/theses/causal-decision-foundations-thesis.md"),
    Path("content/research-program/theses/self-modifying-software-substrate-thesis.md"),
    Path("content/research-program/theses/alignment-invariants-and-scoped-trust-thesis.md"),
    Path("content/research-program/theses/risks-and-criticisms.md"),
    Path("content/research-program/theses/standing-guidelines-registry.md"),
    Path("content/research-program/theses/thesis-0-cross-reference-map.md"),
    Path("content/research-program/appendices/appendix-formal-models.md"),
    Path("content/research-program/appendices/appendix-evidence-ledger-schema.md"),
    Path("content/research-program/appendices/appendix-implementation-evidence-map.md"),
    Path("content/research-program/appendices/appendix-literature-grounding.md"),
    Path("content/research-program/appendices/appendix-substrates.md"),
    Path("content/research-program/appendices/appendix-organizational-recursive-self-improvement.md"),
    Path("content/research-program/appendices/appendix-thesis-0-schema-validation-tests.md"),
    Path("content/research-program/appendices/appendix-thesis-1-improvement-loop-benchmarks.md"),
    Path("content/research-program/appendices/appendix-thesis-2-cognitive-workflow-benchmarks.md"),
    Path("content/research-program/appendices/appendix-thesis-3-causal-decision-benchmarks.md"),
    Path("content/research-program/appendices/appendix-thesis-4-software-substrate-benchmarks.md"),
    Path("content/research-program/appendices/appendix-thesis-5-alignment-benchmarks.md"),
    Path("content/research-program/appendices/appendix-thesis-5-operational-contracts.md"),
)
PAGE_SOURCES = (
    Path("OVERVIEW.md"),
    Path("content/index.md"),
    Path("content/start-here.md"),
    Path("content/architecture.md"),
    Path("content/constitutional-commitments.md"),
    Path("content/research-program/five-theses.md"),
    Path("content/research-program/falsifiers.md"),
    Path("content/research-program/benchmarks.md"),
    Path("content/engineering/atomic-decomposition.md"),
    Path("content/engineering/llm-native-functional-java.md"),
    Path("content/engineering/empirical-self-improvement.md"),
    Path("content/history/from-cyc-to-consullo.md"),
    Path("content/governance/authority-and-custody.md"),
    Path("content/governance/oagf-relationship.md"),
    Path("content/governance/corrections.md"),
    Path("STATUS.md"),
    Path("GOVERNANCE.md"),
    Path("NOTICE.md"),
    Path("evidence/README.md"),
    Path("evidence/public-experiments/README.md"),
    Path("evidence/negative-results/README.md"),
) + DERIVED_RESEARCH_SOURCES

SOURCE_ATTACHMENTS = (
    Path("README.md"),
    Path("CHANGELOG.md"),
    Path("CITATION.cff"),
    Path("CODE_OF_CONDUCT.md"),
    Path("CONTRIBUTING.md"),
    Path("HANDOFF.md"),
    Path("LICENSE"),
    Path("LICENSE-CODE"),
    Path("llms.txt"),
    Path("SECURITY.md"),
    Path("assets/README.md"),
    Path("claims/claims.yaml"),
    Path("claims/evidence.yaml"),
    Path("claims/source-dispositions.yaml"),
    Path("declassification/RELEASES.md"),
    Path("declassification/public-receipts/README.md"),
    Path("declassification/public-receipts/DDR-0005.md"),
)

PUBLIC_ASSETS = {
    Path("assets/logo-light.png"),
    Path("assets/logo-dark.png"),
}

OUTPUTS = {
    Path("OVERVIEW.md"): Path("overview/index.html"),
    Path("content/index.md"): Path("index.html"),
    Path("content/start-here.md"): Path("start-here/index.html"),
    Path("content/architecture.md"): Path("architecture/index.html"),
    Path("content/constitutional-commitments.md"): Path("constitutional-commitments/index.html"),
    Path("content/research-program/five-theses.md"): Path("research-program/five-theses/index.html"),
    Path("content/research-program/falsifiers.md"): Path("research-program/falsifiers/index.html"),
    Path("content/research-program/benchmarks.md"): Path("research-program/benchmarks/index.html"),
    Path("content/engineering/atomic-decomposition.md"): Path("engineering/atomic-decomposition/index.html"),
    Path("content/engineering/llm-native-functional-java.md"): Path("engineering/llm-native-functional-java/index.html"),
    Path("content/engineering/empirical-self-improvement.md"): Path("engineering/empirical-self-improvement/index.html"),
    Path("content/history/from-cyc-to-consullo.md"): Path("history/from-cyc-to-consullo/index.html"),
    Path("content/governance/authority-and-custody.md"): Path("governance/authority-and-custody/index.html"),
    Path("content/governance/oagf-relationship.md"): Path("governance/oagf-relationship/index.html"),
    Path("content/governance/corrections.md"): Path("governance/corrections/index.html"),
    Path("STATUS.md"): Path("status/index.html"),
    Path("GOVERNANCE.md"): Path("governance/index.html"),
    Path("NOTICE.md"): Path("notices/index.html"),
    Path("evidence/README.md"): Path("evidence/index.html"),
    Path("evidence/public-experiments/README.md"): Path("evidence/public-experiments/index.html"),
    Path("evidence/negative-results/README.md"): Path("evidence/negative-results/index.html"),
    **{
        source: source.relative_to("content").with_suffix("") / "index.html"
        for source in DERIVED_RESEARCH_SOURCES
    },
}

NAVIGATION = (
    ("Start here", Path("content/start-here.md")),
    ("Document index", Path("OVERVIEW.md")),
    ("Architecture", Path("content/architecture.md")),
    ("Research program", Path("content/research-program/five-theses.md")),
    ("Governance", Path("GOVERNANCE.md")),
    ("Evidence and status", Path("STATUS.md")),
    ("Engineering", Path("content/engineering/atomic-decomposition.md")),
    ("History", Path("content/history/from-cyc-to-consullo.md")),
    ("Disclosures and corrections", Path("content/governance/corrections.md")),
)

LINK_PATTERN = re.compile(r"(?P<prefix>!?\[[^\]]*\]\()(?P<target>[^)]+)(?P<suffix>\))")
HTML_ASSET_PATTERN = re.compile(
    r'(?P<prefix>\b(?:src|srcset)=")(?P<target>[^"\s]+)(?P<suffix>")'
)
DOCUMENT_MARK_PATTERN = re.compile(
    r'<picture class="document-mark">\s*'
    r'<source media="\(prefers-color-scheme: dark\)" '
    r'srcset="(?P<dark>(?:\.\./)*assets/logo-dark\.png)">\s*'
    r'<img src="(?P<light>(?:\.\./)*assets/logo-light\.png)" '
    r'alt="Consullo cornucopia mark" width="112">\s*'
    r'</picture>',
    re.DOTALL,
)


def render_inline(value: str) -> str:
    """Render the deliberately small inline Markdown subset used by public pages."""
    escaped = html.escape(value, quote=False)
    placeholders: list[str] = []

    def preserve(fragment: str) -> str:
        token = f"\x00{len(placeholders)}\x00"
        placeholders.append(fragment)
        return token

    escaped = re.sub(
        r"`([^`]+)`",
        lambda match: preserve(f"<code>{match.group(1)}</code>"),
        escaped,
    )
    escaped = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda match: preserve(
            f'<a href="{html.escape(match.group(2), quote=True)}">{match.group(1)}</a>'
        ),
        escaped,
    )
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", escaped)
    for index, fragment in enumerate(placeholders):
        escaped = escaped.replace(f"\x00{index}\x00", fragment)
    return escaped


def heading_id(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    return slug or "section"


def markdown_to_html(source: str) -> str:
    """Render a deterministic, auditable block-Markdown subset with no runtime dependency."""
    lines = source.splitlines()
    output: list[str] = []
    index = 0

    def is_block_start(position: int) -> bool:
        line = lines[position]
        return bool(
            re.match(r"^(#{1,6})\s+", line)
            or line.startswith("```")
            or re.match(r"^>\s?", line)
            or re.match(r"^\s*(?:[-*]|\d+\.)\s+", line)
            or line == '<picture class="document-mark">'
            or re.fullmatch(r"<!-- (?:BEGIN|END) OVERVIEW PROSE SLOT -->", line)
        )

    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue

        if re.fullmatch(r"<!-- (?:BEGIN|END) OVERVIEW PROSE SLOT -->", line):
            index += 1
            continue

        if line == '<picture class="document-mark">':
            block = [line]
            index += 1
            while index < len(lines) and lines[index] != "</picture>":
                block.append(lines[index])
                index += 1
            if index == len(lines):
                raise ValueError("unclosed document mark")
            block.append(lines[index])
            index += 1
            fragment = "\n".join(block)
            if not DOCUMENT_MARK_PATTERN.fullmatch(fragment):
                raise ValueError("document mark does not match the public logo convention")
            output.append(fragment)
            continue

        if line.startswith("```"):
            language = line[3:].strip()
            index += 1
            code_lines = []
            while index < len(lines) and not lines[index].startswith("```"):
                code_lines.append(lines[index])
                index += 1
            if index == len(lines):
                raise ValueError("unclosed fenced code block")
            index += 1
            class_name = f' class="language-{html.escape(language, quote=True)}"' if language else ""
            output.append(f"<pre><code{class_name}>{html.escape(chr(10).join(code_lines))}</code></pre>")
            continue

        heading = re.match(r"^(#{1,6})\s+(.+?)\s*#*$", line)
        if heading:
            level = len(heading.group(1))
            title = heading.group(2)
            output.append(f'<h{level} id="{heading_id(title)}">{render_inline(title)}</h{level}>')
            index += 1
            continue

        if index + 1 < len(lines) and "|" in line and re.match(
            r"^\s*\|?\s*:?-{3,}", lines[index + 1]
        ):
            header_cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            index += 2
            rows = []
            while index < len(lines) and "|" in lines[index] and lines[index].strip():
                rows.append([cell.strip() for cell in lines[index].strip().strip("|").split("|")])
                index += 1
            head = "".join(f"<th>{render_inline(cell)}</th>" for cell in header_cells)
            body_rows = []
            for row in rows:
                padded = row + [""] * (len(header_cells) - len(row))
                body_rows.append("<tr>" + "".join(
                    f"<td>{render_inline(cell)}</td>" for cell in padded[: len(header_cells)]
                ) + "</tr>")
            output.append(
                '<div class="table-wrap"><table><thead><tr>' + head + "</tr></thead><tbody>"
                + "".join(body_rows) + "</tbody></table></div>"
            )
            continue

        if re.match(r"^>\s?", line):
            quote_lines = []
            while index < len(lines) and re.match(r"^>\s?", lines[index]):
                quote_lines.append(re.sub(r"^>\s?", "", lines[index]))
                index += 1
            output.append(f"<blockquote><p>{render_inline(' '.join(quote_lines))}</p></blockquote>")
            continue

        list_match = re.match(r"^\s*(?P<marker>[-*]|\d+\.)\s+(?P<text>.+)", line)
        if list_match:
            ordered = list_match.group("marker")[0].isdigit()
            tag = "ol" if ordered else "ul"
            items = []
            while index < len(lines):
                item = re.match(r"^\s*(?P<marker>[-*]|\d+\.)\s+(?P<text>.+)", lines[index])
                if not item or item.group("marker")[0].isdigit() != ordered:
                    break
                text = item.group("text")
                index += 1
                continuations = []
                while index < len(lines) and lines[index].startswith("  ") and lines[index].strip():
                    continuations.append(lines[index].strip())
                    index += 1
                if continuations:
                    text += " " + " ".join(continuations)
                items.append(f"<li>{render_inline(text)}</li>")
            output.append(f"<{tag}>" + "".join(items) + f"</{tag}>")
            continue

        paragraph = [line.strip()]
        index += 1
        while index < len(lines) and lines[index].strip() and not is_block_start(index):
            if index + 1 < len(lines) and "|" in lines[index] and re.match(
                r"^\s*\|?\s*:?-{3,}", lines[index + 1]
            ):
                break
            paragraph.append(lines[index].strip())
            index += 1
        output.append(f"<p>{render_inline(' '.join(paragraph))}</p>")

    return "\n".join(output)


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path.relative_to(ROOT)}: missing YAML front matter")
    try:
        _, raw_meta, body = text.split("---\n", 2)
    except ValueError as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: malformed YAML front matter") from exc
    metadata = yaml.safe_load(raw_meta)
    if not isinstance(metadata, dict):
        raise ValueError(f"{path.relative_to(ROOT)}: front matter must be a mapping")
    return metadata, body


def page_url(from_output: Path, to_output: Path) -> str:
    relative = posixpath.relpath(to_output.as_posix(), start=from_output.parent.as_posix())
    if relative == "index.html":
        return "./"
    if relative.endswith("/index.html"):
        return relative[: -len("index.html")]
    return relative


def source_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.split("#", 1)[0].split("?", 1)[0]
    if not target or "://" in target or target.startswith(("mailto:", "#")):
        return None
    candidate = (source.parent / target)
    if target.endswith("/"):
        candidate = candidate / "README.md"
    normalized = Path(os.path.normpath(candidate.as_posix()))
    return normalized


def rewrite_links(source: Path, output: Path, body: str) -> str:
    def replace(match: re.Match[str]) -> str:
        raw_target = match.group("target")
        target_path = source_target(source, raw_target)
        if target_path is None:
            return match.group(0)
        anchor = ""
        if "#" in raw_target:
            anchor = "#" + raw_target.split("#", 1)[1]
        if target_path in OUTPUTS:
            rewritten = page_url(output, OUTPUTS[target_path]) + anchor
        elif target_path in SOURCE_ATTACHMENTS:
            attachment = Path("source") / target_path
            rewritten = posixpath.relpath(attachment.as_posix(), start=output.parent.as_posix()) + anchor
        elif target_path in PUBLIC_ASSETS:
            rewritten = posixpath.relpath(target_path.as_posix(), start=output.parent.as_posix()) + anchor
        else:
            return match.group(0)
        return match.group("prefix") + rewritten + match.group("suffix")

    rewritten = LINK_PATTERN.sub(replace, body)

    def replace_html_asset(match: re.Match[str]) -> str:
        raw_target = match.group("target")
        target_path = source_target(source, raw_target)
        if target_path not in PUBLIC_ASSETS:
            return match.group(0)
        target = posixpath.relpath(target_path.as_posix(), start=output.parent.as_posix())
        return match.group("prefix") + target + match.group("suffix")

    return HTML_ASSET_PATTERN.sub(replace_html_asset, rewritten)


def render_llms_index() -> str:
    """Rewrite the repository-oriented llms.txt links for the generated site root."""
    source = Path("llms.txt")
    text = (ROOT / source).read_text(encoding="utf-8")

    def replace(match: re.Match[str]) -> str:
        target = source_target(source, match.group("target"))
        if target in OUTPUTS:
            rewritten = page_url(Path("llms.txt"), OUTPUTS[target])
        elif target in SOURCE_ATTACHMENTS:
            rewritten = (Path("source") / target).as_posix()
        else:
            return match.group(0)
        return match.group("prefix") + rewritten + match.group("suffix")

    return LINK_PATTERN.sub(replace, text)


def evidence_stratum(claim_ids: list[str], claims: dict[str, dict], evidence: dict[str, dict]) -> str:
    strata = []
    for claim_id in claim_ids:
        claim = claims[claim_id]
        if not claim["evidence_ids"]:
            strata.append("none")
        else:
            strata.extend(evidence[item]["stratum"] for item in claim["evidence_ids"])
    if not strata:
        return "none"
    order = {"none": 0, "self-authored diagnostic": 1, "witnessed": 2, "independent": 3}
    return max(strata, key=order.__getitem__)


def render_banner(metadata: dict, claims: dict[str, dict], evidence: dict[str, dict]) -> str:
    claim_ids = metadata.get("claim_ids", [])
    evidence_value = evidence_stratum(claim_ids, claims, evidence)
    receipt = metadata.get("receipt", "none")
    non_claims = metadata.get("non_claims", [])
    non_claim_items = "".join(f"<li>{html.escape(str(item))}</li>" for item in non_claims)
    details = ""
    if non_claim_items:
        details = (
            "<details><summary>Explicit non-claims</summary>"
            f"<ul>{non_claim_items}</ul></details>"
        )
    claim_value = ", ".join(claim_ids) if claim_ids else "none"
    return (
        '<aside class="claim-banner" aria-label="Claim and provenance status">'
        "<dl>"
        f"<dt>Status</dt><dd>{html.escape(str(metadata['status']))}</dd>"
        f"<dt>Claims</dt><dd>{html.escape(claim_value)}</dd>"
        f"<dt>Evidence</dt><dd>{html.escape(evidence_value)}</dd>"
        f"<dt>Provenance</dt><dd>{html.escape(str(metadata['provenance']))}</dd>"
        f"<dt>Receipt</dt><dd>{html.escape(str(receipt))}</dd>"
        f"<dt>Last reviewed</dt><dd>{html.escape(str(metadata['last_reviewed']))}</dd>"
        "</dl>"
        f"{details}</aside>"
    )


def load_records() -> tuple[dict[str, dict], dict[str, dict]]:
    claims_document = yaml.safe_load((ROOT / "claims/claims.yaml").read_text(encoding="utf-8"))
    evidence_document = yaml.safe_load((ROOT / "claims/evidence.yaml").read_text(encoding="utf-8"))
    claims = {item["id"]: item for item in claims_document["claims"]}
    evidence = {item["id"]: item for item in evidence_document["evidence"]}
    return claims, evidence


def nav_html(current_output: Path) -> str:
    items = []
    for label, source in NAVIGATION:
        target = OUTPUTS[source]
        current = ' aria-current="page"' if current_output == target else ""
        items.append(
            f'<li><a href="{html.escape(page_url(current_output, target))}"{current}>'
            f"{html.escape(label)}</a></li>"
        )
    return "".join(items)


def render_page(
    source: Path,
    output: Path,
    metadata: dict,
    body: str,
    claims: dict[str, dict],
    evidence: dict[str, dict],
) -> str:
    rewritten = rewrite_links(source, output, body)
    article = markdown_to_html(rewritten)
    root_prefix = posixpath.relpath(".", start=output.parent.as_posix())
    if root_prefix == ".":
        root_prefix = ""
    else:
        root_prefix += "/"
    source_copy = Path("source") / source
    source_link = posixpath.relpath(source_copy.as_posix(), start=output.parent.as_posix())
    title = html.escape(str(metadata["title"]))
    summary = html.escape(str(metadata["summary"]), quote=True)
    banner = render_banner(metadata, claims, evidence)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{summary}">
  <meta name="color-scheme" content="light dark">
  <title>{title} · Consullo</title>
  <link rel="icon" type="image/png" href="{root_prefix}assets/favicon.png">
  <link rel="stylesheet" href="{root_prefix}assets/site.css">
</head>
<body>
  <a class="skip-link" href="#main-content">Skip to content</a>
  <header class="site-header">
    <div class="masthead">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="{root_prefix}assets/logo-dark.png">
        <img src="{root_prefix}assets/logo-light.png" alt="Consullo cornucopia mark" width="74" height="70">
      </picture>
      <a class="wordmark" href="{root_prefix}">
        <strong>Consullo</strong>
        <span>Public research record</span>
      </a>
    </div>
    <nav class="site-nav" aria-label="Primary"><ul>{nav_html(output)}</ul></nav>
  </header>
  <main id="main-content">
    {banner}
    <article>{article}</article>
  </main>
  <footer class="site-footer"><div>
    <p><a href="{html.escape(source_link)}">Source Markdown</a> · Content CC BY 4.0 · Code Apache-2.0</p>
    <p>Build verification establishes reproducibility, not the truth of research claims.</p>
  </div></footer>
</body>
</html>
"""


def validate_output_path(output: Path) -> None:
    resolved = output.resolve()
    if resolved == ROOT or resolved == ROOT.parent or resolved == Path(resolved.anchor):
        raise ValueError(f"refusing unsafe output path: {resolved}")


# The public address. A SUBDOMAIN by deliberate choice, not the apex:
#   * the apex is left free for the company site, so the research record never
#     has to move -- and moving it is precisely the link rot this exists to avoid;
#   * a subdomain uses a CNAME to <org>.github.io, which follows GitHub's
#     infrastructure automatically, whereas an apex needs A records pinned to
#     GitHub IPs that can change beneath you;
#   * `.ai` matches what the record is about; `.com` is the company's.
#
# Changing this is a one-line edit here. Everything else derives from it.
SITE_DOMAIN = "research.consullo.ai"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(output_root: Path) -> None:
    validate_output_path(output_root)
    if output_root.exists():
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True)

    claims, evidence = load_records()
    for source in PAGE_SOURCES:
        metadata, body = parse_frontmatter(ROOT / source)
        output = OUTPUTS[source]
        destination = output_root / output
        destination.parent.mkdir(parents=True, exist_ok=True)
        rendered = render_page(source, output, metadata, body, claims, evidence)
        destination.write_text(rendered, encoding="utf-8", newline="\n")

        source_destination = output_root / "source" / source
        source_destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / source, source_destination)

    for attachment in SOURCE_ATTACHMENTS:
        destination = output_root / "source" / attachment
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / attachment, destination)

    (output_root / "llms.txt").write_text(
        render_llms_index(), encoding="utf-8", newline="\n"
    )

    assets_destination = output_root / "assets"
    assets_destination.mkdir()
    for asset in ("logo-light.png", "logo-dark.png", "favicon.png", "site.css"):
        shutil.copyfile(ROOT / "assets" / asset, assets_destination / asset)

    # CNAME must be EMITTED, never hand-placed. `build()` begins with
    # shutil.rmtree(output_root), so a CNAME dropped into docs/ by hand is
    # deleted by the next routine rebuild. GitHub Pages then silently reverts to
    # the default *.github.io address and every published link at the custom
    # domain breaks -- with no error, on a build that reports success.
    #
    # Emitting it makes the custom domain a build output like any other, and
    # verify_public.py asserts its presence and content so a regression here
    # fails the gate rather than the site.
    (output_root / "CNAME").write_text(SITE_DOMAIN + "\n", encoding="utf-8", newline="\n")

    (output_root / ".nojekyll").write_text("", encoding="utf-8")
    generated = sorted(
        path for path in output_root.rglob("*") if path.is_file() and path.name != "build-manifest.json"
    )
    manifest = {
        "schema_version": 1,
        "generator": "tools/build.py",
        "files": [
            {"path": path.relative_to(output_root).as_posix(), "sha256": sha256(path)}
            for path in generated
        ],
    }
    (output_root / "build-manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"Built {len(PAGE_SOURCES)} pages in {output_root}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    build(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
