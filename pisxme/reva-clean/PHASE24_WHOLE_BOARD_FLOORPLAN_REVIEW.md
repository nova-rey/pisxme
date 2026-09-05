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
| USB3/storage | U7, J3, Y1, R23, C42, C43 | (132.11, 132.11) | 67.61 | 36.06 | U7/J3/clock are remote from USB3 launch and compete with SATA/PCIe/power corridors. |
| SERVICE USB2 | J4 | (45.00, 100.00) | 21.97 | 19.96 | J4 is already the natural local endpoint for the right-side USB2 launch. |

### Non-signal islands

| island | current refs/region | native body/assembly constraint | floorplan finding |
|---|---|---|---|
| Power input/protection | J5/J6, F1/F2, U1/U2, Q1/Q2 | connector access, fuse service access, high-current copper and returns | real corridor occupant; do not rank as empty acreage or move piecemeal |
| Regulator/load delivery | U3/U4/U5 plus local support | vendor-reference component relationships, thermal/current paths, return access | coherent islands must remain intact; they compete with remote Ethernet/storage corridors |
| V100/SXM2/cooling | J1 plus SXM2/mechanical reservation | actual module/connector and approved topside cooler reservation | PCIe endpoint and mechanical anchor; not a generic underside keepout |

## Placement-only candidate comparison

| candidate | Ethernet distance (mm) | storage distance (mm) | SERVICE distance (mm) | PCIe changed? | expected topology |
|---|---:|---:|---:|---|---|
| `CURRENT` | 59.2 | 67.6 | 22.0 | no | baseline; remote Ethernet/storage corridors |
| `ETH_WEST_LOCAL_STORAGE` | 16.9 | 51.0 | 22.0 | no | best joint migration: local GBE neighborhood, USB3-side storage, PCIe/SERVICE retained |
| `CM5_NEIGHBORHOODS` | 5.1 | 51.0 | 17.1 | no | shortest Ethernet but displaces solved SERVICE endpoint |
| `SWAP_ETH_STORAGE` | 22.5 | 52.6 | 22.0 | no | improves both interfaces but less than selected joint migration |
| `STORAGE_LOCAL` | 59.2 | 53.4 | 22.0 | no | improves storage only; leaves Ethernet remote |

## Same-net ratsnest topology metric

For each source pad, the metric connects it to the nearest same-net pad in the listed endpoint island. It is computed from saved native pads only; no tracks, vias, synthetic edges, or prior route quality enter the comparison.

| candidate | Ethernet same-net sum (mm) | PCIe/V100 same-net sum (mm) | USB3/storage same-net sum (mm) | SERVICE same-net sum (mm) |
|---|---:|---:|---:|---:|
| `CURRENT` | 443.9 | 490.8 | 231.2 | 40.0 |
| `ETH_WEST_LOCAL_STORAGE` | 88.7 | 490.8 | 116.5 | 40.0 |
| `CM5_NEIGHBORHOODS` | 101.3 | 490.8 | 116.5 | 30.1 |
| `SWAP_ETH_STORAGE` | 127.7 | 490.8 | 103.2 | 40.0 |
| `STORAGE_LOCAL` | 443.9 | 490.8 | 103.2 | 40.0 |

## Decision

`MACRO_FLOORPLAN_REVIEW = COMPLETE`. The topology winner is `ETH_WEST_LOCAL_STORAGE`: it materially reduces the two remote high-speed neighborhoods while preserving the PCIe and already-local SERVICE anchors. `CM5_NEIGHBORHOODS` is not preferred because it trades away the solved SERVICE launch for a smaller Ethernet centroid distance. `SWAP_ETH_STORAGE` is a useful alternative but is less favorable on both distances.

This decision answers floorplan question A only. It does not claim the selected candidate is routed. Any first-pass copper failure on the selected candidate is classified as `ROUTE IMPLEMENTATION FAILURE` until a fair native-pad, obstacle-aware routing cycle has been attempted; raw DRC comparison against the mature historical board is prohibited.

Next action: retain the selected topology, regenerate the affected Ethernet/storage/clock neighborhoods from native pad/net authority, then validate those routes and the unaffected PCIe/SERVICE/power islands separately.
