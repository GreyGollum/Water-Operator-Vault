---
type: dashboard
project: Water Operator Vault
status: release-candidate
cssclasses: [water-vault-dashboard]
tags: [dashboard, water-operator, t5-study]
---

# Water Operator Vault Dashboard

<div class="water-vault-hero">
<span class="water-vault-status">Release Candidate</span>

**Water Operator Vault** is the standalone study system for drinking-water operator review, California T5 preparation, MCLs, PFAS, water math, treatment processes, compliance, flashcards, practice exams, printable sheets, and source verification.

Main theme: **blue** · Accent 1: **green** · Accent 2: **white**
</div>

<div class="water-vault-button-row">
<a class="water-vault-button" href="obsidian://open?file=01%20Study%20Hub%2FT5%20Study%20Hub">Start Studying</a>
<a class="water-vault-button" href="obsidian://open?file=04%20Tables%20and%20Databases%2FMaster%20Exam%20Numbers">Master Numbers</a>
<a class="water-vault-button" href="obsidian://open?file=05%20Regulations%20and%20Compliance%2FCalifornia%20Compliance%20Matrix">Compliance Matrix</a>
<a class="water-vault-button" href="obsidian://open?file=09%20Verification%20and%20Sources%2FWater%20Operator%20Source%20Bibliography">Sources</a>
</div>

## Build / Export Controls

| Action | Link / Command |
|---|---|
| Build printable PDF/DOCX artifact ZIP | [Open Build Printable Packets workflow](https://github.com/GreyGollum/Water-Operator-Vault/actions/workflows/build-printable-packets.yml) |
| Printable packet dashboard | [[08 Printable Study Materials/Printable Packet Dashboard]] |
| Local build command | `python tools/run_printable_packet_build.py --local` |
| Open build workflow locally | `python tools/run_printable_packet_build.py --open-actions` |

> GitHub Actions is the recommended build path. It creates the downloadable artifact named `water-operator-vault-printable-packets`.

## Core Navigation

<div class="water-vault-grid">

<div class="water-vault-card">
<h3>Study Hub</h3>
<p>Central launch point for T5 study paths, weak areas, and review flow.</p>
<p><strong>Open:</strong> [[01 Study Hub/T5 Study Hub]]</p>
<p class="water-vault-muted">Status: release candidate</p>
</div>

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
| Printable packets | GitHub Actions artifact workflow active |

## Disclaimer

This vault is a study aid. Always verify current regulations, source-water requirements, CT tables, PFAS values, monitoring schedules, public-notification requirements, lab methods, cross-connection rules, and local SOPs against official sources before exam day or compliance use.
