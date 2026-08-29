# SKiDL evaluation result

Status: `SKIDL_M6_AUTHORITY_PATH_BLOCKED` at Mac handoff.

Observed environment: Python 3.11, SKiDL 2.3.0, kinet2pcb 1.1.4, KiCad
10.0.5. The flat fixture in `work/skidl_spike/` generated a KiCad schematic
and netlist; a disposable Linux-like pcbnew path was not available on Mac, so
the PCB mapping was only structural evidence. The genuine hierarchy fixture
produced four native ERC errors for dangling/invalid sheet labels and pins.
The auto-stub variant removed real sheet-pin authority and is not a proof.

Custom-part and PiSXMe graft authority proofs were not completed. The normal
Mac Python environment did not expose a usable `pcbnew` module for kinet2pcb.
Linux must reproduce the flat path, then close hierarchy, custom pin mapping,
and schematic-derived PCB-net authority before SKiDL can support M6.
