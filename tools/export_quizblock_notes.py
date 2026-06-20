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
        "tags: [quizblock, t5, practice-exam, interactive]",
        "---",
        "",
        f"# {title} - Quiz Block",
        "",
        f"> Batch ID: `{batch_id}`  ",
        "> Requires Obsidian community plugin: **quizblock**.",
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
        "tags: [quizblock, t5, practice-exam, index]",
        "---",
        "",
        "# Quiz Block Practice Exam Index",
        "",
        "> Interactive Obsidian-native quiz notes generated from `05 Quiz App/t5_quiz_app_questions.json`.",
        "",
        "## Plugin Required",
        "",
        "Install the Obsidian community plugin **quizblock** to render these as interactive quizzes.",
        "",
        "## Sets",
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
