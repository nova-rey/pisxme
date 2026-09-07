# Phase 24 Path-A SATA selector route V3 — 2026-09-07

Status: `REJECTED ROUTE IMPLEMENTATION; SOURCE AND NATIVE ENDPOINT AUTHORITY PASS`

V3 was regenerated from the corrected source-derived placement and net
authority, including U13 exposed pad 43 assigned to `POWER_GND`.

## Evidence

* Board: `PHASE24_STORAGE_SATA_SELECTOR_MINIMAL_V3_20260907.kicad_pcb`
* Native DRC: `PHASE24_STORAGE_SATA_SELECTOR_MINIMAL_V3_20260907-drc.rpt`
* Native selector audit: all 12 endpoint assertions PASS
* Native negative-control method remains PASS on the same topology
* DRC summary: 133 findings / 52 opens; 2 shorts / 10 crossings

## Failure classification

This is not an authority or architecture failure. The remaining shorts are
concrete route defects:

1. the M.2-side TXN corridor still crosses U13's grounded thermal pad;
2. one TXN final launch interacts with the adjacent M.2 RX contact field.

The other crossings are route-layer/corridor conflicts in the disposable
author. No V3 copper is promoted to the integrated board. The corrected source
mapping and U13 thermal-pad assignment remain authoritative.

## Next bounded experiment

Move TXN to a thermal-pad-clearing B.Cu escape with an ordinary via outside
the U13 pad field, and re-author the four M.2 final dogbones with ordered
target-via columns. Re-run native DRC, the 12-endpoint audit, pair geometry,
and the selector negative control before considering integration.

The TX-only thermal-clear experiment is preserved as
`PHASE24_STORAGE_SATA_SELECTOR_TX_THERMAL_ESCAPE_V4.kicad_pcb`. It removed
the two original U13 thermal-pad shorts but regressed to 136 native DRC
findings / 52 opens, including TXP/TXN via spacing and inherited corridor
crossings. It is rejected as a route implementation; no V4 copper is
promoted.

The isolated launch fixture
`PHASE24_PATHA_M2_LANE0_LAUNCH_ISOLATED_V1.kicad_pcb` removes all inherited
selector/bridge copper and tests only U13 lane-0 to J3. Native DRC reports
84 findings / 32 opens, including M.2 mounting-hole/ground interactions and
connector-side target-via conflicts. It is rejected; the next launch class
must move target vias farther outboard and explicitly clear the connector's
mechanical holes.

## V3 split-layer launch — rejected

`PHASE24_PATHA_M2_LANE0_LAUNCH_ISOLATED_V3.kicad_pcb` tested separate TX/RX
layer corridors and connector-ordered target vias. Native DRC reports 103
violations / 32 unconnected items. The target-via field still shorted RXN and
RXP, TXN interacted with inherited TUSB_SATA_RXP copper, and a track crossing
remained. V3 is rejected as route implementation evidence; the connector
launch needs a less congested fanout/side assignment.

## V5/V6 launch comparison — rejected

V5 (`PHASE24_PATHA_M2_LANE0_LAUNCH_ISOLATED_V5.kicad_pcb`) used orthogonal
source escapes and vertical contact-row dogbones. Native DRC: 80 violations /
33 unconnected items, no shorts, one RX source crossing. V6 changed the RX
source corridors; native DRC regressed to 83 violations / 33 unconnected and
introduced an M1 mounting-hole interaction. V5 is retained as the best
isolated baseline; neither candidate is integrated.

## V2 isolated launch — rejected

`PHASE24_PATHA_M2_LANE0_LAUNCH_ISOLATED_V2.kicad_pcb` moved the RX lower
corridors around M1 before the connector launch. Native DRC reports 83
violations / 32 unconnected items. This did not pass: the TXP final dogbone
contacts J3 pad 47 (TXN), the TXN final dogbone contacts J3 ground pad 45,
the RXP final dogbone contacts J3 ground pad 39, and the RXN/RXP corridors
cross in the target-via field. The experiment remains useful evidence that
the M1 detour alone is insufficient. It is rejected as route implementation;
the next candidate must reorder and move the connector-side target vias and
final dogbones together.

## V7/V8 RXP layer alternatives — rejected

V7 moved RXP to a lower B.Cu corridor and reported 84 violations / 34
unconnected items, including an M1 short and one crossing. V8 routed below
and outboard of M1 and reported 82 / 34, with no shorts and one crossing.
Both are rejected; V5 remains the preferred isolated baseline.

V9 moved RXN farther left and reported 81 violations / 34 unconnected with
one RX source short. V10 moved the RXP transition below that escape and
reported 81 / 34 with zero shorts and zero crossings. V10 is retained as the
best topological baseline; its remaining issue is the clearance-constrained
M.2 contact-row fanout.

V11 reduced the clearance count to 72 but introduced one RXP/TXN final
dogbone crossing. V12 swapped those departure heights and returned to zero
shorts/crossings at 75 clearance findings, 34 unconnected items, four
disposable via-dangling findings, and two track-dangling findings. V12 is the
best current topological candidate but remains rejected pending full native
clearance/connectivity closure.
