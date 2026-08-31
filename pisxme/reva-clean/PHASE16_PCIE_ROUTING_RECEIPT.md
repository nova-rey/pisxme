# Phase 16 PCIe routing receipt

Status: `CLOSED_WITH_REV_A_EMPIRICAL_RISK`

`ACREAGE_PCIE_PHASE16.kicad_pcb` is derived from the accepted Phase 15
acreage board, saved through the KiCad ABI Python API, and checked by native
KiCad 10.0.5 DRC. PCIe copper is confined to F.Cu/B.Cu, uses ordinary
0.50/0.30 mm through vias, and materializes the Phase 13 `HS_PCIE_90R` class
at 0.13208 mm track width and 0.2032 mm pair gap.

`validation/phase3/test_phase16_pcie_route.py` passes after a native board
load. It proves the exact PER0, REFCLK, PERST, and transmitter-side PET0
endpoint graphs, preserves the capacitor split, checks every PCIe track
width, and rejects target-net crossings, shorts, and dangling vias. Native
DRC report `ACREAGE_PCIE_PHASE16-drc10.rpt` has no
`tracks_crossing`, `shorting_items`, or `via_dangling` findings. Four
ordinary GND transition vias are placed outside the dense CM5/capacitor
fields.

Two native DRC clearance findings remain at the CM5 J7 REFCLK breakout. They
are caused by the authoritative CM5 0.4 mm row pitch and 0.7 mm pad length:
ordinary through-via routing cannot escape those SMD pads while maintaining
the board-wide 0.20 mm rule without via-in-pad, a footprint change, or a
local fabrication-rule exception. This is explicitly retained as
`REV_A_EMPIRICAL_RISK` for a fabrication coupon/assembly review; it is not a
clean board-wide DRC result or hardware-release approval. Remaining DRC
findings are inherited acreage mechanical/unconnected baseline debt.

Decision closed: Phase 16 PCIe logical authority is preserved, transmitter
AC-coupling is physically split, and the focused route topology has no target
shorts/crossings/dangling transitions. Phase 17 may begin as the next
sequential phase; no Phase 18+ routing is included.
