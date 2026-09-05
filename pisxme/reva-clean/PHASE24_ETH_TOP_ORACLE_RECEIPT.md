# Phase 24 Ethernet top-oracle candidate receipt

Date: 2026-09-05

## Parent and method

Parent: `PHASE24_SELECTED_MACRO_PARENT_20260905.kicad_pcb`

Parent SHA-256:
`da8c9012ddedf5feac774d96c8110e0e0ab7fba2b8ae04e0423727be613f8701`

The disposable `phase24_clean_eth_overlay.py` removed only invalidated
Ethernet, USB3/storage, and clock copper, moved U6/U9/J2 to the exact
CM5IO-direct-oracle geometry, and transplanted the unmodified CM5IO MDI
tracks. J7 remained fixed at its native carrier-mating coordinates.

## Native evidence

Artifact: `PHASE24_CLEAN_ETH_OVERLAY.kicad_pcb`

Native refill/DRC: `PHASE24_CLEAN_ETH_OVERLAY-drc.rpt`

* 387 total DRC violations
* 2 shorting items, both inherited U7/C17 `POWER_GND` versus
  `BRIDGE_SATA_RX_N/RX_P` pad-field defects
* 0 track crossings
* 416 unconnected items, all board-wide/non-Ethernet; the native unconnected
  section contains no `CM5_GBE_` item

All eight MDI net names are present on native copper:

`CM5_GBE_TD0_P/N`, `CM5_GBE_TD1_P/N`, `CM5_GBE_TD2_P/N`,
`CM5_GBE_TD3_P/N`.

Track metrics from the saved board:

| pair | P length (mm) | N length (mm) | skew (mm) | vias | layers |
|---|---:|---:|---:|---:|---|
| TD0 | 68.171 | 67.491 | 0.680 | 0/0 | F.Cu/F.Cu |
| TD1 | 69.701 | 70.530 | 0.829 | 0/0 | F.Cu/F.Cu |
| TD2 | 65.666 | 65.119 | 0.547 | 0/0 | F.Cu/F.Cu |
| TD3 | 63.534 | 64.222 | 0.688 | 0/0 | F.Cu/F.Cu |

## Decision

Retain `ETH_WEST_LOCAL_STORAGE` as the macro-floorplan selection based on
placement/ratsnest topology, not on historical or immature DRC counts. The
top-oracle geometry is a separate routing-development candidate because its
clean-neighborhood trial has zero Ethernet crossings or shorts after
invalidated copper was removed. This does not close Ethernet:
center-tap, LED, shield/return, ESD support, full-board connectivity, and
mechanical/service checks remain required. Storage and clock remain on their
own selected-local island and must be regenerated independently.

The prior selected-local Ethernet route is a `ROUTE IMPLEMENTATION FAILURE`
with 15 shorts and 13 crossings against the same immutable parent; it is not a
`MACRO-PLACEMENT FAILURE`. The top-oracle move is therefore an authorized
routing-development experiment, not evidence that the historical or selected
macro placement is inferior. Any floorplan change requires a placement/ratsnest
or structural-corridor argument independent of immature routing quality.
