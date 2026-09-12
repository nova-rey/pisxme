# Phase 24 JMS_XAVDDH local receipt

Candidate: `PHASE24_STORAGE_MKEY_USB3_XAVDDH_LOCAL_V2_20260912.kicad_pcb`

Starting from the validated REXT base, C84 was moved to `(150,120)`. U11.52
escapes west from the QFN pad row, changes layer through ordinary 0.60/0.30
mm through-vias, crosses the storage pocket on B.Cu, and returns to C84.1.
The earlier eastward escape is rejected because it crossed adjacent U11 pads.

Native KiCad 10.0.5: endpoint authority, saved-copper connectivity, and
trace-removal negative control pass. The candidate is rejected for a local
solder-mask bridge at the U11.52 escape; fresh Light validation reports 562
violations / 415 unconnected items under KiCad 10.0.6. This is not support
closure. The REXT base remains the active basis.

The failure is a route-implementation/manufacturing-rule issue, not evidence
against the JMS_XAVDDH circuit or the frozen RTL9210B placement.
