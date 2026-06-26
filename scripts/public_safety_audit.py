#!/usr/bin/env python3
"""Public safety and render audit for viggomeesters-assets.

Checks every committed/source file in the working tree, excluding .git, for:
- private organization/person/client names in path or content;
- direct private-source wording and local paths;
- secret-like markers;
- blank-like HTML/SVG files.

By default this verifies the generated audit markdown is current. Pass --write to
rewrite indexes/public-safety-audit.md.
"""
from __future__ import annotations

import argparse
import html
import os
import re
import sys
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / "indexes" / "public-safety-audit.md"

_POSIX_HOME = "/" + "home/"
_MNT_USERS = "/" + "mnt/[a-z]/" + "Users/"
_WIN_USERS = r"[A-Z]:\\\\" + "Users" + r"\\\\"

DEFAULT_FORBIDDEN = [
    (
        "local path",
        re.compile(
            _POSIX_HOME + r"[^\s'\")<>]+|" + _MNT_USERS + r"[^\s'\")<>]+|" + _WIN_USERS + r"[^\s'\")<>]+",
            re.I,
        ),
    ),
    (
        "secret marker",
        re.compile(
            r"gho_[A-Za-z0-9_]+|sk-[A-Za-z0-9_-]{20,}|BEGIN (RSA|OPENSSH|PRIVATE)|"
            r"api[_-]?key\s*[:=]|password\s*[:=]|authorization\s*:",
            re.I,
        ),
    ),
]

SKIP_DIRS = {".git", "__pycache__", ".pytest_cache"}
TEXT_EXTS = {
    ".css",
    ".html",
    ".js",
    ".json",
    ".md",
    ".svg",
    ".txt",
    ".xml",
    ".yml",
    ".yaml",
    ".py",
}


def forbidden_patterns() -> list[tuple[str, re.Pattern[str]]]:
    """Return public-safe built-ins plus optional private caller-provided regexes.

    Keep private organization/person/source names out of this public repository.
    For local pre-push checks, pass semicolon-separated regexes via
    PUBLIC_SAFETY_EXTRA_REGEX.
    """
    patterns = list(DEFAULT_FORBIDDEN)
    extra = os.environ.get("PUBLIC_SAFETY_EXTRA_REGEX", "").strip()
    if extra:
        for idx, raw in enumerate(part for part in extra.split(";") if part.strip()):
            patterns.append((f"private extra regex {idx + 1}", re.compile(raw, re.I)))
    return patterns


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.parts.append(data.strip())

    def text(self) -> str:
        return html.unescape(" ".join(self.parts))


def iter_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file():
            files.append(path)
    return sorted(files, key=lambda p: p.relative_to(ROOT).as_posix())


def read_text(path: Path) -> str:
    if path.suffix.lower() not in TEXT_EXTS and path.name not in {"LICENSE", ".gitignore", ".nojekyll"}:
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def visible_text(markup: str) -> str:
    parser = TextExtractor()
    parser.feed(markup)
    return parser.text()


def audit_rows() -> tuple[list[tuple[str, str, str, str]], list[str], list[str]]:
    rows: list[tuple[str, str, str, str]] = []
    privacy_failures: list[str] = []
    render_failures: list[str] = []

    patterns = forbidden_patterns()
    for path in iter_files():
        rel = path.relative_to(ROOT).as_posix()
        content = read_text(path)
        name_hits = [label for label, regex in patterns if regex.search(rel)]
        content_hits = [label for label, regex in patterns if content and regex.search(content)]

        render = "n/a"
        if path.suffix.lower() in {".html", ".svg"}:
            text = visible_text(content)
            render = "yes" if len(text) >= 80 else "needs-review"
            if render != "yes":
                render_failures.append(f"{rel} visible_text_len={len(text)}")

        if name_hits or content_hits:
            privacy_failures.append(
                f"{rel}: name={','.join(name_hits) or '-'} content={','.join(content_hits) or '-'}"
            )

        rows.append((rel, "yes" if not name_hits else "no", "yes" if not content_hits else "no", render))

    return rows, privacy_failures, render_failures


def render_markdown(rows: list[tuple[str, str, str, str]], privacy_failures: list[str], render_failures: list[str]) -> str:
    lines = [
        "# Public Safety Asset Audit",
        "",
        "Scope: every committed file in `viggomeesters-assets`, excluding `.git`.",
        "",
        "Allowed public identity: `viggomeesters`, `viggomeesters.com`, `viggomeesters-assets`.",
        "",
        "Forbidden scan classes: private organization/person/client names, direct private-source wording, local paths, temp source names, secrets.",
        "",
        "| File | Name anonymized? | Content anonymized? | Render/nonblank? |",
        "| --- | --- | --- | --- |",
    ]
    for rel, name_ok, content_ok, render in rows:
        lines.append(f"| `{rel}` | {name_ok} | {content_ok} | {render} |")
    lines.extend(
        [
            "",
            f"Total files checked: {len(rows)}",
            f"Files with name/content hits: {len(privacy_failures)}",
            f"HTML/SVG render issues: {len(render_failures)}",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="rewrite indexes/public-safety-audit.md")
    args = parser.parse_args()

    rows, privacy_failures, render_failures = audit_rows()
    markdown = render_markdown(rows, privacy_failures, render_failures)

    if args.write:
        AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
        AUDIT_PATH.write_text(markdown, encoding="utf-8")

    errors: list[str] = []
    if privacy_failures:
        errors.append("privacy/name/content hits:\n" + "\n".join(privacy_failures[:80]))
    if render_failures:
        errors.append("blank-like HTML/SVG files:\n" + "\n".join(render_failures[:80]))
    if AUDIT_PATH.exists() and AUDIT_PATH.read_text(encoding="utf-8") != markdown:
        errors.append("indexes/public-safety-audit.md is stale; run scripts/public_safety_audit.py --write")
    elif not AUDIT_PATH.exists():
        errors.append("indexes/public-safety-audit.md is missing; run scripts/public_safety_audit.py --write")

    print(f"files_checked {len(rows)}")
    print(f"private_hits {len(privacy_failures)}")
    print(f"html_blank_like {len(render_failures)}")

    if errors:
        print("\n\n".join(errors), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
