# Phase 24 selected storage data-route receipt

Date: 2026-09-06

Candidate: `PHASE24_SELECTED_MACRO_SWAP_STORAGE_SATA_PAIR_CORRIDOR_V26_AUTH_SKEW.kicad_pcb`

## Native evidence

- J3: authoritative `JAE_SM3ZS067U410ABR1000_BKEY` footprint refreshed from
  `PiSXMe_RevA_Clean.pretty`; saved pad-number net ownership preserved.
- SATA native endpoint audit: PASS for all eight U7/coupler/J3 endpoint pairs.
- USB3 native endpoint audit: PASS for all four J7/U7 endpoint pairs.
- Native DRC: 0 shorting items, 0 track crossings, 0 clearance violations,
  0 hole-clearance violations, 0 dangling vias, and 0 footprint errors.
- Remaining DRC records: 11 unrelated text/silkscreen warnings and 80
  unrelated/incomplete-board unconnected items.

## Geometry

- SATA target: 100 ohm differential, F.Cu/B.Cu only, ordinary 0.50/0.30 mm
  through-vias, no plane-layer signal routing, no via-in-pad.
- End-to-end SATA skew: TX 0.970 mm; RX 0.365 mm; recorded bound 1.2 mm.
- J3 is at native orientation 0 degrees in this disposable route candidate;
  the connector's actual 2280 mechanical envelope remains subject to the
  integrated mechanical review.

## Decision

`STORAGE_DATA_ROUTE = PASS_MILESTONE`

This receipt does not claim Phase 19 or Phase 24 closure. The selected data
route must still be composed with the complete U7 clock, reset, configuration,
rail, return, and support circuitry and then revalidated on the integrated
board.
