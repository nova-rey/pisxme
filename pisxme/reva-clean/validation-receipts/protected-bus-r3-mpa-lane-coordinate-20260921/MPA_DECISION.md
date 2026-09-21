# MPA lane-coordinate correction: J5.2 / F2

Decision ID: `PISXME-P24-R3-J5.2-F2-LANE-R2`
Work package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
Decision type: `BINDING_DECISION`
Current authority base: `57332e98` (CAD geometry); queue integration head is recorded separately.

The prior topology-first probe used north-shifted P2 coordinates and caused branch shorts. The corrected J5.2/F2 row is:

- `PWR_SRC_J5_P2`: F.Cu `(16.20,25.00) -> (24.00,25.00)`; In2 `(24.00,25.00) -> (57.60,26.25)`.
- `PWR_FUSED_J5_P2`: F.Cu `(66.90,26.25) -> (72.00,26.25)`; In2 `(72.00,26.25) -> (106.00,26.25)`.

`(57.60,26.25)` and `(66.90,26.25)` are the F2 raw/fused pad-side coordinates. `x=106.00` is within the authorized In2 join field `x=103.5..112`. The source-to-join trunk remains forbidden on F.Cu except for the two local escapes. J5.5 remains a distinct In4 return to `POWER_RETURN_JOIN` at `x>=104`; no positive/return sharing is allowed.

Acceptance: exact current-head reconciliation; no residual P2 segments at `y=13.75` or `y=10.00`; native continuity J5.2 -> F2 raw -> F2 fused -> `12V_BRANCH_JOIN`; zero P2/P1 shorts or crossings; nine-branch census; F.Cu clip; preserved high-speed corridors; complete hot path <=8.50 mOhm.
