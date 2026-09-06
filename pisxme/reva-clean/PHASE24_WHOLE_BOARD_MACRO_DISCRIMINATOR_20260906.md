# Phase 24 whole-board functional-island macro-floorplan discriminator

Native basis: `PHASE24_U7_3V3_CURRENT_LOCAL.kicad_pcb`. Candidate boards are disposable placement probes; no candidate copper is promoted.

The comparison deliberately excludes existing tracks, DRC counts, and completeness. Those answer route implementation question B, while this review answers whether the macro placement gives each functional circuit a natural physical neighborhood.

## Native CM5 launch map

| group | native source pads | launch centroid |
|---|---:|---:|
| Ethernet | 8 | (34.50, 99.90) |
| PCIe/V100 | 7 | (69.60, 101.50) |
| Storage USB3-SATA-M.2 | 4 | (70.04, 105.30) |
| SERVICE USB2 | 2 | (66.96, 99.30) |
| Power input/protection | n/a | n/a |
| Regulator/load delivery | n/a | n/a |

## Placement topology metrics

| candidate | island | island centroid | Euc. source distance | Manhattan source distance | nearest native pad | same-net ratsnest |
|---|---|---:|---:|---:|---:|---:|
| CURRENT | Ethernet | (77.8,59.6) | 59.2 | 83.6 | 50.7 | 443.9 |
| CURRENT | PCIe/V100 | (150.0,90.0) | 81.2 | 91.9 | 55.4 | 490.8 |
| CURRENT | Storage USB3-SATA-M.2 | (130.7,131.0) | 65.9 | 86.4 | 19.8 | 231.2 |
| CURRENT | SERVICE USB2 | (46.9,100.0) | 20.1 | 20.8 | 8.5 | 17.1 |
| CURRENT | Power input/protection | (72.4,76.9) | n/a | n/a | n/a | n/a |
| CURRENT | Regulator/load delivery | (173.3,125.0) | n/a | n/a | n/a | n/a |
| ETH_LOCAL_STORAGE_MID | Ethernet | (30.6,103.2) | 5.1 | 7.2 | 6.9 | 101.3 |
| ETH_LOCAL_STORAGE_MID | PCIe/V100 | (150.0,90.0) | 81.2 | 91.9 | 55.4 | 490.8 |
| ETH_LOCAL_STORAGE_MID | Storage USB3-SATA-M.2 | (115.5,124.9) | 49.5 | 65.1 | 19.8 | 116.5 |
| ETH_LOCAL_STORAGE_MID | SERVICE USB2 | (46.9,100.0) | 20.1 | 20.8 | 8.5 | 17.1 |
| ETH_LOCAL_STORAGE_MID | Power input/protection | (72.4,76.9) | n/a | n/a | n/a | n/a |
| ETH_LOCAL_STORAGE_MID | Regulator/load delivery | (173.3,125.0) | n/a | n/a | n/a | n/a |
| SWAP_ETH_STORAGE | Ethernet | (28.0,121.5) | 22.5 | 28.0 | 11.8 | 127.7 |
| SWAP_ETH_STORAGE | PCIe/V100 | (150.0,90.0) | 81.2 | 91.9 | 55.4 | 490.8 |
| SWAP_ETH_STORAGE | Storage USB3-SATA-M.2 | (115.5,124.9) | 49.5 | 65.1 | 19.8 | 116.5 |
| SWAP_ETH_STORAGE | SERVICE USB2 | (46.9,100.0) | 20.1 | 20.8 | 8.5 | 17.1 |
| SWAP_ETH_STORAGE | Power input/protection | (72.4,76.9) | n/a | n/a | n/a | n/a |
| SWAP_ETH_STORAGE | Regulator/load delivery | (173.3,125.0) | n/a | n/a | n/a | n/a |
| ETH_SOUTH_STORAGE_NORTH | Ethernet | (68.9,150.4) | 61.1 | 84.9 | 39.9 | 350.7 |
| ETH_SOUTH_STORAGE_NORTH | PCIe/V100 | (150.0,90.0) | 81.2 | 91.9 | 55.4 | 490.8 |
| ETH_SOUTH_STORAGE_NORTH | Storage USB3-SATA-M.2 | (129.4,83.7) | 63.2 | 81.0 | 19.8 | 191.8 |
| ETH_SOUTH_STORAGE_NORTH | SERVICE USB2 | (46.9,100.0) | 20.1 | 20.8 | 8.5 | 17.1 |
| ETH_SOUTH_STORAGE_NORTH | Power input/protection | (72.4,76.9) | n/a | n/a | n/a | n/a |
| ETH_SOUTH_STORAGE_NORTH | Regulator/load delivery | (173.3,125.0) | n/a | n/a | n/a | n/a |
| STORAGE_LOCAL | Ethernet | (77.8,59.6) | 59.2 | 83.6 | 50.7 | 443.9 |
| STORAGE_LOCAL | PCIe/V100 | (150.0,90.0) | 81.2 | 91.9 | 55.4 | 490.8 |
| STORAGE_LOCAL | Storage USB3-SATA-M.2 | (115.5,124.9) | 49.5 | 65.1 | 19.8 | 116.5 |
| STORAGE_LOCAL | SERVICE USB2 | (46.9,100.0) | 20.1 | 20.8 | 8.5 | 17.1 |
| STORAGE_LOCAL | Power input/protection | (72.4,76.9) | n/a | n/a | n/a | n/a |
| STORAGE_LOCAL | Regulator/load delivery | (173.3,125.0) | n/a | n/a | n/a | n/a |
| POWER_EAST_REGULATORS_WEST | Ethernet | (77.8,59.6) | 59.2 | 83.6 | 50.7 | 443.9 |
| POWER_EAST_REGULATORS_WEST | PCIe/V100 | (150.0,90.0) | 81.2 | 91.9 | 55.4 | 490.8 |
| POWER_EAST_REGULATORS_WEST | Storage USB3-SATA-M.2 | (130.7,131.0) | 65.9 | 86.4 | 19.8 | 231.2 |
| POWER_EAST_REGULATORS_WEST | SERVICE USB2 | (46.9,100.0) | 20.1 | 20.8 | 8.5 | 17.1 |
| POWER_EAST_REGULATORS_WEST | Power input/protection | (199.3,39.3) | n/a | n/a | n/a | n/a |
| POWER_EAST_REGULATORS_WEST | Regulator/load delivery | (163.3,125.0) | n/a | n/a | n/a | n/a |

