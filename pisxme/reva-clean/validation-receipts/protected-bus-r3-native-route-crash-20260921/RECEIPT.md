# Protected-bus R3 native route attempt crash

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Base: canonical `1f02e202`
- Method: explicit native KiCad Light script adding nearest-neighbour copper/vias for raw, fused, and protected nets on In2/In3 with F.Cu launches
- Launcher: `pisxme-worker start kicad-light`
- Result: **implementation failure; process exited 139**
- Candidate: none; no output board was written

The attempt did not produce a candidate or validation result. No canonical CAD was modified. The crash is retained as evidence that the bulk automated spanning-tree authoring method is unsafe in this KiCad API context; it must not be replayed unchanged.
