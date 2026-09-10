# Phase 24 Path-B V1603 integration receipt

Date: 2026-09-10  
Status: ACCEPTED AS CURRENT PATH-B INTEGRATION CANDIDATE; Phase 24 remains open

The accepted V1603 physical-envelope launch was integrated into the complete
V1601 Path-B support candidate without changing the closed U1 orientation or
the approved two-layer signal policy. The six native mappings are:

`U1.61 REFCLK_P -> J1.55`, `U1.62 REFCLK_N -> J1.53`,
`U1.64 LANE0_RXP -> J1.43`, `U1.65 LANE0_RXN -> J1.41`,
`U1.67 LANE0_TXN -> J1.47`, `U1.68 LANE0_TXP -> J1.49`.

## Evidence

- Board: `PHASE24_RTL9210B_PATHB_V1603_INTEGRATED.kicad_pcb`
- Native DRC: `PHASE24_RTL9210B_PATHB_V1603_INTEGRATED-drc.rpt`
- Native DRC reports zero errors from the V1603 six-net launch. The 12
  remaining findings are inherited support-field dangling-via/track warnings
  from the unfinished V1601 candidate; they are not waived or reclassified.
- `phase24_rtl9210b_integrated_v1603_audit.py` derives connectivity from the
  saved PCB's actual pads/tracks/vias and passes all six U1-to-J1 links plus
  six source-track-removal negative controls.

## Remaining gate

This is not a production promotion or Phase 24 close. Complete Path-B support
connections, native integrated parity, return/reference checks, and the
remaining support-field warnings must still be resolved. The launch topology
and U1 orientation are frozen as the implementation baseline.
