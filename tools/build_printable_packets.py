#!/usr/bin/env python3
"""
Build Markdown source packets for printable PDF/DOCX export.

The workflow converts these Markdown packets to DOCX/PDF artifacts with Pandoc.
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = REPO_ROOT / "08 Printable Study Materials" / "Generated Packets"

PACKETS = {
    "Water-Operator-Vault-Flashcards-Packet.md": [
        "02 Flash Cards/T5 Flash Cards - PFAS and MCLs.md",
        "02 Flash Cards/T5 Flash Cards - SDWA and Regulations.md",
        "02 Flash Cards/T5 Flash Cards - Water Quality and Contaminants.md",
        "02 Flash Cards/T5 Flash Cards - Water Math.md",
        "02 Flash Cards/T5 Flash Cards - Disinfection and CT.md",
        "02 Flash Cards/T5 Flash Cards - Treatment Processes.md",
        "02 Flash Cards/T5 Flash Cards - Lab Procedures and Methods.md",
        "02 Flash Cards/T5 Flash Cards - Cross Connection Control.md",
        "02 Flash Cards/T5 Flash Cards - Distribution Source Hydrants and Disinfection.md",
    ],
    "Water-Operator-Vault-Practice-Exam-Packet.md": [
        "03 Practice Exams/Randomized Final Drafts/Randomized Practice Exam Manifest.md",
        "03 Practice Exams/Randomized Final Drafts/Practice-Exam-01-Core-Regulations-MCLs-and-Operator-Math - Randomized Final Draft.md",
        "03 Practice Exams/Randomized Final Drafts/Practice-Exam-02-Treatment-Processes-and-Water-Quality - Randomized Final Draft.md",
        "03 Practice Exams/Randomized Final Drafts/Practice-Exam-03-Source-Water-Distribution-Sampling-and-Public-Health - Randomized Final Draft.md",
        "03 Practice Exams/Randomized Final Drafts/Practice-Exam-04-Advanced-Math-Pumps-SCADA-and-Operations - Randomized Final Draft.md",
        "03 Practice Exams/Randomized Final Drafts/Practice-Exam-05-Scenario-Judgment-Compliance-and-Troubleshooting - Randomized Final Draft.md",
        "03 Practice Exams/Randomized Final Drafts/T5-Math-Only-Practice-Bank - Randomized Final Draft.md",
        "03 Practice Exams/Randomized Final Drafts/T5-PFAS-and-Emerging-Contaminants-Mini-Exam - Randomized Final Draft.md",
        "03 Practice Exams/Randomized Final Drafts/T5-Practice-Exam-06-Advanced-Scenario-Mix - Randomized Final Draft.md",
        "03 Practice Exams/Randomized Final Drafts/T5-Lab-Procedures-and-Methods-Mini-Exam - Randomized Final Draft.md",
        "03 Practice Exams/Randomized Final Drafts/T5-Cross-Connection-Control-Mini-Exam - Randomized Final Draft.md",
        "03 Practice Exams/Randomized Final Drafts/T5-Distribution-Source-Hydrants-and-Disinfection-Mini-Exam - Randomized Final Draft.md",
    ],
    "Water-Operator-Vault-Source-and-Verification-Packet.md": [
        "README.md",
        "09 Verification and Sources/Verification Master Index.md",
        "09 Verification and Sources/Standalone Transfer Manifest.md",
        "09 Verification and Sources/Water Operator Source Bibliography.md",
        "09 Verification and Sources/Practice Exam Audit Status.md",
        "09 Verification and Sources/Practice Exam Finalization Status.md",
        "09 Verification and Sources/Current Regulatory Recheck - 2026-06-19.md",
        "09 Verification and Sources/Lead and Copper Rule Transition Note.md",
        "09 Verification and Sources/Pass 5 Sync Report.md",
        "05 Quiz App/Quiz App Status.md",
    ],
}


def read_file(path: str) -> str:
    full = REPO_ROOT / path
    if not full.exists():
        return f"\n\n# Missing File\n\n`{path}` was not found during packet build.\n"
    return full.read_text(encoding="utf-8")


def clean_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        parts = text.split("---\n", 2)
        if len(parts) == 3:
            return parts[2]
    return text


def build_packet(name: str, files: list[str]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    packet_title = name.removesuffix(".md").replace("-", " ")
    chunks = [
        "---",
        f"title: {packet_title}",
        "project: Water Operator Vault",
        "status: draft-printable",
        "---",
        "",
        f"# {packet_title}",
        "",
        "> Draft printable packet. Verify current regulations, local requirements, and source caveats before public/final release.",
        "",
    ]
    for path in files:
        chunks.extend(["", "\\newpage", "", f"<!-- Source: {path} -->", ""])
        chunks.append(clean_frontmatter(read_file(path)))
    (OUT_DIR / name).write_text("\n".join(chunks), encoding="utf-8")


def main() -> None:
    for name, files in PACKETS.items():
        build_packet(name, files)
    print(f"Built {len(PACKETS)} Markdown packet(s) in {OUT_DIR}")


if __name__ == "__main__":
    main()
