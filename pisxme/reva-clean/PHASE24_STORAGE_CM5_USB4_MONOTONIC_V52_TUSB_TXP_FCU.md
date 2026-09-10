# Phase 24 Path-A V52 direct F.Cu TX_P experiment

**REJECTED — route implementation experiment.** V52 replaced only the
`TUSB_SATA_TXP` mixed-layer route with a direct F.Cu corridor. The complete
SATA endpoint audit passed, but native DRC worsened to **604 violations / 399
opens** and reported real shorts involving `MODE_IN`/`STORAGE_SEL`,
`XOUT`/`JMS_XAVDDH`, and `NC_26`/`STORAGE_SEL`. No production PCB,
schematic authority, layer contract, or validation rule changed.

Return to V50's mixed-layer topology; the direct F.Cu class is unsuitable
for this acreage congestion pattern.
