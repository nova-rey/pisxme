# Phase 24 U12 transformed target-launch receipt — V144

Date: 2026-09-10  
Base: `PHASE24_STORAGE_USB3_R80_RELOCATED_V127.kicad_pcb`  
Fixture: `PHASE24_STORAGE_SUPPORT_U12_ROT180_NATIVE_LAUNCH_V144.kicad_pcb`

V144 is a corrected transform-aware 180-degree U12 support experiment. The
generator queried the transformed U12 pad field for the target-side launch;
it did not reuse the normal-orientation target coordinates. Native saved-board
connectivity passed all six local support endpoint assertions. This is only a
local fixture, so the four CM5 source endpoints are intentionally absent.

Native KiCad DRC reported 13 violations and 32 unconnected pads. The real
failures include B.Cu USB pair crossings, USB_TXN1/JMS_USB3_TXN and
USB_TXP1/JMS_USB3_TXP shorts, RX-pair shorting, target-field clearance
violations, and two silkscreen warnings. No rule severity was changed, no
via-in-pad was used, and no production PCB or Path-A schematic was changed.

Disposition: rejected route-implementation evidence. The transformed
coordinate correction was necessary but insufficient; the next attempt must
co-author the complete U12 target/source field rather than merely relocating
target vias or reusing fixed corridor coordinates.
