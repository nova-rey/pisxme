# Phase 24 V58/V59 ground-stitch validation

**V58 REJECTED — native short interaction.** V58 added one ordinary
`POWER_GND` through-via at `(78,108)` to V54. Native DRC reported 601
violations / 349 opens, but three real shorts appeared. V59 is the
no-geometry load/refill/save control and reproduces V54 at 601 violations /
350 opens with zero shorting entries. The V58 interaction is preserved as
real evidence, not attributed to stale V54 fills.
