# RTL9210B QFN escape authority — V11

Source: native KiCad 10.0.5 load of
`PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V11_NATIVE_RSET.kicad_pcb`.
Raw coordinate receipt: `PHASE24_RTL9210B_QFN_ESCAPE_MAP_V11.txt`.

## Loaded footprint facts

- U1 is an 8 x 8 mm QFN-68 with 0.4 mm perimeter pitch.
- Perimeter pads are 0.2 x 0.9 mm on the top/bottom edges and 0.9 x 0.2
  mm on the left/right edges.
- The exposed pad is U1 pad 69, 4.8 x 4.8 mm at (80.000, 62.000).
- Power pads are interleaved with USB, SPI, clock, reset, and PCIe pads; a
  power escape cannot be treated as an unconstrained edge bus.

## Current loaded copper

- RTL_1V1 has one local source escape from U1 pad 36 through an ordinary
  0.6/0.3 mm via at (83.500, 56.800), then an outboard B.Cu route.
- RSET is separately proven from U1 pad 51 to R1.1 through the native V7
  oscillator route; its saved-board audit and negative control pass.
- Crystal and SPI routes are retained only where their saved-board audits
  pass; no map entry authorizes synthetic connectivity.

## Open authority boundary

The V11 native DRC remains 16 violations / 25 opens. The unresolved local
opens include RTL_1V1/RTL_3V3/RTL_5V QFN fanout and GND pad-field continuity,
plus intentionally incomplete PCIe and SSD-power fixture boundaries. These
are current native findings, not waived by the endpoint audits.

The V6, V7, V8, V9, and V10 serialized rail probes are rejected evidence;
their copper must not be promoted. The next candidate must use a
native/reference-derived QFN power escape or change the local support
footprint/placement within the isolated fixture. Production CAD and Path A
remain unchanged.
