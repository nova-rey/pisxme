# Phase 24 whole-board functional-island macro review (fresh discriminator)

Date: 2026-09-05

## Basis

Native-loaded basis: `PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb`. This is a placement/topology comparison only. Existing copper and its accumulated DRC/connectivity are excluded from ranking; moved candidates are disposable.

CM5 is evaluated in the carrier mating view after native KiCad transforms. Source centroids are derived from saved J7 pad net identities.

| group | source pads | source centroid (mm) | current endpoint island | centroid distance | nearest endpoint pad |
|---|---:|---:|---:|---:|---:|
| Ethernet | 8 | (34.50,99.90) | U6,U9,J2 | 32.71 mm | 8.37 mm |
| PCIe/V100 | 7 | (69.60,101.50) | J1 | 81.22 mm | 55.93 mm |
| USB3→SATA | 4 | (70.04,105.30) | U7,J3,Y1,R23,C42,C43 | 58.54 mm | 33.61 mm |
| SERVICE USB2 | 2 | (66.96,99.30) | J4 | 21.97 mm | 19.96 mm |

## Candidate topology metrics

Centroid distance is not a route proof. It is used with endpoint ordering, corridor competition, mechanical access, expected transitions, and island coherence to answer floorplan question A independently of route-development question B.

| candidate | Ethernet island | storage island | PCIe endpoint | SERVICE endpoint | Eth distance | USB3-storage distance | PCIe distance | SERVICE distance | Eth nearest | storage nearest |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `CURRENT_CORRECTED` | (18.5,128.4) | (124.8,125.9) | (150.0,90.0) | (45.0,100.0) | 32.7 | 58.5 | 81.2 | 22.0 | 8.4 | 33.6 |
| `ETH_LOCAL_STORAGE_MID` | (30.6,103.2) | (117.0,125.1) | (150.0,90.0) | (45.0,100.0) | 5.1 | 51.0 | 81.2 | 22.0 | 8.6 | 25.7 |
| `ETH_LOCAL_STORAGE_OUTBOARD` | (17.7,101.2) | (131.9,125.1) | (150.0,90.0) | (45.0,100.0) | 16.9 | 64.9 | 81.2 | 22.0 | 10.1 | 34.3 |
| `SWAP_ETH_STORAGE` | (30.6,103.2) | (112.9,125.1) | (150.0,90.0) | (45.0,100.0) | 5.1 | 47.2 | 81.2 | 22.0 | 8.6 | 19.6 |
| `ETH_SOUTH_STORAGE_NORTH` | (61.1,134.9) | (123.0,83.1) | (150.0,90.0) | (45.0,100.0) | 44.0 | 57.4 | 81.2 | 22.0 | 8.7 | 13.6 |
| `PCIe_EXCHANGE_TEST` | (30.6,103.2) | (117.4,125.4) | (188.0,90.0) | (45.0,100.0) | 5.1 | 51.5 | 119.0 | 22.0 | 8.6 | 25.7 |

## Physical map and discriminator

- `J7` native body is the dominant source anchor. Ethernet launches from the left-side pad group near `(34.50,99.90)`; PCIe, USB3, and SERVICE launch from the right-side groups near `(69.60,101.50)`, `(70.04,105.30)`, and `(66.96,99.30)`.
- PCIe/V100 `J1` remains a sensitive, already-validated endpoint. Its long physical distance is a known routing cost, but the current island has a direct established corridor; moving it is tested only as a discriminator and is not selected without a strong global win.
- SERVICE `J4` is already near its source and is not a useful exchange target. Moving it to make room for Ethernet would trade a solved neighborhood for another launch problem.
- The corrected current storage island remains a coherent U7/J3/clock group, but it is still remote from the USB3 source and competes for central acreage. The `ETH_LOCAL_STORAGE_MID` and `SWAP_ETH_STORAGE` candidates explicitly test whether storage can occupy USB3-side acreage while Ethernet occupies its left-side source neighborhood.
- The `ETH_SOUTH_STORAGE_NORTH` candidate tests a separated connector-edge strategy; it reduces central corridor competition but imposes a long Ethernet source-to-jack path and is therefore a secondary option.
- The PCIe exchange candidate is deliberately retained to prove the frozen PCIe anchor is a choice, not an unexamined constraint. It is not preferred because it does not improve Ethernet/storage source proximity enough to justify invalidating the validated high-speed anchor.

## Topology-only burden metrics

Apparent crossings are straight source-pad to first silicon endpoint segments, not authored copper. External bbox overlaps are an early mechanical screen; native courtyard/3D review remains required.

| candidate | Eth apparent crossings | USB3 apparent crossings | external bbox overlaps | sample overlaps |
|---|---:|---:|---:|---|
| `CURRENT_CORRECTED` | 12 | 0 | 0 | none |
| `ETH_LOCAL_STORAGE_MID` | 23 | 0 | 9 | J2↔C4, J2↔Q2, J2↔U2, J3↔R13, J3↔R14, U6↔J4, U6↔J7, U9↔J4 |
| `ETH_LOCAL_STORAGE_OUTBOARD` | 6 | 0 | 6 | J2↔C4, J2↔Q2, J2↔U2, J3↔R13, J3↔R14, U6↔U2 |
| `SWAP_ETH_STORAGE` | 23 | 0 | 10 | C42↔J7, J2↔C4, J2↔Q2, J2↔U2, J3↔R13, J3↔R14, U6↔J4, U6↔J7 |
| `ETH_SOUTH_STORAGE_NORTH` | 23 | 0 | 13 | J2↔C7, J2↔C8, J2↔C9, J2↔R5, J2↔R6, J2↔TP4, J3↔C18, J3↔J1 |
| `PCIe_EXCHANGE_TEST` | 23 | 0 | 12 | J1↔C18, J1↔R11, J1↔R12, J2↔C4, J2↔Q2, J2↔U2, J3↔R13, J3↔R14 |

## Candidate classification

`CURRENT_CORRECTED` is the preferred topology candidate in this fresh comparison. It is the only tested basis with zero new coarse body overlaps, the lowest apparent Ethernet source-to-first-endpoint crossing count, preserves the already-local SERVICE island and validated PCIe anchor, and keeps the storage bridge/clock/M.2 group coherent. `ETH_LOCAL_STORAGE_MID` improves centroid distances but creates direct J7/J4/regulator/body conflicts and a higher apparent Ethernet crossing burden; it is rejected by the mechanical/topology discriminator, not by immature routing. `ETH_LOCAL_STORAGE_OUTBOARD` and `SWAP_ETH_STORAGE` remain fallback acreage variants only.

These candidates have not been routed and must not be compared with the mature historical board by raw DRC counts. Any first-pass route defect is `ROUTE IMPLEMENTATION FAILURE` until a valid obstacle-aware routing cycle demonstrates a placement-inherent obstruction. A macro candidate becomes `MACRO-PLACEMENT FAILURE` only if its actual required corridors remain structurally impossible after valid regeneration.

## Decision

`MACRO_FLOORPLAN_DISCRIMINATOR = COMPLETE`
`SELECTED_TOPOLOGY = CURRENT_CORRECTED`
`PHASE24 = OPEN_PENDING_FUNCTIONAL-NEIGHBORHOOD_REGENERATION`
