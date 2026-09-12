
## Phase 24 execution baseline evidence — 2026-09-12

The selected d0ef22b6 baseline was reproduced once in KiCad Light 10.0.6 using image sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9. Native ERC reported 355 findings; native DRC reported 440 violations and 265 unconnected items, with zero shorting_items. Native XML and hierarchy checks completed, and the bounded parity check recorded 814 schematic nodes, 1262 PCB pads, and zero mismatches. Raw reports and the receipt are retained under validation-receipts/baseline-d0ef22b6.

## Phase 24 integrated recheck — 2026-09-12

A fresh Light validation checkout at canonical commit 76873ea8 reproduced the integrated candidate result: 433 DRC violations and 265 unconnected items. This remains an open repair result, not a closure claim; the retained TUSB integrated receipt supplies the raw report for the same physical candidate lineage, while the current commit adds campaign evidence only.
