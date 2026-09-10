# Path-A isolated R81 storage-rail tap — V1567

Date: 2026-09-10  
Parent: V1562  
Status: **rejected route class; local In2 corridor remains occupied**

The isolated R81 `STORAGE_3V3` pad was escaped with an ordinary F.Cu
dogbone/via and an In2 handoff. The J3 nine-contact power audit and its
necessary-trace negative control remained PASS. The adjusted corridor removed
the earlier direct `JMS_AVDDL` short, but native DRC remained 605 violations /
341 unconnected items versus V1562's 603 / 342, with a clearance finding to
the existing USB via field.

This is rejected route evidence. R81 is not a QFN-field impossibility, but
the tested corridor still needs a more carefully obstacle-aware dogleg before
promotion. V1562 remains the accepted focused primitive.

Raw board/report: `PHASE24_STORAGE_R81_POWER_V1567.kicad_pcb`,
`PHASE24_STORAGE_R81_POWER_V1567-drc.rpt`.
