# RTL9210B local fine-pitch QFN escape receipt

Date: 2026-09-10  
Candidate: `PHASE24_RTL9210B_FINE_QFN_ESCAPE_FIXTURE.kicad_pcb`  
Status: `FIXTURE_AND_INTEGRATION_PASS`

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
the first proof artifact. Those defects were corrected. The fresh DFM review
passes the saved fixture: courtyard contains the body, the pin-1 marker is
distinct, handoff courtyards are separated, and fine geometry is confined to
the named QFN escape nets/window. The accepted primitive is also applied to
the integrated V1603 support/launch without disturbing its downstream route.

## Integrated evidence

`PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb` contains exactly
six 0.15-mm source-departure segments, all inside the declared QFN window;
all remaining high-speed track segments are 0.20 mm and all vias remain
0.60/0.30 mm ordinary through-vias. Native DRC is 0/0/0. The integrated
saved-board audit passes six endpoint mappings, six trace-removal negative
controls, and the local-rule scope assertions.

Raw native DRC: `PHASE24_RTL9210B_FINE_QFN_ESCAPE_FIXTURE-drc.rpt`.  
Saved-board audit: `PHASE24_RTL9210B_FINE_QFN_ESCAPE_AUDIT.json`.
