# Phase 5 power network implementation specification

Status: `IMPLEMENTATION_REQUIRED`

This specification is derived from the locally preserved TI datasheets
`authority-inventory/primary-docs/LM74700-Q1.pdf` (revision G) and
`authority-inventory/primary-docs/TPSM63606.pdf` (revision B). It is an
implementation contract, not a claim that the current four-pin schematic has
already implemented these networks.

## Dual 12 V input branches

Each mandatory cold-plug input is a separate branch:

`J5/J6 -> fuse -> TVS/protection review -> LM74700-Q1 -> external N-MOSFET -> 12V_PROTECTED merge`.

For the DBV six-pin LM74700-Q1 (`LM74700QDBVRQ1`), the exact mapping is:

| Pin | Name | Required connection |
|---:|---|---|
| 1 | VCAP | charge-pump capacitor to GND, placed at the controller |
| 2 | GND | quiet controller ground |
| 3 | EN | tie to ANODE for always-on cold-plug operation unless a deliberate enable circuit is approved |
| 4 | CATHODE | external MOSFET drain / protected side |
| 5 | GATE | external N-MOSFET gate |
| 6 | ANODE | raw fused input / external MOSFET source |

The external MOSFET is not internal to the controller. The selected Rev-A
candidate is TI `CSD19536KCS`; its source, drain, and gate must be wired to
ANODE, CATHODE, and GATE respectively, with the body-diode orientation
verified against the TI LM74700 OR-ing application. The current clean sheet is
missing this device and therefore cannot pass the power gate.

Fuse rating, TVS standoff/clamp choice, MOSFET SOA, inrush, branch sharing,
connector contact current, and protected-rail copper must be calculated for
the locked current-limited cold-plug supply. A 15 A fuse is not accepted by
name alone.

## TPSM63606 rails

Each `TPSM63606RDLR` is the exact 20-pin RDL package. Pin groups required in
the native symbol and footprint mapping are:

| Pins | Names | Required connection |
|---|---|---|
| 1, 16 | VIN1, VIN2 | protected input with local ceramic input capacitors |
| 2 | SW | short switch-node copper only; no external signal/component |
| 3, 4 | CBOOT, RBOOT | leave at the datasheet default unless slew-rate network is intentionally selected |
| 5 | VLDOIN | connect per datasheet bias recommendation and decouple as specified |
| 6, 11 | AGND | quiet analog ground, joined to PGND at the recommended point |
| 7 | VCC | internal control output; no external load |
| 8, 9 | VOUT1, VOUT2 | join to the selected rail and output capacitors |
| 10 | FB | feedback divider midpoint; never leave open or hard-ground |
| 12 | RT | frequency-setting resistor to AGND |
| 13 | PG | open-drain power-good with pull-up when used |
| 14 | EN/SYNC | explicit enable/UVLO policy; do not merge PG and enable |
| 15 | NC | no-connect or datasheet-approved ground treatment |
| 17–20 | PGND | power return and thermal current path |

The three rails are `CM5_5V` (U3), `BRIDGE_3V3` (U4), and `BRIDGE_1V1`
(U5). Each requires its own input/output capacitor set, feedback values,
RT value, enable policy, PG pull-up policy, thermal-via array, and vendor
layout overlay. U4/U5 must not be represented as TUSB9261 devices.

## Acceptance before Phase 14/15

- native symbols contain every package pin number exactly once, including LM
  pins 1–6 and TPSM pins 1–20;
- all external FETs, fuses, capacitors, feedback/RT/PG/EN parts, and selected
  TVS parts have exact MPNs and package footprints;
- netlist proves no raw 12 V reaches M.2 or low-voltage rails;
- current, voltage-drop, fuse, thermal, and effective-capacitance calculations
  are saved beside the schematic;
- native KiCad reopen/ERC, netlist export, and schematic↔PCB pad parity pass;
- only then may V100 power and regulator copper routing begin.
