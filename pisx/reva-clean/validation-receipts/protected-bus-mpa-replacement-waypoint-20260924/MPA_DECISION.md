# Macro Placement Authority Decision — Replacement Protected-Bus Corridor

- Date: 2026-09-24
- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Base authority: current `reva-clean` HEAD at dispatch
- Decision: bind one alternate local J5.2 to F2.1 corridor; reject the prior via route.

Authorized top-side `F.Cu` path using the existing 0.20 mm prototype rule:

`J5.2 (16.20,25.00) -> (18.35,27.15) -> (50.00,27.15) -> (50.00,13.75) -> F2.1 (57.60,13.75)`

Use no via, no `In2.Cu` raw lane, no diagonal segment, and no endpoint via. Clip
`REV_A_TOP_POWER_GND_RETURN_FULL` from this local corridor as already authorized by
MPA R2; preserve `In1.Cu`/`In4.Cu` returns and fixed `12V_PROTECTED` geometry.

Clearance basis: F1 courtyard ends at x=46.8 and F2 begins at x=53.2, leaving
6.4 mm; the x=50 vertical is 3.2 mm from each courtyard. The y=27.15 horizontal
is 1.35 mm below courtyard edges. At J5.3, pad-center separation is 2.15 mm,
providing 0.20 mm edge clearance under the current rule. The route remains in the
J5/F2 bank and avoids the fixed J9/TP3 `12V_PROTECTED` geometry near (12,75)/(13,76.45).

No CAD edits or global rule changes are authorized by this decision. Preserve R3
branch resistance, current, DFM, and native DRC acceptance gates.
