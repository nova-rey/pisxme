# Phase 24 V60/V61 mode-support corridor experiments

**V61 REJECTED — local selector-field conflicts.** V60 added one outboard
POWER_GND stitch and reached 601 DRC / 349 opens, but native refill exposed
an NC26/STORAGE_SEL short. V61 rerouted `STORAGE_SEL` through a right/outboard
B.Cu corridor; native DRC reached 610 / 348 and reported real
`STORAGE_SEL`/U13 `NC_41` and `XOUT`/`JMS_XAVDDH` shorts.

The mode contract remained passing, but the route is unacceptable. V54
remains the clean ground-access parent; no production PCB or validation rule
changed. The next mode-support experiment must escape locally around U13.
