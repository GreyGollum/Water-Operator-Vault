---
type: transfer-manifest
project: Water Operator Vault
status: active
created: 2026-06-19
last_updated: 2026-06-19
source_repo: GreyGollum/Vault-37
source_path: _vault_exports/Water-Operator-Vault/
target_repo: GreyGollum/Water-Operator-Vault
tags: [transfer, standalone-vault, github, obsidian]
---

# Standalone Transfer Manifest

> Tracks the migration from `GreyGollum/Vault-37/_vault_exports/Water-Operator-Vault/` into the standalone public repo `GreyGollum/Water-Operator-Vault`.

---

## Transfer Policy

```yaml
copy_uploaded_books_or_pdfs: false
copy_original_notes: true
copy_flashcards: true
copy_practice_exams: true
copy_source_indexes: true
copy_quiz_app: true
public_repo: true
```

Do not upload copyrighted manuals, PDFs, books, or source scans into this public repo. Keep only original notes, source-control summaries, flashcards, practice exams, databases, and app files.

---

## Completed In Transfer Pass 1

| Area | Status |
|---|---|
| README.md | transferred / initialized |
| Dashboard | transferred |
| T5 Study Hub | transferred |
| Flash Cards Index | transferred |
| Practice Exams Index | transferred |
| Verification Master Index | transferred |
| Source Bibliography Backbone | transferred |
| Standalone Transfer Manifest | created |

---

## Completed In Transfer Pass 2

| Area | Status |
|---|---|
| Tables and Databases Index | transferred |
| Lab Procedures Index | transferred |
| Lab Methods Source Plan | transferred |
| EPA Approved Methods Index | transferred |
| Lab Methods Source Database | transferred |
| Distribution Source Reference Database | transferred |
| Cross Connection Control Index | transferred |
| Backflow Prevention Device Matrix | transferred |
| Cross Connection Source Plan | transferred |

---

## Completed In Transfer Pass 3

| Area | Status |
|---|---|
| Current Regulatory Recheck note | transferred |
| Lead and Copper Rule Transition Note | transferred |
| Practice Exam Audit Status | transferred |
| Practice Exam Finalization Status | transferred |
| Lab Methods Source Bibliography Supplement | transferred |
| Cross Connection Source Bibliography Supplement | transferred |
| Water Supply Distribution Source Intake | transferred |
| Distribution and Source Module Build Roadmap | transferred |
| Distribution Source Content Audit | transferred |

---

## Completed In Transfer Pass 4

| Area | Status |
|---|---|
| Lab flashcards | transferred |
| Cross-connection flashcards | transferred |
| Distribution/source flashcards | transferred |
| Lab mini-exam | transferred |
| Cross-connection mini-exam | transferred |
| Distribution/source mini-exam | transferred |
| Quiz app HTML shell | transferred as starter shell |
| Generator workflow/script | transferred and adapted for standalone repo |

---

## Pass 5 - Large Decks and Generated Outputs

| Item | Status |
|---|---|
| Sync script for large decks/source banks | installed |
| GitHub Actions workflow for sync/generate/export | installed |
| Quiz JSON exporter scaffold | installed |
| Full Water Math deck | automation pending / not yet confirmed in repo |
| Full Disinfection and CT deck | automation pending / not yet confirmed in repo |
| Full Treatment Processes deck | automation pending / not yet confirmed in repo |
| Original 450-question source banks | automation pending / not yet confirmed in repo |
| Randomized 570-question output confirmation | pending |
| Quiz-app JSON export | pending |
| Expanded quiz app shell after JSON format is finalized | pending |

Manual fallback if Actions does not run:

1. Open GitHub Actions in `GreyGollum/Water-Operator-Vault`.
2. Run workflow: `Sync Remaining Files From Vault-37`.
3. Confirm the bot commit adds the large decks, source banks, randomized drafts, and `05 Quiz App/t5_quiz_app_questions.json`.

---

## Current Standalone Status

```yaml
transfer_started: true
repo_initialized: true
core_navigation_transferred: true
source_backbone_transferred: true
core_module_shells_transferred: true
source_status_files_transferred: true
short_flashcard_decks_transferred: true
mini_exams_transferred: true
quiz_app_shell_transferred: true
generator_transferred: true
pass_5_automation_installed: true
pass_5_outputs_confirmed: false
full_standalone_vault_complete: false
```

---

## Related

- [[Verification Master Index]]
- [[Water Operator Source Bibliography]]
- [[00 Dashboard/Water Operator Vault Dashboard]]
