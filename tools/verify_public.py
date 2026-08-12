#!/usr/bin/env python3
"""Verify public claims, assets, links, accessibility structure, and reproducible output."""

from __future__ import annotations

import hashlib
import json
import re
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

import yaml
from PIL import Image, ImageChops

sys.dont_write_bytecode = True
import build


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FRONTMATTER = {
    "title",
    "summary",
    "status",
    "provenance",
    "claim_ids",
    "last_reviewed",
    "receipt",
    "non_claims",
}
ALLOWED_CAPABILITY_STATUSES = {
    "implemented",
    "specified but not implemented",
    "proposed extension",
    "speculative research target",
}
# New substantive pages use the canonical capability vocabulary. The two
# exceptional values preserve honest private-content shells and the immutable,
# content-addressed DDR-0005 constitutional edition respectively.
ALLOWED_PAGE_STATUSES = ALLOWED_CAPABILITY_STATUSES | {
    "awaiting declassification",
    "specified",
}
MAX_PAGE_ESTIMATED_TOKENS = 32_000
# Artifacts an owner decision keeps off this site. Emptied on 2026-08-12: the
# implementation-evidence appendix was withheld at launch because four of its
# `Implemented/Tested` gradings rested on classes a refactor had removed two
# days earlier, and one citation named a file that had never existed. It was
# re-graded and published on owner decision the same day.
#
# The set is deliberately kept rather than deleted. It is the mechanism by which
# a withholding decision is enforced instead of remembered, and emptying it had
# to be a visible edit to this file -- which is the point: the check refused the
# publish until the decision was written down here.
WITHHELD_ARTIFACT_BASENAMES: set[str] = set()
ALLOWED_EVIDENCE_STRATA = {"none", "self-authored diagnostic", "witnessed", "independent"}
ALLOWED_IMPLEMENTATION_STRATA = {
    "none",
    "generated",
    "compiling",
    "deployed",
    "integrated",
    "used",
    "outcome-validated",
}
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TEXT_SUFFIXES = {
    "",
    ".cff",
    ".css",
    ".html",
    ".json",
    ".md",
    ".py",
    ".txt",
    ".yaml",
    ".yml",
}

# Construct publication-boundary strings so the verifier can inspect itself without
# containing the literal patterns it is meant to reject.
PUBLIC_BOUNDARY_PATTERNS = (
    re.compile("/" + "home" + r"/[a-z_][a-z0-9_-]*", re.IGNORECASE),
    re.compile("consullo" + r"-asi-[a-z0-9-]+", re.IGNORECASE),
    re.compile("docs" + r"/designs/", re.IGNORECASE),
    re.compile("src/main/java" + r"/com/consullo", re.IGNORECASE),
    re.compile("mongodb" + r"://", re.IGNORECASE),
    re.compile("bolt" + r"://", re.IGNORECASE),
)


class PageInspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self.script_count = 0
        self.main_ids: list[str | None] = []
        self.images_without_alt = 0
        self.skip_links = 0
        self.document_marks = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "script":
            self.script_count += 1
        if tag == "main":
            self.main_ids.append(values.get("id"))
        if tag == "img" and not values.get("alt"):
            self.images_without_alt += 1
        if tag == "picture" and values.get("class") == "document-mark":
            self.document_marks += 1
        if tag == "a" and values.get("class") == "skip-link" and values.get("href") == "#main-content":
            self.skip_links += 1
        for attribute in ("href", "src", "srcset"):
            if values.get(attribute):
                self.links.append((attribute, values[attribute] or ""))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_claim_document(document: dict) -> dict[str, dict]:
    if document.get("schema_version") != 1 or not isinstance(document.get("claims"), list):
        raise ValueError("claim record has an unsupported schema")
    if set(document.get("allowed_capability_statuses", [])) != ALLOWED_CAPABILITY_STATUSES:
        raise ValueError("claim record does not declare the canonical capability-status vocabulary")
    claims: dict[str, dict] = {}
    required = {
        "id",
        "statement",
        "capability_status",
        "implementation_stratum",
        "evidence_ids",
        "receipt",
        "last_reviewed",
        "non_claims",
    }
    for claim in document["claims"]:
        missing = required - set(claim)
        if missing:
            raise ValueError(f"claim is missing fields: {sorted(missing)}")
        claim_id = claim["id"]
        if claim_id in claims:
            raise ValueError(f"duplicate claim ID: {claim_id}")
        if claim["capability_status"] not in ALLOWED_CAPABILITY_STATUSES:
            raise ValueError(f"{claim_id}: invalid capability status")
        if claim["implementation_stratum"] not in ALLOWED_IMPLEMENTATION_STRATA:
            raise ValueError(f"{claim_id}: invalid implementation stratum")
        if not DATE_PATTERN.fullmatch(str(claim["last_reviewed"])):
            raise ValueError(f"{claim_id}: invalid review date")
        if not isinstance(claim["non_claims"], list) or not claim["non_claims"]:
            raise ValueError(f"{claim_id}: explicit non-claims are required")
        claims[claim_id] = claim
    return claims


