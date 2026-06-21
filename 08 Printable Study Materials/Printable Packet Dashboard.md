---
type: dashboard-control
project: Water Operator Vault
area: printable-study-materials
status: active
created: 2026-06-19
last_updated: 2026-06-19
cssclasses: [water-vault-dashboard, water-vault-gui]
tags: [printable, artifacts, dashboard, local-build, ipad]
---

# Printable Packet Dashboard

<div class="water-vault-hero compact">
<span class="water-vault-status">Print / Export</span>
<div class="water-vault-title">Printable Packets</div>
<p class="water-vault-subtitle">Maintainer control dashboard for printable artifacts, desktop local builds, iPad/mobile workflow, GitHub Actions, and finished DOCX/PDF packet output.</p>
</div>

## Build Printable Artifacts

<div class="water-vault-kpi-grid">
<div class="water-vault-kpi"><strong>DOCX</strong><span>specialized layouts</span></div>
<div class="water-vault-kpi"><strong>PDF</strong><span>packet outputs</span></div>
<div class="water-vault-kpi"><strong>iPad</strong><span>GitHub Actions path</span></div>
<div class="water-vault-kpi"><strong>Windows</strong><span>local script path</span></div>
</div>

<div class="water-vault-action-grid">

<div class="water-vault-action-card featured">
<h3>Printable Launcher</h3>
<p>Cross-platform launcher that helps shared users find the right printable path.</p>
<a class="water-vault-action" href="obsidian://open?file=08%20Printable%20Study%20Materials%2FPrintable%20Launcher.html">Open Launcher</a>
</div>

<div class="water-vault-action-card featured">
<h3>Build Artifacts Folder</h3>
<p>Finished printable files should land in this folder before the vault is shared.</p>
<p><code>08 Printable Study Materials/Build Artifacts</code></p>
</div>

<div class="water-vault-action-card">
<h3>Windows Local Build</h3>
<p>Run this from the vault root when rebuilding locally on Windows.</p>
<p><code>scripts\build_printable_packets_windows.bat</code></p>
</div>

<div class="water-vault-action-card">
<h3>Direct Python Build</h3>
<p>Direct maintainer command for the local printable packet builder.</p>
<p><code>python tools/run_printable_packet_build.py --local</code></p>
</div>

</div>

## iPad / Mobile Path

<div class="water-vault-callout">
Obsidian on iPad cannot run local Python or shell scripts directly. For iPad, use the GitHub workflow and let it commit the generated PDF/DOCX files back into the vault.
</div>

<div class="water-vault-action-grid">
<div class="water-vault-action-card featured"><h3>Build Printable Packets Workflow</h3><p>Open GitHub Actions, run the workflow, keep <code>commit_artifacts</code> set to <code>true</code>, wait for the green check, then sync/pull the vault.</p><a class="water-vault-action" href="https://github.com/GreyGollum/Water-Operator-Vault/actions/workflows/build-printable-packets.yml">Open Workflow</a></div>
<div class="water-vault-action-card"><h3>After Workflow Completes</h3><p>Sync/pull the vault using Git, Working Copy, Obsidian sync method, or GitHub Desktop. Then open the Build Artifacts folder.</p><p><code>08 Printable Study Materials/Build Artifacts</code></p></div>
</div>

## Desktop Local Button Path

<div class="water-vault-callout">
A normal Obsidian Markdown link cannot run Python by itself. To make a real desktop button that runs the local script, use the Shell Commands community plugin, then optionally expose it with Commander, Buttons, or another dashboard-button plugin.
</div>

<div class="water-vault-panel">

```yaml
shell_command_name: Build Water Operator Printable Packets
windows_command: scripts\build_printable_packets_windows.bat
mac_linux_command: bash scripts/build_printable_packets_unix.sh
working_directory: vault_root
example_button_text: Build Printable Packets
```

</div>

## Manual Local Run

<div class="water-vault-directory-grid">
<div class="water-vault-directory-card"><h3>Windows</h3><p><code>scripts\build_printable_packets_windows.bat</code></p></div>
<div class="water-vault-directory-card"><h3>macOS / Linux</h3><p><code>bash scripts/build_printable_packets_unix.sh</code></p></div>
<div class="water-vault-directory-card"><h3>Direct Python</h3><p><code>python tools/run_printable_packet_build.py --local</code></p></div>
</div>

## Local Dependencies

<div class="water-vault-panel">

```text
python-docx
```

Optional for generic PDF/DOCX conversion:

```text
pandoc
xelatex
```

Without Pandoc, the specialized DOCX files still build, but generic PDF packet conversion may be skipped.

</div>

## Artifact Contents

<div class="water-vault-panel">

```text
Water-Operator-Vault-Flashcards-Packet.docx
Water-Operator-Vault-Practice-Exam-Packet.docx
Water-Operator-Vault-Source-and-Verification-Packet.docx
Water-Operator-Vault-Flashcards-Packet.pdf
Water-Operator-Vault-Practice-Exam-Packet.pdf
Water-Operator-Vault-Source-and-Verification-Packet.pdf
```

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

</div>

## Related

<div class="water-vault-directory-grid">
<div class="water-vault-directory-card"><h3>DOCX Layout Specification</h3><p>Layout rules for printable packet generation.</p><a class="water-vault-action" href="obsidian://open?file=08%20Printable%20Study%20Materials%2FDOCX%20Layout%20Specification">Open</a></div>
<div class="water-vault-directory-card"><h3>Flashcards Packet</h3><p>Generated flashcard packet note.</p><a class="water-vault-action" href="obsidian://open?file=08%20Printable%20Study%20Materials%2FGenerated%20Packets%2FWater-Operator-Vault-Flashcards-Packet">Open</a></div>
<div class="water-vault-directory-card"><h3>Practice Exam Packet</h3><p>Generated practice exam packet note.</p><a class="water-vault-action" href="obsidian://open?file=08%20Printable%20Study%20Materials%2FGenerated%20Packets%2FWater-Operator-Vault-Practice-Exam-Packet">Open</a></div>
<div class="water-vault-directory-card"><h3>Release Readiness</h3><p>Current release status and blockers.</p><a class="water-vault-action" href="obsidian://open?file=09%20Verification%20and%20Sources%2FRelease%20Readiness%20Status">Open</a></div>
</div>
