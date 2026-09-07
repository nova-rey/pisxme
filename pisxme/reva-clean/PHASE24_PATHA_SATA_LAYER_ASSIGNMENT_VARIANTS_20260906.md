# Phase 24 Path-A SATA layer-assignment variants

Classification: rejected route experiments. The project-local U7 footprint
was used and all variants retained the native eight-endpoint audit PASS.

| Candidate | Bridge-layer change | DRC findings | Relevant classes | Disposition |
|---|---|---:|---|---|
| Baseline mono2 | TX B / RX F | 12 | 2 shorts, 1 crossing, 5 clearance, 4 silk; 38 fixture opens | Existing best reference |
| V2 | TX-P alternate B escape, RX-P moved F | 15 | 3 shorts, 2 crossings, 4 clearance, 2 mask, 4 silk; 38 opens | Reject |
| V3 | TX-P F, RX-P B | 11 | 0 shorts, 3 crossings, 4 clearance, 4 silk; 38 opens | Reject: zero-short result still violates no-crossing gate |
| V4 | TX-P long F escape, RX-P B | 13 | 2 shorts, 3 crossings, 4 clearance, 4 silk; 38 opens | Reject |

All results are disposable route-method evidence. The apparent V3 improvement
does not pass because three real copper crossings remain, and its corridors
are longer/less direct. The committed route author is restored to the mono2
baseline after the comparison; no production PCB changed.

Raw boards and DRC reports are retained as `...ROUTE_V2`, `...ROUTE_V3`, and
`...ROUTE_V4` artifacts. The next credible repair class must address the QFN
source escape as a coordinated obstacle-aware fanout, not repeat the same
two-layer assignment with longer dogbones.
