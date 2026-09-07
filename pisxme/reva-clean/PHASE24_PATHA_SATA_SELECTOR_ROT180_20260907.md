# Phase 24 Path-A U13 180-degree placement experiment — 2026-09-07

Status: `REJECTED ROUTE IMPLEMENTATION / LOCAL VIA GEOMETRY`

The disposable fixture rotated U13 by 180 degrees so its SATA Port-B pads
face U7/C30–C33 and its Port-A pads face J3. This is the correct signal-flow
orientation to test; it preserved the corrected source nets and U13.43
`POWER_GND` authority.

The first author still failed native DRC: 180 findings / 52 opens, 23 shorts,
and 5 crossings. The dominant defect is not the orientation itself but the
0.5-mm through-via columns placed beside adjacent 0.4-mm-pitch U13 pads,
plus unspaced U7/capacitor escape lanes. The twelve-endpoint native audit
passed, so this is retained as a placement/routing experiment rather than an
architecture rejection.

The V2 follow-up used staggered pad-derived dogbones and smaller ordinary
through-vias, reducing the short count to 6, but still failed native DRC at
138 findings / 52 opens with 6 shorts and 11 crossings. V3 tightened the
local dogbone width and changed the via geometry again; it regressed to 204
findings / 52 opens with 6 shorts and 12 crossings. V3 is therefore rejected
as worse than V2. Both raw V2 and V3 boards/reports are retained as route
implementation evidence; no production CAD changed. The next comparison
must change the endpoint-side launch geometry or corridor ordering rather
than repeat the same via-column class.
