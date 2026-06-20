---
type: setup-note
project: Water Operator Vault
area: practice-exams
status: active
plugin: quizblock
tags: [quizblock, obsidian, interactive-quiz, setup]
---

# Quiz Block Setup

## What This Adds

Quiz Block creates interactive multiple-choice quiz blocks directly inside Obsidian notes.

This vault can generate Quiz Block practice exam notes from:

```text
05 Quiz App/t5_quiz_app_questions.json
```

Generated notes live in:

```text
03 Practice Exams/Quiz Block
```

## Plugin

Install the Obsidian community plugin:

```text
quizblock
```

The plugin renders fenced `quiz` code blocks as interactive questions.

## Format Used

```quiz
What does RTCR stand for?
[ ] Revised Treatment Control Rule
[c] Revised Total Coliform Rule
[ ] Routine Turbidity Compliance Rule
[ ] Regional Testing Certification Rule

The Revised Total Coliform Rule is the microbial monitoring rule for total coliform and E. coli in drinking water systems.
```

## Generator

Script:

```text
tools/export_quizblock_notes.py
```

Workflow:

```text
.github/workflows/generate-quizblock-notes.yml
```

## Notes

- Quiz Block is optional.
- Existing printable packets and the standalone quiz app still work.
- Quiz Block gives Obsidian users a native interactive mode.
- Correct answers are marked with `[c]` in source mode.
- Explanation/details appear after answering.

## Related

- [[Quiz Block Practice Exam Index]]
- [[03 Practice Exams/Practice Exams Index]]
- [[05 Quiz App/Quiz App Status]]
