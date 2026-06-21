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

# Start Here - Setup and Plugins

<div class="water-vault-hero compact">
<div class="water-vault-title">Start Here</div>
<p class="water-vault-subtitle">First-time setup, plugin guidance, and the recommended path through the Water Operator Vault.</p>
<div class="water-vault-button-row">
<a class="water-vault-button green" href="obsidian://open?file=00%20Dashboard%2FWater%20Operator%20Vault%20Dashboard">Main Dashboard</a>
<a class="water-vault-button" href="obsidian://open?file=02%20Flash%20Cards%2FFlash%20Cards%20Index">Flash Cards</a>
<a class="water-vault-button" href="obsidian://open?file=03%20Practice%20Exams%2FPractice%20Exams%20Index">Practice Exams</a>
<a class="water-vault-button" href="obsidian://open?file=05%20Quiz%20App%2FProgress%20Report">Progress Report</a>
</div>
</div>

## Quick Setup Path

<div class="water-vault-panel">

| Step | What to do |
|---|---|
| 1 | Open this vault in Obsidian. |
| 2 | Enable CSS snippets for the blue-glass dashboard look. |
| 3 | Install optional plugins only if you want sync or extra navigation help. |
| 4 | Use the Main Dashboard, Flash Cards, Practice Exams, and Progress Report pages. |

</div>

## Required Plugins

<div class="water-vault-callout">
<strong>Required community plugins: none.</strong> The dashboard, flash cards, printable DOCX files, on-screen quiz app, and progress report are designed to work without Dataview, Buttons, Commander, Shell Commands, QuizBlock, or any other community plugin.
</div>

<div class="water-vault-panel">

```yaml
required_for_basic_study: none
required_for_printable_flashcards: none
required_for_printable_practice_exams: none
required_for_on_screen_quiz: none
required_for_progress_report: none
required_for_blue_glass_theme: css_snippets_enabled
optional_plugins:
  - Obsidian Git
  - Homepage
  - File Tree Alternative
not_required:
  - Dataview
  - Buttons
  - Commander
  - Shell Commands
  - QuizBlock
```

</div>

## Enable the Blue-Glass Theme

<div class="water-vault-action-grid">

<div class="water-vault-action-card featured">
<h3>Enable CSS Snippets</h3>
<p>In Obsidian, go to <code>Settings &gt; Appearance &gt; CSS snippets</code>, then enable the Water Operator snippets.</p>
<p class="water-vault-muted">Enable these if visible: <code>water-operator-vault-theme</code>, <code>water-vault-dashboard</code>, <code>water-operator-vault-readable</code>, and <code>zz-water-operator-vault-readable</code>.</p>
</div>

<div class="water-vault-action-card">
<h3>If Snippets Do Not Show</h3>
<p>In the CSS snippets section, click the refresh icon. If they still do not show, confirm this folder exists:</p>
<p><code>.obsidian/snippets</code></p>
</div>

<div class="water-vault-action-card">
<h3>Best View</h3>
<p>Use Reading View for dashboard pages. Live Preview may show editing controls and can look busier.</p>
</div>

</div>

## How to Install Community Plugins

<div class="water-vault-panel">

1. Open <code>Settings</code> in Obsidian.
2. Go to <code>Community plugins</code>.
3. If Restricted Mode is on, turn it off.
4. Click <code>Browse</code>.
5. Search for the plugin name.
6. Click the plugin, then click <code>Install</code>.
7. After it installs, click <code>Enable</code>.
8. Return to <code>Settings &gt; Community plugins</code> and confirm the plugin toggle is on.

</div>

## Optional Plugins

<div class="water-vault-action-grid">

<div class="water-vault-action-card featured">
<h3>Obsidian Git</h3>
<p>Optional. Use this if you want to pull updates from GitHub or push your own changes from desktop Obsidian.</p>
<p class="water-vault-muted">Search plugin browser for: <code>Obsidian Git</code></p>
</div>

<div class="water-vault-action-card">
<h3>Homepage</h3>
<p>Optional. Use this if you want Obsidian to open the Water Operator Vault Dashboard automatically.</p>
<p class="water-vault-muted">Suggested homepage: <code>00 Dashboard/Water Operator Vault Dashboard</code></p>
</div>

<div class="water-vault-action-card">
<h3>File Tree Alternative</h3>
<p>Optional. Use this only if you want a different folder navigation sidebar. The normal Obsidian file explorer is enough.</p>
</div>

</div>

## Plugins Not Needed for This Vault

<div class="water-vault-callout">
Do not install plugins just because older notes mention them. QuizBlock exports are legacy/experimental. The supported test path is <code>05 Quiz App/t5_quiz_app.html</code>, and the supported progress path is <code>05 Quiz App/progress_report.html</code>.
</div>

<div class="water-vault-panel">

| Plugin | Status |
|---|---|
| Dataview | Not required |
| Buttons | Not required |
| Commander | Not required |
| Shell Commands | Not required |
| QuizBlock | Not required; legacy/experimental only |

</div>

## Where to Go

<div class="water-vault-action-grid">

<div class="water-vault-action-card featured">
<h3>Main Dashboard</h3>
<p>The simple front door for the vault.</p>
<a class="water-vault-action" href="obsidian://open?file=00%20Dashboard%2FWater%20Operator%20Vault%20Dashboard">Open Dashboard</a>
</div>

<div class="water-vault-action-card">
<h3>Flash Cards</h3>
<p>Open the printer-ready flashcard DOCX and source decks.</p>
<a class="water-vault-action" href="obsidian://open?file=02%20Flash%20Cards%2FFlash%20Cards%20Index">Open Flash Cards</a>
</div>

<div class="water-vault-action-card">
<h3>Practice Exams</h3>
<p>Launch the on-screen exam or open the printer-ready practice exam DOCX.</p>
<a class="water-vault-action" href="obsidian://open?file=03%20Practice%20Exams%2FPractice%20Exams%20Index">Open Practice Exams</a>
</div>

<div class="water-vault-action-card">
<h3>Progress Report</h3>
<p>See strengths, weaknesses, missed questions, and suggested study areas.</p>
<a class="water-vault-action" href="obsidian://open?file=05%20Quiz%20App%2FProgress%20Report">Open Progress Report</a>
</div>

</div>
