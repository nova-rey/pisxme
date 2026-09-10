# Phase 24 Path-A storage USB3 source-transition V40

V40 is a disposable route-development candidate derived from the valid V37
J8-authority basis. It replaces only the CM5 USB3 `CM5_USB3_TX_N` source
escape: the source transitions to B.Cu at `(72.0,106.3)`, passes below the
local `CM5_PER0_P` F.Cu corridor, and returns through the existing U12 launch
via at `(149.8,136.2)`. No schematic, footprint, selector, storage, or
unrelated copper authority changed.

Native KiCad 10.0.5 validation of
`PHASE24_STORAGE_CM5_USB4_MONOTONIC_V40_TXN_SOURCE_TRANSITION.kicad_pcb`:

- USB3 native endpoint connectivity: PASS;
- SATA native endpoint connectivity: PASS;
- current `PHASE24_STORAGE_MODE_J8.xml` pad parity: PASS, zero mismatches;
- native DRC: 600 violations and 399 unconnected items;
- shorting entries: zero;
- no validation severity or rule was relaxed.

V40 improves the V37 native DRC count by three without introducing a new
shorting class. It remains disposable because inherited crossings, clearance
debt, opens, and whole-board Phase 24 gates remain unresolved.
