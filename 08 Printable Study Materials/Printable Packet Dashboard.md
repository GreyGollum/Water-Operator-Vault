---
type: dashboard-control
project: Water Operator Vault
area: printable-study-materials
status: active
created: 2026-06-19
last_updated: 2026-06-19
tags: [printable, artifacts, dashboard, github-actions]
---

# Printable Packet Dashboard

## Build Printable Artifacts

Use this when you want to rebuild the printable packet ZIP containing PDF/DOCX files.

<div class="water-vault-button-row">
<a class="water-vault-button" href="https://github.com/GreyGollum/Water-Operator-Vault/actions/workflows/build-printable-packets.yml">Build Printable Packets in GitHub Actions</a>
</div>

## Recommended Path

1. Click **Build Printable Packets in GitHub Actions**.
2. Click **Run workflow**.
3. Select branch `main`.
4. Wait for the green check.
5. Download artifact: `water-operator-vault-printable-packets`.

## Artifact Contents

Expected ZIP contents:

```text
Water-Operator-Vault-Flashcards-Packet.docx
Water-Operator-Vault-Flashcards-Packet.pdf
Water-Operator-Vault-Practice-Exam-Packet.docx
Water-Operator-Vault-Practice-Exam-Packet.pdf
Water-Operator-Vault-Source-and-Verification-Packet.docx
Water-Operator-Vault-Source-and-Verification-Packet.pdf
```

Specialized DOCX layouts:

```yaml
flashcards_docx:
  layout: 8 cut cards per landscape page
  duplex: front page followed by matching back page
  print_setting: double-sided, flip on long edge

practice_exam_docx:
  questions: left aligned, no visible question table lines
  choices: 2 columns x 2 rows, no visible choice table lines
  answer_keys: own page after each exam
```

## Local Build Option

If this repo is cloned locally and dependencies are installed, run:

```bash
python tools/run_printable_packet_build.py --local
```

To open the GitHub Actions page from a local machine:

```bash
python tools/run_printable_packet_build.py --open-actions
```

## Local Dependencies

```bash
python -m pip install python-docx
```

Optional for generic PDF/DOCX conversion:

```text
pandoc
xelatex
```

## Related

- [[DOCX Layout Specification]]
- [[Generated Packets/Water-Operator-Vault-Flashcards-Packet]]
- [[Generated Packets/Water-Operator-Vault-Practice-Exam-Packet]]
- [[09 Verification and Sources/Release Readiness Status]]
