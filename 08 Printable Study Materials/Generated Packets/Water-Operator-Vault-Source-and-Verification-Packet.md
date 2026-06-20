---
title: Water Operator Vault Source and Verification Packet
project: Water Operator Vault
status: draft-printable
---

# Water Operator Vault Source and Verification Packet

> Draft printable packet. Verify current regulations, local requirements, and source caveats before public/final release.


\newpage

<!-- Source: README.md -->

# Water Operator Vault

> Standalone Obsidian vault for drinking-water operator study, focused on California T5 preparation and high-level water-operations review.

## Status

```yaml
project: Water Operator Vault
standalone_repo: true
source_history_repo: GreyGollum/Vault-37
source_export_path: _vault_exports/Water-Operator-Vault/
release_type: internal_study_release
public_final_release_ready: false
quiz_app_ready: false
```

## Start Here

Open this repository as an Obsidian vault and begin with:

- [[00 Dashboard/Water Operator Vault Dashboard]]
- [[01 Study Hub/T5 Study Hub]]
- [[09 Verification and Sources/Verification Master Index]]

## Important Caveat

This vault is an operator-study tool. It does not replace California DDW requirements, EPA regulations, certified-lab SOPs, approved cross-connection tester manuals, engineering specifications, site SOPs, SDS, or authority-having-jurisdiction requirements.

## Copyright / Source Policy

This repo should contain original study notes, source-control notes, summaries, flashcards, quizzes, indexes, and app files. Do **not** upload copyrighted source books, manuals, or PDFs directly into this public repository unless they are clearly public-domain/open-licensed and allowed to be redistributed.

## Current Build Priorities

1. Finish standalone vault transfer from `GreyGollum/Vault-37`.
2. Copy remaining full flashcard decks.
3. Confirm randomized 570-question generated output.
4. Generate quiz-app JSON with batch IDs.
5. Build PDF/DOCX printable packets.
6. Complete final legal/technical source audit before public/final release.


\newpage

<!-- Source: 09 Verification and Sources/Verification Master Index.md -->


# Verification Master Index

> Central audit dashboard for the Water Operator Vault. This index tracks flashcard deck audits, practice-test audit status, copied/exported files, source-intake batches, and what still blocks final `verified` status.

## Release Status

| Release Type | Status | Date | Notes |
|---|---|---:|---|
| Internal study release | Ready / released | 2026-06-19 | Ready for personal T5 study and draft printable use with caveats. |
| Draft printable practice exams | Ready with caveats | 2026-06-19 | Randomized final drafts are committed; lab, cross-connection, and distribution-source mini-exams added to generator path. |
| Public/final release | Not ready | — | Legal/technical/lab/cross-connection/distribution source-depth blockers remain. |
| Quiz-app release | Not ready | — | Needs quiz-app JSON export from randomized answer keys. |

## Module Wiring Status

```yaml
lab_sources_in_bibliography: true
lab_source_database_created: true
lab_flashcards_added: 48
lab_mini_exam_questions_added: 50
lab_answer_key_checked: true
lab_generator_path_enabled: true
cross_connection_section_created: true
cross_connection_database_created: true
cross_connection_flashcards_added: 25
cross_connection_awwa_c510_captured: true
cross_connection_usc_manual_pending: true
water_supply_distribution_source_intake_added: true
water_supply_distribution_uploaded_reference_count: 12
distribution_source_roadmap_added: true
distribution_source_database_created: true
distribution_source_flashcards_added: 42
distribution_source_mini_exam_questions_added: 40
distribution_source_answer_key_checked: true
distribution_source_generator_path_enabled: true
new_total_study_questions: 570
```

## Core Status Tables

| Area | Status |
|---|---|
| Practice questions checked | 570 |
| Answer-key corrections required | 0 |
| Lab procedures | Source-supported with caveats |
| Cross-connection control | Source-supported; USC/AWWA M14/CA context pending |
| Distribution/source/hydrant content | Source-supported with caveats |
| Quiz app | JSON/export pending |
| Public/final release | Not ready |

## Source Control Files

