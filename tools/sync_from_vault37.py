#!/usr/bin/env python3
"""
Sync remaining original Water Operator Vault study files from GreyGollum/Vault-37.

This script intentionally copies only original study notes/decks/exams/source-control files.
It does NOT copy uploaded copyrighted source PDFs, books, or scans.

The sync is tolerant: missing files are reported but do not abort the workflow.
"""

from __future__ import annotations

from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import urlopen

REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_BASE = "https://raw.githubusercontent.com/GreyGollum/Vault-37/main"
REPORT_PATH = REPO_ROOT / "09 Verification and Sources" / "Pass 5 Sync Report.md"

FILES = [
    (
        "14 Water Operations/Flash Cards/T5 Flash Cards - Water Math.md",
        "02 Flash Cards/T5 Flash Cards - Water Math.md",
    ),
    (
        "14 Water Operations/Flash Cards/T5 Flash Cards - Disinfection and CT.md",
        "02 Flash Cards/T5 Flash Cards - Disinfection and CT.md",
    ),
    (
        "14 Water Operations/Flash Cards/T5 Flash Cards - Treatment Processes.md",
        "02 Flash Cards/T5 Flash Cards - Treatment Processes.md",
    ),
    (
        "14 Water Operations/Flash Cards/T5 Flash Cards - SDWA and Regulations.md",
        "02 Flash Cards/T5 Flash Cards - SDWA and Regulations.md",
    ),
    (
        "14 Water Operations/Flash Cards/T5 Flash Cards - Water Quality and Contaminants.md",
        "02 Flash Cards/T5 Flash Cards - Water Quality and Contaminants.md",
    ),
    (
        "_vault_exports/Water-Operator-Vault/02 Flash Cards/T5 Flash Cards - PFAS and MCLs.md",
        "02 Flash Cards/T5 Flash Cards - PFAS and MCLs.md",
    ),
    (
        "14 Water Operations/Practice Exams/T5 Practice Exam Suite - 250 Questions.md",
        "03 Practice Exams/T5 Practice Exam Suite - 250 Questions.md",
    ),
    (
        "14 Water Operations/Practice Exams/T5 Math-Only Practice Bank.md",
        "03 Practice Exams/T5 Math-Only Practice Bank.md",
    ),
    (
        "14 Water Operations/Practice Exams/T5 PFAS and Emerging Contaminants Mini Exam.md",
        "03 Practice Exams/T5 PFAS and Emerging Contaminants Mini Exam.md",
    ),
    (
        "14 Water Operations/Practice Exams/T5 Practice Exam 06 - Advanced Scenario Mix.md",
        "03 Practice Exams/T5 Practice Exam 06 - Advanced Scenario Mix.md",
    ),
    (
        "14 Water Operations/Practice Exams/T5 Practice Exam Printable Score Sheets.md",
        "03 Practice Exams/T5 Practice Exam Printable Score Sheets.md",
    ),
    (
        "_vault_exports/Water-Operator-Vault/09 Verification and Sources/Card Audit - Water Math.md",
        "09 Verification and Sources/Card Audit - Water Math.md",
    ),
    (
        "_vault_exports/Water-Operator-Vault/09 Verification and Sources/Card Audit - Disinfection and CT.md",
        "09 Verification and Sources/Card Audit - Disinfection and CT.md",
    ),
    (
        "_vault_exports/Water-Operator-Vault/09 Verification and Sources/Card Audit - Treatment Processes.md",
        "09 Verification and Sources/Card Audit - Treatment Processes.md",
    ),
]


def raw_url(path: str) -> str:
    return f"{SOURCE_BASE}/{quote(path, safe='/')}"


def download_text(path: str) -> str:
    with urlopen(raw_url(path), timeout=60) as response:
        return response.read().decode("utf-8")


def write_file(target: str, content: str) -> None:
    out = REPO_ROOT / target
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")


def write_report(copied: list[tuple[str, str]], failed: list[tuple[str, str, str]]) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "---",
        "type: sync-report",
        "project: Water Operator Vault",
        "area: standalone-transfer",
        "status: generated",
        "---",
        "",
        "# Pass 5 Sync Report",
        "",
        "## Summary",
        "",
        "```yaml",
        f"copied_count: {len(copied)}",
        f"failed_count: {len(failed)}",
        "workflow_should_continue: true",
        "```",
        "",
        "## Copied Files",
        "",
        "| Source | Target |",
        "|---|---|",
    ]
    for source, target in copied:
        lines.append(f"| `{source}` | `{target}` |")
    lines.extend(["", "## Failed Files", "", "| Source | Target | Error |", "|---|---|---|"])
    for source, target, error in failed:
        lines.append(f"| `{source}` | `{target}` | `{error}` |")
    lines.append("")
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    copied: list[tuple[str, str]] = []
    failed: list[tuple[str, str, str]] = []
    for source, target in FILES:
        print(f"Copying {source} -> {target}")
        try:
            write_file(target, download_text(source))
            copied.append((source, target))
        except (HTTPError, URLError, TimeoutError, UnicodeDecodeError) as exc:
            print(f"WARNING: failed to copy {source}: {exc}")
            failed.append((source, target, str(exc)))
    write_report(copied, failed)
    print(f"Copied {len(copied)} file(s); failed {len(failed)} file(s).")


if __name__ == "__main__":
    main()
