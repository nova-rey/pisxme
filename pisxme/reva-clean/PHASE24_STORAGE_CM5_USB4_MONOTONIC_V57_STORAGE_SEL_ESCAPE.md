# Phase 24 V57 STORAGE_SEL escape experiment

**REJECTED — support-route shorting.** V57 rerouted `STORAGE_SEL` from U14
around the MODE_IN pad field using ordinary through-vias. The mode contract
and complete SATA endpoint audits passed, but native DRC reported **614
violations / 350 opens** and three real shorts to U12/U13 `POWER_GND` and
the TUSB SATA TX_N corridor. No production PCB, schematic authority, layer
policy, or DRC severity changed.

Return to V54 for the next mode-support route class; do not promote V57.
