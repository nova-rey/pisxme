# Fresh integrated validation — GATE_B redundant-via repair — 2026-09-13

Integrated candidate/source: commit `47364e6d`; selected PCB changed only by deletion of the via co-located with Q2 pad 3 on `GATE_B`. Qualified KiCad 10.0.6 Light was used; raw inputs and outputs are retained here.

Native DRC: 300 violations, 499 unconnected items, zero `shorting_items`; ERC: 293 findings, RC 5. Native netlist export RC 0. Corrected Path-A census: 11/26 pass, 15 open. Pad ownership parity: 814 schematic nodes, 1,262 PCB pads, zero expected mismatches.

The repair removed the two co-located-hole findings while preserving GATE_B connectivity through Q2’s plated-through pad. This is a material integrated candidate validation result, not Phase 24 closure; all remaining DRC, ERC, connectivity, power, SI, mechanical, DFM, and provenance requirements remain open.
