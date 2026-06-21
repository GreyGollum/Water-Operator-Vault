---
type: dashboard
project: Water Operator Vault
status: release-candidate
cssclasses: [water-vault-dashboard, water-vault-gui]
tags: [dashboard, water-operator, t5-study]
---

# Water Operator Vault Dashboard

<div class="water-vault-hero">
<span class="water-vault-status">Release Candidate</span>
<div class="water-vault-title">Water Operator Vault</div>
<p class="water-vault-subtitle">A blue/green/white study command center for T5 review, flashcards, practice exams, printable packets, source verification, and shared-user onboarding.</p>
<div class="water-vault-button-row">
<a class="water-vault-button green" href="obsidian://open?file=00%20Dashboard%2FShared%20Vault%20Quick%20Start">Shared Quick Start</a>
<a class="water-vault-button" href="obsidian://open?file=08%20Printable%20Study%20Materials%2FPrintable%20Launcher.html">Printable Launcher</a>
<a class="water-vault-button" href="obsidian://open?file=01%20Study%20Hub%2FT5%20Study%20Hub">Start Studying</a>
<a class="water-vault-button" href="obsidian://open?file=07%20Water%20Math%2FWater%20Math%20Index">Water Math</a>
<a class="water-vault-button" href="obsidian://open?file=09%20Verification%20and%20Sources%2FWater%20Operator%20Source%20Bibliography">Sources</a>
</div>
</div>

## System Snapshot

<div class="water-vault-kpi-grid">
<div class="water-vault-kpi"><strong>570</strong><span>Validated practice questions</span></div>
<div class="water-vault-kpi"><strong>11</strong><span>Randomized quiz sets</span></div>
<div class="water-vault-kpi"><strong>8/card</strong><span>Printable duplex flashcards</span></div>
<div class="water-vault-kpi"><strong>Ready</strong><span>Friends study release</span></div>
</div>

## Quick Launch

<div class="water-vault-action-grid">

<div class="water-vault-action-card featured">
<h3>Shared Quick Start</h3>
<p>Friend-proof entry point. No GitHub, Python, Pandoc, or plugins required.</p>
<p class="water-vault-muted">Audience: shared users</p>
<a class="water-vault-action" href="obsidian://open?file=00%20Dashboard%2FShared%20Vault%20Quick%20Start">Open Quick Start</a>
</div>

<div class="water-vault-action-card featured">
<h3>Printable Launcher</h3>
<p>Auto-detects Windows, Mac, iPad, and Android and shows the best printable path.</p>
<p class="water-vault-muted">Cross-platform HTML</p>
<a class="water-vault-action" href="obsidian://open?file=08%20Printable%20Study%20Materials%2FPrintable%20Launcher.html">Open Launcher</a>
</div>

<div class="water-vault-action-card">
<h3>Study Hub</h3>
<p>Daily study paths, weak-area review, and T5 focus flow.</p>
<p class="water-vault-muted">Start here for study sessions</p>
<a class="water-vault-action" href="obsidian://open?file=01%20Study%20Hub%2FT5%20Study%20Hub">Start Studying</a>
</div>

<div class="water-vault-action-card">
<h3>Quiz App</h3>
<p>Load the generated 570-question JSON into the quiz shell.</p>
<p class="water-vault-muted">JSON validated / smoke test passed</p>
<a class="water-vault-action" href="obsidian://open?file=05%20Quiz%20App%2FQuiz%20App%20Status">Open Quiz Status</a>
</div>

</div>

## Shared User Path

<div class="water-vault-action-grid">

<div class="water-vault-action-card featured">
<h3>Start Here</h3>
<p>Use this first if the vault was shared with you. It explains the study path and avoids maintainer-only tools.</p>
<a class="water-vault-action" href="obsidian://open?file=00%20Dashboard%2FShared%20Vault%20Quick%20Start">Open Shared Quick Start</a>
</div>

<div class="water-vault-action-card">
<h3>Printable Options</h3>
<p>Auto-detect printable options for Windows, Mac, iPad, iPhone, and Android.</p>
<a class="water-vault-action" href="obsidian://open?file=08%20Printable%20Study%20Materials%2FPrintable%20Launcher.html">Open Printable Launcher</a>
</div>

