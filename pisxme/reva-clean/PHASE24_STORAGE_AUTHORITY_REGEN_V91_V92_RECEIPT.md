# Source-authority storage regeneration — 2026-09-10

V79 was not a valid current authority baseline: its U13 exposed pad 43 was
un-netted even though the reviewed generator assigns that package thermal pad
to `POWER_GND`. The source correction also assigns the nine J3 supply
contacts to the regulator-owned `STORAGE_3V3` rail.

## Results

* V91 (`PHASE24_STORAGE_AUTHORITY_REGEN_V91.kicad_pcb`) applies both reviewed
  pad/net ownership corrections to V79 without synthetic graph edges or
  copper. Native DRC: 596 violations / 350 unconnected items, with no
  shorting section.
* V92 (`PHASE24_STORAGE_AUTHORITY_FCU_V92.kicad_pcb`) adds a disposable,
  no-via F.Cu perimeter power corridor from existing `U14.5` to the three J3
  same-net contact groups. Native DRC: 597 violations / 341 unconnected
  items. The focused native power audit passes all 9 J3 contacts and its
  trace-removal negative control. USB3, SATA, and 814-node/1263-pad parity
  audits pass. V92 has one added crossing relative to V91 and is not yet a
  production ancestor.

V92 is the current disposable routing basis. It corrects the prior stale
  exposed-pad authority while providing actual M.2 power connectivity; the
  remaining crossing and full-board DRC/manufacturing gates stay open.
