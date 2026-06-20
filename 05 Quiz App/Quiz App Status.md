---
type: status-note
project: Water Operator Vault
area: quiz-app
status: active
created: 2026-06-19
last_updated: 2026-06-19
verification_status: shell_transferred_json_pending
---

# Quiz App Status

## Current Status

```yaml
browser_app_shell: transferred
batch_id_display: included
separate_answer_key_view: included
attempt_history_by_batch_id: included
json_export_exists: false
validator_passes: false
quiz_app_working: false
```

## Still Needed

- Generate `t5_quiz_app_questions.json` from randomized final drafts.
- Include all 570 questions after regenerated output is confirmed.
- Include batch IDs for every set and question.
- Smoke-test file picker, scoring, answer key view, and local history.

## Related

- [[t5_quiz_app.html]]
- [[Quiz App Contract]]
- [[09 Verification and Sources/Practice Exam Finalization Status]]
