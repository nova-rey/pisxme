# Phase 24 USB3 shifted escape V121 receipt

V121 is a disposable J7/U12-only fixture derived from the alias-clean V116
storage board. It uses explicit CM5IO-style shifted source dogbones, separated
ordinary through-vias, a B.Cu corridor, and short F.Cu U12 launches. The
source transitions were adjusted so RX-P clears RX-N's via and TX-P exits on
the opposite side of the TX-N corridor.

Evidence:

- J7.128/130/140/142 map to U12.16/15/12/11 respectively.
- Native KiCad DRC: 0 violations; 63 unconnected pads are intentionally
  present in the J7/U12-only fixture because local support/ground copper was
  removed.
- Native `BuildConnectivity()` audit: all four USB3 endpoints PASS.
- Negative control removed one saved RX-N segment; the same audit failed at
  J7.128, proving the audit derives connectivity from saved copper rather than
  expected edges.

V121 is a successful isolated route-development candidate, not integrated
  Phase 18/24 closure. Its next use is as a source-escape template for the
  storage island, with obstacle-aware local continuation and full-board DRC.
