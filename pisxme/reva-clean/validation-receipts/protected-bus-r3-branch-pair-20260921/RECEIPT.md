# Protected Bus R3 Complete Branch-Pair Microbatch

- Base: `99c8add7`
- Worker: `root-mediated-r3-branch-pair-20260921`
- Image/KiCad: `pisxme-kicad-light:v1` / `10.0.6`
- Scope: one source branch pair, J5/F1 and J6/F4, with ordered F.Cu positive escapes and distinct return vias; no J1/high-speed edits and no global rule changes.
- Producer DRC: 1012 violations, 433 unconnected items, exit code 5.
- Connectivity movement: one fewer unconnected item than the 434-item support-local checkpoint; DRC worsened by 30 compared with 982 gate-loop checkpoint.
- Result: candidate awaiting exact-SHA fresh validation; no integration claim.
- Fresh exact-SHA Light: 1014 violations, 433 unconnected items, exit code 5; candidate rejected for integration.
