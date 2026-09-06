# Phase 24 whole-board functional-island floorplan discriminator

Baseline: `PHASE24_U7_3V3_CURRENT_LOCAL.kicad_pcb` (native-loaded integrated candidate; SHA-256 `48840a9e353249f43853547a891c5588cdc5254fd771ac7ddfdb21efaddd058e`).
This is a placement/ratsnest topology comparison. Existing copper and DRC counts are excluded from ranking because historical routing maturity is not floorplan evidence.

## Native CM5 launch map

| functional group | native J7 pads | launch centroid (mm) | actual launch side |
|---|---|---:|---|
| Ethernet | 3, 4, 5, 6, 9, 10, 11, 12 | (34.50, 99.90) | B.Cu |
| PCIe/V100 | 109, 110, 112, 116, 118, 122, 124 | (69.60, 101.50) | B.Cu |
| USB3/storage | 128, 130, 140, 142 | (70.04, 105.30) | B.Cu |
| SERVICE USB2 | 103, 105 | (66.96, 99.30) | B.Cu |

## Current island map

| island | refs | centroid (mm) | source distance (mm) | nearest pad (mm) | topology observations |
|---|---|---:|---:|---:|---|
| Ethernet | U6, U9, J2 | (77.76, 59.56) | 59.15 | 50.70 | J2 is remote from GBE launch; west/power/SERVICE corridors intervene. |
| PCIe/V100 | J1 | (150.00, 90.00) | 81.22 | 55.39 | J1 is the sensitive validated anchor; retain unless global evidence forces bounded regeneration. |
| USB3/storage | U7, J3, C16, C17, C19, C30, C31, C32, C33, Y1, R23, C42, C43 | (130.65, 131.04) | 65.85 | 19.76 | U7/J3/clock are remote from USB3 launch and compete with SATA/PCIe/power corridors. |
| SERVICE USB2 | J4, U8 | (46.88, 100.00) | 20.09 | 8.54 | J4 is already the natural local endpoint for the right-side USB2 launch. |

### Non-signal islands

| island | current refs/region | native body/assembly constraint | floorplan finding |
|---|---|---|---|
| Power input/protection | J5/J6, F1/F2, U1/U2, Q1/Q2 | connector access, fuse service access, high-current copper and returns | real corridor occupant; do not rank as empty acreage or move piecemeal |
| Regulator/load delivery | U3/U4/U5 plus local support | vendor-reference component relationships, thermal/current paths, return access | coherent islands must remain intact; they compete with remote Ethernet/storage corridors |
| V100/SXM2/cooling | J1 plus SXM2/mechanical reservation | actual module/connector and approved topside cooler reservation | PCIe endpoint and mechanical anchor; not a generic underside keepout |

## Placement-only candidate comparison

| candidate | Ethernet distance (mm) | storage distance (mm) | SERVICE distance (mm) | PCIe changed? | expected topology |
|---|---:|---:|---:|---|---|
| `CURRENT` | 58.4 | 59.1 | 18.6 | no | baseline; remote Ethernet/storage corridors |
| `ETH_WEST_LOCAL_STORAGE` | 16.6 | 37.3 | 18.6 | no | best joint migration: local GBE neighborhood, USB3-side storage, PCIe/SERVICE retained |
| `ETH_WEST_OUTBOARD_STORAGE_CLEAR` | 31.9 | 52.8 | 18.6 | no | clears west Ethernet and moves complete storage support as a coherent pair |
| `ETH_WEST_CLEAR_STORAGE_MID` | 31.9 | 45.6 | 18.6 | no | keeps Ethernet clear of west power bodies while co-locating the complete storage island |
| `CM5_NEIGHBORHOODS` | 4.9 | 41.6 | 10.7 | no | shortest Ethernet but displaces solved SERVICE endpoint |
| `SWAP_ETH_STORAGE` | 20.9 | 39.0 | 18.6 | no | improves both interfaces but less than selected joint migration |
| `STORAGE_LOCAL_CLEAR` | 58.4 | 51.3 | 18.6 | no | improves storage only; leaves Ethernet remote |

## Same-net ratsnest topology metric

For each source pad, the metric connects it to the nearest same-net pad in the listed endpoint island. It is computed from saved native pads only; no tracks, vias, synthetic edges, or prior route quality enter the comparison.

