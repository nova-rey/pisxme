# Phase 24 storage USB3 source-field V37

Checked 2026-09-09 from the filled V32 basis. This is a disposable Path-A
routing experiment; it does not replace the Path-A authority or close Phase
24.

V37 regenerates all four CM5 USB3 source departures together from the saved
J7 pad coordinates, preserves the existing ordinary through-vias and B.Cu
tails, and changes only the J7-side F.Cu source field. The TXN lane is moved
to x=70.5 mm and TXP to x=74.5 mm to clear the retained CM5_REFCLK via field.

Native KiCad 10.0.5 results on
`PHASE24_STORAGE_CM5_USB4_MONOTONIC_V37_FILLED.kicad_pcb`:

- 603 DRC violations;
- 399 unconnected pads;
- zero `[shorting_items]` entries;
- zero footprint errors;
- USB3 native endpoint audit: 10/10 PASS;
- SATA native endpoint audit: 12/12 PASS;
- mode-control native endpoint audit: 4/4 PASS;
- JMS583 physical endpoint audit: 7/7 PASS;
- schematic-to-PCB pad parity: PASS, zero mismatches.

The candidate removes the V36 CM5_REFCLK/USB3_TXN short without introducing a
new shorting class. It remains a route implementation basis because the
unconnected and inherited full-board Phase 24 debt is not closed. The native
report and generated PCB are retained as raw experiment evidence.

## Superseded status

V37 is not the current Path-A candidate. Rechecking V37 against the current
`PHASE24_STORAGE_MODE_J8.xml` gives ten pad-net mismatches, including stale J5
mode ownership and pre-normalization U12/U13 names. The current candidate is
`PHASE24_STORAGE_J8_V5_VBUS_V1.kicad_pcb`, which passes zero-mismatch parity
against that current XML. The V37 PCB and original receipts remain unchanged
for historical route comparison.

The preceding historical wording is superseded by the live recheck: V37
passes zero-mismatch parity against `PHASE24_STORAGE_MODE_J8.xml`. It remains
a valid disposable route candidate with 603 DRC violations, 399 opens, and
no shorting entries. The ten-mismatch result applies only to the superseded
`PHASE24_STORAGE_NATIVE_FINAL.xml` oracle.