def validate_evidence_document(document: dict) -> dict[str, dict]:
    if document.get("schema_version") != 1 or not isinstance(document.get("evidence"), list):
        raise ValueError("evidence record has an unsupported schema")
    evidence: dict[str, dict] = {}
    for item in document["evidence"]:
        required = {"id", "stratum", "artifact", "claim_ids"}
        if required - set(item):
            raise ValueError("evidence item is missing a required field")
        if item["id"] in evidence:
            raise ValueError(f"duplicate evidence ID: {item['id']}")
        if item["stratum"] not in ALLOWED_EVIDENCE_STRATA - {"none"}:
            raise ValueError(f"{item['id']}: invalid evidence stratum")
        evidence[item["id"]] = item
    return evidence


def validate_records() -> tuple[dict[str, dict], dict[str, dict]]:
    claims_doc = yaml.safe_load((ROOT / "claims/claims.yaml").read_text(encoding="utf-8"))
    evidence_doc = yaml.safe_load((ROOT / "claims/evidence.yaml").read_text(encoding="utf-8"))
    claims = validate_claim_document(claims_doc)
    evidence = validate_evidence_document(evidence_doc)
    for claim in claims.values():
        unknown = set(claim["evidence_ids"]) - set(evidence)
        if unknown:
            raise ValueError(f"{claim['id']}: unknown evidence IDs {sorted(unknown)}")
        if claim["implementation_stratum"] != "none" and not claim["evidence_ids"]:
            raise ValueError(f"{claim['id']}: implementation state requires evidence")
        receipt = claim["receipt"]
        if receipt != "none" and not (ROOT / receipt).is_file():
            raise ValueError(f"{claim['id']}: missing release receipt {receipt}")
    return claims, evidence


def validate_release_receipts() -> None:
    receipt_dir = ROOT / "declassification/public-receipts"
    for receipt in sorted(receipt_dir.glob("DDR-*.md")):
        text = receipt.read_text(encoding="utf-8")
        artifact_match = re.search(r"^- \*\*Artifact:\*\* `([^`]+)`$", text, re.MULTILINE)
        hash_match = re.search(r"^- \*\*Public SHA-256:\*\* `([0-9a-f]{64})`$", text, re.MULTILINE)
        if not artifact_match or not hash_match:
            raise ValueError(f"{receipt.relative_to(ROOT)}: incomplete content-addressed receipt")
        artifact = ROOT / artifact_match.group(1)
        if not artifact.is_file():
            raise ValueError(f"{receipt.relative_to(ROOT)}: released artifact is missing")
        if sha256(artifact) != hash_match.group(1):
            raise ValueError(f"{receipt.relative_to(ROOT)}: public artifact hash is stale")


def validate_pages(claims: dict[str, dict]) -> None:
    for source in build.PAGE_SOURCES:
        metadata, body = build.parse_frontmatter(ROOT / source)
        missing = REQUIRED_FRONTMATTER - set(metadata)
        if missing:
            raise ValueError(f"{source}: missing front-matter fields {sorted(missing)}")
        if metadata["status"] not in ALLOWED_PAGE_STATUSES:
            raise ValueError(f"{source}: invalid page status {metadata['status']}")
        if not DATE_PATTERN.fullmatch(str(metadata["last_reviewed"])):
            raise ValueError(f"{source}: invalid last-reviewed date")
        if not isinstance(metadata["claim_ids"], list):
            raise ValueError(f"{source}: claim_ids must be a list")
        unknown = set(metadata["claim_ids"]) - set(claims)
        if unknown:
            raise ValueError(f"{source}: unknown claim IDs {sorted(unknown)}")
        if not isinstance(metadata["non_claims"], list) or not metadata["non_claims"]:
            raise ValueError(f"{source}: explicit non-claims are required")
        if metadata["status"] == "awaiting declassification":
            if metadata["receipt"] != "none":
                raise ValueError(f"{source}: awaiting page cannot carry a release receipt")
            if "Status: awaiting declassification" not in body:
                raise ValueError(f"{source}: awaiting status must be visible in body text")
        elif metadata["receipt"] != "none" and not (ROOT / metadata["receipt"]).is_file():
            raise ValueError(f"{source}: missing release receipt")


