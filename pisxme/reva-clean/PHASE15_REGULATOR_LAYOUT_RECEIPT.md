# Phase 15 regulator layout receipt

Status: `IN_PROGRESS`

This checkpoint establishes the first vendor-layout-derived geometry for the
three TPSM63606 modules. `phase15_thermal_vias.py` starts from the closed
Phase 14 board and adds four ordinary through vias per module, one centered in
each of the four TI RDL0020 central PGND lands. The project board rule is
honored with 0.50 mm finished diameter and 0.30 mm drill; the 0.10 mm annulus
is compatible with the current JLC six-layer ordinary-through-via basis.

The four separate exposed PGND lands are joined by 0.25 mm same-net F.Cu
links across their 0.25 mm inter-land gaps. Exact hierarchical net objects
are assigned through `SetNet`, avoiding the KiCad Python binding's incorrect
nearest-pad reassignment observed when vias were placed over perimeter pads.

Evidence:

- `validation/phase3/test_phase15_thermal_vias.py` passes after native
  save/reload and verifies all 12 vias are `/REGULATORS/POWER_GND`, span
  F.Cu-B.Cu, and are 0.50/0.30 mm.
- Fresh native DRC of `ACREAGE_REGULATOR_PHASE15.kicad_pcb` reports 192
  acreage violations and no new thermal-via diameter, drill, annular,
  solder-mask, short, or dangling-via defect. The baseline Phase 14 board
  reported 216 findings; the count is not used as a closure criterion because
  the board-wide acreage remains intentionally unrouted.
- Authority is `TPSM63606.pdf` revision B, TI SLVSGB4B, pages 31-32, plus
  the project-local `TPSM63606_SUPPORT_AUTHORITY.md` and corrected
  `TPSM63606RDLR_RDL0020.kicad_mod`.

- `phase15_power_escape.py` now applies the same pad-edge escape to all three
  VIN/VOUT islands that have output capacitors in the current schematic: U3
  and U4 receive both VIN and VOUT escapes, while U5 receives its three VIN
  escapes. U4 output capacitors are deliberately escaped from the left output
  land to preserve clearance from U5 and the storage bridge.
- The focused native regression reports no `shorting_items` or
  `tracks_crossing` defects and reduces the base candidate from 296 to 280
  unrouted items. The remaining unrouted regulator items are the required
  bootstrap, feedback, RT, PG, VCC_INTERNAL, and control connections.
- Independent KiCad review corrected the U3 VOUT escape to the true right edge
  of pad 9 at `(54.95, 80.00)` rather than the inward pad-8 tie. The regression
  now asserts that both U3 VOUT capacitor escapes terminate at that exact
  edge coordinate; U4 remains intentionally escaped from the left pad-8 edge.

This does not close Phase 15. Remaining required work is localized VIN and
VOUT high-dI/dt routing, feedback/RT/PG routing, switch-node containment,
effective-capacitance calculation, and reference-layout overlay evidence for
each rail.
