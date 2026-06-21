---
type: start-here
project: Water Operator Vault
area: onboarding
status: active
created: 2026-06-19
last_updated: 2026-06-20
cssclasses: [water-vault-hub, water-vault-gui]
tags: [start-here, plugins, onboarding, shared-vault]
---

# Start Here - Required Plugins

<div class="water-vault-hero compact">
<span class="water-vault-status">Plugin Setup</span>
<div class="water-vault-title">Required Plugins</div>
<p class="water-vault-subtitle">The Water Operator Vault should work as a shared study vault without requiring community plugins. The blue/green/white GUI uses only an Obsidian CSS snippet.</p>
</div>

## Quick Answer

<div class="water-vault-panel">

```yaml
required_for_basic_study: none
required_for_gui_theme: css_snippets_enabled
supported_interactive_quiz_mode: included_html_quiz_app
quizblock_status: legacy_experimental_export_not_required
optional_for_sync: obsidian_git_or_working_copy
```

</div>

## Required for Basic Study

<div class="water-vault-callout">
None. The dashboard notes, study hub notes, flashcard Markdown notes, practice exam Markdown notes, source notes, printable PDF/DOCX files, and Printable Launcher can be used without community plugins.
</div>

## Required for the Blue / Green / White GUI Theme

<div class="water-vault-action-grid">
<div class="water-vault-action-card featured"><h3>CSS Snippet</h3><p>Enable the Water Operator theme snippet in Obsidian.</p><p><code>Settings → Appearance → CSS snippets → water-operator-vault-theme</code></p></div>
<div class="water-vault-action-card"><h3>Snippet File</h3><p>The file should exist inside the vault here:</p><p><code>.obsidian/snippets/water-operator-vault-theme.css</code></p></div>
<div class="water-vault-action-card"><h3>Best View</h3><p>Use Reading View for the clean dashboard look. Live Preview may still show editing controls depending on Obsidian settings.</p></div>
</div>

## Interactive Quizzes

<div class="water-vault-action-grid">
<div class="water-vault-action-card featured"><h3>Supported Quiz App</h3><p>The supported interactive quiz mode for this vault is the included browser quiz app, not a required Obsidian community plugin.</p><a class="water-vault-action" href="obsidian://open?file=05%20Quiz%20App%2FQuiz%20App%20Status">Open Quiz App Status</a></div>
<div class="water-vault-action-card"><h3>Quiz App HTML</h3><p>Open this file in a browser and load the generated JSON file when prompted.</p><p><code>05 Quiz App/t5_quiz_app.html</code></p></div>
<div class="water-vault-action-card"><h3>Quiz JSON</h3><p>The generated quiz data lives here:</p><p><code>05 Quiz App/t5_quiz_app_questions.json</code></p></div>
</div>

<div class="water-vault-callout">
<strong>QuizBlock correction:</strong> Earlier notes referenced a `quizblock` plugin. That export path exists as an experimental generated format, but it is not required for this vault and should not block studying. If a matching community plugin is not visible in Obsidian's plugin browser, use the included HTML quiz app instead.
</div>

## Optional Extras

<div class="water-vault-directory-grid">
<div class="water-vault-directory-card"><h3>Obsidian Git</h3><p>Optional. Useful for pulling/pushing vault updates from desktop.</p></div>
<div class="water-vault-directory-card"><h3>Working Copy</h3><p>Optional external iOS app for iPad/iPhone Git sync.</p></div>
</div>

## Recommended Setup

<div class="water-vault-panel">

```yaml
minimum:
  - Obsidian
  - this vault
  - CSS snippets enabled for best look

recommended_for_quizzes:
  - included HTML quiz app

not_required:
  - QuizBlock
```

</div>

## Related

<div class="water-vault-directory-grid">
<div class="water-vault-directory-card"><h3>Shared Quick Start</h3><p>Shared-user onboarding page.</p><a class="water-vault-action" href="obsidian://open?file=00%20Dashboard%2FShared%20Vault%20Quick%20Start">Open</a></div>
<div class="water-vault-directory-card"><h3>Dashboard Index</h3><p>Dashboard launcher.</p><a class="water-vault-action" href="obsidian://open?file=00%20Dashboard%2FDashboard%20Index">Open</a></div>
<div class="water-vault-directory-card"><h3>Main Dashboard</h3><p>Water Operator Vault command center.</p><a class="water-vault-action" href="obsidian://open?file=00%20Dashboard%2FWater%20Operator%20Vault%20Dashboard">Open</a></div>
<div class="water-vault-directory-card"><h3>Printable Packet Dashboard</h3><p>Maintainer packet build controls.</p><a class="water-vault-action" href="obsidian://open?file=08%20Printable%20Study%20Materials%2FPrintable%20Packet%20Dashboard">Open</a></div>
</div>