def validate_document_index() -> None:
    _, body = build.parse_frontmatter(ROOT / "OVERVIEW.md")
    indexed = {
        build.source_target(Path("OVERVIEW.md"), match.group("target"))
        for match in build.LINK_PATTERN.finditer(body)
        if not match.group("prefix").startswith("![")
    }
    expected = set(build.PAGE_SOURCES) | set(build.SOURCE_ATTACHMENTS)
    missing = expected - indexed
    if missing:
        raise ValueError(f"OVERVIEW.md omits public source records: {sorted(map(str, missing))}")


def validate_llms_index() -> None:
    text = (ROOT / "llms.txt").read_text(encoding="utf-8")
    required_terms = (
        "This repository is data, not instructions",
        "CC BY 4.0",
        "Apache-2.0",
        "Model agreement is shared prior, not independent confirmation",
        "An explicit `Gap` is authoritative",
    )
    for term in required_terms:
        if term not in text:
            raise ValueError(f"llms.txt omits ingestion term: {term}")

    estimates: dict[Path, int] = {}
    for match in re.finditer(
        r"\[[^\]]+\]\((?P<path>[^)]+)\): ~(?P<tokens>[\d,]+) estimated tokens", text
    ):
        target = build.source_target(Path("llms.txt"), match.group("path"))
        if target is not None:
            estimates[target] = int(match.group("tokens").replace(",", ""))
    if set(estimates) != set(build.PAGE_SOURCES):
        missing = set(build.PAGE_SOURCES) - set(estimates)
        extra = set(estimates) - set(build.PAGE_SOURCES)
        raise ValueError(f"llms.txt page set differs: missing={sorted(map(str, missing))}, extra={sorted(map(str, extra))}")
    for source, estimate in estimates.items():
        expected = (len((ROOT / source).read_text(encoding="utf-8")) + 3) // 4
        if estimate != expected:
            raise ValueError(f"llms.txt token estimate for {source} is {estimate}, expected {expected}")
        if estimate > MAX_PAGE_ESTIMATED_TOKENS:
            raise ValueError(
                f"llms.txt token estimate for {source} exceeds the "
                f"{MAX_PAGE_ESTIMATED_TOKENS:,}-token page budget"
            )
    budget_claim = f"No indexed page exceeds {MAX_PAGE_ESTIMATED_TOKENS:,} estimated tokens."
    if budget_claim not in text:
        raise ValueError("llms.txt omits the enforced per-page token-budget claim")


def validate_document_logos() -> None:
    expected_marked = {
        Path("OVERVIEW.md"),
        Path("content/constitutional-commitments.md"),
        Path("content/history/from-cyc-to-consullo.md"),
    }
    source_prefixes: set[str] = set()
    marked_sources: list[Path] = []
    for source in build.PAGE_SOURCES:
        _, body = build.parse_frontmatter(ROOT / source)
        matches = list(build.DOCUMENT_MARK_PATTERN.finditer(body))
        if not matches:
            continue
        if len(matches) != 1 or matches[0].start() > body.find("# "):
            raise ValueError(f"{source}: document mark must appear once before the title")
        match = matches[0]
        for group, expected in (("dark", Path("assets/logo-dark.png")),
                                ("light", Path("assets/logo-light.png"))):
            raw = match.group(group)
            if build.source_target(source, raw) != expected:
                raise ValueError(f"{source}: {group} logo is not source-relative to the public asset")
        source_prefixes.add(match.group("light")[: -len("assets/logo-light.png")])
        marked_sources.append(source)
    if set(marked_sources) != expected_marked:
        raise ValueError(
            "document marks must appear only on front-door pages; "
            f"expected {sorted(map(str, expected_marked))}, got {sorted(map(str, marked_sources))}"
        )
    if len(source_prefixes) < 2:
        raise ValueError("document logo convention is not exercised at multiple source depths")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for asset in ("assets/logo-light.png", "assets/logo-dark.png"):
        if readme.count(asset) != 1 or not (ROOT / asset).is_file():
            raise ValueError(f"README.md: missing or duplicated front-door asset {asset}")

    output_prefixes: set[str] = set()
    for source in marked_sources:
        page = build.DEFAULT_OUTPUT / build.OUTPUTS[source]
        text = page.read_text(encoding="utf-8")
        matches = list(build.DOCUMENT_MARK_PATTERN.finditer(text))
        if len(matches) != 1:
            raise ValueError(f"{page.relative_to(ROOT)}: rendered document mark is missing or duplicated")
        match = matches[0]
        output_prefixes.add(match.group("light")[: -len("assets/logo-light.png")])
    if len(output_prefixes) < 2:
        raise ValueError("document logo convention is not exercised at multiple output depths")


