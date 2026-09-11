# Phase 24 schematic ERC classification — 2026-09-11

## Corrected generator discriminator — 2026-09-11

After transforming the legacy direct-root links with the same native-grid
coordinate map, the fresh generated hierarchy reports 110 native ERC
findings: 59 scaffold `unconnected_wire_endpoint`, 41 scaffold
`isolated_pin_label`, and 10 library-symbol warnings. It reports zero
`pin_not_connected` and zero `endpoint_off_grid` findings. This demonstrates
that the contract family and direct root links can be serialized coherently.
The residual scaffold warnings are not a production pass; live child
circuitry and project-specific symbol authorities still require a controlled
merge and comparison.

## Current evidence

Native KiCad 10.0.5 ERC on the canonical clean root after the library and
footprint namespace repairs reports 872 warnings and 0 errors. The class
counts in `PHASE24_CLEAN_SCHEMATIC_ERC_FOOTPRINTS_REPAIRED.rpt` are:

| Class | Count | Current disposition |
|---|---:|---|
| `endpoint_off_grid` | 416 | Open source-authoring investigation |
| `isolated_pin_label` | 232 | Open; distinguish contract labels from real omissions |
| `unconnected_wire_endpoint` | 147 | Open; correlate with hierarchy wiring |
| `same_local_global_label` | 30 | Open; do not remove without proving net ownership |
| `multiple_net_names` | 24 | Open; review intentional NC/ground aliases |
| `no_connect_dangling` | 11 | Open; review against actual unused pins |
| `no_connect_connected` | 9 | Open; likely contradictory annotations, not waived |
| `lib_symbol_mismatch` | 3 | Open: two standard power symbols and one Ethernet contract |

The footprint-link and missing-library-symbol classes are absent after the
namespace repairs. No ERC severity was changed or waived.

## Source correlation

`phase3_scaffold.py` emits contract labels and root connections at 3 mm
intervals (`10 + index * 3` and `45 + row * 30 + 2 + index * 3`) and places
sheet anchors at metric coordinates such as 35/45 mm. The native report’s
repeated off-grid locations at 25/60/95/130 mm and y=47, 50, 53 ... match
those generated root connections. The child ERC report independently shows
the same generated contract labels at 5 mm, y=10, 13, 16 ... . This is strong
evidence of an authoring/grid defect, not proof that every off-grid finding is
safe to snap.

The root generator’s second-row wire expression uses `row * 30` while
`sheet_block()` uses `row * 65`; this is a separate hierarchy-wiring defect
candidate. It must be tested on a disposable copy before any production source
change.

## Next discriminating experiment

Create a disposable root/child copy that changes only generated contract and
sheet-connection geometry to a consistent native KiCad grid and corrects the
root row-pitch expression. Run native reopen/ERC and compare connectivity and
netlist against the current canonical source. Do not quantize actual child
circuit geometry or remove labels/no-connect flags until that experiment
separates grid/wiring artifacts from genuine electrical findings.

This classification is evidence only; it does not close the Phase 24 ERC gate.

## Discriminator result — 2026-09-11

Two disposable probes were run with native KiCad 10.0.5 ERC:

| Probe | Result | Interpretation |
|---|---:|---|
| broad root coordinate snap | 1132 violations | independent root snapping detached hierarchy-associated geometry |
| child contract label/wire snap | 946 violations, including 56 `pin_not_connected` | child geometry cannot be changed without regenerating the embedded contract symbol pin pitch |

The first probe is retained only as a failed discriminator. The second probe
included the project/library namespace and still failed. Neither probe
modified the canonical source. The evidence rejects coordinate-only repair.
The next valid experiment is a coherent generator-level regeneration of the
contract symbol definition, child contract geometry, and parent sheet
connection geometry, followed by native hierarchy reopen/ERC and netlist
comparison.

## Coherent generator probe — 2026-09-11

The generator source was updated in the disposable authoring path to use
2.54 mm contract pitch and native-grid sheet anchors. A fresh generated
hierarchy produced 341 native ERC findings, including only 9
`endpoint_off_grid` findings, but 59 `pin_not_connected` findings. The
remaining disconnects are attributable to direct root links still using the
old metric sheet coordinates; those links are not yet transformed by the
same mapping. The source correction is therefore an unpromoted intermediate
checkpoint, not a closure of the production ERC gate.