<div class="water-vault-action-card">
<h3>Flashcards</h3>
<p>Open the master flashcard index for MCLs, PFAS, SDWA, math, treatment, lab, and distribution review.</p>
<a class="water-vault-action" href="obsidian://open?file=02%20Flash%20Cards%2FFlash%20Cards%20Index">Open Flashcards</a>
</div>

<div class="water-vault-action-card">
<h3>Practice Exams</h3>
<p>Open practice exams, generated batches, answer checks, and printable exam materials.</p>
<a class="water-vault-action" href="obsidian://open?file=03%20Practice%20Exams%2FPractice%20Exams%20Index">Open Practice Exams</a>
</div>

</div>

<div class="water-vault-callout">
<strong>Shared-user rule:</strong> Friends should not need GitHub, Python, Pandoc, Shell Commands, or build scripts. Printable DOCX/PDF files should already be included in the vault.
</div>

## Maintainer Build / Export Controls

<div class="water-vault-action-grid">

<div class="water-vault-action-card featured">
<h3>Printable Packet Dashboard</h3>
<p>Main maintainer control page for rebuilding and checking printable study packets.</p>
<a class="water-vault-action" href="obsidian://open?file=08%20Printable%20Study%20Materials%2FPrintable%20Packet%20Dashboard">Open Packet Dashboard</a>
</div>

<div class="water-vault-action-card">
<h3>Printable Launcher</h3>
<p>Cross-platform launcher file for shared users and quick local testing.</p>
<a class="water-vault-action" href="obsidian://open?file=08%20Printable%20Study%20Materials%2FPrintable%20Launcher.html">Open Launcher</a>
</div>

<div class="water-vault-action-card">
<h3>Local Build Script</h3>
<p>Use on Windows after content changes when printable files need to be rebuilt locally.</p>
<p><code>scripts\\build_printable_packets_windows.bat</code></p>
</div>

<div class="water-vault-action-card">
<h3>Build Artifacts</h3>
<p>Finished DOCX/PDF packets should be included here before sharing the vault.</p>
<p><code>08 Printable Study Materials/Build Artifacts</code></p>
</div>

</div>

> Maintainer-only: rebuild packets after content changes, then include/sync the finished files before sharing the vault.

## Core Navigation

<div class="water-vault-directory-grid">

<div class="water-vault-directory-card">
<h3>Flash Cards</h3>
<p>PFAS, MCLs, SDWA, lab, cross-connection, distribution, disinfection, CT, water quality, water math, and treatment-process decks.</p>
<p class="water-vault-muted">Status: partially verified / printable cards available</p>
<a class="water-vault-action" href="obsidian://open?file=02%20Flash%20Cards%2FFlash%20Cards%20Index">Open Index</a>
</div>

<div class="water-vault-directory-card">
<h3>Practice Exams</h3>
<p>Question banks, mini exams, answer sheets, randomized batch drafts, and printable exam packets.</p>
<p class="water-vault-muted">Status: 570 generated and validated questions</p>
<a class="water-vault-action" href="obsidian://open?file=03%20Practice%20Exams%2FPractice%20Exams%20Index">Open Index</a>
</div>

<div class="water-vault-directory-card">
<h3>Tables and Databases</h3>
<p>Master numbers, MCL databases, PFAS values, contaminant tables, formula references, lab/source/cross-connection databases.</p>
<p class="water-vault-muted">Status: partially verified</p>
<a class="water-vault-action" href="obsidian://open?file=04%20Tables%20and%20Databases%2FTables%20and%20Databases%20Index">Open Index</a>
</div>

<div class="water-vault-directory-card">
<h3>Regulations and Compliance</h3>
<p>SDWA, Title 22, public notification, MCL memory, PFAS caveats, monitoring, reporting, and compliance-response review.</p>
<p class="water-vault-muted">Status: date-sensitive source verification required</p>
<a class="water-vault-action" href="obsidian://open?file=05%20Regulations%20and%20Compliance%2FRegulations%20and%20Compliance%20Index">Open Index</a>
</div>