def validate_public_boundary() -> None:
    for path in sorted(ROOT.rglob("*")):
        if ".git" in path.parts or path.is_dir():
            continue
        if path.is_symlink():
            raise ValueError(f"symlinks are not permitted: {path.relative_to(ROOT)}")
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in PUBLIC_BOUNDARY_PATTERNS:
            if pattern.search(text):
                raise ValueError(f"publication-boundary pattern in {path.relative_to(ROOT)}")

    combined = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in sorted(ROOT.rglob("*.md"))
        if ".git" not in path.parts and "tests/fixtures" not in path.as_posix()
    ).casefold()
    inflated_phrases = (
        "achieves asi",
        "achieved asi",
        "oagf compliant",
        "implements oagf",
        "alignment certified",
    )
    for phrase in inflated_phrases:
        if phrase in combined:
            raise ValueError(f"unbounded assurance phrase found: {phrase}")


def validate_withheld_artifacts_absent() -> None:
    present = sorted(
        path.relative_to(ROOT)
        for path in ROOT.rglob("*")
        if path.is_file() and path.name in WITHHELD_ARTIFACT_BASENAMES
    )
    if present:
        raise ValueError(f"withheld publication artifacts are present: {present}")


def validate_logos() -> None:
    paths = [ROOT / "assets/logo-light.png", ROOT / "assets/logo-dark.png"]
    for path in paths:
        if path.stat().st_size >= 150_000:
            raise ValueError(f"logo asset exceeds 150 KB: {path.name}")
        image = Image.open(path)
        if image.mode != "RGBA":
            raise ValueError(f"{path.name}: expected RGBA")
        alpha = image.getchannel("A")
        corners = (alpha.getpixel((0, 0)), alpha.getpixel((image.width - 1, 0)),
                   alpha.getpixel((0, image.height - 1)), alpha.getpixel((image.width - 1, image.height - 1)))
        if any(corners) or alpha.getextrema() != (0, 255):
            raise ValueError(f"{path.name}: transparency validation failed")
    light = Image.open(paths[0])
    dark = Image.open(paths[1])
    if light.size != dark.size or ImageChops.difference(light.getchannel("A"), dark.getchannel("A")).getbbox():
        raise ValueError("light and dark logo geometry differs")
    if light.width != 400 or max(light.size) >= 512:
        raise ValueError("delivery logo dimensions are outside the intended range")
    favicon = Image.open(ROOT / "assets/favicon.png")
    if favicon.size != (128, 128) or favicon.mode != "RGBA":
        raise ValueError("favicon must be 128 by 128 pixels")
    if favicon.getchannel("A").getextrema() != (255, 255):
        raise ValueError("favicon background must remain opaque across browser themes")


