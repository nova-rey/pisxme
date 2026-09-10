# RTL9210B Path-B native support parity receipt

Date: 2026-09-10  
Board: `PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb`  
Audit: `phase24_rtl9210b_support_parity_audit.py`

The audit passes for 14 support groups using KiCad's native saved-board
connectivity graph built from actual pads, tracks, vias, and zones. The
asserted endpoint table supplies expected ownership only; it does not add
connectivity edges.

Native-closed groups are `RESET_N` (including the restored TP6 test point),
`CLKREQ_N`, `PEDET`, `RSET`, `XTAL_IN`, `XTAL_OUT`,
`RTL_1V1`, `RTL_3V3`, `RTL_5V`, `SPICS`, `SPISO`, `SPISI`, `SPICLK`, and
`SPISO3`. The integrated `RESET_N` path also passes its actual-trace-removal
negative control. The machine-readable result is in
`PHASE24_RTL9210B_PATHB_SUPPORT_PARITY.json`.

Explicit open boundaries are `ISOLATEB` (U1.12 boundary-only) and `PERST_N`
(U1.14 to J1.50, with pull/sequence ownership still open). The earlier V12
TP6 endpoint for `RESET_N` was restored and is now natively connected in the
integrated candidate.

`RTL9210B_ISOLATEB_CORROBORATION.md` records the retained community
MIC2545A-1YM implementation as a candidate support direction. It is not
promoted until the PiSXMe SSD-power source, inrush/current budget, and
production application circuit are reconciled.

These are support-authority/open-gate findings, not waived DRC errors. The
isolated candidate remains native DRC-clean and the six high-speed endpoint
and negative-control audits remain passing. No Path-A or production CAD was
changed.
