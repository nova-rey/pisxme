# Phase 19 SATA routing experiments

Status: `IN_PROGRESS`; no SATA candidate is accepted yet.

## Rejected candidates

`ACREAGE_PHASE19_SATA_LOCAL.kicad_pcb` placed J3 at (140,130) mm, rotation
0°, and used direct F.Cu SATA tracks. Native DRC found three shorting items,
including crossings through adjacent U7 pads and a J3 SATA/power launch. The
outboard M.2 body itself removed the earlier PCIe/mechanical overlap, so this
candidate is rejected specifically for pad-field escape, not authority.

`ACREAGE_PHASE19_SATA_VIA_LOCAL.kicad_pcb` placed J3 at (140,130) mm,
rotation 90°, and attempted ordinary through-via fanout with pair-layer
separation. Native DRC found four shorting items and four crossings: the
chosen corridors intersect the frozen PCIe B.Cu trunk and the two F.Cu SATA
launches are too close to U7 adjacent pads/J3 power. The duplicated-via
mistake was removed before this evidence was recorded.

## Current conclusion

The SATA/M.2 authority is closed, and Phase 18 USB3 remains valid. The next
authorized experiment is a connector placement/corridor outside the PCIe
trunk endpoint, with a deliberate B.Cu detour around that endpoint and local
U7 fanout transitions. No architectural, layer-contract, or PCIe change is
being proposed.