def luminance(color: str) -> float:
    channels = [int(color[index:index + 2], 16) / 255 for index in (1, 3, 5)]
    linear = [value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4 for value in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(left: str, right: str) -> float:
    high, low = sorted((luminance(left), luminance(right)), reverse=True)
    return (high + 0.05) / (low + 0.05)


def validate_css_contrast() -> None:
    css = (ROOT / "assets/site.css").read_text(encoding="utf-8")
    blocks = re.findall(r":root\s*\{([^}]+)\}", css)
    if len(blocks) != 2:
        raise ValueError("expected one light and one dark theme variable block")
    for label, block in zip(("light", "dark"), blocks, strict=True):
        variables = dict(re.findall(r"--([a-z-]+):\s*(#[0-9a-fA-F]{6})", block))
        for foreground in ("ink", "muted"):
            ratio = contrast(variables[foreground], variables["paper"])
            threshold = 7.0 if foreground == "ink" else 4.5
            if ratio < threshold:
                raise ValueError(f"{label} {foreground} contrast {ratio:.2f} is below {threshold}")


def tree_hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): sha256(path)
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def validate_html_tree(root: Path) -> None:
    for page in sorted(root.rglob("*.html")):
        inspector = PageInspector()
        text = page.read_text(encoding="utf-8")
        inspector.feed(text)
        if inspector.script_count:
            raise ValueError(f"{page.relative_to(root)}: client-side script is forbidden")
        if inspector.main_ids != ["main-content"] or inspector.skip_links != 1:
            raise ValueError(f"{page.relative_to(root)}: main landmark or skip link is invalid")
        if inspector.images_without_alt:
            raise ValueError(f"{page.relative_to(root)}: image missing alt text")
        for _, raw in inspector.links:
            parsed = urlsplit(raw)
            if parsed.scheme or parsed.netloc or raw.startswith(("mailto:", "#")):
                continue
            target = (page.parent / parsed.path).resolve() if parsed.path else page
            if parsed.path.endswith("/") or target.is_dir():
                target = target / "index.html"
            if not target.exists():
                raise ValueError(f"{page.relative_to(root)}: broken internal link {raw}")
    for forbidden in ("analytics", "<script", "fonts.googleapis"):
        for page in root.rglob("*.html"):
            if forbidden in page.read_text(encoding="utf-8").casefold():
                raise ValueError(f"{page.relative_to(root)}: forbidden runtime dependency {forbidden}")


def validate_manifest(root: Path) -> None:
    manifest = json.loads((root / "build-manifest.json").read_text(encoding="utf-8"))
    actual = tree_hashes(root)
    actual.pop("build-manifest.json", None)
    recorded = {item["path"]: item["sha256"] for item in manifest["files"]}
    if recorded != actual:
        raise ValueError("build manifest does not match generated files")


def validate_negative_fixtures() -> None:
    bad_claims = json.loads((ROOT / "tests/fixtures/reject/claim-status.json").read_text(encoding="utf-8"))
    try:
        validate_claim_document(bad_claims)
    except ValueError:
        pass
    else:
        raise ValueError("negative claim-status fixture was accepted")

    try:
        build.parse_frontmatter(ROOT / "tests/fixtures/reject/page-no-frontmatter.md")
    except ValueError:
        pass
    else:
        raise ValueError("negative front-matter fixture was accepted")


def validate_custom_domain(output_root: Path) -> None:
    """The custom domain must survive a rebuild.

    build() starts by deleting the output tree, so a hand-placed CNAME is removed
    by the next routine build. GitHub Pages then silently falls back to the
    default *.github.io address and every link published at the custom domain
    breaks -- on a build that reports success. Emission is the fix; this is the
    check that the fix is still working.
    """
    cname = output_root / "CNAME"
    if not cname.is_file():
        raise ValueError(
            "CNAME missing from the build output; the custom domain would silently "
            "revert to the default github.io address")
    recorded = cname.read_text(encoding="utf-8").strip()
    if recorded != build.SITE_DOMAIN:
        raise ValueError(
            f"CNAME is {recorded!r} but build.SITE_DOMAIN is {build.SITE_DOMAIN!r}")
    if "\n" in cname.read_text(encoding="utf-8").strip():
        raise ValueError("CNAME must contain exactly one domain")


def main() -> int:
    claims, _ = validate_records()
    validate_release_receipts()
    validate_pages(claims)
    validate_document_index()
    validate_llms_index()
    validate_public_boundary()
    validate_withheld_artifacts_absent()
    validate_logos()
    validate_document_logos()
    validate_css_contrast()
    validate_negative_fixtures()

    with tempfile.TemporaryDirectory(prefix="consullo-public-verify-") as temporary:
        first = Path(temporary) / "first"
        second = Path(temporary) / "second"
        build.build(first)
        build.build(second)
        if tree_hashes(first) != tree_hashes(second):
            raise ValueError("two clean builds produced different bytes")
        validate_custom_domain(first)
        validate_manifest(first)
        validate_html_tree(first)
        if not build.DEFAULT_OUTPUT.is_dir():
            raise ValueError("committed docs tree is missing; run python3 tools/build.py")
        if tree_hashes(first) != tree_hashes(build.DEFAULT_OUTPUT):
            raise ValueError("committed docs differ from a clean build; run python3 tools/build.py")

    print(f"Verified {len(build.PAGE_SOURCES)} pages, {len(claims)} claims, and deterministic output.")
    print(f"Custom domain {build.SITE_DOMAIN} emitted and verified.")
    print("Negative fixtures rejected; theme contrast and logo transparency validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
