# Path-A U12 local storage-rail taps — V1565

Date: 2026-09-10  
Parent: V1562  
Status: **rejected route class**

This bounded trial attached only the three native U12 `STORAGE_3V3` pads,
using separated F.Cu escapes, ordinary vias, and In2 connections. J3's
already-passing nine-contact handoff was retained.

| Check | Result |
|---|---|
| J3 power-owner audit | PASS; negative control PASS |
| Native DRC | 610 violations / 339 unconnected items |
| V1562 parent | 603 violations / 342 unconnected items |
| New local defect | Real `STORAGE_3V3` / `CM5_USB3_RX_P` short plus route crossings |

The three fewer opens do not justify the added local DRC findings. Reject this
U12 escape placement. The result is route-implementation evidence; it does
not reject In2 power or the V1562 J3 handoff.

Raw board/report: `PHASE24_STORAGE_U12_SEPARATED_POWER_V1565.kicad_pcb`,
`PHASE24_STORAGE_U12_SEPARATED_POWER_V1565-drc.rpt`.
