---
type: dashboard-control
project: Water Operator Vault
area: printable-study-materials
status: active
created: 2026-06-19
last_updated: 2026-06-19
tags: [printable, artifacts, dashboard, local-build]
---

# Printable Packet Dashboard

## Build Printable Artifacts Locally

Use this when you want Obsidian to trigger a local script that creates the printable files inside the vault.

Output folder:

```text
08 Printable Study Materials/Build Artifacts
```

## Dashboard Button Setup

A normal Obsidian Markdown link cannot run Python by itself. To make a real button that runs the local script, use the **Shell Commands** community plugin, then optionally expose it with Commander, Buttons, or another dashboard-button plugin.

### Shell Command

Create a Shell Commands plugin command named:

```text
Build Water Operator Printable Packets
```

Command on Windows:

```cmd
scripts\build_printable_packets_windows.bat
```

Command on macOS/Linux:

```bash
bash scripts/build_printable_packets_unix.sh
```

Working directory should be the vault root.

## Button Block Example

If using an Obsidian button plugin that can run commands, connect the button to this command:

```text
Build Water Operator Printable Packets
```

Example display text:

```text
Build Printable Packets
```

## Manual Local Run

Windows:

```cmd
scripts\build_printable_packets_windows.bat
```

macOS/Linux:

```bash
bash scripts/build_printable_packets_unix.sh
```

Direct Python:

```bash
python tools/run_printable_packet_build.py --local
```

## Local Dependencies

The launcher scripts install/update:

```text
python-docx
```

Optional for generic PDF/DOCX conversion:

```text
pandoc
xelatex
```

Without Pandoc, the specialized DOCX files still build, but generic PDF packet conversion may be skipped.

## Artifact Contents

Expected local outputs:

```text
Water-Operator-Vault-Flashcards-Packet.docx
Water-Operator-Vault-Practice-Exam-Packet.docx
Water-Operator-Vault-Source-and-Verification-Packet.docx
Water-Operator-Vault-Flashcards-Packet.pdf
Water-Operator-Vault-Practice-Exam-Packet.pdf
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

## GitHub Actions Backup

GitHub Actions can still build the artifact ZIP when needed:

[Open Build Printable Packets workflow](https://github.com/GreyGollum/Water-Operator-Vault/actions/workflows/build-printable-packets.yml)

## Related

- [[DOCX Layout Specification]]
- [[Generated Packets/Water-Operator-Vault-Flashcards-Packet]]
- [[Generated Packets/Water-Operator-Vault-Practice-Exam-Packet]]
- [[09 Verification and Sources/Release Readiness Status]]
