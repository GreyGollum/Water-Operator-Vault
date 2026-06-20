---
type: card-audit
project: Water Operator Vault
area: flashcards
deck: T5 Flash Cards - Disinfection and CT
status: active
audit_date: 2026-06-19
cards_audited: 250
verification_status: audited_partially_verified
source_ids: [EPA-NPDWR, EPA-PUBLIC-NOTIFICATION, CA-EXAM-CONVERSION-2026, CA-T5-DESCRIPTION-2026]
---

# Card Audit - Disinfection and CT

> Deck audited: [[T5 Flash Cards - Disinfection and CT]]  
> Cards audited: **250 / 250**  
> Result: **Audited, partially verified**. No immediately incorrect cards found. The deck is strong for active study, but it cannot be marked fully verified until CT tables, SWTR details, ozone/UV technical guidance, chloramination/nitrification guidance, DBPR details, and chemical-safety/SOP items are source-audited.

## Summary Counts

| Status | Count | Meaning |
|---|---:|---|
| Verified | 101 | Stable core concepts, source-linked formulas, arithmetic, MRDL/MCL values, and public-health priorities |
| Caveated | 91 | Correct enough for study, but context-dependent or rule/table/SOP dependent |
| Technical audit pending | 58 | Operationally reasonable but needs EPA/AWWA/OWP/site-SOP style technical source before final verified status |
| Needs revision | 0 | No clearly wrong cards found during this pass |
| **Total** | **250** | All cards accounted for |

---

# Key Findings

## No Immediate Corrections Required

No card was found with an obviously incorrect formula, regulatory value, arithmetic answer, or misleading public-health priority.

## Existing Caveats Must Stay

The deck correctly warns that:

- `CT = disinfectant residual × effective contact time` is verified as a formula, but **required CT values must come from official CT tables**.
- DBP MCLs and disinfectant MRDLs are source-supported but should be rechecked before exam day.
- UV and ozone concepts need technical-source verification before full verified status.
- Safety cards are conceptual only and must defer to SDS, site SOPs, training, and emergency procedures.

## Biggest Remaining Risk Areas

The risky material is not basic arithmetic; it is **context**:

1. Which CT table applies.
2. Which organism/log-inactivation target applies.
3. Which disinfectant and residual type applies.
4. Whether the system is using free chlorine, chloramine, ozone, UV, or multiple barriers.
5. Whether a public notice trigger is rule-specific.
6. Whether chloramine/nitrification actions are approved and system-specific.
7. Whether UV/ozone credit claims match validated operating conditions.

---

# Section-Level Audit

| Section | Cards | Audit Status | Notes |
|---|---:|---|---|
| Disinfection Fundamentals | 1-20 | partially verified | Strong concepts; Crypto/filtration and pathogen barrier statements need SWTR/source support for final. |
| Chlorine Chemistry | 21-45 | partially verified | HOCl/OCl-, pH, demand, breakpoint, total/free/combined chlorine are conceptually correct; chemistry source audit still needed. |
| Feed and Residual Control | 46-65 | partially verified | Operator logic is sound; analyzer/feed-system items need SOP/technical source for final. |
| CT Calculations and Contact Time | 66-90 | formula/arithmetic verified, table caveated | CT arithmetic checks out. Required CT values remain table-specific. |
| Surface Water Disinfection Compliance | 91-110 | caveated | Multiple barrier and pathogen-control concepts are sound; SWTR/IESWTR/LT2 details need source audit. |
| Chloramines | 111-130 | technical audit pending | Concepts are strong; nitrification/free ammonia/temporary free chlorine conversion require technical and regulatory source support. |
| Ozone and UV | 131-155 | technical audit pending | Basic ozone/UV statements are reasonable; validation, dose, UVT, bromate, and credit details need technical-source audit. |
| Distribution Residual and Storage | 156-175 | partially verified / technical pending | Concepts are strong; storage, flushing, intrusion, and backflow details need distribution/source support. |
| Disinfection Byproducts | 176-195 | partially verified | TTHM/HAA5/bromate/chlorite values source-supported; DBPR/LRAA/sample-location details need DBPR audit. |
| Chemical Handling / Safety | 196-210 | caveated | Safety mindset correct; final version must defer to SDS, SOPs, and site training. |
| T5 Troubleshooting / Scenario Judgment | 211-250 | partially verified | Strong T5-style logic; source audit should support recurring operational claims. |

---

# Source-Verified / High-Confidence Items

| Item | Card Range | Source / Status |
|---|---:|---|
| CT formula | 66-71, 141-style concepts in related decks | [[Water Operator Source Bibliography#CA-EXAM-CONVERSION-2026]] |
| CT pass/fail arithmetic | 68-71, 77, 85-86 | arithmetic checked; table values still caveated |
| TTHM MCL | 178 | [[Water Operator Source Bibliography#EPA-NPDWR]] |
| HAA5 MCL | 180 | [[Water Operator Source Bibliography#EPA-NPDWR]] |
| Bromate MCL | 136 | [[Water Operator Source Bibliography#EPA-NPDWR]] |
| Public Notification Tier 1 timing | 106 | [[Water Operator Source Bibliography#EPA-PUBLIC-NOTIFICATION]] |
| T5 public-health/scenario emphasis | many scenario cards | [[Water Operator Source Bibliography#CA-T5-DESCRIPTION-2026]] |
| Chemical feed formula | 51-52 | [[Water Operator Source Bibliography#CA-EXAM-CONVERSION-2026]] |

---

# Caveats to Preserve in the Deck

## CT Tables

Do not let cards imply that CT is only `residual × time`. The formula gives actual CT, but compliance requires comparison to **required CT** from the correct table.

## Crypto

Cards saying Cryptosporidium is resistant to normal chlorination are useful and conceptually correct, but final verification should cite SWTR/LT2 or accepted treatment guidance.

## Chloramines

Chloramine residual stability, nitrification, free ammonia, nitrite, and temporary free-chlorine conversion should remain caveated because responses are system-specific and regulatory/SOP-dependent.

## UV

UV concepts should keep the validation caveat: credit depends on validated reactor conditions, flow, UVT, intensity, sleeve condition, lamp status, and approved operating envelope.

## Ozone

Ozone cards should retain the bromate caveat where bromide is present and note that ozone does not provide a lasting distribution residual.

## DBPs

DBP control must not be framed as simply lowering chlorine. The deck correctly emphasizes balancing DBP control with microbial protection.

---

# Required Deck Edits

1. Add `cards_audited: 250/250`.
2. Add audit-count metadata.
3. Keep `verification_status: partially_verified`.
4. Add `cards_needs_revision_count: 0`.
5. Preserve CT table caveat.
6. Preserve SDS/SOP safety caveat.
7. Add future source IDs when audited: `EPA-SWTR`, `EPA-DBPR`, `EPA-UV-GUIDANCE`, `EPA-CHLORAMINE-NITRIFICATION`, and an accepted operator-treatment technical source.

---

# Bottom Line

This is a strong study deck. It is safe for active study with caveats and is suitable for draft printable use. It should not be marked fully verified or public-final until CT tables, SWTR, DBPR, UV/ozone, chloramination/nitrification, and safety-source references are completed.
