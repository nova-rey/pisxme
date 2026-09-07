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
