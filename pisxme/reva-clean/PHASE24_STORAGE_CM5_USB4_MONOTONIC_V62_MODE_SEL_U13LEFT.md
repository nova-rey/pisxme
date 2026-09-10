# Phase 24 V62 local STORAGE_SEL escape

**REJECTED — U13/M.2 field collision.** V62 kept the U12.9-to-U13.9 local
segment and escaped `STORAGE_SEL` left of U13 before a B.Cu outboard trunk.
The mode contract remained passing, but native DRC reported **598 violations
/ 349 opens**, including real `STORAGE_SEL` to M.2
`M2_SATA_B_P_PCIE_RXN0` shorting at the U13 transition and the independent
`XOUT`/`JMS_XAVDDH` short. No production authority or validation rule
changed. V62 is not promoted.
