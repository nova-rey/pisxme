# Phase 15 TPSM63606 vendor-layout overlay

Status: `IN_PROGRESS`

## Authority

The authoritative layout guidance is TI `TPSM63606` revision B, SLVSGB4B,
pages 31–32 (sections 11.1 and 11.2). The preserved PDF is
`authority-inventory/primary-docs/TPSM63606.pdf`. It requires:

- symmetric VIN capacitor placement close to VIN1/VIN2;
- localized top-side PGND return copper for VIN and VOUT capacitors;
- symmetric VOUT capacitor placement close to VOUT1/VOUT2;
- a wide lower-layer VOUT plane to the load;
- a short FB route and nearby feedback components;
- a solid ground plane directly below the module;
- PGND thermal vias into the adjacent ground plane; and
- enough copper to keep junction temperature below 150 C.

The TI figure is a qualitative placement authority, not a dimensioned CAD
file. The package land pattern and four central PGND lands are independently
closed by `TPSM63606_SUPPORT_AUTHORITY.md` and the native footprint receipt.

## Rev-A comparison

| TI requirement | U3 CM5 5 V | U4 bridge 3.3 V | U5 bridge 1.1 V | Evidence/status |
|---|---|---|---|---|
| VIN close and edge-escaped | yes | yes | yes | `phase15_power_escape.py`; focused native DRC |
| VOUT close and edge-escaped | yes | yes | yes | U5 bank in `phase15_u5_vout_bank.py`; U3/U4 escapes in same pipeline |
| localized capacitor PGND return | thermal PGND array | thermal PGND array | 16 dedicated local return vias | Phase 15 board candidates; native regression |
| lower-layer VOUT feed | pending final overlay audit | pending final overlay audit | In2.Cu trunk | route candidate, not final board closure |
| FB components close to FB | routed island | routed island | routed island | `test_phase15_u4_u5_controls.py` and U3 control regression |
| solid plane below module | POWER_GND plane | POWER_GND plane | POWER_GND plane | Phase 14 plane regression |
| thermal-via array | 4 PGND vias | 4 PGND vias | 4 PGND vias | `test_phase15_thermal_vias.py` |
| thermal margin to Tj <125 C | 19.8 C screen | 50.7 C screen | 71.0 C screen | `phase15_thermal_screen.py`; board-specific proof OPEN |

## Closure boundary

This document records the reproducible comparison and its limits. It does not
claim geometric equivalence to TI's illustrative figure. The thermal screen
uses 90% efficiency, 50 C ambient, and TI's conservative 33.1 C/W metric; the
metric is specified for a different 2-oz reference board, so board-specific
thermal closure remains `REV_A_EMPIRICAL_RISK` pending fabricated-board or
equivalent thermal evidence.
Phase 15 remains open until the final three-rail candidate has a measured
geometry overlay, exact effective-capacitance evidence or an explicitly
bounded `REV_A_EMPIRICAL_RISK`, and a calculated thermal margin for the
design-envelope currents.

Provenance: TI datasheet retained locally for design-reference use under TI
datasheet terms; all board observations are generated from native KiCad
candidate boards in this repository.
