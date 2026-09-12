# Phase 24 storage M-key source regeneration — 2026-09-12

## Disposable baseline

`phase24_place_dual_mode_storage_island.py` regenerated
`PHASE24_DUAL_MODE_STORAGE_PLACEMENT_FRESH_20260912.kicad_pcb` from the
selected `SWAP_ETH_STORAGE` macro ancestor. The candidate contains the
project-local TE `1-2199230-4_MKEY` footprint with 67 electrical contacts
(1–58 and 67–75) plus M1/M2/S1/S2 mechanical pads.

Native pad inspection confirms the reviewed J3 ownership, including:

- J3.2/.4/.70/.72/.74: `M2_3V3`;
- J3.3/.71/.73: `POWER_GND`;
- J3.41/.43/.47/.49: shared SATA/PCIe lane-0;
- J3.50/.52/.53/.54/.55/.68: PCIe sidebands/reference signals;
- J3.69: `AUTO_PEDET`.

## Validation

Native DRC reports 798 violations and 499 unconnected items because this is
an unrouted placement/source-authority candidate. The native M.2 power-owner
audit fails with the expected nine unconnected J3 power contacts; it does not
report missing serialized pads. No copper or canonical board was promoted.

This closes the prior PCB-footprint identity defect as a source-regeneration
baseline. The next gate is authoritative local power and high-speed routing
against this pad field, followed by native parity and DRC; the placement
candidate is not itself a Phase 24 PASS.
