# Phase 24 Path-A SATA escape repair — rejected 2026-09-06

## Classification

`ROUTE_IMPLEMENTATION_FAILURE`. These disposable native experiments did not
change the selected storage architecture, production CAD, or committed mono2
author.

## Experiments

| Candidate | Native DRC findings | Result |
|---|---:|---|
| `PHASE24_U7_REPAIRED_ESCAPES_20260906` | 22 | Rejected |
| `PHASE24_U7_REPAIRED_ESCAPES_V2_20260906` | 23 | Rejected |

The first variant introduced an RX_P-to-U7 power-ground short and TX pair
crossing near the U7 oscillator field. The second moved the TX vias and put
RX_P on B.Cu, but introduced additional crossings and shorts against U7
BRIDGE_1V1/VSSOSC/XO/RX_N geometry. Neither is evidence that the storage
architecture or macro-floorplan is impossible.

## Decision

Both candidates are preserved as raw reports and rejected. The author
`phase24_storage_sata_pair_corridor.py` was restored to the committed mono2
source-order baseline. The next repair must use coordinated QFN escape
channel allocation around the actual pad field, rather than isolated via
translation.
