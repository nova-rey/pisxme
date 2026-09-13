# Fresh baseline after disk recovery — 2026-09-13

Base SHA: `9e72fde1`. Qualified image: `pisxme-kicad-light:v1`; native KiCad `10.0.6`. The supported `validate` workflow created a fresh detached checkout after disposable workspace cleanup.

Commands:

- `kicad-cli sch erc --severity-all --format json --output erc.json PiSXMe_RevA_Clean.kicad_sch`
- `kicad-cli pcb drc --severity-all --format json --output drc.json PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- `kicad-cli sch export netlist --format kicadxml --output native-netlist.xml PiSXMe_RevA_Clean.kicad_sch`

Results: ERC 293 findings; DRC 300 violations and 499 unconnected items; no reported shorting items; native netlist export completed. Return-code record and raw JSON/XML are retained beside this receipt. This is a fresh baseline validation result, not a completion claim; all corresponding Phase 24 acceptance rows remain open.
