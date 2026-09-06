# Phase 24 fresh whole-board functional-island floorplan review

Baseline: `PHASE24_U7_STORAGE_3V3_PAD24_CURRENT.kicad_pcb` (native-loaded integrated candidate).

This discriminator answers floorplan question A independently from route question B. Existing copper, historical DRC counts, and prior route maturity are excluded from ranking. All moved boards are disposable.

## Native CM5 carrier-mating launch map

| group | J7 pads / nets | launch centroid (mm) |
|---|---|---:|
| Ethernet | 3=CM5_GBE_TD3_P, 4=CM5_GBE_TD1_P, 5=CM5_GBE_TD3_N, 6=CM5_GBE_TD1_N, 9=CM5_GBE_TD2_N, 10=CM5_GBE_TD0_N, 11=CM5_GBE_TD2_P, 12=CM5_GBE_TD0_P | (34.50, 99.90) |
| PCIe/V100 | 109=/CORE_CM5/CM5_PERST, 110=/CORE_CM5/CM5_REFCLK_P, 112=/CORE_CM5/CM5_REFCLK_N, 116=/CORE_CM5/CM5_PER0_P, 118=/CORE_CM5/CM5_PER0_N, 122=/CORE_CM5/CM5_PET0_P, 124=/CORE_CM5/CM5_PET0_N | (69.60, 101.50) |
| Storage USB3/SATA | 128=/CORE_CM5/CM5_USB3_RX_N, 130=/CORE_CM5/CM5_USB3_RX_P, 140=/CORE_CM5/CM5_USB3_TX_N, 142=/CORE_CM5/CM5_USB3_TX_P | (70.04, 105.30) |
| SERVICE USB2 | 103=/CORE_CM5/SERVICE_USB2_DM, 105=/CORE_CM5/SERVICE_USB2_DP | (66.96, 99.30) |

## Current physical island map

| island | refs | centroid (mm) | source centroid distance (mm) | source-to-nearest-pad (mm) |
|---|---|---:|---:|---:|
| Ethernet | U6, U9, J2 | (18.48,128.42) | 32.71 | 6.63 |
| PCIe/V100 | J1 | (150.00,90.00) | 81.22 | 55.39 |
| Storage USB3/SATA | U7, J3, Y1, R23, C42, C43, C16, C17, C19, C30, C31, C32, C33 | (130.81,130.97) | 65.97 | 26.17 |
| SERVICE USB2 | J4, U8 | (46.88,100.00) | 20.09 | 8.54 |
| Power input/protection | J5, J6, F1, F2, U1, U2, Q1, Q2 | (72.43,76.91) | n/a | n/a |
| Regulator/load delivery | U3, U4, U5 | (173.33,125.00) | n/a | n/a |

## Topology-only candidate comparison

Distances and same-net ratsnest lengths are computed from native transformed pads only. They do not claim a candidate is routed. `ROUTE IMPLEMENTATION FAILURE` and `MACRO-PLACEMENT FAILURE` remain separate dispositions.

