# Protected-bus R1-routed to R2 corridor attempt

- Isolated source: retained `protected-bus-producer-candidate-20260917` routed artifact
- Method change: apply MPA R2 F.Cu `POWER_GND` occupancy correction to the routed producer, then run native Light DRC
- KiCad: `10.0.6`
- Candidate path: `/home/nyx/eda-workspaces/protected_bus_source_r3_producer/project/pisxme/reva-clean/PHASE24_PROTECTED_BUS_R3_ROUTED_CANDIDATE.kicad_pcb`
- Native result: **314 DRC violations / 499 unconnected items**
- Result: **FAIL; not eligible for integration**

The routed predecessor contains obsolete topology and does not reconcile to the current canonical source contract. Applying the R2 corridor occupancy change alone does not close connectivity. This attempt is retained as evidence and triggers Unblocker review rather than another same-class route replay.
