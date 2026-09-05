# Phase 23 status — test/debug access

Status: CLOSED

The Phase 22 ancestor remains the active clean baseline. The first disposable
probe implementation was rejected, not promoted: large underside SMD test
points were placed directly over source component pads, producing true
shorting and hole-clearance violations in native KiCad DRC. This experiment
does not invalidate the board or the Phase 22 ground/return closure.

A second candidate, `PHASE23_TEST_DEBUG_PADS_V2.kicad_pcb`, used smaller
underside pads and dogbones, but was also rejected. Native DRC found new
shorting/crossing and hole-clearance errors where the selected dogbones entered
the U1/U2/U4/U5 pad fields and existing control-via corridor. It is retained
only as disposable evidence and is not a production ancestor.

The accepted candidate is `PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb`. It uses
small through-hole probe pads in open acreage, with short low-speed dogbones
and ordinary vias where required. It covers raw/fused/protected 12 V, CM5 5 V,
storage 3.3 V, both bridge PG nets, CM5 PERST, POWER_GND, and the
schematic-authorized `/DEBUG/UART`, `/DEBUG/RECOVERY`,
`/DEBUG/POWER_PG_FAULT`, and `/DEBUG/DEBUG_GND` pads. Native DRC reports 193
inherited-class violations and 391 unconnected items, with zero shorting,
crossing, hole-clearance, width, or footprint-courtyard errors attributable to
the probe implementation. No high-speed net was stubbed and no signal was
placed on a plane layer. The regression test
`validation/phase3/test_phase23_test_debug_pads.py` passes.
