# Phase 24 integrated native DRC receipt — V1559

Board: `PHASE24_PGND_CLUSTER_CURRENT.kicad_pcb`.

Command: KiCad 10.0.5 `kicad-cli pcb drc --format report`.

Result: **OPEN** — 443 native DRC violations and 254 unconnected items.
The raw report is `PHASE24_PGND_CLUSTER_CURRENT-V1559-drc.rpt`.

This result is independent of the U5 connectivity audit. U5 native
connectivity and its trace-removal negative control pass; the board still has
substantial inherited/local clearance, crossing, open, and support-field debt.
No DRC severity or validation rule was changed.
