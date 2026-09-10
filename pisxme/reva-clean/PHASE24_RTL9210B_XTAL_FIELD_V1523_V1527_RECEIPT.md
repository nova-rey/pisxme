# Phase 24 RTL9210B crystal-field receipt — V1523/V1526/V1527

Date: 2026-09-10

## V1523 accepted

`PHASE24_RTL9210B_RTL3V3_REHOME_U152_V1523.kicad_pcb` removes the obsolete
U1.52 west departure and rehomes pad 52 through an ordinary 0.50/0.30-mm
through-via at (94.05,65.8), then an outboard B.Cu rail to the existing
RTL_3V3 network. Native DRC: 0 violations / 6 opens.

## V1526 accepted

`PHASE24_RTL9210B_XTALOUT_FCU_C2_DOGBONE_V1526.kicad_pcb` routes native U1.54
to C2.1 and Y1.2 on F.Cu, approaching C2 below its adjacent C2.2 GND pad.
Native DRC: 0 violations / 4 opens. Saved-board connectivity joins U1.54,
C2.1, and Y1.2. Trace-removal negative controls for XTAL_OUT and RTL_3V3
both fail as required.

## V1527 rejected

The outboard XTAL_IN trial was rejected by native DRC: 11 violations,
including GND-stitch collision/shorting, live RTL_3V3-field crossings, and
exposed-pad clearance. It is route evidence only; no production authority
changed.

## Current disposition

V1523 plus V1526 are the current accepted isolated basis. XTAL_IN and
REFCLK_P/N remain open; Path A, production integration, firmware, procurement,
and complete Path-B closure remain unchanged and open.
