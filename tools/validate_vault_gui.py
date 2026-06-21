#!/usr/bin/env python3
"""Validate the Water Operator Vault GUI contract."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse


REPO_ROOT = Path(__file__).resolve().parents[1]
SNIPPET = REPO_ROOT / ".obsidian" / "snippets" / "water-operator-vault-theme.css"
TEMPLATE_SNIPPET = REPO_ROOT / "10 Templates" / "water-operator-vault-theme.css"

REQUIRED_LAUNCHERS = [
    "00 Dashboard/Dashboard Index.md",
    "00 Dashboard/Water Operator Vault Dashboard.md",
    "00 Dashboard/Shared Vault Quick Start.md",
    "00 Dashboard/Start Here - Required Plugins.md",
    "01 Study Hub/T5 Study Hub.md",
    "02 Flash Cards/Flash Cards Index.md",
    "03 Practice Exams/Practice Exams Index.md",
    "05 Quiz App/Quiz App Status.md",
    "04 Tables and Databases/Tables and Databases Index.md",
    "05 Regulations and Compliance/Regulations and Compliance Index.md",
    "06 Treatment Processes/Treatment Processes Index.md",
    "07 Water Math/Water Math Index.md",
    "08 Lab Procedures/Lab Procedures Index.md",
    "08 Printable Study Materials/Printable Packet Dashboard.md",
    "09 Verification and Sources/Verification Master Index.md",
    "09 Verification and Sources/Local Source Shelf - Water Books.md",
    "11 Cross Connection Control/Cross Connection Control Index.md",
    "03 Practice Exams/Quiz Block/Quiz Block Practice Exam Index.md",
]

PARITY_FILES = REQUIRED_LAUNCHERS + [
    ".obsidian/snippets/water-operator-vault-theme.css",
    "10 Templates/water-operator-vault-theme.css",
    "README.md",
    "05 Quiz App/t5_quiz_app.html",
    "05 Quiz App/t5_quiz_app_questions.json",
]

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---", re.S)
CSSCLASS_RE = re.compile(r"cssclasses:\s*\[(.*?)\]")
CLASS_ATTR_RE = re.compile(r'class="([^"]+)"')
CSS_SELECTOR_RE = re.compile(r"\.([A-Za-z][A-Za-z0-9_-]*)")
OBSIDIAN_OPEN_RE = re.compile(r'href="(obsidian://open\?[^"]+)"')
WIKILINK_RE = re.compile(r"\[\[([^\]#|]+)")


def rel(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter(text: str) -> str:
    match = FRONTMATTER_RE.search(text)
    return match.group(1) if match else ""


def cssclasses_from_frontmatter(text: str) -> set[str]:
    match = CSSCLASS_RE.search(frontmatter(text))
    if not match:
        return set()
    return {item.strip().strip("'\"") for item in match.group(1).split(",") if item.strip()}


def resolve_vault_file(target: str) -> Path | None:
    target = unquote(target).lstrip("/\\")
    base = REPO_ROOT / target
    candidates = [base]
    if base.suffix == "":
        candidates.extend([base.with_suffix(".md"), base.with_suffix(".html"), base.with_suffix(".json")])
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def mostly_raw_navigation(text: str) -> bool:
    table_nav_headers = re.findall(r"^\|\s*(Action|Need|File|Open|Page|Section)\s*\|", text, re.I | re.M)
    bullet_links = re.findall(r"^\s*[-*]\s+(?:\[\[|<a\s|[^\n]*obsidian://open)", text, re.I | re.M)
    gui_cards = len(re.findall(r"water-vault-(?:action-card|directory-card|card)", text))
    if table_nav_headers and gui_cards < 2:
        return True
    return len(bullet_links) >= 8 and gui_cards < 2


def default_export_root() -> Path | None:
    candidates = [
        REPO_ROOT.parent / "Vault-37" / "_vault_exports" / "Water-Operator-Vault",
        REPO_ROOT.parent.parent / "Vault-37" / "_vault_exports" / "Water-Operator-Vault",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--export-root", type=Path, default=None, help="Optional Vault-37 export copy root.")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    if not SNIPPET.exists():
        errors.append(f"Missing CSS snippet: {rel(SNIPPET)}")
        css_text = ""
    else:
        css_text = read(SNIPPET)

    if not TEMPLATE_SNIPPET.exists():
        errors.append(f"Missing template CSS snippet: {rel(TEMPLATE_SNIPPET)}")
    elif css_text and read(TEMPLATE_SNIPPET) != css_text:
        errors.append("Template CSS does not match .obsidian snippet.")

    css_classes = set(CSS_SELECTOR_RE.findall(css_text))

    for rel_path in REQUIRED_LAUNCHERS:
        path = REPO_ROOT / rel_path
        if not path.exists():
            errors.append(f"Missing required launcher: {rel_path}")
            continue
        text = read(path)
        classes = cssclasses_from_frontmatter(text)
        if "water-vault-gui" not in classes:
            errors.append(f"{rel_path} missing water-vault-gui cssclass.")
        if not classes:
            errors.append(f"{rel_path} missing cssclasses frontmatter.")
        missing_css = sorted(c for c in classes if c not in css_classes)
        if missing_css:
            errors.append(f"{rel_path} references missing CSS classes: {', '.join(missing_css)}")
        if "water-vault-hero" not in text:
            errors.append(f"{rel_path} missing water-vault-hero block.")
        if mostly_raw_navigation(text):
            errors.append(f"{rel_path} still looks like mostly raw table/bullet navigation.")

    for path in REPO_ROOT.rglob("*.md"):
        text = read(path)
        for class_attr in CLASS_ATTR_RE.findall(text):
            for class_name in class_attr.split():
                if class_name.startswith("water-vault-") and class_name not in css_classes:
                    errors.append(f"{rel(path)} uses undefined CSS class: {class_name}")

        for url in OBSIDIAN_OPEN_RE.findall(text):
            parsed = urlparse(url)
            target = parse_qs(parsed.query).get("file", [""])[0]
            if target and resolve_vault_file(target) is None:
                errors.append(f"{rel(path)} has obsidian://open link to missing file: {target}")

    for rel_path in ["05 Quiz App/t5_quiz_app.html", "05 Quiz App/t5_quiz_app_questions.json"]:
        if not (REPO_ROOT / rel_path).exists():
            errors.append(f"Missing supported quiz app file: {rel_path}")

    quiz_required_patterns = [
        re.compile(r"Requires\s+Obsidian\s+community\s+plugin:\s*\*\*quizblock\*\*", re.I),
        re.compile(r"##\s*Plugin\s+Required\s*.*?quizblock", re.I | re.S),
        re.compile(r"quizblock\s+.*required|required\s+.*quizblock", re.I),
    ]
    for path in REPO_ROOT.rglob("*.md"):
        text = read(path)
        lowered = text.lower()
        if "quizblock" not in lowered and "quiz block" not in lowered:
            continue
        if "not required" in lowered or "legacy/experimental" in lowered:
            continue
        if any(pattern.search(text) for pattern in quiz_required_patterns):
            errors.append(f"{rel(path)} appears to mark QuizBlock as required.")

    export_root = args.export_root or default_export_root()
    if export_root:
        for rel_path in PARITY_FILES:
            source = REPO_ROOT / rel_path
            export = export_root / rel_path
            if not export.exists():
                errors.append(f"Export copy missing key file: {rel_path}")
                continue
            if source.exists() and read(source) != read(export):
                errors.append(f"Export copy differs for key file: {rel_path}")
    else:
        warnings.append("No Vault-37 export root found; skipped export parity checks.")

    if warnings:
        print("WARNINGS")
        for warning in warnings:
            print(f"- {warning}")
        print()

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    print(f"Checked {len(REQUIRED_LAUNCHERS)} required launchers.")
    if export_root:
        print(f"Export parity root: {export_root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
