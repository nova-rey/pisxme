# Phase 24 storage power perimeter-escape V95 receipt — 2026-09-11

V95 tested perimeter-only F.Cu escape paths around the U12/U13 RUA0042A
fields, with one farther-out ordinary via per selector and an In2 source
tree. It intentionally removed the immediately adjacent source vias used by
V94.

- Non-strict native M.2 power-owner audit: **PASS**; all nine J3 power pads
  reach a real source pad.
- Strict source-owner audit: **FAIL**; U12.20, U12.30, U13.5, U13.13,
  U13.20, U13.30, R81.2, and U14.5 are not in the selected source component.
- Native DRC: **FAIL**, 627 violations / 337 unconnected items.

V95 is rejected and not promoted. The perimeter topology avoids the V94
shorting-via pattern but requires a coherent local source tree and valid
component-field escape before it can be reconsidered. No canonical PCB or
schematic changed.
