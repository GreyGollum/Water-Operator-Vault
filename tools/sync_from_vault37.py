#!/usr/bin/env python3
"""
Sync remaining original Water Operator Vault study files from GreyGollum/Vault-37.

This script intentionally copies only original study notes/decks/exams/source-control files.
It does NOT copy uploaded copyrighted source PDFs, books, or scans.

Trigger note: updated to force the standalone sync workflow after initial workflow install.
"""

from __future__ import annotations

from pathlib import Path
from urllib.parse import quote
from urllib.request import urlopen

REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_BASE = "https://raw.githubusercontent.com/GreyGollum/Vault-37/main"

FILES = [
    # Large flashcard decks from Jeremy's Water Operations source tree
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
    # Existing verified smaller decks from export, to keep standalone repo complete
    (
        "_vault_exports/Water-Operator-Vault/02 Flash Cards/T5 Flash Cards - PFAS and MCLs.md",
        "02 Flash Cards/T5 Flash Cards - PFAS and MCLs.md",
    ),
    (
        "_vault_exports/Water-Operator-Vault/02 Flash Cards/T5 Flash Cards - SDWA and Regulations.md",
        "02 Flash Cards/T5 Flash Cards - SDWA and Regulations.md",
    ),
    (
        "_vault_exports/Water-Operator-Vault/02 Flash Cards/T5 Flash Cards - Water Quality and Contaminants.md",
        "02 Flash Cards/T5 Flash Cards - Water Quality and Contaminants.md",
    ),
    # Original source question banks, needed for standalone generator to reach 570 after all transfers
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
    # Audit reports for the large deck transfer and card checks
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
    return f"{SOURCE_BASE}/{quote(path)}"


def download_text(path: str) -> str:
    with urlopen(raw_url(path), timeout=60) as response:
        return response.read().decode("utf-8")


def write_file(target: str, content: str) -> None:
    out = REPO_ROOT / target
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")


def main() -> None:
    copied = 0
    for source, target in FILES:
        print(f"Copying {source} -> {target}")
        write_file(target, download_text(source))
        copied += 1
    print(f"Copied {copied} files from Vault-37.")


if __name__ == "__main__":
    main()