| File | Purpose | Status |
|---|---|---|
| [[Water Operator Source Bibliography]] | Core source IDs, URLs, verified values, formula constants, lab/cross-connection/distribution sources | active |
| [[Water Supply Distribution Source Intake - 2026-06-19]] | Supply/distribution/hydrants/disinfection/treatment media source batch | active |
| [[Distribution and Source Module Build Roadmap]] | Module build plan from the new source batch | active |
| [[Distribution Source Content Audit - 2026-06-19]] | Verification note for distribution-source cards/exam/database | active |
| [[Lab Methods Source Bibliography Supplement]] | Detailed lab-method source IDs | active |
| [[Cross Connection Source Bibliography Supplement]] | Backflow/cross-connection source IDs | active |
| [[Practice Exam Audit Status]] | Tracks practice exam inventory and validation status | active |
| [[Practice Exam Finalization Status]] | Tracks randomized final drafts | active |

## Final Verification Blockers

1. Direct California Title 22 section-level audit.
2. Direct eCFR 40 CFR 141 legal-text audit.
3. RTCR exact Level 1 / Level 2 assessment trigger wording.
4. CCR exact delivery/content rule audit.
5. SWTR / IESWTR / LT2 surface-water treatment audit.
6. Official CT table source audit for required CT values.
7. DBPR details including LRAA/sample-location specifics.
8. UV/ozone technical guidance and validation criteria.
9. Chloramination/nitrification technical guidance.
10. Cross-connection/backflow California-specific audit.
11. USC Foundation Manual source capture for field-test procedures and device-selection details.
12. AWWA M14 source capture for program guidance.
13. Distribution/source/hydrant module deep build from new AWWA source batch.
14. Source-integrity review for uploaded Water Sources file.
15. Treatment-process technical-source audit using accepted operator-training or engineering references.
16. Lab-procedure final source audit, including California DDW lab/reporting context and method-version details.
17. Lab/cross-connection/distribution-source mini-exam randomized output confirmation and quiz-app JSON export.
18. Final pre-print date-sensitive recheck for PFAS, lead/copper, current California operator-certification materials, lab-method references, cross-connection rules, and distribution-management references.

## Recommended Next Actions

1. Finish full standalone transfer into this repo.
2. Copy full audited deck bodies for Water Math, Disinfection/CT, and Treatment Processes.
3. Confirm generated 570-question randomized output.
4. Generate quiz-app JSON.
5. Build printable PDF/Word packets.


\newpage

<!-- Source: 09 Verification and Sources/Standalone Transfer Manifest.md -->


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

## Completed In Transfer Pass 5

