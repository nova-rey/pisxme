# Phase 24 fresh whole-board functional-island floorplan review

Baseline: `PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb` (native-loaded integrated candidate).

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
| Ethernet | U6, U9, J2 | (77.76,59.56) | 59.15 | 50.70 |
| PCIe/V100 | J1 | (150.00,90.00) | 81.22 | 55.39 |
| Storage USB3/SATA | U7, J3, Y1, R23, C42, C43, C16, C17, C19, C30, C31, C32, C33 | (130.65,131.04) | 65.85 | 19.76 |
| SERVICE USB2 | J4, U8 | (46.88,100.00) | 20.09 | 8.54 |
| Power input/protection | J5, J6, F1, F2, U1, U2, Q1, Q2 | (72.43,76.91) | n/a | n/a |
| Regulator/load delivery | U3, U4, U5 | (173.33,125.00) | n/a | n/a |

## Topology-only candidate comparison

Distances and same-net ratsnest lengths are computed from native transformed pads only. They do not claim a candidate is routed. `ROUTE IMPLEMENTATION FAILURE` and `MACRO-PLACEMENT FAILURE` remain separate dispositions.

| candidate | Eth Euc | Eth Manhattan | storage Euc | storage Manhattan | PCIe Euc | service Euc | USB3 same-net | Eth same-net | moved body screen |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `CURRENT` | 59.2 | 83.6 | 65.9 | 86.4 | 81.2 | 20.1 | 231.2 | 443.9 | none |
| `ETH_LOCAL` | 32.7 | 44.5 | 65.9 | 86.4 | 81.2 | 20.1 | 231.2 | 97.4 | none |
| `STORAGE_LOCAL` | 59.2 | 83.6 | 39.1 | 46.6 | 81.2 | 20.1 | 69.1 | 443.9 | C42<->C15, J3<->C31, J3<->C32, J3<->C33, J3<->J1 |
| `ETH_LOCAL_STORAGE_LOCAL` | 32.7 | 44.5 | 39.1 | 46.6 | 81.2 | 20.1 | 69.1 | 97.4 | C42<->C15, J3<->C31, J3<->C32, J3<->C33, J3<->J1 |
| `ETH_LOCAL_STORAGE_CLEAR` | 32.7 | 44.5 | 43.8 | 60.2 | 81.2 | 20.1 | 88.1 | 97.4 | J3<->C23, J3<->C24, J3<->C25, J3<->C30, J3<->TP5, U7<->C16, U7<->C17 |
| `ETH_EAST_STORAGE_NORTH` | 152.8 | 178.0 | 73.4 | 96.0 | 81.2 | 20.1 | 257.5 | 1149.9 | J3<->J1, U7<->J1 |

## Functional-neighborhood findings

- J7 has two physically distinct launch regions: Ethernet pads at x≈32.96/36.04, y≈99.1–100.7, and PCIe/USB3/SERVICE pads at x≈66.96/70.04, y≈99.1–106.7. This is native pad geometry, not schematic drawing order.
- SERVICE is already adjacent to its right-side launch and is a poor exchange target.
- PCIe remains the most sensitive validated anchor; no candidate is allowed to invalidate it merely to improve a lower-priority neighborhood.
- The current Ethernet J2/U6/U9 group is remote from the actual GBE launch. The current storage group is remote from the actual USB3 launch. These are topology costs even where historical routing has been made to work.
- `ETH_LOCAL_STORAGE_LOCAL` is the explicit island-swap candidate: it places Ethernet in the left/source acreage and storage in the nearby central region while preserving PCIe, SERVICE, power, and regulator coordinates. It must receive a valid obstacle-aware routing cycle before any placement conclusion is drawn.
- `ETH_EAST_STORAGE_NORTH` is a connector-edge stress candidate; its long source paths make it a fallback, not a preferred topology.

## Discriminator decision

`MACRO_FLOORPLAN_DISCRIMINATOR = COMPLETE`
`CURRENT_CORRECTED` remains the historical integrated baseline only; the fresh topology study identifies `ETH_LOCAL_STORAGE_LOCAL` as the candidate that most directly tests the user-requested island swap. It is not promoted until its affected USB3/SATA/Ethernet routes are regenerated and validated.

The comparison deliberately does not use raw DRC counts from the mature baseline against first-pass candidate routing. A candidate route defect is a route implementation failure unless a valid routing-development cycle demonstrates a structural placement obstruction.
