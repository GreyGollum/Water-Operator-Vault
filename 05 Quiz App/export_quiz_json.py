#!/usr/bin/env python3
"""
Export randomized practice exam Markdown files into quiz-app JSON.

Input:
    03 Practice Exams/Randomized Final Drafts/*.md

Output:
    05 Quiz App/t5_quiz_app_questions.json

This exporter expects generated drafts with visible batch IDs, a Questions section,
and an Answer Key Page section.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RANDOMIZED_DIR = REPO_ROOT / "03 Practice Exams" / "Randomized Final Drafts"
OUT_FILE = REPO_ROOT / "05 Quiz App" / "t5_quiz_app_questions.json"
SUPPLEMENTAL_FILE = REPO_ROOT / "05 Quiz App" / "supplemental_questions.json"

BATCH_RE = re.compile(r"batch_id:\s*(?P<batch>\S+)|Batch ID:\s*`(?P<batch2>[^`]+)`", re.IGNORECASE)
QUESTION_RE = re.compile(r"^(?P<num>\d+)\.\s+(?P<prompt>.*?)\s+A\)\s+(?P<A>.*?)\s+B\)\s+(?P<B>.*?)\s+C\)\s+(?P<C>.*?)\s+D\)\s+(?P<D>.*)$")
KEY_RE = re.compile(r"^\|\s*(?P<num>\d+)\s*\|\s*(?P<answer>[ABCD])\s*\|\s*(?P<explanation>.*?)\s*\|")
TITLE_RE = re.compile(r"^#\s+(?P<title>.*?)\s+-\s+Randomized Final Draft")


def extract_batch(text: str) -> str:
    for match in BATCH_RE.finditer(text):
        return match.group("batch") or match.group("batch2")
    return "T5-UNBATCHED"


def extract_title(lines: list[str], fallback: str) -> str:
    for line in lines:
        match = TITLE_RE.match(line)
        if match:
            return match.group("title").strip()
    return fallback


def parse_answer_key(lines: list[str]) -> dict[int, tuple[str, str]]:
    key = {}
    in_key = False
    for line in lines:
        if line.startswith("## Answer Key Page"):
            in_key = True
            continue
        if in_key and line.startswith("## Metadata"):
            break
        if in_key:
            match = KEY_RE.match(line)
            if match:
                key[int(match.group("num"))] = (match.group("answer"), match.group("explanation").strip())
    return key


def parse_exam(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    title = extract_title(lines, path.stem)
    batch = extract_batch(text)
    key = parse_answer_key(lines)
    questions = []
    in_questions = False
    for line in lines:
        if line.startswith("## Questions"):
            in_questions = True
            continue
        if in_questions and line.startswith("---"):
            break
        if not in_questions:
            continue
        match = QUESTION_RE.match(line)
        if not match:
            continue
        num = int(match.group("num"))
        answer, explanation = key.get(num, ("", ""))
        review_status = "source_supported_review_needed" if explanation == "source-supported with caveats" else "source_supported"
        questions.append({
            "id": f"{batch}-Q{num:03d}",
            "number": num,
            "batch_id": batch,
            "domain": "unknown",
            "difficulty": "unknown",
            "prompt": match.group("prompt"),
            "choices": {letter: match.group(letter).strip() for letter in "ABCD"},
            "answer": answer,
            "explanation": "" if explanation == "source-supported with caveats" else explanation,
            "answer_review_status": review_status,
            "review_flag": False,
            "review_links": [],
        })
    return {
        "id": batch,
        "title": title,
        "source_file": path.name,
        "question_count": len(questions),
        "batch_id": batch,
        "quiz_page_title": f"{title} - Quiz Page",
        "answer_key_page_title": f"{title} - Answer Key",
        "questions": questions,
    }


def main() -> None:
    RANDOMIZED_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    sets = [parse_exam(path) for path in sorted(RANDOMIZED_DIR.glob("*.md")) if path.name != "Randomized Practice Exam Manifest.md"]
    if SUPPLEMENTAL_FILE.exists():
        supplemental = json.loads(SUPPLEMENTAL_FILE.read_text(encoding="utf-8"))
        sets.extend(supplemental.get("sets", []))
    payload = {
        "project": "Water Operator Vault",
        "export_type": "quiz_app_questions",
        "schema_version": "0.2",
        "sets": sets,
        "set_count": len(sets),
        "question_count": sum(len(s["questions"]) for s in sets),
    }
    OUT_FILE.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Exported {payload['set_count']} sets / {payload['question_count']} questions to {OUT_FILE}")


if __name__ == "__main__":
    main()
