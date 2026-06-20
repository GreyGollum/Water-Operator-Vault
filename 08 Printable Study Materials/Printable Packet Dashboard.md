---
type: dashboard-control
project: Water Operator Vault
area: printable-study-materials
status: active
created: 2026-06-19
last_updated: 2026-06-19
tags: [printable, artifacts, dashboard, local-build, ipad]
---

# Printable Packet Dashboard

## Build Printable Artifacts

Output folder inside the vault:

```text
08 Printable Study Materials/Build Artifacts
```

There are two supported build paths:

```yaml
desktop_windows:
  mode: local_python_build
  script: scripts/build_printable_packets_windows.bat
  output: vault_build_artifacts_folder

ipad_mobile:
  mode: github_actions_build_then_sync
  workflow: Build Printable Packets
  commit_artifacts_to_vault: true
  output: vault_build_artifacts_folder_after_sync
```

## iPad / Mobile Path

Obsidian on iPad cannot run local Python or shell scripts directly. For iPad, use the GitHub workflow and let it commit the generated PDF/DOCX files back into the vault.

1. Open the workflow:

[Build Printable Packets](https://github.com/GreyGollum/Water-Operator-Vault/actions/workflows/build-printable-packets.yml)

2. Tap **Run workflow**.
3. Keep `commit_artifacts` set to `true`.
4. Wait for the green check.
5. Sync/pull the vault on iPad using your normal Git/Working Copy/Obsidian sync method.
6. Open:

```text
08 Printable Study Materials/Build Artifacts
```

The generated DOCX/PDF files should now be in the vault.

## Desktop Local Button Path

A normal Obsidian Markdown link cannot run Python by itself. To make a real desktop button that runs the local script, use the **Shell Commands** community plugin, then optionally expose it with Commander, Buttons, or another dashboard-button plugin.

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

Expected outputs:

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

## Related

- [[DOCX Layout Specification]]
- [[Generated Packets/Water-Operator-Vault-Flashcards-Packet]]
- [[Generated Packets/Water-Operator-Vault-Practice-Exam-Packet]]
- [[09 Verification and Sources/Release Readiness Status]]
