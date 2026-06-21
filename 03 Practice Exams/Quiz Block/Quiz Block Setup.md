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
<p class="water-vault-subtitle">The supported on-screen test path is the included browser quiz app: one question, answer it, then move to the next question. Generated printed tests and on-screen tests share the same batch IDs.</p>
</div>

## Current Recommendation

<div class="water-vault-action-grid">
<div class="water-vault-action-card featured"><h3>Use the On-Screen Test</h3><p>The reliable interactive path is the included browser app and generated JSON. It shows one question at a time.</p><a class="water-vault-action" href="obsidian://open?file=05%20Quiz%20App%2Ft5_quiz_app.html">Open Quiz App</a></div>
<div class="water-vault-action-card"><h3>Printed-Test Batch IDs</h3><p>Choose the same batch ID in the app that appears on the generated printed test.</p><p><code>T5-20260619-...</code></p></div>
<div class="water-vault-action-card"><h3>Quiz JSON</h3><p>Generated data source for the on-screen app.</p><p><code>05 Quiz App/t5_quiz_app_questions.json</code></p></div>
</div>

<div class="water-vault-callout">
If no plugin named QuizBlock or Quiz Block appears in Obsidian's community plugin browser, nothing is broken in your vault. The supported QuizBlock-style experience is the included on-screen browser app.
</div>

## What This Experimental Export Does

<div class="water-vault-panel">

The optional Markdown export converts the quiz JSON into notes using fenced `quiz` blocks:

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
