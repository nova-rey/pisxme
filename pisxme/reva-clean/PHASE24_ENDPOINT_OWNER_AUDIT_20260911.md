# Phase 24 residual endpoint-owner audit — 2026-09-11

The current canonical native ERC receipt is
`PHASE24_CLEAN_SCHEMATIC_ERC_REGULATOR_PIN_STUB_PROMOTED_20260911.rpt`.
It reports 197 `endpoint_off_grid` findings after the duplicate POWER_INPUT
wire repair. The pre-repair description census identified 66 horizontal
10 mm wires, 8 horizontal 3 mm wires, 4 horizontal 65 mm
wires, 2 horizontal 2.06 mm wires, and 121 symbol/label endpoints.

Native source inspection shows the root schematic contains 65 10 mm
sheet/contract wire objects; the regulator sheet's previously repeated 5 mm
and 1 mm unowned wire families have already been removed. The complete root
coordinate-grid probe preserved hierarchy and exact netlist parity but left
the ERC census unchanged, so the residual family is not a global root-x
offset defect.

## Current decision

The duplicate POWER_INPUT 3 mm wire family is now closed with exact native
netlist parity. The next repair must map each remaining symbol/label endpoint to its owning
instance and attached wire family, then transform one complete owner group in
a disposable native copy. Do not normalize root coordinates globally and do
not remove hierarchy wires without native netlist parity.
