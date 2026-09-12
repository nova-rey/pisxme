# Phase 24 integrated power/return native census — 2026-09-12

## State and provenance

- Candidate state: **validation result** for the integrated PCB, not a producer
  candidate and not a closure claim.
- Source commit: `09c15cf8f18c82e2a2a47aeddd33df4da774385d`.
- PCB: `pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`.
- PCB SHA-256: `26b8b032cb46895c62af267af46f1bbe2bb3c9f7f689ea8fdba41e74d16effd5`.
- Qualified worker: `/home/nyx/pisxme-eda-workers/scripts/pisxme-worker validate`.
- Image: `pisxme-kicad-light:v1`.
- Image digest: `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`.
- KiCad: `10.0.6`.

## Native checker command and result

The fresh detached Light checkout ran:

```text
kicad-cli pcb drc --format json --severity-all --exit-code-violations \
  -o /workspace/output/power-drc.json \
  /workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb
```

Return code was `5` because violations were present. Native DRC reported **314
violations** and **499 unconnected items**. Violation classes were:

| class | count |
|---|---:|
| clearance | 138 |
| track_width | 118 |
| copper_edge_clearance | 16 |
| holes_co_located | 9 |
| track_dangling | 9 |
| via_dangling | 7 |
| courtyards_overlap | 6 |
| pth_inside_courtyard | 5 |
| tracks_crossing | 2 |
| silk_over_copper | 2 |
| lib_footprint_issues | 2 |

There were **0 `shorting_items`** in this run. The five configured ignored checks
remain findings requiring explicit Phase 24 disposition: `missing_courtyard`,
`track_not_centered_on_via`, `tuning_profile_track_geometries`,
`footprint_filters_mismatch`, and `footprint_type_mismatch`.

## Native PCB object census

The committed PCB serialization was parsed by
`validation/phase24_power_return_census.py` without modifying it. Counts below
are physical serialized objects, not continuity or current-capacity proof.
Segment lengths are the sum of straight-segment lengths for that net.

| net | pads | segments | length (mm) | vias | zones/layers |
|---|---:|---:|---:|---:|---|
| `12V_IN_A` | 8 | 3 | 228.5762 | 1 | 0 |
| `12V_IN_B` | 7 | 0 | 0 | 0 | 0 |
| `FUSED_12V_A` | 8 | 7 | 66.9900 | 1 | 0 |
| `FUSED_12V_B` | 7 | 0 | 0 | 0 | 0 |
| `12V_PROTECTED` | 151 | 6 | 23.6000 | 1 | 0 |
| `POWER_GND` | 325 | 47 | 173.4916 | 17 | 3 (`F.Cu`, `In1.Cu`, `In4.Cu`) |
| `CM5_5V` | 16 | 38 | 234.0291 | 9 | 0 |
| `BRIDGE_3V3` | 19 | 0 | 0 | 0 | 0 |
| `BRIDGE_1V1` | 32 | 0 | 0 | 0 | 0 |
| `STORAGE_3V3` | 18 | 22 | 76.0292 | 4 | 0 |
| `JMS_AVDD33` | 2 | 3 | 19.7000 | 2 | 0 |
| `JMS_AVDDL` | 18 | 7 | 53.7785 | 4 | 0 |
| `JMS_VCCO` | 7 | 4 | 30.8500 | 0 | 0 |
| `JMS_VDDREG_5V` | 4 | 4 | 11.4121 | 2 | 0 |

The `POWER_GND` zones are one named full-board F.Cu zone
`REV_A_TOP_POWER_GND_RETURN_FULL` plus unnamed In1.Cu and In4.Cu zones. Their
presence does not establish a connected return: the same native run reports
171 `POWER_GND` unconnected items and 44 DRC violations touching
`POWER_GND` (37 clearance, 6 co-located holes, 1 silkscreen-over-copper).

The most consequential physical gaps are:

- Branch B has no serialized `12V_IN_B` or `FUSED_12V_B` copper/vias.
- `12V_PROTECTED` has only 6 short segments and 1 via for 151 pads, including
  130 J1 power contacts; its native run reports 146 unconnected items.
- `BRIDGE_3V3` and `BRIDGE_1V1` have no serialized segments/vias; their native
  unconnected counts are 18 and 31 respectively.
- `CM5_5V` has copper objects but still has 2 native unconnected items and 19
  DRC violations touching the net (8 edge-clearance, 5 dangling vias, 4
  dangling tracks, 1 clearance, 1 silkscreen-over-copper).
- Storage local rail objects remain scoped evidence only: `STORAGE_3V3` has 8
  native unconnected items and 12 DRC violations touching it.

## Power/thermal acceptance disposition

This receipt closes no Phase 24 acceptance row. It establishes a corrected,
current integrated object census and the fresh native DRC evidence needed to
queue repair. It does not prove physical continuity, route current capacity,
voltage drop, transient/inrush response, regulator loss, connector/fuse
sharing, thermal rise, or cooling behavior.

The existing design-envelope records remain applicable but unresolved: the
budget allows 300 W nominal / 330 W peak V100 power and 28.5 A continuous /
34.3 A peak input with two 15 A branches. Those are design allowances, not
measurements. The regulator overlay and conservative thermal screen in
`PHASE24_REGULATOR_LAYOUT_RECEIPT.md` remain scoped Phase 15 evidence and do
not close this integrated Phase 24 row. The next power-owned action is a
bounded, pad-aware integrated repair of branch B, protected 12 V distribution,
and regulator/return corridors, followed by fresh Light validation; current,
transient, and thermal evidence must then be added against the same integrated
SHA.
