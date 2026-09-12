# Phase 24 current-head fresh Light validation receipt

- Candidate source SHA: `9b214aae3f6d60080e7d7b3260014c9b6675d3d5`
- PCB: `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- Schematic: `PiSXMe_RevA_Clean.kicad_sch`
- Rules: `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_dru`
- Worker: `phase24-current-head-validation-20260912`
- Toolchain: KiCad Light 10.0.6, image `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`
- Commands: `kicad-cli sch erc --severity-all --format json`; `kicad-cli pcb drc --severity-all --format json`
- Return codes: ERC 0; DRC 0 (reports contain findings)
- Results: ERC 351 findings / 0 errors; DRC 370 violations / 499 unconnected items.
- PCB SHA-256: `02f5c421ac63afbf135b951eaedcf7173ff6e83acc04e792ddba20bb15f9da13`
- Schematic SHA-256: `6eef63bd3d2b0b9fafc0150d3c34f636ce24a48b2ecbd3d28a5f0bfec167e9f1`
- Rules SHA-256: `d5473e6262fdf3b53d5de051626f0ed76dedf7257ba591f79ab8ad55f5b411ec`

This is a current integrated-candidate recheck. It does not close any Phase 24 acceptance row; all required integrated evidence remains open until repaired and revalidated.
