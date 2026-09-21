# MPA R3: F2 placement reconciliation

Decision ID: `PISXME-P24-R3-J5.2-F2-LANE-R3`
Work package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
Decision: `BINDING_DECISION`
CAD base: `57332e98`; canonical queue head at integration: `4c2b63af`.

Native F2 is centered at `(64.00,15.00)` with raw/fused pad centers `(57.60,13.75)` and `(66.90,13.75)`. Apply exactly one placement transform to F2: `T_F2=(0,+11.25 mm)`. The resulting center is `(64.00,26.25)` and pad centers are `(57.60,25.00)` and `(66.90,25.00)`.

Bind J5.2/F2 lanes:

- `PWR_SRC_J5_P2`: F.Cu `(16.20,25.00)->(24.00,25.00)`; In2 `(24.00,25.00)->(57.60,25.00)`.
- `PWR_FUSED_J5_P2`: F.Cu `(66.90,25.00)->(72.00,25.00)`; In2 `(72.00,25.00)->(106.00,25.00)`.

F.Cu is limited to those local escapes. No y=13.75, y=10.00, or diagonal F.Cu source-to-join trunk remains. J5.5 stays a separate In4 return to `POWER_RETURN_JOIN` at x>=104. Acceptance requires transformed-footprint proof, exact route graph, native continuity, zero P2/P1 shorts/crossings, nine-branch census, preserved high-speed corridors, and complete hot path <=8.50 mOhm.
