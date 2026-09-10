# Phase 24 RX F.Cu target-launch receipt — V147

Date: 2026-09-10  
Base: `PHASE24_STORAGE_USB3_R80_RELOCATED_V127.kicad_pcb`  
Fixture: `PHASE24_STORAGE_SUPPORT_U12_TARGET_RX_FCU_V147.kicad_pcb`

V147 tested the consultant-recommended solution class of keeping RX on
F.Cu without target-side transitions. The first implementation used naive
same-row shoulders from the native U11 RX pads to the U12 target pads.
Native endpoint connectivity passed all six local support assertions, but
native DRC rejected the fixture at 36 violations / 32 unconnected pads.

The failures are implementation-specific: the U11 RX pads share a y-row,
so the naive shoulders cross the U11 source pad field; the inherited TX
launch also retained U12-field conflicts. V147 is rejected and is not
evidence against the RX-without-target-vias class. No production PCB,
schematic, layer contract, or DRC severity was changed.
