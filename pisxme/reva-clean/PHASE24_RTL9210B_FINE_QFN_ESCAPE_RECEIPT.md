# RTL9210B local fine-pitch QFN escape receipt

Date: 2026-09-10  
Candidate: `PHASE24_RTL9210B_FINE_QFN_ESCAPE_FIXTURE.kicad_pcb`  
Status: `FIXTURE_PASS_PRODUCTION_INTEGRATION_OPEN`

## Accepted local rule

- Immediate U1 escape: 0.15 mm trace width and 0.15 mm copper clearance.
- Ordinary through-vias: 0.60 mm diameter / 0.30 mm drill; a smaller via was
  tested as unnecessary and is not used.
- Normal handoff and downstream routing: 0.20 mm traces/clearance.
- No via-in-pad, blind, buried, microvia, or plane-layer signal routing.

The local rule is width- and net-gated in the companion `.kicad_dru`, and the
saved-board scope guard proves that all ten 0.15-mm traces remain inside the
explicit QFN source window. Ten 0.20-mm handoff tracks are present.

## Native evidence

- KiCad 10.0.5 native DRC: 0 violations, 0 unconnected pads, 0 footprint
  errors.
- U1 source-to-handoff physical connectivity: 5/5 PASS.
- Actual trace-removal negative controls: 5/5 PASS.
- Full U1 package context is retained: 69 pads, exposed pad 69, body/silk,
  pin-1 marker, and courtyard geometry.
- JLCPCB current capability source and exact numerical basis are recorded in
  `authority-inventory/rtl9210b/RTL9210B_QFN_LOCAL_ESCAPE_MANUFACTURING_BASIS.md`.

The earlier DFM FAIL receipt is retained as historical evidence of defects in
the first proof artifact. Those defects were corrected; a fresh independent
DFM sign-off is still a release gate, as is applying this primitive to the
integrated support routing without disturbing V1603.

Raw native DRC: `PHASE24_RTL9210B_FINE_QFN_ESCAPE_FIXTURE-drc.rpt`.  
Saved-board audit: `PHASE24_RTL9210B_FINE_QFN_ESCAPE_AUDIT.json`.
