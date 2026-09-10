# Path-A stale-parent power experiment — V1563

Date: 2026-09-10  
Parent: `PHASE24_STORAGE_V75_COAUTHORED_V196.kicad_pcb`  
Status: **rejected; stale source-net parent**

The V1562 pad-derived In2 handoff was applied without changing its geometry to
the older V196 support-field parent. Native power-owner audit failed for all
nine J3 pads because V196 still owns them as legacy `M2_3V3`, while the
current schematic authority uses `STORAGE_3V3`. Native DRC reported 638
violations / 347 unconnected items and real `M2_3V3`/`STORAGE_3V3` shorts.

This is not evidence against the V1562 power topology. It proves V196 is not
a valid source-corrected parent. The source-corrected V79 descendant remains
the valid parent; PCB-only net repair is not permitted.

Raw rejected board/report: `PHASE24_STORAGE_V196_POWER_IN2_V1563.kicad_pcb`,
`PHASE24_STORAGE_V196_POWER_IN2_V1563-drc.rpt`.
