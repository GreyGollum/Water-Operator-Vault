#!/usr/bin/env python3
"""
Validate Water Operator Vault quiz-app JSON.

Checks:
- JSON exists and parses
- expected set/question counts
- set-level batch IDs
- question-level batch IDs match set batch IDs
- answer keys are A/B/C/D
- every question has four choices
- quiz and answer-key titles exist
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
QUIZ_JSON = REPO_ROOT / "05 Quiz App" / "t5_quiz_app_questions.json"
REPORT = REPO_ROOT / "09 Verification and Sources" / "Quiz JSON Validation Report.md"
EXPECTED_SETS = 11
EXPECTED_QUESTIONS = 570


def fail(message: str) -> None:
    raise AssertionError(message)


def validate() -> tuple[dict, list[str]]:
    if not QUIZ_JSON.exists():
        fail(f"Missing quiz JSON: {QUIZ_JSON}")
    payload = json.loads(QUIZ_JSON.read_text(encoding="utf-8"))
    sets = payload.get("sets", [])
    errors: list[str] = []

    if payload.get("set_count") != len(sets):
        errors.append(f"set_count mismatch: declared {payload.get('set_count')} actual {len(sets)}")
    if len(sets) != EXPECTED_SETS:
        errors.append(f"expected {EXPECTED_SETS} sets, found {len(sets)}")

    total = 0
    seen_batches = set()
    for set_index, item in enumerate(sets, start=1):
        title = item.get("title", f"set {set_index}")
        batch = item.get("batch_id", "")
        questions = item.get("questions", [])
        total += len(questions)

        if not batch:
            errors.append(f"{title}: missing batch_id")
        if batch in seen_batches:
            errors.append(f"{title}: duplicate batch_id {batch}")
        seen_batches.add(batch)
        if not item.get("quiz_page_title"):
            errors.append(f"{title}: missing quiz_page_title")
        if not item.get("answer_key_page_title"):
            errors.append(f"{title}: missing answer_key_page_title")
        if item.get("question_count") != len(questions):
            errors.append(f"{title}: question_count mismatch declared {item.get('question_count')} actual {len(questions)}")

        for q in questions:
            qid = q.get("id", "UNKNOWN")
            if q.get("batch_id") != batch:
                errors.append(f"{qid}: question batch_id does not match set batch_id")
            choices = q.get("choices", {})
            if sorted(choices.keys()) != ["A", "B", "C", "D"]:
                errors.append(f"{qid}: choices must be A/B/C/D")
            if q.get("answer") not in ["A", "B", "C", "D"]:
                errors.append(f"{qid}: answer must be A/B/C/D")
            if not q.get("prompt"):
                errors.append(f"{qid}: missing prompt")

    if payload.get("question_count") != total:
        errors.append(f"question_count mismatch: declared {payload.get('question_count')} actual {total}")
    if total != EXPECTED_QUESTIONS:
        errors.append(f"expected {EXPECTED_QUESTIONS} questions, found {total}")
    return payload, errors


def write_report(payload: dict, errors: list[str]) -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    passed = not errors
    lines = [
        "---",
        "type: validation-report",
        "project: Water Operator Vault",
        "area: quiz-app",
        f"status: {'passed' if passed else 'failed'}",
        "---",
        "",
        "# Quiz JSON Validation Report",
        "",
        "## Summary",
        "",
        "```yaml",
        f"validator_passes: {str(passed).lower()}",
        f"set_count: {payload.get('set_count')}",
        f"question_count: {payload.get('question_count')}",
        f"expected_set_count: {EXPECTED_SETS}",
        f"expected_question_count: {EXPECTED_QUESTIONS}",
        f"error_count: {len(errors)}",
        "```",
        "",
    ]
    if errors:
        lines.extend(["## Errors", ""])
        for error in errors:
            lines.append(f"- {error}")
    else:
        lines.extend([
            "## Result",
            "",
            "Quiz JSON passed schema/count/batch-ID validation.",
            "",
            "## Confirmed",
            "",
            "- 11 quiz sets",
            "- 570 questions",
            "- set-level batch IDs",
            "- question-level batch IDs",
            "- quiz page titles",
            "- answer-key page titles",
            "- A/B/C/D answers",
            "- A/B/C/D choices",
        ])
    lines.append("")
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    payload, errors = validate()
    write_report(payload, errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
    print(f"Quiz JSON valid: {payload.get('set_count')} sets / {payload.get('question_count')} questions")


if __name__ == "__main__":
    main()
