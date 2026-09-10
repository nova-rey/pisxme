# Path-A storage support-rail attachment — V1564

Date: 2026-09-10  
Parent: V1562 source-corrected storage power primitive  
Status: **rejected route class; retain V1562**

## Experiment

Native pad coordinates for the remaining `STORAGE_3V3` pads on U12, U13, and
R81 were escaped with ordinary F.Cu dogbones and through-vias, then connected
to the existing In2 spine. The J3 nine-contact handoff was retained.

## Result

| Check | Result |
|---|---|
| J3 power-owner audit | PASS — 9 contacts |
| J3 trace-removal negative control | PASS |
| Native DRC | 634 violations / 334 unconnected items |
| Parent V1562 | 603 violations / 342 unconnected items |
| New route class | Rejected — crossings/shorts/clearance findings in support-field attachment |

The eight fewer unconnected items do not outweigh the 31 added DRC findings.
The common-spine geometry is not promoted. This is route-implementation
evidence, not evidence against the source-owned `STORAGE_3V3` net or the
storage architecture.

Raw board/report: `PHASE24_STORAGE_M2_POWER_IN2_SUPPORT_V1564.kicad_pcb`,
`PHASE24_STORAGE_M2_POWER_IN2_SUPPORT_V1564-drc.rpt`.
