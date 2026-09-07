# Path-B crystal V11 native audit

Fixture: `PHASE24_RTL9210B_CRYSTAL_V11.kicad_pcb`

The audit uses KiCad's saved pads/tracks/vias and `BuildConnectivity()`;
expected endpoint sets are assertions only and do not provide graph edges.

- `XTAL_IN`: U1.53, Y1.1, C1.1 — PASS
- `XTAL_OUT`: U1.54, Y1.2, C2.1 — PASS
- `RTL_1V1`: U1.16/U1.36/U1.40/U1.50/U1.55/U1.60/U1.63, C4.1 — PASS
- negative control removing XTAL_OUT copper — PASS (audit fails as required)
- native DRC: 6 violations / 25 unconnected items
- production CAD: unchanged; V11 remains disposable
