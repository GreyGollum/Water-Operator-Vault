---
type: source-spot-check
project: Water Operator Vault
area: verification
status: active
created: 2026-06-19
last_updated: 2026-06-19
verification_status: official_source_spot_check_complete_public_final_still_pending
---

# Final Source Spot Check - 2026-06-19

> Dated official-source spot check for the Water Operator Vault release candidate. This is a spot check, not a complete line-by-line legal audit.

## Sources Checked

| Source ID | Source | Spot-Check Result |
|---|---|---|
| EPA-NPDWR | EPA National Primary Drinking Water Regulations | Core MCL/MRDL values used in the vault remain source-supported. |
| EPA-PFAS-NPDWR | EPA PFAS NPDWR page | PFOA/PFOS 4.0 ppt remain shown in the 2024 final rule table; 2026 proposed rule actions remain date-sensitive. |
| EPA-LCR | EPA Lead and Copper Rule page | Lead/copper language remains transition-sensitive; EPA LCR page still references 15 ppb lead and 1.3 ppm copper action-level framework, while NPDWR table language and LCRI updates require caveats. |
| EPA-PUBLIC-NOTIFICATION | EPA Public Notification Rule | Tier 1 = 24 hours; Tier 2 = within 30 days; Tier 3 = annual notice concept remains source-supported. |
| EPA-CCR | EPA Consumer Confidence Reports | CCR remains official EPA source for consumer report concepts. |
| EPA-RTCR | EPA Revised Total Coliform Rule | Level 1 / Level 2 assessment and repeat-sampling concepts remain source-supported. |
| CA-DWOP | California Drinking Water Operator Certification Program | Operator certification page remains active and includes T5 exam links. |
| CA-T5-DESCRIPTION-2026 | California T5 Exam Description, Rev. 1/22/26 | T5 oral exam format and scope remain source-supported. |
| CA-EXAM-CONVERSION-2026 | California Exam Conversion Sheet, Rev. 4/30/2026 | Water math constants/formulas remain source-supported. |

## Release Decision

```yaml
standalone_internal_release_candidate: true
public_final_release_ready: false
reason_not_public_final: spot_check_complete_but_line_by_line_legal_audit_still_pending
```

## Notes

- This spot check supports the current internal/study release candidate.
- It does not replace the final public-release legal audit.
- PFAS and lead/copper remain explicitly caveated because regulatory language/timing is changing.
- California operator-certification and exam pages should be checked again immediately before public release.

## Related

- [[Current Regulatory Recheck - 2026-06-19]]
- [[Water Operator Source Bibliography]]
- [[Release Readiness Status]]