| candidate | Ethernet same-net sum (mm) | PCIe/V100 same-net sum (mm) | USB3/storage same-net sum (mm) | SERVICE same-net sum (mm) |
|---|---:|---:|---:|---:|
| `CURRENT` | 443.9 | 490.8 | 231.2 | 17.1 |
| `ETH_WEST_LOCAL_STORAGE` | 88.7 | 490.8 | 116.5 | 17.1 |
| `ETH_WEST_OUTBOARD_STORAGE_CLEAR` | 97.4 | 490.8 | 192.0 | 17.1 |
| `ETH_WEST_CLEAR_STORAGE_MID` | 97.4 | 490.8 | 145.1 | 17.1 |
| `CM5_NEIGHBORHOODS` | 101.3 | 490.8 | 116.5 | 17.1 |
| `SWAP_ETH_STORAGE` | 127.7 | 490.8 | 103.2 | 17.1 |
| `STORAGE_LOCAL_CLEAR` | 443.9 | 490.8 | 192.0 | 17.1 |

## Newly introduced native body-bbox overlaps

This is a conservative collision screen, not a replacement for final courtyard/3D review. Only overlaps newly introduced by a moved candidate are listed.

| candidate | new overlap pairs | disposition |
|---|---|---|
| `CURRENT` | none | no new bbox overlap in this screen |
| `ETH_WEST_LOCAL_STORAGE` | J2/Q2, J2/U2 | reject exact coordinates |
| `ETH_WEST_OUTBOARD_STORAGE_CLEAR` | none | no new bbox overlap in this screen |
| `ETH_WEST_CLEAR_STORAGE_MID` | none | no new bbox overlap in this screen |
| `CM5_NEIGHBORHOODS` | J2/Q2, J2/U2 | reject exact coordinates |
| `SWAP_ETH_STORAGE` | none | no new bbox overlap in this screen |
| `STORAGE_LOCAL_CLEAR` | none | no new bbox overlap in this screen |

## Decision

`MACRO_FLOORPLAN_REVIEW = COMPLETE`. The conceptual winner remains the Ethernet-west/storage-local migration, but the exact earlier `ETH_WEST_LOCAL_STORAGE` coordinates are rejected by the independent native bbox review because they overlap `C4/Q2/U2`, `U2`, and `C17`. The corrected candidates retain the same topology while moving coherent bodies clear of those verified obstacles; `ETH_WEST_CLEAR_STORAGE_MID` is the preferred next routing basis, with `ETH_WEST_OUTBOARD_STORAGE_CLEAR` as the lower-risk fallback. `CM5_NEIGHBORHOODS` is not preferred because it trades away the solved SERVICE launch.

This decision answers floorplan question A only. It does not claim the selected candidate is routed. Any first-pass copper failure on the selected candidate is classified as `ROUTE IMPLEMENTATION FAILURE` until a fair native-pad, obstacle-aware routing cycle has been attempted; raw DRC comparison against the mature historical board is prohibited.

Next action: promote only the corrected collision-free candidate after a native courtyard/body review, then regenerate the affected Ethernet/storage/clock neighborhoods from native pad/net authority. This review answers floorplan question A; route development and native closure remain open.

## Comparison-bias correction — 2026-09-06

The earlier prose above is retained as historical review evidence, but its
`ETH_WEST_CLEAR_STORAGE_MID` preference was superseded by the later
six-candidate discriminator. That later discriminator uses the same native
CM5 launch map and adds the complete Ethernet support island, the complete
storage island, and a zero-overlap coarse major-body screen for the selected
candidate.

The current decision is therefore:

| decision | result |
|---|---|
| floorplan question A | `SWAP_ETH_STORAGE` selected on native transformed-pad topology |
| route question B | still open; affected USB3/SATA/clock copper has not passed |
| historical DRC comparison | prohibited for ranking |
| first-pass candidate DRC | implementation evidence only, not floorplan evidence |
| fallback | `ETH_WEST_CLEAR_STORAGE_MID`, if a valid routing cycle establishes a placement-inherent obstruction |

`SWAP_ETH_STORAGE` reduces the combined Ethernet and storage source distance
and same-net ratsnest burden relative to the current placement while keeping
PCIe, SERVICE, power, and regulator anchors unchanged. The candidate’s
immature DRC/open counts must not be compared directly with the mature
historical acreage board. A new route failure remains
`ROUTE IMPLEMENTATION FAILURE` until a competent native-pad, obstacle-aware
routing cycle demonstrates a structural macro-placement defect.

`MACRO_COMPARISON_BIAS_CONTROL = PASS`
