---
type: setup-note
project: Water Operator Vault
area: practice-exams
status: legacy-experimental
plugin: quizblock
cssclasses: [water-vault-quiz, water-vault-gui]
tags: [quizblock, obsidian, interactive-quiz, setup, legacy]
---

# Quiz Block Setup

<div class="water-vault-hero compact">
<span class="water-vault-status">Legacy / Experimental</span>
<div class="water-vault-title">Quiz Block Export</div>
<p class="water-vault-subtitle">This is an experimental Obsidian-native quiz export path. It is not required for the Water Operator Vault. The supported interactive quiz mode is the included browser quiz app.</p>
</div>

## Current Recommendation

<div class="water-vault-action-grid">
<div class="water-vault-action-card featured"><h3>Use the Included Quiz App</h3><p>The reliable interactive path is the included browser app and generated JSON.</p><a class="water-vault-action" href="obsidian://open?file=05%20Quiz%20App%2FQuiz%20App%20Status">Open Quiz App Status</a></div>
<div class="water-vault-action-card"><h3>Quiz App HTML</h3><p>Open this file in a browser, then load the question JSON.</p><p><code>05 Quiz App/t5_quiz_app.html</code></p></div>
<div class="water-vault-action-card"><h3>Quiz JSON</h3><p>Generated data source for the quiz app.</p><p><code>05 Quiz App/t5_quiz_app_questions.json</code></p></div>
</div>

<div class="water-vault-callout">
If no plugin named QuizBlock or Quiz Block appears in Obsidian's community plugin browser, nothing is broken in your vault. This export was generated as an experimental plugin-format path, not as a required dependency.
</div>

## What This Experimental Export Does

<div class="water-vault-panel">

The export converts the quiz JSON into Markdown notes using fenced `quiz` blocks:

```quiz
What does RTCR stand for?
[ ] Revised Treatment Control Rule
[c] Revised Total Coliform Rule
[ ] Routine Turbidity Compliance Rule
[ ] Regional Testing Certification Rule

The Revised Total Coliform Rule is the microbial monitoring rule for total coliform and E. coli in drinking water systems.
```

</div>

## Generator

<div class="water-vault-panel">

```text
tools/export_quizblock_notes.py
```

Generated notes live in:

```text
03 Practice Exams/Quiz Block
```

</div>

## Related

<div class="water-vault-directory-grid">
<div class="water-vault-directory-card"><h3>Quiz Block Practice Exam Index</h3><p>Generated experimental quiz-block note index.</p><a class="water-vault-action" href="obsidian://open?file=03%20Practice%20Exams%2FQuiz%20Block%2FQuiz%20Block%20Practice%20Exam%20Index">Open</a></div>
<div class="water-vault-directory-card"><h3>Practice Exams Index</h3><p>Main practice exam launcher.</p><a class="water-vault-action" href="obsidian://open?file=03%20Practice%20Exams%2FPractice%20Exams%20Index">Open</a></div>
<div class="water-vault-directory-card"><h3>Quiz App Status</h3><p>Supported quiz app status and launch info.</p><a class="water-vault-action" href="obsidian://open?file=05%20Quiz%20App%2FQuiz%20App%20Status">Open</a></div>
</div>
