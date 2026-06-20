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
<a class="water-vault-button" href="obsidian://open?file=04%20Tables%20and%20Databases%2FMaster%20Exam%20Numbers">Master Numbers</a>
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

<div class="water-vault-grid">

<div class="water-vault-card featured">
<h3>Shared Quick Start</h3>
<p>Friend-proof entry point. No GitHub, Python, Pandoc, or plugins required.</p>
<p><strong>Open:</strong> [[00 Dashboard/Shared Vault Quick Start]]</p>
<p class="water-vault-muted">Audience: shared users</p>
</div>

<div class="water-vault-card featured">
<h3>Printable Launcher</h3>
<p>Auto-detects Windows, Mac, iPad, and Android and shows the best printable path.</p>
<p><strong>Open:</strong> <code>08 Printable Study Materials/Printable Launcher.html</code></p>
<p class="water-vault-muted">Cross-platform HTML</p>
</div>

<div class="water-vault-card">
<h3>Study Hub</h3>
<p>Daily study paths, weak-area review, and T5 focus flow.</p>
<p><strong>Open:</strong> [[01 Study Hub/T5 Study Hub]]</p>
<p class="water-vault-muted">Start here for study sessions</p>
</div>

<div class="water-vault-card">
<h3>Quiz App</h3>
<p>Load the generated 570-question JSON into the quiz shell.</p>
<p><strong>Open:</strong> [[05 Quiz App/Quiz App Status]]</p>
<p class="water-vault-muted">JSON validated / smoke test passed</p>
</div>

</div>

## Shared User Path

<div class="water-vault-panel">

| Action | Open |
|---|---|
| Start here if this vault was shared with you | [[00 Dashboard/Shared Vault Quick Start]] |
| Auto-detect printable options | `08 Printable Study Materials/Printable Launcher.html` |
| Open printable files | `08 Printable Study Materials/Build Artifacts` |
| Study hub | [[01 Study Hub/T5 Study Hub]] |
| Flashcards | [[02 Flash Cards/Flash Cards Index]] |
| Practice exams | [[03 Practice Exams/Practice Exams Index]] |

</div>

<div class="water-vault-callout">
<strong>Shared-user rule:</strong> Friends should not need GitHub, Python, Pandoc, Shell Commands, or build scripts. Printable DOCX/PDF files should already be included in the vault.
</div>

## Maintainer Build / Export Controls

<div class="water-vault-panel">

| Action | Local Target |
|---|---|
| Cross-platform printable launcher | `08 Printable Study Materials/Printable Launcher.html` |
| Rebuild printable files locally | `scripts\\build_printable_packets_windows.bat` |
| Printable packet dashboard | [[08 Printable Study Materials/Printable Packet Dashboard]] |
| Direct Python local build | `python tools/run_printable_packet_build.py --local` |
| Output folder | `08 Printable Study Materials/Build Artifacts` |

</div>

> Maintainer-only: rebuild packets after content changes, then include/sync the finished files before sharing the vault.

## Core Navigation

<div class="water-vault-grid">

<div class="water-vault-card">
<h3>Flash Cards</h3>
<p>PFAS, MCLs, SDWA, lab, cross-connection, distribution, disinfection, CT, water quality, water math, and treatment-process decks.</p>
<p><strong>Open:</strong> [[02 Flash Cards/Flash Cards Index]]</p>
<p class="water-vault-muted">Status: partially verified / printable cards available</p>
</div>

<div class="water-vault-card">
<h3>Practice Exams</h3>
<p>Question banks, mini exams, answer sheets, randomized batch drafts, and printable exam packets.</p>
<p><strong>Open:</strong> [[03 Practice Exams/Practice Exams Index]]</p>
<p class="water-vault-muted">Status: 570 generated and validated questions</p>
</div>

<div class="water-vault-card">
<h3>Tables and Databases</h3>
<p>Master numbers, MCL databases, PFAS values, contaminant tables, formula references, lab/source/cross-connection databases.</p>
<p><strong>Open:</strong> [[04 Tables and Databases/Tables and Databases Index]]</p>
<p class="water-vault-muted">Status: partially verified</p>
</div>

<div class="water-vault-card">
<h3>Lab Procedures</h3>
<p>EPA-approved methods, Colilert, HPC, QA/QC, wet chemistry, titration, probes, meters, and method-recognition notes.</p>
<p><strong>Open:</strong> [[08 Lab Procedures/Lab Procedures Index]]</p>
<p class="water-vault-muted">Status: source-supported with caveats</p>
</div>

<div class="water-vault-card">
<h3>Cross Connection Control</h3>
<p>Backflow, backsiphonage, backpressure, DC/RP/PVB/AVB, testing concepts, and device-selection caveats.</p>
<p><strong>Open:</strong> [[11 Cross Connection Control/Cross Connection Control Index]]</p>
<p class="water-vault-muted">Status: source-supported; USC/AWWA M14 pending</p>
</div>

<div class="water-vault-card">
<h3>Verification and Sources</h3>
<p>Source bibliography, audit reports, validation status, and migration/scrub notes.</p>
<p><strong>Open:</strong> [[09 Verification and Sources/Verification Master Index]]</p>
<p class="water-vault-muted">Status: active source control</p>
</div>

</div>

## T5 Oral Exam Response Memory

<div class="water-vault-callout">
<strong>Default answer pattern:</strong> Protect public health → verify data → stabilize operations → notify internally → coordinate with DDW/regulators → communicate externally as required → correct root cause → document and follow up.
</div>

## Validation Snapshot

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

## Disclaimer

This vault is a study aid. Always verify current regulations, source-water requirements, CT tables, PFAS values, monitoring schedules, public-notification requirements, lab methods, cross-connection rules, and local SOPs against official sources before exam day or compliance use.
