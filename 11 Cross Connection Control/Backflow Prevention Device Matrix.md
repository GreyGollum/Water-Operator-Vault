---
type: study-note
project: Water Operator Vault
area: cross-connection-control
status: active
created: 2026-06-19
last_updated: 2026-06-19
verification_status: source_supported_with_caveats
---

# Backflow Prevention Device Matrix

> Operator-study comparison. Local program rules and approved lists control actual selection and installation.

## Device / Assembly Crosswalk

| Type | Name | Field-Testable? | Protects Against | Study Use |
|---|---|---:|---|---|
| AG | Air gap | visual inspection | backsiphonage and backpressure | strongest physical separation |
| RP | Reduced-pressure assembly | yes | backsiphonage and backpressure | high-hazard use where approved |
| DC | Double check assembly | yes | backsiphonage and backpressure | lower-hazard use where approved |
| PVB | Pressure vacuum breaker | yes | backsiphonage only | irrigation and similar use where approved |
| SVB | Spill-resistant vacuum breaker | yes | backsiphonage only | similar use to PVB |
| AVB | Atmospheric vacuum breaker | inspection | backsiphonage only | point-of-use, not continuous pressure |
| Dual check | Dual check valve | usually no | limited low-hazard use | not the same as a DC assembly |

## Key Memory Aid

```yaml
air_gap: strongest_physical_separation
rp: higher_hazard_where_approved
dc: lower_hazard_where_approved
vacuum_breakers: backsiphonage_only
avb_continuous_pressure: false
local_authority_controls: true
```

## Caveats

USC Foundation, AWWA M14, California rules, and local program requirements are still pending for final-public release.

## Related

- [[Cross Connection Control Index]]
- [[Cross Connection Source Plan]]
