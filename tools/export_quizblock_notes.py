#!/usr/bin/env python3
"""
Export Water Operator Vault quiz JSON into Obsidian Quiz Block notes.

Source:
    05 Quiz App/t5_quiz_app_questions.json

Output:
    03 Practice Exams/Quiz Block/

Quiz Block plugin format:

```quiz
Question text
[ ] Wrong option
[c] Correct option
[ ] Wrong option
[ ] Wrong option

Explanation/details shown after answering.
```
"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
QUIZ_JSON = REPO_ROOT / "05 Quiz App" / "t5_quiz_app_questions.json"
OUT_DIR = REPO_ROOT / "03 Practice Exams" / "Quiz Block"


def clean_text(text: str) -> str:
    text = str(text or "").strip()
    text = text.replace("```", "'''")
    text = re.sub(r"\s+", " ", text)
    return text


def slugify(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-")
    return text or "quiz-block-set"


def render_quiz_block(question: dict) -> str:
    prompt = clean_text(question.get("prompt", ""))
    choices = question.get("choices", {})
    answer = question.get("answer", "")
    explanation = clean_text(question.get("explanation", ""))
    domain = clean_text(question.get("domain", ""))
    difficulty = clean_text(question.get("difficulty", ""))
    batch_id = clean_text(question.get("batch_id", ""))

    lines = ["```quiz", prompt]
    for letter in ["A", "B", "C", "D"]:
        marker = "[c]" if letter == answer else "[ ]"
        lines.append(f"{marker} {letter}) {clean_text(choices.get(letter, ''))}")
    details = []
    if explanation:
        details.append(explanation)
    details.append(f"Batch ID: `{batch_id}`")
    if domain or difficulty:
        details.append(f"Metadata: {domain or 'Unknown domain'} · {difficulty or 'unknown difficulty'}")
    lines.append("")
    lines.extend(details)
    lines.append("```")
    return "\n".join(lines)


def render_set_note(item: dict) -> str:
    title = clean_text(item.get("title", "Quiz Block Set"))
    batch_id = clean_text(item.get("batch_id", ""))
    questions = item.get("questions", [])
    lines = [
        "---",
        "type: quizblock-practice-exam",
        "project: Water Operator Vault",
        "area: practice-exams",
        "status: generated",
        f"batch_id: {batch_id}",
        f"question_count: {len(questions)}",
        "plugin: quizblock",
        "cssclasses: [water-vault-quiz, water-vault-gui]",
        "tags: [quizblock, t5, practice-exam, interactive]",
        "---",
        "",
        f"# {title} - Quiz Block",
        "",
        f"> Batch ID: `{batch_id}`  ",
        "> Optional Markdown QuizBlock export. The supported on-screen test is `05 Quiz App/t5_quiz_app.html`, using this same batch ID.",
        "",
        "## Interactive Questions",
        "",
    ]
    for question in questions:
        lines.append(f"### Question {question.get('number', '')}")
        lines.append("")
        lines.append(render_quiz_block(question))
        lines.append("")
    return "\n".join(lines)


def render_index(sets: list[dict]) -> str:
    lines = [
        "---",
        "type: quizblock-index",
        "project: Water Operator Vault",
        "area: practice-exams",
        "status: generated",
        "plugin: quizblock",
        "cssclasses: [water-vault-quiz, water-vault-index, water-vault-gui]",
        "tags: [quizblock, t5, practice-exam, index]",
        "---",
        "",
        "# Quiz Block Practice Exam Index",
        "",
        '<div class="water-vault-hero compact">',
        '<span class="water-vault-status">On-Screen Tests</span>',
        '<div class="water-vault-title">QuizBlock On-Screen Tests</div>',
        '<p class="water-vault-subtitle">Use the included browser app for the QuizBlock-style flow: one question, answer it, go to the next question. These tests use the same batch IDs as the generated printed tests.</p>',
        '</div>',
        "",
        "## Supported On-Screen Test",
        "",
        '<div class="water-vault-action-grid">',
        '<div class="water-vault-action-card featured"><h3>On-Screen Quiz App</h3><p>Load JSON, select a printed-test batch ID, then answer one question at a time.</p><a class="water-vault-action" href="obsidian://open?file=05%20Quiz%20App%2Ft5_quiz_app.html">Open App</a></div>',
        '<div class="water-vault-action-card"><h3>Quiz JSON</h3><p>Validated generated quiz data used by the app and optional Markdown export.</p><a class="water-vault-action" href="obsidian://open?file=05%20Quiz%20App%2Ft5_quiz_app_questions.json">Open JSON</a></div>',
        '<div class="water-vault-action-card"><h3>Quiz App Status</h3><p>Status page for batch IDs, scoring, answer keys, and validation.</p><a class="water-vault-action" href="obsidian://open?file=05%20Quiz%20App%2FQuiz%20App%20Status">Open Status</a></div>',
        '</div>',
        "",
        '<div class="water-vault-callout">The old Markdown QuizBlock export remains optional. The supported on-screen testing path is <code>05 Quiz App/t5_quiz_app.html</code>.</div>',
        "",
        "## Sets",
        "",
        '<div class="water-vault-panel">',
        "",
        "| Set | Questions | Batch ID | Open |",
        "|---|---:|---|---|",
    ]
    for item in sets:
        title = clean_text(item.get("title", "Quiz Block Set"))
        batch_id = clean_text(item.get("batch_id", ""))
        filename = f"{slugify(title)} - Quiz Block.md"
        lines.append(f"| {title} | {len(item.get('questions', []))} | `{batch_id}` | [[{filename.removesuffix('.md')}]] |")
    lines.extend([
        "",
        "</div>",
        "",
        "## Notes",
        "",
        "- Quiz Block supports one correct answer per question.",
        "- Correct answers are marked with `[c]` in source mode.",
        "- Explanations/details appear after answering.",
        "- These notes are generated files; edit the source question bank or JSON, then regenerate.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    if not QUIZ_JSON.exists():
        raise SystemExit(f"Missing quiz JSON: {QUIZ_JSON}")
    payload = json.loads(QUIZ_JSON.read_text(encoding="utf-8"))
    sets = payload.get("sets", [])
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for item in sets:
        title = clean_text(item.get("title", "Quiz Block Set"))
        filename = f"{slugify(title)} - Quiz Block.md"
        (OUT_DIR / filename).write_text(render_set_note(item), encoding="utf-8")
    (OUT_DIR / "Quiz Block Practice Exam Index.md").write_text(render_index(sets), encoding="utf-8")
    print(f"Exported {len(sets)} Quiz Block note(s) to {OUT_DIR}")


if __name__ == "__main__":
    main()
