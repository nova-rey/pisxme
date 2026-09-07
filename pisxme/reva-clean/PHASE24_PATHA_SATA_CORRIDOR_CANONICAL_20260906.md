# Phase 24 Path A SATA canonical-corridor trial — 2026-09-06

## Scope

Disposable route-development evidence only. Path A production schematic and
the accepted storage architecture were not changed by this trial.

## Corrections applied

- Socket-side nets use the live canonical names from `STORAGE.kicad_sch`.
- M-key lane-0 endpoints are J3.49/J3.47/J3.43/J3.41, not the obsolete
  J3.1–J3.4 assumptions.
- J3 placement/orientation is configurable for disposable experiments and
  post-transform pad coordinates are used for the final launch.
- U7 escape starts are derived from native U7 pads rather than stale guessed
  coordinates.
- Generated track and via net codes are written explicitly.

## Result

The assertion-only native endpoint audit passes all eight SATA endpoint pairs:

```
BRIDGE_SATA_TX_P U7.57 <-> C30.2       PASS
BRIDGE_SATA_TX_N U7.56 <-> C31.2       PASS
BRIDGE_SATA_RX_P U7.60 <-> C32.2       PASS
BRIDGE_SATA_RX_N U7.59 <-> C33.2       PASS
M2...TXP0       C30.1 <-> J3.49       PASS
M2...TXN0       C31.1 <-> J3.47       PASS
M2...RXP0       C32.1 <-> J3.43       PASS
M2...RXN0       C33.1 <-> J3.41       PASS
```

Native DRC still rejects the disposable fixture: 251 violations. The raw
report is `PHASE24_PATHA_SATA_CORRIDOR_CANONICAL_20260906-drc.rpt`. The
remaining errors are route-implementation failures in the trial (U7 escape,
local corridor crossings, and inherited support/USB obstacles); this is not
evidence against the canonical connector mapping or storage architecture.

The empty-routing-base variant also passes the eight endpoint assertions but
still fails native DRC with 71 violations. It is retained as a negative
comparison, not a candidate. No routed Path-A board was promoted.

The follow-up empty-routing-base fanout iteration, with separated native-pad
vertical escapes, reduced the isolated DRC result to 67 findings while
retaining the eight-endpoint audit PASS. It remains rejected: native DRC
identifies pair-corridor crossings and one local QFN escape interaction.
This is a route-implementation result, not a connector or architecture
result.

The next bounded experiment separated the TX pair onto B.Cu and the RX pair
onto F.Cu while preserving pair-local routing and the same rotated J3 launch.
The eight-endpoint audit remained PASS; native DRC reported 66 findings and
still rejected the trial because the independently authored corridors cross
in the shared storage acreage. This is retained as another rejected route
implementation, with no production promotion.

Finally, the same author was run against a minimal native fixture containing
only U7, C30–C33, and J3, with all inherited footprints, copper, and zones
removed. The eight-endpoint audit again passed. Native DRC improved to 59
findings, and the remaining errors are now directly attributable to the
trial's pair ordering around the U7/coupling row and the deliberate absence
of the other storage support connections. This isolates the problem as route
implementation/escape development; it does not reject the M-key authority or
the Path-A topology. Raw evidence is
`PHASE24_PATHA_MINIMAL_SATA_CORRIDOR_20260906-drc.rpt`.

The best current minimal-island candidate is the width-corrected, socket-lane
ordering trial `PHASE24_PATHA_MINIMAL_SATA_CORRIDOR_W020C_20260906.kicad_pcb`.
It uses the saved 0.20-mm minimum signal width, retains the eight-endpoint
audit PASS, and reduces the native DRC result to 14 findings. The remaining
findings are local U7 escape/corridor interactions, U7 footprint clearances,
and silkscreen warnings; the candidate is not yet promoted to production.

## Next action

Continue with a layer-separated, native-pad-derived U7 escape trial or a
proper interactive/native router on the disposable storage fixture. Promote
only a candidate that passes native DRC, the physical-connectivity audit, and
the existing pair/reference/mechanical gates.
