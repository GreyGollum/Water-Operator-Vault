---
type: layout-specification
project: Water Operator Vault
area: printable-study-materials
status: active
created: 2026-06-19
last_updated: 2026-06-19
tags: [docx, printable, flashcards, exams]
---

# DOCX Layout Specification

## Purpose

The `.md` packet files remain informational/reference files with Obsidian links. The `.docx` packet files are print-layout files and may intentionally differ from the Markdown structure.

## Flashcard DOCX

```yaml
file: 08 Printable Study Materials/Build Artifacts/Water-Operator-Vault-Flashcards-Packet.docx
layout: duplex_cut_cards
page_orientation: landscape
cards_per_page: 8
grid: 4_rows_x_2_columns
front_pages: questions
back_pages: answers_and_sources
printing: double_sided_flip_on_long_edge
```

Design notes:

- Each front page is followed by the matching back page.
- Card fronts show deck name, card number, and question.
- Card backs show card number, answer, and source/deck reference.
- Table borders act as cut lines.

## Practice Exam DOCX

```yaml
file: 08 Printable Study Materials/Build Artifacts/Water-Operator-Vault-Practice-Exam-Packet.docx
layout: exam_blocks
question_format: one_question_block
choices_format: separate_choices_block_below_question
answer_key: own_page_after_each_exam
```

Design notes:

- Each question is placed in its own shaded block.
- Multiple-choice answers are placed in a separate bordered block beneath the question.
- Answer keys start on their own page after each exam.
- Batch IDs are preserved.

## Source and Verification DOCX

```yaml
file: 08 Printable Study Materials/Build Artifacts/Water-Operator-Vault-Source-and-Verification-Packet.docx
layout: informational_reference
source: markdown_packet_via_pandoc
```

## Related

- [[Generated Packets/Water-Operator-Vault-Flashcards-Packet]]
- [[Generated Packets/Water-Operator-Vault-Practice-Exam-Packet]]
- [[Generated Packets/Water-Operator-Vault-Source-and-Verification-Packet]]
- [[09 Verification and Sources/Release Readiness Status]]
