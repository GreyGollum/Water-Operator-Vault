#!/usr/bin/env python3
"""Smoke-test the starter T5 quiz app shell."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
HTML = REPO_ROOT / "05 Quiz App" / "t5_quiz_app.html"
PROGRESS_HTML = REPO_ROOT / "05 Quiz App" / "progress_report.html"
REPORT = REPO_ROOT / "09 Verification and Sources" / "Quiz App Smoke Test Report.md"

REQUIRED_SNIPPETS = {
    "file input": "type=\"file\"",
    "json parsing": "JSON.parse",
    "batch id display": "batch_id",
    "start quiz function": "function startQuiz",
    "score quiz function": "function scoreQuiz",
    "answer key function": "function showKey",
    "answer key view": "Answer Key",
    "questions array": "questions",
}

REQUIRED_PROGRESS_SNIPPETS = {
    "progress local storage": "wov-quiz-attempt-",
    "strengths section": "Strengths",
    "weaknesses section": "Weaknesses and Suggested Study Areas",
    "missed review": "Missed Questions to Review",
    "exam link": "t5_quiz_app.html",
}


def main() -> None:
    errors = []
    if not HTML.exists():
        errors.append(f"Missing {HTML}")
        text = ""
    else:
        text = HTML.read_text(encoding="utf-8")
    for label, snippet in REQUIRED_SNIPPETS.items():
        if snippet not in text:
            errors.append(f"Missing required shell feature: {label} / {snippet}")

    if not PROGRESS_HTML.exists():
        errors.append(f"Missing {PROGRESS_HTML}")
        progress_text = ""
    else:
        progress_text = PROGRESS_HTML.read_text(encoding="utf-8")
    for label, snippet in REQUIRED_PROGRESS_SNIPPETS.items():
        if snippet not in progress_text:
            errors.append(f"Missing required progress feature: {label} / {snippet}")

    passed = not errors
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "---",
        "type: smoke-test-report",
        "project: Water Operator Vault",
        "area: quiz-app",
        f"status: {'passed' if passed else 'failed'}",
        "---",
        "",
        "# Quiz App Smoke Test Report",
        "",
        "## Summary",
        "",
        "```yaml",
        f"smoke_test_passes: {str(passed).lower()}",
        f"error_count: {len(errors)}",
        "browser_manual_test_still_recommended: true",
        "```",
        "",
    ]
    if errors:
        lines.extend(["## Errors", ""])
        lines.extend(f"- {error}" for error in errors)
    else:
        lines.extend([
            "## Result",
            "",
            "Starter quiz app shell passed static smoke test.",
            "",
            "## Confirmed Shell Hooks",
            "",
        ])
        lines.extend(f"- {label}" for label in REQUIRED_SNIPPETS)
        lines.extend(f"- progress: {label}" for label in REQUIRED_PROGRESS_SNIPPETS)
    lines.append("")
    REPORT.write_text("\n".join(lines), encoding="utf-8")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
    print("Quiz app static smoke test passed")


if __name__ == "__main__":
    main()
