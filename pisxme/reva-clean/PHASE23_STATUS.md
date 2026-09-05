# Phase 23 status — test/debug access

Status: IN PROGRESS

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

Remaining work is to add physically accessible, net-connected probe pads with
short low-speed dogbones and ordinary-via transitions, while adding the
missing schematic-authority path for recovery/UART if those signals are
required by the final debug contract. No high-speed net will be stubbed and no
rejected Phase 23 board is used as a production ancestor.
