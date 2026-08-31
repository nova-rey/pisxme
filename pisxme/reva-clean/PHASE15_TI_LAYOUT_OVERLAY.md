# Phase 15 TPSM63606 vendor-layout overlay

Status: `CLOSED_WITH_REV_A_EMPIRICAL_RISK`

## Authority

The authoritative layout guidance is TI `TPSM63606` revision B, SLVSGB4B,
pages 31–32 (sections 11.1 and 11.2). The preserved PDF is
`authority-inventory/primary-docs/TPSM63606.pdf`. The public EVM guide and
original Altium layout archive are also preserved as
`authority-inventory/primary-docs/power/TPSM63606_EVM_User_Guide.pdf` and
`TPSM63606_EVM_Layout_Files_SLVRBI7.zip`. They provide the dimensioned
reference board's copper, assembly, and stackup figures. TI requires:

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

The retained TI EVM package provides a useful quantitative sanity reference
without being treated as a coordinate overlay.  In the imported native EVM
board, U1 is at `(149.1401,102.862)` and its four VOUT capacitors C10--C13
are the documented `GRM32EC81C476ME15L` parts.  Their maximum regulator-to-
capacitor-center distance is 5.85 mm (the other three are 5.85, 3.42, and
3.43 mm).  This measurement is derived from the official TI layout archive
retained at `authority-inventory/primary-docs/power/TPSM63606_EVM_Layout_Files_SLVRBI7.zip`;
the imported board is a disposable measurement aid and is not a project
design artifact.
Archive SHA-256 is
`7ddcb1b8754445c99459b9e2eed72d6c4b833b3c0a7efcd6ad98f764ecffeb0c`.
The four-capacitor value and EVM placement guidance are also stated in the
official user guide retained as `TPSM63606_EVM_User_Guide.pdf`, including its
Figure 5-11 effective-capacitance example.

## Rev-A comparison

| TI requirement | U3 CM5 5 V | U4 bridge 3.3 V | U5 bridge 1.1 V | Evidence/status |
|---|---|---|---|---|
| VIN close and edge-escaped | yes | yes | yes | `phase15_power_escape.py`; focused native DRC |
| VOUT close and edge-escaped | yes | yes | yes; PG island offset left | `phase15_overlay_measure.py`; U5 bank in `phase15_u5_vout_bank.py` |
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

The native measurement audit is the reproducible geometry evidence for this
checkpoint. Its measured maximum regulator-to-capacitor-center distances are
recorded by the script output and must remain attached to any later routing
review; the U5 PG support island is offset left to preserve a compact output
bank without violating its control-route clearance.

Current measurements are U3 7.4 mm, U4 16.3 mm, and U5 51.7 mm, versus the
5.85 mm maximum measured on the TI EVM reference. U5's larger envelope is a
known Rev-A exception caused by the adjacent U7 pads and control island; it
is not presented as equivalent to the TI illustration. U4 is also outside
the EVM distance metric because its bank is offset to preserve the adjacent
U5 and U7 corridors.
Phase 15 closes with the measured native geometry comparison, calculated
nominal/effective-capacitance screen, and calculated design-envelope thermal
margin. The exact TDK DC-bias/temperature sum, U4/U5 constrained placement
envelopes, and board-specific thermal response are explicitly classified
`REV_A_EMPIRICAL_RISK`: the retained public authorities do not provide a
tabulated exact operating-point capacitance sum, and fabricated-board data is
outside the design-only gate. These risks are carried forward and do not
authorize later routing inside the accepted regulator keepouts.

Provenance: TI datasheet retained locally for design-reference use under TI
datasheet terms; all board observations are generated from native KiCad
candidate boards in this repository.
