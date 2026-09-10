# RTL9210B Path-B native support parity receipt

Date: 2026-09-10  
Board: `PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb`  
Audit: `phase24_rtl9210b_support_parity_audit.py`

The audit passes for 13 support groups using KiCad's native saved-board
connectivity graph built from actual pads, tracks, vias, and zones. The
asserted endpoint table supplies expected ownership only; it does not add
connectivity edges.

Native-closed groups are `CLKREQ_N`, `PEDET`, `RSET`, `XTAL_IN`, `XTAL_OUT`,
`RTL_1V1`, `RTL_3V3`, `RTL_5V`, `SPICS`, `SPISO`, `SPISI`, `SPICLK`, and
`SPISO3`. The machine-readable result is in
`PHASE24_RTL9210B_PATHB_SUPPORT_PARITY.json`.

Explicit open boundaries are `RESET_N` (U1.3 boundary-only), `ISOLATEB`
(U1.12 boundary-only), and `PERST_N` (U1.14 to J1.50, with pull/sequence
ownership still open). The earlier V12 TP6 endpoint for `RESET_N` is recorded
as a regression and is not silently waived.

These are support-authority/open-gate findings, not waived DRC errors. The
isolated candidate remains native DRC-clean and the six high-speed endpoint
and negative-control audits remain passing. No Path-A or production CAD was
changed.
