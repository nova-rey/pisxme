# CM5/Ethernet edge DFM bounded attempt

Package: `P24-MECHANICS-CM5-ETHERNET-EDGE-DFM`
Base state: `b483f0776c6712dd1738cbf0d985f76556aaec2d` (dispatch recorded against queue base `c7c8cd88`)
Workspace: `/home/nyx/eda-workspaces/cm5-ethernet-edge-producer-20260918`
Worker: `cm5-ethernet-edge-producer-20260918`
Validation: KiCad Light `10.0.6`, `--refill-zones`, `--save-board` was used for this retained candidate receipt.

Producer scope: C48/C49/C50/C51 moved from y=180.0 to y=178.5; C8 moved y=170.5 to y=172.5; seven CM5_5V track segments and two CM5_5V vias moved to the y=177 local path. Protected bus and high-speed corridors were declared untouched in producer metadata.

Baseline refill DRC: 282 violations, 395 unconnected; classes `{"clearance": 120, "copper_edge_clearance": 15, "courtyards_overlap": 6, "pth_inside_courtyard": 5, "track_dangling": 9, "track_width": 118, "tracks_crossing": 2, "via_dangling": 7}`.
Candidate refill DRC: 275 violations, 395 unconnected; classes `{"clearance": 120, "courtyards_overlap": 5, "lib_footprint_issues": 2, "pth_inside_courtyard": 5, "track_dangling": 9, "track_width": 125, "tracks_crossing": 2, "via_dangling": 7}`.
Target result: all 8 C48-C51 copper-edge-clearance findings and the C7/C8 courtyard-overlap finding are absent in candidate DRC.
Unresolved candidate regression: candidate DRC reports 2 `lib_footprint_issues` (U6/U9) and 7 additional `track_width` findings relative to the retained baseline. Their provenance was not resolved within this bounded attempt; candidate is not authorized for canonical integration.

Return state: `BLOCKED` pending one bounded current-candidate revalidation/reconciliation of the new checker findings. No canonical CAD was changed and no candidate was integrated.