| candidate | Eth Euc | Eth Manhattan | storage Euc | storage Manhattan | PCIe Euc | service Euc | USB3 same-net | Eth same-net | moved body screen |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `CURRENT` | 32.7 | 44.5 | 66.0 | 86.4 | 81.2 | 20.1 | 231.2 | 97.4 | none (inherited overlaps excluded |
| `ETH_OUTBOARD` | 17.3 | 18.6 | 66.0 | 86.4 | 81.2 | 20.1 | 231.2 | 95.6 | C4<->J2, J2<->Q2, J2<->U2, U2<->U6 |
| `STORAGE_LOCAL` | 32.7 | 44.5 | 39.3 | 46.7 | 81.2 | 20.1 | 69.1 | 97.4 | C15<->C42, C16<->U7, C31<->J3, C32<->J3, C33<->J3, J1<->J3 |
| `STORAGE_LOCAL_CLEAR2` | 32.7 | 44.5 | 39.9 | 52.1 | 81.2 | 20.1 | 88.1 | 97.4 | none (inherited overlaps excluded |
| `STORAGE_LOCAL_J3_EDGE` | 32.7 | 44.5 | 50.1 | 65.3 | 81.2 | 20.1 | 88.1 | 97.4 | none (inherited overlaps excluded |
| `STORAGE_SOUTH_CLEAR` | 32.7 | 44.5 | 66.6 | 92.9 | 81.2 | 20.1 | 192.0 | 97.4 | J3<->MECH_M2_2280 |
| `STORAGE_CENTER_CLEAR` | 32.7 | 44.5 | 63.1 | 87.4 | 81.2 | 20.1 | 175.4 | 97.4 | J3<->MECH_M2_2280 |
| `ETH_OUTBOARD_STORAGE_LOCAL` | 17.3 | 18.6 | 39.3 | 46.7 | 81.2 | 20.1 | 69.1 | 95.6 | C15<->C42, C16<->U7, C31<->J3, C32<->J3, C33<->J3, C4<->J2, J1<->J3, J2<->Q2, J2<->U2, U2<->U6 |
| `ETH_OUTBOARD_STORAGE_LOCAL_CLEAR2` | 17.3 | 18.6 | 39.9 | 52.1 | 81.2 | 20.1 | 88.1 | 95.6 | C4<->J2, J2<->Q2, J2<->U2, U2<->U6 |
| `ETH_OUTBOARD_STORAGE_SOUTH_CLEAR` | 17.3 | 18.6 | 66.6 | 92.9 | 81.2 | 20.1 | 192.0 | 95.6 | C4<->J2, J2<->Q2, J2<->U2, J3<->MECH_M2_2280, U2<->U6 |
| `ETH_OUTBOARD_STORAGE_LOCAL_J3_EDGE` | 17.3 | 18.6 | 50.1 | 65.3 | 81.2 | 20.1 | 88.1 | 95.6 | C4<->J2, J2<->Q2, J2<->U2, U2<->U6 |
| `ETH_OUTBOARD_STORAGE_CENTER_CLEAR` | 17.3 | 18.6 | 63.1 | 87.4 | 81.2 | 20.1 | 175.4 | 95.6 | C4<->J2, J2<->Q2, J2<->U2, J3<->MECH_M2_2280, U2<->U6 |
| `ETH_OUTBOARD_STORAGE_CLEAR` | 17.3 | 18.6 | 43.9 | 60.3 | 81.2 | 20.1 | 88.1 | 95.6 | C16<->U7, C23<->J3, C24<->J3, C25<->J3, C30<->J3, C4<->J2, J2<->Q2, J2<->U2, J3<->TP5, U2<->U6 |
| `ETH_EAST_STORAGE_NORTH` | 152.8 | 178.0 | 73.6 | 96.2 | 81.2 | 20.1 | 257.5 | 1149.9 | J1<->J3, J1<->U7 |

## Functional-neighborhood findings

- J7 has two physically distinct launch regions: Ethernet pads at x≈32.96/36.04, y≈99.1–100.7, and PCIe/USB3/SERVICE pads at x≈66.96/70.04, y≈99.1–106.7. This is native pad geometry, not schematic drawing order.
- SERVICE is already adjacent to its right-side launch and is a poor exchange target.
- PCIe remains the most sensitive validated anchor; no candidate is allowed to invalidate it merely to improve a lower-priority neighborhood.
- The accepted baseline already has the Ethernet island in the left/source acreage, so the remaining topology question is storage placement, not another Ethernet relocation.
- The current storage group remains remote from the actual USB3 launch. `STORAGE_LOCAL`, `STORAGE_LOCAL_CLEAR2`, and the joint Ethernet/storage variants are topology candidates that shorten the storage source relationship; body overlaps are mechanical-screen findings, not route-quality scores.
- `STORAGE_LOCAL_J3_EDGE` is the next screened candidate: it moves U7 and all local support toward USB3 while retaining the already mechanically valid J3 edge position, avoiding the inherited PCIe/PERST corridor.
- `ETH_EAST_STORAGE_NORTH` is a connector-edge stress candidate; its long source paths make it a fallback, not a preferred topology.

## Discriminator decision

`MACRO_FLOORPLAN_DISCRIMINATOR = COMPLETE`
The topology-only comparison selects `STORAGE_LOCAL_J3_EDGE` as the next development basis because it shortens the bridge-side USB3 relationship while retaining J3's mechanically compatible edge position. It is not promoted until its affected USB3/SATA/clock routes are regenerated and validated.

The comparison deliberately does not use raw DRC counts from the mature baseline against first-pass candidate routing. A candidate route defect is a route implementation failure unless a valid routing-development cycle demonstrates a structural placement obstruction.