## Coarse mechanical/corridor screen

The following is a screening metric only: native footprint body-box overlap among major islands after transforms. It is not a substitute for courtyard, 3-D, mating, or assembly review.

| candidate | body-box overlap area pairs | example pairs |
|---|---:|---|
| CURRENT | 0 | none |
| ETH_LOCAL_STORAGE_MID | 4 | U6/J4, U9/J4, J2/U2, J2/Q2 |
| SWAP_ETH_STORAGE | 0 | none |
| ETH_SOUTH_STORAGE_NORTH | 2 | J1/U7, J1/J3 |
| STORAGE_LOCAL | 0 | none |
| POWER_EAST_REGULATORS_WEST | 0 | none |

## Whole-board assessment

- The CM5 source is on `J7` in the native carrier-mating view. Ethernet launches from the left-side group near the west side of the module; PCIe, USB3-storage, and SERVICE launch from the opposite/right-side group.
- PCIe/V100 remains the strongest anchor because its validated endpoint and corridor already occupy the natural eastward continuation of the right-side high-speed launch. It is not granted priority because of sunk routing cost; it wins because moving it increases source distance without improving the other source groups enough.
- SERVICE remains a local neighborhood and is not a useful exchange target: moving it would trade a short USB2 launch for another source-to-connector corridor.
- Ethernet-local and storage-local/swap candidates are retained as true topology probes. Their early route quality must be developed separately and must not be ranked against the mature historical board by raw DRC/open counts.
- Power and regulator clusters are evaluated as physical neighborhoods and corridor occupants. Their electrical topology remains unchanged in these probes; any promoted movement would require affected Phase 14/15 power and native mechanical revalidation.

### Classification rule

A first-pass candidate route defect is `ROUTE IMPLEMENTATION FAILURE` until a valid native, obstacle-aware routing cycle demonstrates a placement-inherent obstruction. Only an obstruction that persists after competent regeneration is `MACRO-PLACEMENT FAILURE`.

## Decision and controlled reopening

`ETH_LOCAL_STORAGE_MID` has the shortest source distances, but its native body-box screen overlaps the SERVICE/power neighborhood. `SWAP_ETH_STORAGE` is the better acreage topology: it materially reduces both Ethernet and storage source distance while retaining zero coarse major-body overlaps and the existing PCIe/SERVICE anchors. This is a topology decision independent of immature route implementation.

The live integrated board was snapshotted as `PHASE24_MACRO_REVIEW_LIVE_BASIS_20260906.kicad_pcb`. The selected disposable basis is `PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE.kicad_pcb`; it moves only the coherent Ethernet and storage neighborhoods and removes their stale high-speed copper. Native inspection confirms J7, J1, J4, power-entry, and regulator anchor placements are unchanged.

The selected candidate's early DRC/open findings are not used to rank the floorplans. They are route-development evidence only. Ethernet/storage routing must receive a fair native-pad, obstacle-aware regeneration cycle before any placement-inherent conclusion is allowed.

Consultant dispatch was attempted for the independent review but the orchestration service returned `collab spawn failed: agent thread limit reached`. The review was completed locally from the native-loaded objects; this availability issue is not treated as an engineering blocker.

`WHOLE_BOARD_MACRO_FLOORPLAN_REVIEW = COMPLETE`
`SELECTED_MACRO = SWAP_ETH_STORAGE`
`CURRENT_INTEGRATED_CANDIDATE_UNCHANGED = TRUE`
`PHASE24 = OPEN`
