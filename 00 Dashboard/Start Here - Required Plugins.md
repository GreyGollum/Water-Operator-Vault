---
type: start-here
project: Water Operator Vault
area: onboarding
status: active
created: 2026-06-19
last_updated: 2026-06-19
tags: [start-here, plugins, onboarding, shared-vault]
---

# Start Here - Required Plugins

This vault is designed so the core study material works with **plain Obsidian**.

Most plugins are optional enhancements, not hard requirements.

## Quick Answer

```yaml
required_for_basic_study: none
required_for_gui_theme: css_snippets_enabled
required_for_interactive_quizzes: quizblock
optional_for_local_build_buttons: shell_commands_or_commander_buttons
optional_for_sync: obsidian_git_or_working_copy
```

## Required for Basic Study

None.

The following work without community plugins:

- dashboard notes
- study hub notes
- flashcard Markdown notes
- practice exam Markdown notes
- source bibliography notes
- printable PDF/DOCX files already included in the vault
- `Printable Launcher.html`

## Required for the Blue / Green / White GUI Theme

No community plugin is required, but CSS snippets must be enabled.

Enable:

```text
Settings → Appearance → CSS snippets → water-vault-dashboard
```

CSS file:

```text
.obsidian/snippets/water-vault-dashboard.css
```

## Required for Interactive Obsidian Quizzes

| Plugin | Required? | Used For | Notes |
|---|---:|---|---|
| quizblock | Yes, for interactive quiz notes only | `03 Practice Exams/Quiz Block` | Renders fenced `quiz` code blocks as interactive questions. |

Without Quiz Block, the quiz notes still open as readable Markdown, but they will not behave interactively.

## Optional Maintainer / Power-User Plugins

| Plugin / Tool | Required? | Used For | Who Needs It? |
|---|---:|---|---|
| Shell Commands | Optional | Run local build scripts from Obsidian | Jeremy / maintainer only |
| Commander | Optional | Put script commands into Obsidian UI buttons | Jeremy / maintainer only |
| Buttons | Optional | Create dashboard buttons that trigger commands | Jeremy / maintainer only |
| Obsidian Git | Optional | Pull/push vault updates from desktop/mobile | Anyone syncing by Git |
| Working Copy | Optional external iOS app | Git sync on iPad/iPhone | iPad/iPhone users using Git |

## Not Needed for Friends / Shared Users

Shared users do **not** need:

- GitHub Actions access
- Python
- Pandoc
- LaTeX / xelatex
- Shell Commands
- Commander
- Buttons
- local build scripts

They should use:

- [[Shared Vault Quick Start]]
- `08 Printable Study Materials/Printable Launcher.html`
- already-built files in `08 Printable Study Materials/Build Artifacts`
- optional Quiz Block plugin if they want interactive quizzes

## Recommended Friend Setup

```yaml
minimum:
  - Obsidian
  - this vault
  - CSS snippets enabled for best look

recommended:
  - quizblock plugin

not_required:
  - GitHub
  - Python
  - Pandoc
  - Shell Commands
```

## Recommended Jeremy / Maintainer Setup

```yaml
recommended_plugins:
  - quizblock
  - Shell Commands
  - Commander or Buttons
  - Obsidian Git

recommended_tools:
  - Python 3.12+
  - python-docx
  - Pandoc
  - xelatex if building PDFs locally
```

## Related

- [[Shared Vault Quick Start]]
- [[Dashboard Index]]
- [[Water Operator Vault Dashboard]]
- [[03 Practice Exams/Quiz Block/Quiz Block Setup]]
- [[08 Printable Study Materials/Printable Packet Dashboard]]
