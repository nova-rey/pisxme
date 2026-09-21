# MPA coordinate contradiction: F2 package geometry

Base workspace: current canonical HEAD `8d112ccd`; CAD geometry `57332e98`.
Method: qualified KiCad Light, existing topology-first probe with only the authorized J5.2/F2 y=26.25 correction.

The probe exposed a direct contradiction in the MPA lane decision. The frozen F2 footprint is at `(64.00,15.00)`, and its actual raw/fused pad centers are `(57.60,13.75)` and `(66.90,13.75)` as read from the native board. The MPA decision `PISXME-P24-R3-J5.2-F2-LANE-R2` asserts pad-side coordinates `(57.60,26.25)` and `(66.90,26.25)`, which are not physical F2 pads. The corrected probe therefore still produced route endpoints at y=13.75 for both pad-side transitions; changing the free lane segments to y=26.25 cannot connect to the actual pads without moving/rotating F2 or changing the authority.

Observed topology probe JSON is retained verbatim. It records the free escape/plane segments and the actual pad-derived endpoints. The probe is diagnostic only; no candidate is accepted or integrated. This is an authority/placement reconciliation issue, not permission to invent copper or silently move the fuse.

Required MPA action: reconcile the exact native F2 footprint placement/orientation and bind physically reachable raw/fused pad coordinates, or authorize a specific F2 placement/orientation change with affected cohort and corridor consequences. Preserve J1/J5/J6/J9 anchors, six-layer roles, and 8.50 mOhm contract unless authority explicitly revises them.
