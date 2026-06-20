---
type: contract
project: Water Operator Vault
area: quiz-app
status: active
created: 2026-06-19
last_updated: 2026-06-19
---

# Quiz App Contract

## Required Batch ID

Each generated quiz set must include a visible batch ID.

Format:

```text
T5-YYYYMMDD-SET-BATCH
```

Example:

```text
T5-20260619-E03-B0427
```

The same batch ID must appear on:

1. Quiz page / quiz packet
2. Answer key page
3. Quiz-app attempt record
4. Missed-question review record

## Required Set Fields

```yaml
id: string
title: string
source_file: string
question_count: number
batch_id: string
quiz_page_title: string
answer_key_page_title: string
questions: array
```

## Required Question Fields

```yaml
id: string
number: number
batch_id: string
domain: string
difficulty: string
prompt: string
choices: object
answer: string
explanation: string
review_links: array
```

## Page Separation

- Quiz page shows the batch ID, title, questions, and choices.
- Answer key page shows the same batch ID, answers, and rationales.
- Review page shows score, missed items, and explanations.

## Related

- [[Quiz App Status]]
- [[t5_quiz_app.html]]
