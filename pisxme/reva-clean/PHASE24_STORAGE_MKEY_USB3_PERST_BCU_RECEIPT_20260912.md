# Phase 24 M-key USB3 / CM5_PERST B.Cu relocation probe — 2026-09-12

## Disposition

**REJECTED — local PCIe-sideband route implementation.** The probe moved only
the long vertical `CM5_PERST` segment from F.Cu to B.Cu using ordinary
0.60/0.30 mm through-vias, leaving the V121 USB3 source escape and U12
placement unchanged.

## Evidence

All four J7→U12 USB3 saved-pad links and the serialized-track negative control
pass. Refilled KiCad 10.0.5 DRC reports **380 violations / 427 unconnected
items**, but the moved B.Cu `CM5_PERST` segment has a real same-layer crossing
with the frozen `V100_PET0_P` corridor. The PCIe-sideband reroute therefore
cannot be promoted. The small count reduction is not evidence of a valid
PCIe repair.

## Classification

This is a **route implementation failure**. The accepted PCIe architecture and
V121 USB3 source escape remain valid; no production copper or frozen PCIe
route was changed.
