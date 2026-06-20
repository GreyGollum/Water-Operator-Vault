---
type: card-audit
project: Water Operator Vault
area: flashcards
deck: T5 Flash Cards - Water Math
status: active
audit_date: 2026-06-19
cards_audited: 250
verification_status: audited_partially_verified
source_ids: [CA-EXAM-CONVERSION-2026, CA-DWOP, CA-T5-DESCRIPTION-2026]
---

# Card Audit - Water Math

> Deck audited: [[T5 Flash Cards - Water Math]]  
> Cards audited: **250 / 250**  
> Result: **Audited, partially verified**. Core formulas/constants and arithmetic examples checked in this pass. No arithmetic corrections were required. Remaining caveats involve CT table-specific values, liquid chemical solution interpretation, and technical pump/filter concepts.

## Summary Counts

| Status | Count | Meaning |
|---|---:|---|
| Formula / conversion source-verified | 48 | Directly supported by California 2026 Exam Conversion Sheet or basic unit identity |
| Arithmetic recalculated / checked | 83 | Worked examples and numeric conversions checked during audit |
| Conceptual / exam-strategy reviewed | 88 | Reasonable operator-math concepts, study habits, and scenario logic |
| Caveated / technical-source pending | 31 | Correct enough for study but requires CT table, liquid-chemical, pump/filter, or technical-source caveat |
| Needs revision | 0 | No immediate arithmetic or formula errors found |
| **Total** | **250** | All cards accounted for |

---

# Key Findings

## No Immediate Arithmetic Corrections Required

The worked examples checked during this pass were internally consistent. Examples verified include:

- Chemical dose/feed calculations using `lb/day = mg/L × MGD × 8.34`
- MGD ↔ gpm conversions using **694.4 gpm/MGD**
- cfs ↔ gpm conversions using **448.8 gpm/cfs**
- Volume conversions using **7.48 gal/ft³**
- Detention-time calculations
- CT arithmetic examples
- Pressure/head conversions
- Pump horsepower examples
- Filter loading, overflow, weir loading, percent removal, cost, and energy examples

## Existing Caveats Are Appropriate

The current deck already correctly warns that:

- California 2026 formula sheet uses **1 MGD = 694.4 gpm**.
- `694 gpm` should only be treated as rounded mental math.
- Chemical feed formula gives **active lb/day**; liquid commercial-solution calculations require percent strength and density/specific gravity.
- CT formula is verified, but actual required CT values must come from official CT tables.

## No Value Corrections Required

No card was found with a clearly wrong formula, conversion, or arithmetic answer in this audit pass.

---

# Section-Level Audit

| Section | Cards | Audit Status | Notes |
|---|---:|---|---|
| Core Water Math Rules | 1-20 | reviewed | Study strategy and formula setup concepts are sound. |
| Core Conversions | 21-40 | verified / checked | 8.34, 7.48, 694.4, 448.8, 0.433, 2.31, 325,851 checked against formula sheet. |
| Dosage and Chemical Feed | 41-60 | arithmetic checked / caveated | Active lb/day examples check out; solution-strength caveat must remain. |
| Solution Strength and Feed Pump Output | 61-80 | arithmetic checked / caveated | Drawdown and SG examples check out; chemical-feed equipment source audit still useful. |
| Flow Conversions | 81-100 | arithmetic checked | Flow/firm capacity/peaking examples check out. |
| Volume Calculations | 101-120 | arithmetic checked | Rectangular/cylindrical volume examples check out. |
| Detention Time | 121-140 | arithmetic checked / caveated | Detention-time examples check out; baffling/T10 technical guidance still pending. |
| CT Math | 141-160 | arithmetic checked / caveated | CT arithmetic checks out; actual required CT values are table-specific. |
| Pressure, Head, Hydraulics | 161-180 | arithmetic checked / technical pending | Conversions check out; cavitation/NPSH/water hammer need technical source for final. |
| Pump HP and Efficiency | 181-195 | formula/arithmetic checked / technical pending | WHP/BHP examples check out; pump-curve troubleshooting needs technical source. |
| Filter Math | 196-210 | arithmetic checked / technical pending | Loading/backwash examples check out; filter performance concepts need technical source. |
| Sedimentation / Clarifier Math | 211-220 | arithmetic checked | Overflow and weir examples check out. |
| Percent / Removal / Cost Math | 221-235 | arithmetic checked | Percent, cost, and energy examples check out. |
| T5 Scenario Math | 236-250 | reviewed / caveated | Good scenario logic; some concepts require operational/technical support for final publication. |

---

# High-Value Verified Formulas / Constants

| Item | Value / Formula | Source |
|---|---|---|
| 1 gallon water | 8.34 lb | [[Water Operator Source Bibliography#CA-EXAM-CONVERSION-2026]] |
| 1 cubic foot | 7.48 gal | [[Water Operator Source Bibliography#CA-EXAM-CONVERSION-2026]] |
| 1 MGD | 694.4 gpm | [[Water Operator Source Bibliography#CA-EXAM-CONVERSION-2026]] |
| 1 cfs | 448.8 gpm | [[Water Operator Source Bibliography#CA-EXAM-CONVERSION-2026]] |
| 1 ft head | 0.433 psi | [[Water Operator Source Bibliography#CA-EXAM-CONVERSION-2026]] |
| 1 psi | 2.31 ft head | [[Water Operator Source Bibliography#CA-EXAM-CONVERSION-2026]] |
| 1 acre-foot | 325,851 gal | [[Water Operator Source Bibliography#CA-EXAM-CONVERSION-2026]] |
| Chemical feed | lb/day = mg/L × MGD × 8.34 | [[Water Operator Source Bibliography#CA-EXAM-CONVERSION-2026]] |
| CT | residual × effective contact time | [[Water Operator Source Bibliography#CA-EXAM-CONVERSION-2026]] |
| Water horsepower | GPM × Head / 3960 | [[Water Operator Source Bibliography#CA-EXAM-CONVERSION-2026]] |
| Brake horsepower | GPM × Head / (3960 × efficiency decimal) | [[Water Operator Source Bibliography#CA-EXAM-CONVERSION-2026]] |
| Filter loading | flow / filter area | [[Water Operator Source Bibliography#CA-EXAM-CONVERSION-2026]] |
| Surface overflow | flow / surface area | [[Water Operator Source Bibliography#CA-EXAM-CONVERSION-2026]] |
| Weir loading | flow / weir length | [[Water Operator Source Bibliography#CA-EXAM-CONVERSION-2026]] |
| Percent removal | (initial - final) / initial × 100 | [[Water Operator Source Bibliography#CA-EXAM-CONVERSION-2026]] |

---

# Required Deck Edits

1. Add `cards_audited: 250/250`.
2. Add audit-count metadata.
3. Keep `verification_status: partially_verified`, not fully verified, until technical concepts are source-audited.
4. Keep CT table caveat.
5. Keep liquid chemical solution caveat.
6. Add note that arithmetic examples were recalculated with no corrections required.

---

# Bottom Line

This deck is one of the strongest study decks so far. It is suitable for active study and draft printable use with caveats. It should not be marked fully verified until pump/filter/hydraulic concepts and CT table-specific requirements are technically sourced.
