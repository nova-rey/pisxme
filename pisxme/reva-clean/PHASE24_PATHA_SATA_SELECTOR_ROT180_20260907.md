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

The V3 orientation remains the current comparison baseline. A follow-up
rotated author would need pad-derived staggered dogbones and via columns
outside the QFN courtyard before it can be compared fairly.
