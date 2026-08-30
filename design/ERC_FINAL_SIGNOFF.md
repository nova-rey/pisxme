# ERC final signoff — routed high-speed rework

Date: 2026-08-22  
Decision: **PASS WITH DOCUMENTED TOOL-CONTEXT WARNINGS**

Receipt: `validation/ERC_ROUTED_REWORK_RECEIPT.md`  
Current schematic: `pisxme/PiSXMe.kicad_sch`

| Gate | Result |
|---|---:|
| ERC errors | **0** |
| ERC warnings | **46**, all explained |
| Multiple-net-name findings | **0** |
| Pin-not-connected errors | **0** |
| Dangling no-connect markers | **0** |
| Warnings requiring design change | **0** |

Warning debt is limited to 30 reproducible KiCad CLI local-footprint-library
context warnings and 16 intentional isolated boundary labels. A routed-board
rerun found and corrected the only real violation in the pre-fix copy: J2 pin
104 (`PCIE_nWAKE`) had been left without a no-connect marker while a stale
marker remained at a different coordinate. The corrected marker is at
`(233.68, 121.92)`.

The remaining warning classes are documented in the routed rework receipt and
are not evidence of a missing electrical connection.
