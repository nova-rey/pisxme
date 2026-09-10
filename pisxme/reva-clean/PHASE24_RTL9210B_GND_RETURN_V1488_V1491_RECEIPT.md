# RTL9210B GND return-field receipt: V1488-V1491

## Current accepted result

`PHASE24_RTL9210B_GND_REROUTE_RTL3V3_V1491.kicad_pcb` is the accepted isolated
Path-B QFN-field primitive. It starts from V1469, adds an ordinary 0.50/0.30
mm through-via on the existing GND copper above the QFN field, adds an
intentional In1 GND return field, and moves the RTL_3V3 B.Cu shelf around that
stitch. No signal is routed on In1.

Native KiCad DRC: **0 violations**, 7 inherited unconnected groups. The
remaining opens are RSET, XTAL_IN, XTAL_OUT, and REFCLK; they are not waived.

`phase24_rtl9210b_gnd_in1_return_v1491_audit.py` derives the PASS from the
saved board's native pads, tracks, vias, and connectivity. It verifies U1.45,
U1.66, and U1.69 are GND and connected, and its negative control removes the
97.2/67.2 QFN-to-In1 stitch and confirms the remote GND via is no longer
connected.

## Rejected evidence

V1477-V1479 perimeter/lower launches were rejected for pad-field or support
clearance/crossing violations. V1480-V1484 direct new-pocket launches were
rejected for rail/pad or manufacturing-rule violations. V1485-V1487 showed
that the existing GND copper was the correct launch, but the original
RTL_3V3/RTL_1V1 shelf occupied the needed via pocket. V1488 co-authored the
RTL_1V1 shelf but left one dangling branch; V1490 moved the RTL_3V3 shelf but
left its retained branch endpoint dangling. V1491 closes both implementation
defects without changing design rules.

## Scope and status

This is an isolated Path-B primitive only. It does not promote RTL9210B into
the production schematic/PCB and does not close Phase 24. RSET, crystal,
REFCLK, firmware/configuration, full mode behavior, procurement, integrated
storage routing, and Path-A comparison remain open.
