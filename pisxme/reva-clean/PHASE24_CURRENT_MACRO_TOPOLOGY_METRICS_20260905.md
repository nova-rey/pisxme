# Phase 24 current selected macro topology metrics

Basis: `PHASE24_SELECTED_MACRO_ETH_SUPPORT_V15_LOCAL.kicad_pcb` (native KiCad load).

This supplemental table closes the provenance gap in the whole-board discriminator. It uses the selected candidate with the complete translated CM5IO Ethernet support island. Metrics are transformed native pad topology only; existing copper, DRC maturity, and route completeness are excluded.

| island | source centroid | island centroid | Euclidean centroid distance | Manhattan centroid distance | nearest endpoint pad | same-net source-to-island ratsnest |
|---|---:|---:|---:|---:|---:|---:|
| Ethernet complete | (34.50,99.90) | (15.86,130.05) | 35.45 mm | 48.79 mm | 6.63 mm | 97.45 mm |
| Storage complete | (70.04,105.30) | (123.53,125.30) | 57.10 mm | 73.49 mm | 24.20 mm | 145.11 mm |
| PCIe/V100 | (69.60,101.50) | (150.00,90.00) | 81.22 mm | 91.90 mm | 55.39 mm | 490.82 mm |
| SERVICE USB2 | (66.96,99.30) | (46.88,100.00) | 20.09 mm | 20.78 mm | 8.54 mm | 17.13 mm |
| Power input/protection | n/a | (72.43,76.91) | n/a | n/a | n/a | n/a |
| Regulator/load delivery | n/a | (173.33,125.00) | n/a | n/a | n/a | n/a |

## Interpretation

The selected candidate is the basis for route development, not a production pass. The complete Ethernet support references are included in the island centroid and ratsnest calculation; the complete storage island includes bridge, M.2, clock, reset, and local support references.

This report answers floorplan question A only. It does not use the current candidate's immature DRC/open count to reject the topology. Route implementation question B remains separately gated by native connectivity, DRC, pair geometry, references, mechanics, and full-board validation.

`CURRENT_MACRO_TOPOLOGY_METRICS = COMPLETE`