<div class="water-vault-directory-card">
<h3>Treatment Processes</h3>
<p>Coagulation, flocculation, sedimentation, filtration, disinfection, CT, corrosion control, and process-control study links.</p>
<p class="water-vault-muted">Status: study summaries with operational caveats</p>
<a class="water-vault-action" href="obsidian://open?file=06%20Treatment%20Processes%2FTreatment%20Processes%20Index">Open Index</a>
</div>

<div class="water-vault-directory-card">
<h3>Water Math</h3>
<p>Formula memory, unit conversions, dosage, flow, volume, CT arithmetic, horsepower, and math-only practice.</p>
<p class="water-vault-muted">Status: formulas checked; CT values remain table-specific</p>
<a class="water-vault-action" href="obsidian://open?file=07%20Water%20Math%2FWater%20Math%20Index">Open Index</a>
</div>

<div class="water-vault-directory-card">
<h3>Lab Procedures</h3>
<p>EPA-approved methods, Colilert, HPC, QA/QC, wet chemistry, titration, probes, meters, and method-recognition notes.</p>
<p class="water-vault-muted">Status: source-supported with caveats</p>
<a class="water-vault-action" href="obsidian://open?file=08%20Lab%20Procedures%2FLab%20Procedures%20Index">Open Index</a>
</div>

<div class="water-vault-directory-card">
<h3>Cross Connection Control</h3>
<p>Backflow, backsiphonage, backpressure, DC/RP/PVB/AVB, testing concepts, and device-selection caveats.</p>
<p class="water-vault-muted">Status: source-supported; USC/AWWA M14 pending</p>
<a class="water-vault-action" href="obsidian://open?file=11%20Cross%20Connection%20Control%2FCross%20Connection%20Control%20Index">Open Index</a>
</div>

<div class="water-vault-directory-card">
<h3>Verification and Sources</h3>
<p>Source bibliography, audit reports, validation status, and migration/scrub notes.</p>
<p class="water-vault-muted">Status: active source control</p>
<a class="water-vault-action" href="obsidian://open?file=09%20Verification%20and%20Sources%2FVerification%20Master%20Index">Open Index</a>
</div>

<div class="water-vault-directory-card">
<h3>Study Topics</h3>
<p>Landing pages for answer-key and review links such as CT calculations, PFAS, MCLs, treatment, distribution, and operator decision topics.</p>
<p class="water-vault-muted">Status: source-safe scaffolds</p>
<a class="water-vault-action" href="obsidian://open?file=12%20Study%20Topics%2FStudy%20Topics%20Index">Open Index</a>
</div>

</div>

## T5 Oral Exam Response Memory

<div class="water-vault-callout">
<strong>Default answer pattern:</strong> Protect public health → verify data → stabilize operations → notify internally → coordinate with DDW/regulators → communicate externally as required → correct root cause → document and follow up.
</div>

## Validation Snapshot

<div class="water-vault-panel">

| Area | Current Status |
|---|---|
| Core MCL memory values | Source-linked / partially verified |
| Federal PFAS MCL values | Source-linked / date-sensitive |
| California PFAS NL/RL values | Source-linked / date-sensitive |
| Water math formulas/constants | Source-linked |
| Public Notification timing | Source-linked |
| T5 exam format and scope | Source-linked |
| Lab procedures | Source-supported with caveats |
| Cross-connection control | Source-supported with USC/CA context pending |
| Distribution/source/hydrant content | Source-supported with caveats |
| Practice exam answers | 570 checked; zero corrections |
| Quiz app | JSON validated; static smoke test passed |
| Printable packets | Included for shared users; cross-platform launcher available; maintainer rebuild available |

</div>

## Disclaimer

<div class="water-vault-callout">
This vault is a study aid. Always verify current regulations, source-water requirements, CT tables, PFAS values, monitoring schedules, public-notification requirements, lab methods, cross-connection rules, and local SOPs against official sources before exam day or compliance use.
</div>
