# R3 structural unblocker result

- Outcome: `SELF_UNBLOCK`.
- Clone: 1040 DRC / 391 opens; native lanes: 1120 / 379; focused P2: 961 / 434.
- No result proves the MPA corridor impossible; previous attempts used translated or fixed hand-placed geometry and older bases.
- Next method: exact SHA `57332e98`, topology-first incremental synthesis with pcbnew connectivity and occupancy checks. Prove one branch using actual pad/net graphs and conflict-aware via/escape placement; reserve it before expanding remaining unique In2/In4 lanes.
- Preserve MPA anchors, corridor masks, six layers, branch independence, and <=8.50 mOhm path.
- Validation: reversible one-branch experiment first; then exact-SHA fresh Light, nine-branch census, unique-lane/F.Cu-clip proof, native DRC, resistance/thermal extraction.