| Item | Status |
|---|---|
| Sync script for large decks/source banks | installed and used |
| GitHub Actions workflow for sync/generate/export | installed and used |
| Quiz JSON exporter scaffold | installed and used |
| Full Water Math deck | confirmed in repo |
| Full Disinfection and CT deck | confirmed in repo |
| Full Treatment Processes deck | confirmed in repo |
| Original 450-question source banks | confirmed in repo |
| Randomized 570-question output confirmation | confirmed |
| Quiz-app JSON export | confirmed: 11 sets / 570 questions |
| Expanded quiz app shell after JSON format is finalized | pending enhancement, not blocking standalone transfer |

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
large_flashcard_decks_transferred: true
mini_exams_transferred: true
source_banks_transferred: true
randomized_outputs_confirmed: true
quiz_json_confirmed: true
quiz_json_set_count: 11
quiz_json_question_count: 570
quiz_app_shell_transferred: true
generator_transferred: true
pass_5_automation_installed: true
pass_5_outputs_confirmed: true
full_standalone_vault_complete: true
```

---

## Remaining Release Work

Standalone transfer is complete. Full public/final release still requires:

- final source/legal audit
- final current-regulatory recheck
- printable PDF/DOCX packet build
- optional quiz app UI expansion beyond the starter shell

---

## Related

- [[Verification Master Index]]
- [[Water Operator Source Bibliography]]
- [[00 Dashboard/Water Operator Vault Dashboard]]


\newpage

<!-- Source: 09 Verification and Sources/Water Operator Source Bibliography.md -->


# Water Operator Source Bibliography

> Source-control file for the Water Operator Vault. Use this file to trace facts, formulas, regulations, MCLs, exam-scope claims, lab-method claims, cross-connection claims, distribution-system claims, and operator-study claims back to official or accepted references.

## Source Reliability Tiers

| Tier | Description | Use |
|---|---|---|
| Tier 1 | Official laws, regulations, EPA pages, California Water Boards / DDW pages, CFR/eCFR | Regulatory values, MCLs, action levels, operator certification rules, compliance method authority |
| Tier 2 | Official technical guidance from EPA, California Water Boards, Sacramento State / Office of Water Programs, AWWA manuals when available | Treatment processes, CT guidance, operator training concepts, source water, distribution, cross-connection program concepts |
| Tier 3 | Manufacturer manuals, engineering references, WEF/CRC/operator-training references, peer-reviewed papers, AWWA product/system standards | Equipment-specific or technical background only |
| Not Accepted | Exam dumps, unsourced blogs, quiz sites copying alleged exam questions | Do not cite as authoritative |

---

## Core Regulatory Sources

| Source ID | Source | Use | Last Checked |
|---|---|---|---|
| EPA-NPDWR | EPA National Primary Drinking Water Regulations | MCLs, MRDLs, treatment techniques, DBPs, disinfectants, IOCs, radionuclides | 2026-06-19 |
| EPA-PFAS-NPDWR | EPA PFAS National Primary Drinking Water Regulation | PFAS MCLs, hazard index, date-sensitive PFAS rule status | 2026-06-19 |
| EPA-LCR | EPA Lead and Copper Rule | Lead/copper tap monitoring and action-level transition context | 2026-06-19 |
| EPA-PUBLIC-NOTIFICATION | EPA Public Notification Rule | Tier 1/2/3 timing and notification purpose | 2026-06-19 |
| EPA-CCR | EPA Consumer Confidence Reports | Annual CCR concept, July 1 delivery cue, contents | 2026-06-19 |
| EPA-RTCR | EPA Revised Total Coliform Rule | Total coliform/E. coli, repeat sampling, assessments | 2026-06-19 |
| EPA-PWS | EPA Public Water Systems | PWS and CWS/NTNCWS/TNCWS classification | 2026-06-19 |
| eCFR-40-CFR-141 | 40 CFR Part 141 | Federal legal text for drinking-water regs and approved methods | pending deep audit |
| CA-DWOP | CA Drinking Water Operator Certification Program | California exam/program material | 2026-06-19 |
| CA-T5-DESCRIPTION-2026 | Preparing for T5 Exam, Rev. 1/22/26 | Exact T5 oral exam structure | 2026-06-19 |
| CA-EXAM-CONVERSION-2026 | CA exam conversion sheet, Rev. 4/30/2026 | Official exam math constants | 2026-06-19 |
| CA-DDW-PFAS-DRINKING-WATER | California PFAS drinking-water resources | California PFAS NL/RL values | 2026-06-19 |

---

## Lab Source Supplements

See [[Lab Methods Source Bibliography Supplement]].

Key source IDs:

- EPA-APPROVED-METHODS
- ECFR-APPENDIX-A-PART-141
- EPA-RTCR-METHODS
- EPA-DBP-METHODS
- EPA-INORGANIC-METHODS
- WEF-WATER-WASTEWATER-LAB-TECHNIQUES-2E
- CRC-WATER-WASTEWATER-EXAM-MANUAL-ADAMS
- CAWST-DWQT-MANUAL
- OEWRI-COLILERT-SOP
- IDEXX-HPC-QUANTI-TRAY
- IDEXX-SIMPLATE-HPC
- SMEWW-HPC-POUR-PLATE

---

## Cross-Connection Source Supplements

See [[Cross Connection Source Bibliography Supplement]].

Key source IDs:

- AWWA-C510-1997
- USC-FCCCHR-MANUAL-PENDING
- AWWA-M14-PENDING
- CA-CROSS-CONNECTION-CONTEXT-PENDING

---

## Distribution / Source / Hydrant Source Batch

See [[Water Supply Distribution Source Intake - 2026-06-19]] and [[Distribution and Source Module Build Roadmap]].

Key source IDs:

- AWWA-WSO-WATER-SOURCES-4E
- AWWA-WSO-TD-WORKBOOK-4E
- AWWA-G200-15
- AWWA-C502-18
- AWWA-DISINFECTION-FIELD-GUIDE
- AWWA-M20-CHLORINATION-CHLORAMINATION
- AWWA-B403-16
- AWWA-B600-16
- AWWA-B604-05
- AWWA-B112-19
- AWWA-B114-22
- AWWA-WQT-6E-TOC

---

## Current Verified Value Snapshot

| Item | Value | Source ID | Status |
|---|---:|---|---|
| Arsenic MCL | 10 µg/L | EPA-NPDWR | verified 2026-06-19 |
| Nitrate MCL | 10 mg/L as N | EPA-NPDWR | verified 2026-06-19 |
| Nitrite MCL | 1 mg/L as N | EPA-NPDWR | verified 2026-06-19 |
| Fluoride MCL | 4.0 mg/L | EPA-NPDWR | verified 2026-06-19 |
| Copper Action Level | 1.3 mg/L | EPA-NPDWR / EPA-LCR | verified 2026-06-19 |
| Lead Action Level | transition-sensitive; see note | EPA-LCR / EPA-NPDWR | caveated |
| TTHM MCL | 80 µg/L | EPA-NPDWR | verified 2026-06-19 |
| HAA5 MCL | 60 µg/L | EPA-NPDWR | verified 2026-06-19 |
| Bromate MCL | 10 µg/L | EPA-NPDWR | verified 2026-06-19 |
| Chlorite MCL | 1.0 mg/L | EPA-NPDWR | verified 2026-06-19 |
| Chlorine MRDL | 4.0 mg/L as Cl2 | EPA-NPDWR | verified 2026-06-19 |
| Chloramines MRDL | 4.0 mg/L as Cl2 | EPA-NPDWR | verified 2026-06-19 |
| Chlorine dioxide MRDL | 0.8 mg/L as ClO2 | EPA-NPDWR | verified 2026-06-19 |
| PFOA federal MCL | 4.0 ppt / ng/L | EPA-PFAS-NPDWR | date-sensitive |
| PFOS federal MCL | 4.0 ppt | EPA-PFAS-NPDWR | date-sensitive |

---

## Related

- [[Verification Master Index]]
- [[Current Regulatory Recheck - 2026-06-19]]
- [[Lead and Copper Rule Transition Note]]
- [[Practice Exam Audit Status]]


\newpage

<!-- Source: 09 Verification and Sources/Practice Exam Audit Status.md -->


# Practice Exam Audit Status

> Tracks T5 practice-test answer-key verification and release readiness.

## Answer-Key Verification Progress

| File / Block | Questions | Answer-Key Status | Corrections Required |
|---|---:|---|---:|
| Practice Exam 01 - Core Regulations, MCLs, and Operator Math | 50 | verified with caveats | 0 |
| Practice Exam 02 - Treatment Processes and Water Quality | 50 | verified; randomized final draft committed | 0 |
| Practice Exam 03 - Source Water, Distribution, Sampling, Public Health | 50 | verified; randomized final draft committed | 0 |
| Practice Exam 04 - Advanced Math, Pumps, SCADA, Operations | 50 | verified with caveats | 0 |
| Practice Exam 05 - Scenario Judgment, Compliance, Troubleshooting | 50 | verified; randomized final draft committed | 0 |
| T5 Math-Only Practice Bank | 100 | verified with caveats; randomized final draft committed | 0 |
| T5 PFAS and Emerging Contaminants Mini Exam | 50 | verified with date-sensitive caveats | 0 |
| Practice Exam 06 - Advanced Scenario Mix | 50 | verified; randomized final draft committed | 0 |
| T5 Lab Procedures and Methods Mini Exam | 50 | verified with source caveats | 0 |
| T5 Cross Connection Control Mini Exam | 30 | verified with source caveats | 0 |
| T5 Distribution Source Hydrants and Disinfection Mini Exam | 40 | verified with source caveats | 0 |

## Current Question Count

| Category | Count |
|---|---:|
| Main 5-exam suite | 250 |
| Math-only bank | 100 |
| PFAS/emerging mini-exam | 50 |
| Advanced scenario exam 06 | 50 |
| Lab procedures mini-exam | 50 |
| Cross-connection mini-exam | 30 |
| Distribution source / hydrants / disinfection mini-exam | 40 |
| **Total Study Questions** | **570** |

## Audit Finding

```yaml
practice_questions_checked: 570
answer_key_corrections_required: 0
randomized_final_drafts_committed_for_original_450: true
lab_mini_exam_generator_enabled: true
cross_connection_mini_exam_generator_enabled: true
distribution_source_mini_exam_generator_enabled: true
print_status: draft_ready_with_caveats_after_regeneration
```

## Remaining Work Before Final Public Release

- Confirm generated output includes all 570 questions.
- Export printable PDF/Word packets.
- Generate quiz-app JSON from randomized final drafts.
- Run final current-regulatory/source recheck before public/final release.

## Related

- [[Practice Exam Finalization Status]]
- [[Verification Master Index]]


\newpage

<!-- Source: 09 Verification and Sources/Practice Exam Finalization Status.md -->


# Practice Exam Finalization Status

> Tracks the final polish pass for T5 practice exams: randomization, rationales, metadata, batch IDs, export packaging, and current-regulatory recheck date.

## Current Status

| Item | Status |
|---|---|
| Original 450 answer keys verified | complete |
| Lab mini-exam answer key verified | complete |
| Cross-connection mini-exam answer key verified | complete |
| Distribution-source mini-exam answer key verified | complete |
| New total study questions | 570 |
| Answer-key corrections required | 0 |
| Deterministic randomization generator | updated |
| Batch ID output | generator updated |
| Randomized output files for original 450 | committed |
| Randomized output for added mini-exams | pending output confirmation |
| Quiz-app release | not yet |

## Generator Scope

The generator now targets:

- T5 Practice Exam Suite - 250 Questions
- T5 Math-Only Practice Bank
- T5 PFAS and Emerging Contaminants Mini Exam
- T5 Practice Exam 06 - Advanced Scenario Mix
- T5 Lab Procedures and Methods Mini Exam
- T5 Cross Connection Control Mini Exam
- T5 Distribution Source Hydrants and Disinfection Mini Exam

## Expected Output

```yaml
total_questions_expected: 570
batch_ids_required: true
quiz_page_and_answer_key_page_separate: true
randomized_output_confirmation: pending
quiz_app_json: pending
```

## Remaining Finalization Steps

1. Confirm regenerated 570-question randomized output set.
2. Spot-check generated answer-choice distribution and batch IDs.
3. Generate quiz-app JSON.
4. Export printable PDF/Word packets.
5. Run final current source recheck before public/final release.

## Related

- [[Practice Exam Audit Status]]
- [[Verification Master Index]]


\newpage

<!-- Source: 09 Verification and Sources/Current Regulatory Recheck - 2026-06-19.md -->


# Current Regulatory Recheck - 2026-06-19

> Dated recheck marker for the Water Operator Vault. This note records the vault's current-regulatory snapshot date and the areas that must be rechecked before any public/final release.

## Recheck Date

```yaml
last_current_regulatory_recheck: 2026-06-19
public_final_release_ready: false
future_recheck_required_before_public_release: true
```

## Items Treated As Date-Sensitive

- PFAS federal drinking-water rules and compliance timing
- California PFAS notification/response levels
- Lead and Copper Rule / LCRI transition language
- California operator-certification pages and exam materials
- Public Notification / CCR details
- RTCR exact trigger wording
- Approved analytical methods and method versions
- Cross-connection and distribution rules where state/local requirements apply

## Study Use

The vault is acceptable for internal study with visible caveats. Before a public/final release, source values and legal wording must be rechecked against official current sources.

## Related

- [[Water Operator Source Bibliography]]
- [[Lead and Copper Rule Transition Note]]
- [[Verification Master Index]]


\newpage

<!-- Source: 09 Verification and Sources/Lead and Copper Rule Transition Note.md -->


# Lead and Copper Rule Transition Note

> Lead and copper values and language are transition-sensitive. Use this note to keep study material from mixing older exam-prep language with current rule text without a caveat.

## Study Caveat

```yaml
lead_copper_transition_sensitive: true
verify_before_public_release: true
```

Older/common exam-prep material may reference lead action level language differently from current EPA table language. Keep both exam-context and current-rule context clearly marked until the final legal/source audit is complete.

## Rule

Before final print/public release:

1. Recheck EPA Lead and Copper Rule page.
2. Recheck current NPDWR table.
3. Recheck California DDW context if used.
4. Update all lead/copper cards, questions, and source notes consistently.

## Related

- [[Water Operator Source Bibliography]]
- [[Current Regulatory Recheck - 2026-06-19]]
- [[Verification Master Index]]


\newpage

<!-- Source: 09 Verification and Sources/Pass 5 Sync Report.md -->


# Pass 5 Sync Report

## Summary

```yaml
copied_count: 14
failed_count: 0
vault37_token_present: true
workflow_should_continue: true
```

## Copied Files

| Source | Target |
|---|---|
| `14 Water Operations/Flash Cards/T5 Flash Cards - Water Math.md` | `02 Flash Cards/T5 Flash Cards - Water Math.md` |
| `14 Water Operations/Flash Cards/T5 Flash Cards - Disinfection and CT.md` | `02 Flash Cards/T5 Flash Cards - Disinfection and CT.md` |
| `14 Water Operations/Flash Cards/T5 Flash Cards - Treatment Processes.md` | `02 Flash Cards/T5 Flash Cards - Treatment Processes.md` |
| `14 Water Operations/Flash Cards/T5 Flash Cards - SDWA and Regulations.md` | `02 Flash Cards/T5 Flash Cards - SDWA and Regulations.md` |
| `14 Water Operations/Flash Cards/T5 Flash Cards - Water Quality and Contaminants.md` | `02 Flash Cards/T5 Flash Cards - Water Quality and Contaminants.md` |
| `_vault_exports/Water-Operator-Vault/02 Flash Cards/T5 Flash Cards - PFAS and MCLs.md` | `02 Flash Cards/T5 Flash Cards - PFAS and MCLs.md` |
| `14 Water Operations/Practice Exams/T5 Practice Exam Suite - 250 Questions.md` | `03 Practice Exams/T5 Practice Exam Suite - 250 Questions.md` |
| `14 Water Operations/Practice Exams/T5 Math-Only Practice Bank.md` | `03 Practice Exams/T5 Math-Only Practice Bank.md` |
| `14 Water Operations/Practice Exams/T5 PFAS and Emerging Contaminants Mini Exam.md` | `03 Practice Exams/T5 PFAS and Emerging Contaminants Mini Exam.md` |
| `14 Water Operations/Practice Exams/T5 Practice Exam 06 - Advanced Scenario Mix.md` | `03 Practice Exams/T5 Practice Exam 06 - Advanced Scenario Mix.md` |
| `14 Water Operations/Practice Exams/T5 Practice Exam Printable Score Sheets.md` | `03 Practice Exams/T5 Practice Exam Printable Score Sheets.md` |
| `_vault_exports/Water-Operator-Vault/09 Verification and Sources/Card Audit - Water Math.md` | `09 Verification and Sources/Card Audit - Water Math.md` |
| `_vault_exports/Water-Operator-Vault/09 Verification and Sources/Card Audit - Disinfection and CT.md` | `09 Verification and Sources/Card Audit - Disinfection and CT.md` |
| `_vault_exports/Water-Operator-Vault/09 Verification and Sources/Card Audit - Treatment Processes.md` | `09 Verification and Sources/Card Audit - Treatment Processes.md` |

## Failed Files

| Source | Target | Error |
|---|---|---|


\newpage

<!-- Source: 05 Quiz App/Quiz App Status.md -->


# Quiz App Status

## Current Status

```yaml
browser_app_shell: transferred
batch_id_display: included
separate_answer_key_view: included
attempt_history_by_batch_id: included
json_export_exists: true
json_set_count: 11
json_question_count: 570
batch_ids_present: true
quiz_answer_key_pairing_by_batch_id: true
validator_passes: true
static_smoke_test_passes: true
browser_manual_test: recommended
quiz_app_working: validated_starter_shell
```

## Confirmed Outputs

- `05 Quiz App/t5_quiz_app_questions.json`
- 11 quiz sets
- 570 total questions
- visible batch IDs per set and question
- separate quiz page title and answer-key page title fields
- [[09 Verification and Sources/Quiz JSON Validation Report]] passed
- [[09 Verification and Sources/Quiz App Smoke Test Report]] passed

## Still Recommended

- Open `05 Quiz App/t5_quiz_app.html` in a browser.
- Load `t5_quiz_app_questions.json` through the file picker.
- Confirm scoring works on at least one set.
- Confirm answer-key page shows the matching batch ID.
- Optionally expand the starter shell UI after JSON format is stable.

## Related

- [[t5_quiz_app.html]]
- [[Quiz App Contract]]
- [[09 Verification and Sources/Practice Exam Finalization Status]]
- [[09 Verification and Sources/Standalone Transfer Manifest]]
