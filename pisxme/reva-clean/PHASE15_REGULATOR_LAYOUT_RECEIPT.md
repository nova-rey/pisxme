# Phase 15 regulator layout receipt

Status: `IN_PROGRESS`

This checkpoint establishes the first vendor-layout-derived geometry for the
three TPSM63606 modules. `phase15_thermal_vias.py` starts from the closed
Phase 14 board and adds four ordinary through vias per module, one centered in
each of the four TI RDL0020 central PGND lands. The project board rule is
honored with 0.50 mm finished diameter and 0.30 mm drill; the 0.10 mm annulus
is compatible with the current JLC six-layer ordinary-through-via basis.

The four separate exposed PGND lands are joined by 0.25 mm same-net F.Cu
links across their 0.25 mm inter-land gaps. Exact native net objects
are assigned through `SetNet`, avoiding the KiCad Python binding's incorrect
nearest-pad reassignment observed when vias were placed over perimeter pads.

Evidence:

- `validation/phase3/test_phase15_thermal_vias.py` passes after native
  save/reload and verifies all 12 vias are `POWER_GND`, span
  F.Cu-B.Cu, and are 0.50/0.30 mm.
- Fresh native DRC of `ACREAGE_REGULATOR_PHASE15.kicad_pcb` reports 180
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
  `tracks_crossing` defects and reduces the base candidate from 296 to 272
  unrouted items. The remaining unrouted regulator items are the required
  bootstrap, feedback, RT, PG, isolated VCC, and control connections.
- Independent KiCad review corrected the U3 VOUT escape to the true right edge
  of pad 9 at `(54.95, 80.00)` rather than the inward pad-8 tie. The regression
  now asserts that both U3 VOUT capacitor escapes terminate at that exact
  edge coordinate; U4 remains intentionally escaped from the left pad-8 edge.
- `phase15_u3_controls.py` adds the U3 feedback, RT, and PG network using
  eight deliberate 0.50/0.30 mm F.Cu-B.Cu transitions and separated B.Cu
  corridors. Native DRC reports no route-specific clearance, short, or
  crossing defect and the focused regression reduces unrouted items from 272
  to 264. The same topology remains to be instantiated for U4 and U5.

- U4/U5 were separated to `(200,105)` and `(225,105)` respectively after the
  original 10 mm pitch produced native package-side corridor conflicts with
  U7. `phase15_u4_u5_controls.py` places the support parts in module-scoped
  rows, uses separated ordinary through-via trunks, and ties U4 C18 into the
  local VOUT bank. Native DRC reports zero `clearance`, `shorting_items`, and
  `tracks_crossing` findings; `test_phase15_u4_u5_controls.py` verifies 36
  35 control/thermal vias and 254 unrouted acreage items.

- `phase15_u5_vout_bank.py` adds a 4x4 bank of the sixteen schematic-authority
  output capacitors C26-C41. The first three rows are beside U5; the fourth
  clears the existing PG support resistor. The bank is fed from U5 pad 9 via
  a short F.Cu edge departure and an In2.Cu trunk, with one ordinary
  through-via per capacitor. Native DRC and `test_phase15_u5_vout_bank.py`
  verify 69 total
  vias, 18 output-net vias, 28 PGND vias, all sixteen capacitor pad-1 net
  assignments, and zero route-specific clearance, shorting, or crossing
  findings at 237
  unconnected acreage items. The 16 added PGND vias sit just outside the
  capacitor lands, with short F.Cu links that avoid solder-mask bridging;
  native DRC reports only the pre-existing board-wide mask/acreage findings.
  Quantitative effective capacitance, thermal margin, and reference-layout
  overlay evidence remain open; this checkpoint does not close Phase 15.

The native KiCad hierarchy association was corrected before this candidate was
regenerated. `REGULATORS.kicad_sch` now places one global `12V_PROTECTED` and
one global `POWER_GND` label at the child authority boundary, so native XML has
one root power net rather than `/REGULATORS/...` aliases. The three internal
VCC pins are isolated as `VCC_U3_INTERNAL`, `VCC_U4_INTERNAL`, and
`VCC_U5_INTERNAL`; the regression is
`validation/phase3/test_phase15_regulator_net_authority.py`.

The reproducible COUT floor calculation is
`validation/phase3/phase15_capacitance_check.py`; it verifies the schematic
authority counts against the TI minimum effective values using the documented
90% Rev-A derating floor. The comparison against the TI qualitative placement
authority is recorded in `PHASE15_TI_LAYOUT_OVERLAY.md`. That comparison is
not a thermal simulation and does not claim exact geometric equivalence.

`validation/phase3/phase15_thermal_screen.py` supplies the conservative
design-envelope thermal screen: at 50 C ambient and 90% efficiency it leaves
19.8 C, 50.7 C, and 71.0 C to TI's 125 C junction limit for U3/U4/U5. This
uses TI's 33.1 C/W reference metric and is not a board-specific thermal proof.

This does not close Phase 15. Remaining required work is localized VIN and
VOUT high-dI/dt routing, switch-node containment, exact-part DC-bias evidence,
and board-specific thermal/overlay closure for each rail.
