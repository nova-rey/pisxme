# Path-B RTL_5V native connectivity audit

Fixture: `PHASE24_RTL9210B_5V_PAD17_V3.kicad_pcb`

The audit derives connectivity from KiCad's saved pads, tracks, and vias via
`BuildConnectivity()` and asserts one native component containing U1.17,
U1.33, and C5.1 on `RTL_5V`.

Results:

- positive audit: PASS
- negative control: PASS; removing the pad-17 escape segment fails the audit
- fixture native DRC: 4 violations / 29 unconnected items, all inherited or
  unfinished support geometry; this audit does not waive those open gates
- production CAD: unchanged
