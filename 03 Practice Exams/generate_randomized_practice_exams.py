#!/usr/bin/env python3
"""
Generate randomized Water Operator Vault practice exam drafts.

This standalone-repo version reads practice exam Markdown files from:

    03 Practice Exams/

and writes randomized output to:

    03 Practice Exams/Randomized Final Drafts/

It supports visible batch IDs and separate quiz / answer-key sections.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from random import Random

# Script lives in: <repo>/03 Practice Exams/generate_randomized_practice_exams.py
# Therefore parents[1] is the repository root.
REPO_ROOT = Path(__file__).resolve().parents[1]
EXAM_DIR = REPO_ROOT / "03 Practice Exams"
OUT_DIR = EXAM_DIR / "Randomized Final Drafts"
BATCH_DATE = "20260619"

SOURCE_FILES = [
    EXAM_DIR / "T5 Practice Exam Suite - 250 Questions.md",
    EXAM_DIR / "T5 Math-Only Practice Bank.md",
    EXAM_DIR / "T5 PFAS and Emerging Contaminants Mini Exam.md",
    EXAM_DIR / "T5 Practice Exam 06 - Advanced Scenario Mix.md",
    EXAM_DIR / "T5 Lab Procedures and Methods Mini Exam.md",
    EXAM_DIR / "T5 Cross Connection Control Mini Exam.md",
    EXAM_DIR / "T5 Distribution Source Hydrants and Disinfection Mini Exam.md",
]

QUESTION_RE = re.compile(
    r"^(?P<num>\d+)\.\s+(?P<stem>.*?)\s+"
    r"A\)\s+(?P<A>.*?)\s+"
    r"B\)\s+(?P<B>.*?)\s+"
    r"C\)\s+(?P<C>.*?)\s+"
    r"D\)\s+(?P<D>.*)$"
)
KEY_RE = re.compile(r"^\|\s*(?P<num>\d+)\s*\|\s*(?P<ans>[ABCD])\s*\|")
HEADING_RE = re.compile(r"^#\s+(?P<title>Practice Exam\s+\d+.*?)$")


@dataclass
class Question:
    num: int
    stem: str
    choices: dict[str, str]
    answer: str
    review: str
    domain: str
    difficulty: str


def slugify(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-")
    return text or "practice-exam"


def batch_id(title: str, ordinal: int) -> str:
    seed = int(hashlib.sha256(title.encode("utf-8")).hexdigest(), 16) % 10000
    return f"T5-{BATCH_DATE}-E{ordinal:02d}-B{seed:04d}"


def deterministic_shuffle(items: list[tuple[str, str]], seed_text: str) -> list[tuple[str, str]]:
    rng = Random(int(hashlib.sha256(seed_text.encode("utf-8")).hexdigest(), 16))
    items = list(items)
    rng.shuffle(items)
    return items


def infer_domain(stem: str, title: str) -> str:
    text = f"{stem} {title}".lower()
    rules = [
        ("pfas", "PFAS / Emerging Contaminants"),
        ("mcl", "Regulations / Compliance"),
        ("coliform", "Microbiology / RTCR"),
        ("hpc", "Lab Procedures / Microbiology"),
        ("titration", "Lab Procedures / Wet Chemistry"),
        ("blank", "Lab Procedures / QA-QC"),
        ("accuracy", "Lab Procedures / QA-QC"),
        ("precision", "Lab Procedures / QA-QC"),
        ("backflow", "Distribution / Cross-Connection"),
        ("cross-connection", "Distribution / Cross-Connection"),
        ("backsiphonage", "Distribution / Cross-Connection"),
        ("backpressure", "Distribution / Cross-Connection"),
        ("hydrant", "Distribution / Hydrants"),
        ("pipe", "Distribution / Pipes"),
        ("storage", "Distribution / Storage"),
        ("chlorination", "Disinfection / Chlorination"),
        ("chlorine", "Disinfection / CT"),
        ("membrane", "Treatment Processes / Membranes"),
        ("activated carbon", "Treatment Processes / Activated Carbon"),
        ("aluminum sulfate", "Treatment Chemicals / Coagulation"),
        ("gpm", "Water Math / Hydraulics"),
        ("mgd", "Water Math / Hydraulics"),
        ("psi", "Water Math / Hydraulics"),
    ]
    for needle, domain in rules:
        if needle in text:
            return domain
    if "lab" in title.lower():
        return "Lab Procedures / Methods"
    if "distribution" in title.lower():
        return "Distribution / Source / Hydrants"
    return "General Water Operations"


def infer_difficulty(stem: str) -> str:
    text = stem.lower()
    if any(token in text for token in ["best", "first", "should", "response", "priority"]):
        return "T5-scenario"
    if any(token in text for token in ["calculate", "gpm", "mgd", "psi", "ct", "percent"]):
        return "medium"
    return "easy"


def parse_answer_key(lines: list[str]) -> dict[int, str]:
    key: dict[int, str] = {}
    in_key = False
    for line in lines:
        if line.startswith("## Answer Key"):
            in_key = True
            continue
        if in_key and line.startswith("---"):
            break
        if in_key:
            match = KEY_RE.match(line)
            if match:
                key[int(match.group("num"))] = match.group("ans")
    return key


def parse_exam_block(title: str, block: list[str]) -> list[Question]:
    key = parse_answer_key(block)
    questions: list[Question] = []
    for line in block:
        match = QUESTION_RE.match(line)
        if not match:
            continue
        num = int(match.group("num"))
        if num not in key:
            raise ValueError(f"Missing answer key for {title} Q{num}")
        stem = match.group("stem").strip()
        questions.append(
            Question(
                num=num,
                stem=stem,
                choices={letter: match.group(letter).strip() for letter in "ABCD"},
                answer=key[num],
                review="source-supported with caveats",
                domain=infer_domain(stem, title),
                difficulty=infer_difficulty(stem),
            )
        )
    return questions


def split_suite(text: str) -> list[tuple[str, list[str]]]:
    lines = text.splitlines()
    blocks: list[tuple[str, list[str]]] = []
    current_title: str | None = None
    current: list[str] = []
    for line in lines:
        heading = HEADING_RE.match(line)
        if heading:
            if current_title and current:
                blocks.append((current_title, current))
            current_title = heading.group("title").strip()
            current = [line]
        elif current_title:
            current.append(line)
    if current_title and current:
        blocks.append((current_title, current))
    if blocks:
        return blocks
    title = next((line.lstrip("# ").strip() for line in lines if line.startswith("# ")), "Practice Bank")
    return [(title, lines)]


def render_randomized_exam(title: str, questions: list[Question], source_file: str, ordinal: int) -> str:
    bid = batch_id(title, ordinal)
    out = [
        "---",
        "type: randomized-practice-exam",
        "area: water-operations",
        "exam: T5",
        "status: draft-finalized",
        f"source_file: {source_file}",
        f"batch_id: {bid}",
        "verification_status: answer_key_verified_randomized",
        "randomization: deterministic_sha256_seed",
        "---",
        "",
        f"# {title} - Randomized Final Draft",
        "",
        f"> **Batch ID:** `{bid}`",
        "",
        "## Quiz Page",
        "",
        f"Batch ID: `{bid}`",
        "",
        "## Questions",
        "",
    ]
    answer_rows = []
    metadata_rows = []
    for q in questions:
        shuffled = deterministic_shuffle(list(q.choices.items()), f"{bid}|{title}|{q.num}|{q.stem}")
        new_letters = "ABCD"
        new_choices = {new_letters[i]: item for i, item in enumerate(shuffled)}
        new_answer = next(letter for letter, (old_letter, _text) in new_choices.items() if old_letter == q.answer)
        out.append(f"{q.num}. {q.stem} " + " ".join(f"{letter}) {text}" for letter, (_old, text) in new_choices.items()))
        answer_rows.append(f"| {q.num} | {new_answer} | {q.review} |")
        metadata_rows.append(f"| {q.num} | {bid} | {q.domain} | {q.difficulty} |")
    out.extend(["", "---", "", "## Answer Key Page", "", f"Batch ID: `{bid}`", "", "| Q | Answer | Review |", "|---:|---|---|"])
    out.extend(answer_rows)
    out.extend(["", "## Metadata", "", "| Q | Batch ID | Domain | Difficulty |", "|---:|---|---|---|"])
    out.extend(metadata_rows)
    out.extend(["", "## Release Caveats", "", "- Recheck current rules, source notes, and date-sensitive values before final release.", "- These are study questions, not official exam questions.", ""])
    return "\n".join(out)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    generated = []
    ordinal = 0
    for source in SOURCE_FILES:
        if not source.exists():
            print(f"Skipping missing source: {source}")
            continue
        for title, block in split_suite(source.read_text(encoding="utf-8")):
            questions = parse_exam_block(title, block)
            if not questions:
                continue
            ordinal += 1
            bid = batch_id(title, ordinal)
            filename = f"{slugify(title)} - Randomized Final Draft.md"
            (OUT_DIR / filename).write_text(render_randomized_exam(title, questions, source.name, ordinal), encoding="utf-8")
            generated.append((title, len(questions), filename, bid))
    manifest = ["---", "type: randomized-practice-exam-manifest", "status: generated", "---", "", "# Randomized Practice Exam Manifest", "", "| Exam | Questions | Batch ID | File |", "|---|---:|---|---|"]
    for title, count, filename, bid in generated:
        manifest.append(f"| {title} | {count} | `{bid}` | [[{filename.removesuffix('.md')}]] |")
    manifest.append("")
    manifest.append(f"Total generated question sets: {len(generated)}")
    manifest.append(f"Total questions: {sum(count for _title, count, _filename, _bid in generated)}")
    manifest.append("")
    (OUT_DIR / "Randomized Practice Exam Manifest.md").write_text("\n".join(manifest), encoding="utf-8")
    print(f"Generated {len(generated)} files / {sum(count for _title, count, _filename, _bid in generated)} questions")


if __name__ == "__main__":
    main()
