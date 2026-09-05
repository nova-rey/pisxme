# Phase 24 Ethernet PCB support materialization receipt

Date: 2026-09-05

## Candidate

`PHASE24_ETHERNET_SUPPORT_MATERIALIZED.kicad_pcb` was generated from the
immutable `PHASE24_SELECTED_MACRO_PARENT_20260905.kicad_pcb` using
`phase24_materialize_ethernet_support.py`. The 11 support footprints C48–C52
and R26–R31 were loaded from the project footprint library, placed on B.Cu in
the open west acreage, and assigned from the native production netlist. No
copper or synthetic connectivity edges were authored.

## Evidence

- `phase24_ethernet_support_pcb_parity.py`: `PASS`; all 11 footprints and
  every pad net match `phase24-production.xml`.
- Native DRC: `PHASE24_ETHERNET_SUPPORT_MATERIALIZED-drc.rpt`.
- Candidate DRC: 695 total violations, 463 unconnected pads, 0 footprint
  errors, and no track-crossing records.
- Current immutable parent DRC: 690 total violations and 449 unconnected
  pads. The candidate's additional unconnected records are the expected
  newly materialized support pads awaiting routing; inherited short records
  remain unchanged.

## Decision

`PCB_SUPPORT_MATERIALIZATION = PASS_WITH_ROUTING_OPEN`.

This closes the schematic-to-PCB component/pad materialization discriminator,
not Phase 24 acreage closure. The next gate is an obstacle-aware local
Ethernet support route with explicit return/shield treatment, followed by
full-board parity and native DRC revalidation.
