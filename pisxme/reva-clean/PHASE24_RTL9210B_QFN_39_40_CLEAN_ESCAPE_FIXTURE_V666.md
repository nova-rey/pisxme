# RTL9210B U1.39/U1.40 DFM discriminator V666

Checked 2026-09-09. Disposable geometry fixture only; no production CAD was
changed.

The fixture retains the actual audited `RTL9210B-CG_QUALIFICATION` QFN-68
footprint and tests U1.39 (`RTL_3V3`) and U1.40 (`RTL_1V1`) as two separated
F.Cu exits. The endpoints use rotated local SMD resistor pads placed outside
the QFN field. No via is placed between the adjacent QFN pads. Width remains
0.20 mm; no clearance, via, layer, or severity rule was changed.

Native KiCad 10.0.5 DRC on
`PHASE24_RTL9210B_QFN_39_40_CLEAN_ESCAPE_FIXTURE_V666.kicad_pcb`:

- 0 violations;
- 0 unconnected items;
- 0 footprint errors.

This closes the narrow claim that U1.39/U1.40 cannot be escaped under the
ordinary-via contract. It does not close the complete RTL9210B source-field
allocation: the integrated candidate must still co-author the remaining QFN
rails, USB, SPI, clock, controls, lane 0, and support returns and pass native
DRC/connectivity. V663, V664, and the first V665 allocation remain rejected
route evidence; V666 is a package/DFM discriminator, not full Path-B closure.
