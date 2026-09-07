# Phase 24 U7 rule-basis probe — 2026-09-06

## Purpose

This is a disposable native KiCad probe of the documented JLC multilayer
clearance capability. It tests whether the remaining U7 fixture findings are
being misclassified by the inherited 0.20 mm project netclass, without
changing production rules or suppressing DRC.

## Authority

- JLCPCB's current six-layer capability material documents fine multilayer
  trace/spacing capability, including 0.15 mm-class fabrication examples:
  <https://jlcpcb.com/resources/6-layer-pcbs>
- JLCPCB's capability reference is corroborating fabrication evidence, not a
  blanket waiver for every package or every assembly rule:
  <https://jlcpcb.com/capabilities/pcb-capabilities>
- TI's TUSB9261 Rev-I package drawing remains the component authority. It
  specifies PVP0064A HTQFP, 0.4 mm pitch, 1.2 x 0.2 mm package pad metal;
  see the local land-pattern receipt and the TI datasheet:
  <https://www.ti.com/lit/ds/symlink/tusb9261.pdf>

## Method

`phase24_set_fixture_rule_basis.py` loads the unchanged mono2 disposable
route, sets both the native board global minimum and the native default
netclass clearance to 0.15 mm, recomputes effective netclasses, and saves a
new disposable board. No production `.kicad_pro`, severity, exclusion, or
fabrication rule was changed.

## Results

| Probe | Native DRC findings | Real copper shorts | Real crossings | Fixture opens |
|---|---:|---:|---:|---:|
| Mono2, inherited 0.20 mm class | 12 | 2 | 1 | 38 |
| Mono2, explicit native 0.15 mm class | 7 | 2 | 1 | 38 |

The 0.15 mm basis removes the four U7 intrinsic-pad and socket-launch
clearance findings. It does not remove the TX dogbone short/crossing or the
RX_P-to-U7.45 short. Therefore this probe confirms a rule-basis distinction,
not a route PASS. The fixture remains rejected and no production route was
promoted.

## Files

- Author: `phase24_set_fixture_rule_basis.py`
- Disposable board: `PHASE24_U7_PROJECT_FOOTPRINT_ROUTE_RULE015_20260906.kicad_pcb`
- Raw native report: `PHASE24_U7_PROJECT_FOOTPRINT_ROUTE_RULE015_20260906-drc.rpt`
- Baseline comparison: `PHASE24_U7_PROJECT_FOOTPRINT_ROUTE_20260906-drc.rpt`

## Decision

The next Path-A repair must address the three remaining real copper defects
with native pad/net identity. The 0.15 mm capability is evidence for a future
reviewed rule basis, not permission to lower the integrated board's rule
globally. Package-specific land-pattern and assembly clearances remain gated
by manufacturer geometry and JLC assembly capability.
