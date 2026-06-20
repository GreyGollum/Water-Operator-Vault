---
type: release-blocker
project: Water Operator Vault
area: standalone-transfer
status: action-required
created: 2026-06-19
last_updated: 2026-06-19
blocker_type: manual_github_actions_dispatch
---

# Pass 5 Manual Workflow Run - Required

> Pass 5 automation is installed, but the large deck/source-bank sync has not yet been confirmed in the standalone repo.

## Why This Exists

The remaining large files are too large to safely hand-transfer through the ChatGPT/GitHub connector without truncation risk. The standalone repo now includes a sync workflow that copies the large original study files from `GreyGollum/Vault-37`, generates randomized drafts, and exports quiz-app JSON.

## Required Manual Action

In GitHub:

1. Open `GreyGollum/Water-Operator-Vault`.
2. Click **Actions**.
3. Select **Sync Remaining Files From Vault-37**.
4. Click **Run workflow**.
5. Choose branch: `main`.
6. Click **Run workflow**.
7. Wait for the run to complete.
8. Confirm a bot commit appears on `main`.

## Expected Bot Commit Contents

The workflow should add/update:

```text
02 Flash Cards/T5 Flash Cards - Water Math.md
02 Flash Cards/T5 Flash Cards - Disinfection and CT.md
02 Flash Cards/T5 Flash Cards - Treatment Processes.md
02 Flash Cards/T5 Flash Cards - PFAS and MCLs.md
02 Flash Cards/T5 Flash Cards - SDWA and Regulations.md
02 Flash Cards/T5 Flash Cards - Water Quality and Contaminants.md
03 Practice Exams/T5 Practice Exam Suite - 250 Questions.md
03 Practice Exams/T5 Math-Only Practice Bank.md
03 Practice Exams/T5 PFAS and Emerging Contaminants Mini Exam.md
03 Practice Exams/T5 Practice Exam 06 - Advanced Scenario Mix.md
03 Practice Exams/Randomized Final Drafts/Randomized Practice Exam Manifest.md
05 Quiz App/t5_quiz_app_questions.json
09 Verification and Sources/Card Audit - Water Math.md
09 Verification and Sources/Card Audit - Disinfection and CT.md
09 Verification and Sources/Card Audit - Treatment Processes.md
```

## Expected Final Counts

```yaml
large_flashcard_decks_expected: 3
source_question_banks_expected: 4
randomized_question_total_expected: 570
quiz_json_expected: true
```

## Verification After Workflow

After the workflow run completes, verify these files exist:

- [[02 Flash Cards/T5 Flash Cards - Water Math]]
- [[02 Flash Cards/T5 Flash Cards - Disinfection and CT]]
- [[02 Flash Cards/T5 Flash Cards - Treatment Processes]]
- [[03 Practice Exams/Randomized Final Drafts/Randomized Practice Exam Manifest]]
- `05 Quiz App/t5_quiz_app_questions.json`

Then update [[Standalone Transfer Manifest]]:

```yaml
pass_5_outputs_confirmed: true
full_standalone_vault_complete: true
```

## Current Status

```yaml
sync_script_installed: true
sync_workflow_installed: true
quiz_json_exporter_installed: true
manual_workflow_run_required: true
pass_5_outputs_confirmed: false
```
