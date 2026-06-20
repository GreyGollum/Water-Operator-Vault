---
type: card-audit
project: Water Operator Vault
area: flashcards
deck: T5 Flash Cards - Treatment Processes
status: active
audit_date: 2026-06-19
cards_audited: 265
verification_status: audited_partially_verified
source_ids: [CA-T5-DESCRIPTION-2026, CA-TREAT-ERK, EPA-NPDWR, EPA-PFAS-NPDWR]
---

# Card Audit - Treatment Processes

> Deck audited: [[T5 Flash Cards - Treatment Processes]]  
> Cards audited: **265 / 265**  
> Result: **Audited, partially verified**. No immediately incorrect cards were found, but this is the most technical deck audited so far. It should remain partially verified until operator-training and technical references are added for coagulation, filtration, membranes, ion exchange, GAC, softening, taste/odor, and process-control claims.

## Summary Counts

| Status | Count | Meaning |
|---|---:|---|
| Verified / stable core concept | 94 | Basic process definitions, stable operator concepts, and T5 public-health/process-control logic |
| Caveated | 81 | Generally correct but chemistry/process/design dependent |
| Technical audit pending | 90 | Needs accepted technical source before final verified/public-print status |
| Needs revision | 0 | No clearly wrong cards found during this audit pass |
| **Total** | **265** | All cards accounted for |

---

# Key Finding

This deck is **good as a study deck**, but it should not be treated as a fully verified engineering or compliance reference. Treatment-process details are highly dependent on:

- source-water chemistry
- plant design
- chemical selection
- loading rates
- manufacturer limits
- state approval / permit basis
- jar testing or pilot testing
- operating procedures
- waste handling requirements

The deck is conceptually solid, but final verification needs technical references such as Office of Water Programs texts, EPA guidance, AWWA manuals, manufacturer O&M manuals, or system-specific SOPs.

---

# Section-Level Audit

| Section | Cards | Audit Status | Notes |
|---|---:|---|---|
| Coagulation | 1-30 | partially verified / technical pending | Core ideas are right: destabilization, charge neutralization, sweep floc, pH/alkalinity, jar testing, TOC/DBP precursors. Needs OWP/AWWA-style source audit for final. |
| Flocculation | 31-50 | partially verified / technical pending | Concepts are sound. Mixing intensity, compartments, short-circuiting, carryover, and observation claims need technical-source support. |
| Sedimentation and Clarification | 51-75 | partially verified / technical pending | Surface overflow/weir loading concepts are sound; sludge blanket, tube/plate settlers, DAF, density currents, launders need source support. |
| Filtration | 76-115 | partially verified / technical pending | Strong section; filter ripening, filter-to-waste, mudballs, air binding, filter profiles, UFRV, slow sand/direct filtration need technical source audit. |
| Surface Water Treatment Rules and Log Removal | 116-135 | caveated | Log-removal math is stable; actual SWTR, IESWTR, LT2, turbidity, CT, and credit requirements need direct rule/source audit. |
| GAC and Adsorption | 136-155 | partially verified / technical pending | GAC/PAC/adsorption/breakthrough/EBCT/lead-lag concepts are sound; PFAS removal and BAC claims need technical source and design caveats. |
| Ion Exchange | 156-175 | partially verified / technical pending | IX/resin/anion/cation/regeneration/breakthrough concepts are sound; PFAS, radionuclide, nitrate selectivity and waste issues need source audit. |
| Membranes | 176-205 | partially verified / technical pending | MF/UF/NF/RO, permeate/concentrate/TMP/flux/integrity concepts are sound; log credit, concentrate waste, fouling, validation need technical support. |
| Softening and Stabilization | 206-220 | technical audit pending | Lime softening/recarbonation/stability/corrosion-control statements are reasonable but chemistry/design dependent. |
| Iron, Manganese, Taste/Odor, Organics | 221-235 | technical audit pending | Iron/manganese oxidation, permanganate, geosmin/MIB, aeration, UV254 statements need technical source audit. |
| Process Control and T5 Troubleshooting | 236-265 | partially verified | Strong T5-style scenario logic; source support should be added for public-health/process-control wording and SOP dependence. |

---

# High-Confidence Stable Concepts

The following concepts are high confidence and suitable for study with normal caveats:

- Coagulation destabilizes suspended/colloidal particles.
- Flocculation gently mixes destabilized particles into larger floc.
- Sedimentation removes particles by gravity settling.
- Filtration removes particles through media or membranes.
- Surface overflow rate = flow / surface area.
- Weir loading = flow / weir length.
- Log removal expresses percent reduction by powers of ten.
- GAC and PAC are activated carbon forms.
- Adsorption means attachment to a surface.
- Ion exchange swaps ions between water and resin.
- RO means reverse osmosis.
- Permeate is treated water passing through a membrane.
- Concentrate is rejected water containing concentrated contaminants.
- TMP rising often indicates fouling or plugging.
- Softening reduces hardness, mainly calcium and magnesium.
- Iron commonly causes red-brown staining.
- Manganese commonly causes black staining.
- Geosmin and MIB cause earthy/musty taste and odor.
- Process control uses data and observations to keep treatment stable.
- T5 decisions should prioritize barriers, public health, compliance, and controlled changes.

---

# Caveats to Preserve

## Coagulation

Coagulant performance is pH-, alkalinity-, temperature-, turbidity-, TOC-, and source-water-dependent. Dose changes should be based on jar testing, trends, and controlled process evaluation.

## Filtration

Filter performance statements must be tied to filter type, media condition, loading rate, turbidity goals, run time, backwash performance, and treatment-technique rules.

## Surface Water Rules

The deck gives useful concepts, but exact log-removal/inactivation credits and turbidity compliance requirements must come from the applicable surface-water treatment rules and approved plant basis.

## GAC / PFAS

GAC can remove many PFAS, especially longer-chain compounds, but performance depends on compound, water quality, EBCT, competition, carbon type, media age, and breakthrough monitoring.

## Ion Exchange / PFAS

Specialized anion exchange resins can remove PFAS, but resin exhaustion, disposal, regeneration, selectivity, and competing ions are design/regulatory issues.

## Membranes

RO/NF/MF/UF statements are generally right, but removal credit and compliance use depend on membrane type, integrity testing, operating envelope, and waste/concentrate handling.

## Softening / Stabilization

Softening chemistry is system-specific. pH, alkalinity, stability indices, corrosion control, and sludge handling must be reviewed with technical references and system design.

## Iron/Manganese/Taste/Odor

Treatment depends on oxidation state, pH, oxidant, contact time, filter media, source water, and operational goals.

---

# Required Deck Edits

1. Add verification frontmatter.
2. Add `cards_audited: 265/265`.
3. Add audit-count metadata.
4. Keep `verification_status: partially_verified`.
5. Add technical-source caveat at the top of the deck.
6. Add source IDs for technical references once available: `OWP-TREATMENT`, `EPA-SWTR`, `EPA-DBPR`, `EPA-MEMBRANE-GUIDANCE`, `EPA-PFAS-TREATMENT`, `AWWA-TREATMENT` if used.
7. Preserve warning that this is a study aid, not design guidance.

---

# Bottom Line

This deck is very useful for T5 studying and scenario thinking, but it is the least appropriate deck to mark fully verified without a technical-source pass. It is safe for active study with caveats, but public/print-final status should wait until accepted treatment-process sources are tied to each section.
