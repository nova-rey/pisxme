# Protected-bus integrated candidate validation receipt

- Package: `P24-PROTOTYPE-POWER-BUS-INTEGRATION-VALIDATION`
- Integration candidate: `20c9cb12d8f0cc9c63274a07b8b9a887b29585bf`
- Producer candidate: `8dddf504`
- Producer base / MPA base: `31b30dc0ccb28fe341f9bffb26005b5f50cd7641`
- Board: `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- Schematic: `PiSXMe_RevA_Clean.kicad_sch`
- Rules: `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_dru`
- Worker: `protected-bus-integrated-fresh-light-20c9cb12-20260917T232250Z`
- Toolchain: KiCad Light 10.0.6; image `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`

## Commands

```text
kicad-cli version
kicad-cli pcb drc --severity-all --format json -o /workspace/output/integrated-drc.json PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb
kicad-cli sch erc --severity-all --format json -o /workspace/output/integrated-erc.json PiSXMe_RevA_Clean.kicad_sch
kicad-cli sch export netlist --output /workspace/output/integrated-netlist.xml PiSXMe_RevA_Clean.kicad_sch
```

All commands returned `0`. The return code describes command execution, not a
clean report.

## Result

- DRC: **FAIL**, 307 violations and 250 unconnected items.
- DRC classes include 121 clearance, 118 track-width, 19 via-dangling, 15
  copper-edge-clearance, 8 crossing, 8 track-dangling, 6 courtyard-overlap,
  5 PTH-in-courtyard, 4 shorting-items, 2 solder-mask-bridge, and 1
  hole-clearance finding.
- ERC: **FAIL**, 293 findings remain.
- Native netlist export: command PASS; integrated connectivity acceptance FAIL
  because DRC still reports 250 unconnected items.
- Power extraction: **FAIL/UNPROVEN**. The reproducible segment/via/zone
  extraction is retained in `POWER_EXTRACTION.json`; even its intentionally
  incomplete 35-um copper-only estimate exceeds the 10-mOhm source-to-J1
  contract on individual named nets and does not include contacts, pads, vias,
  plane spreading, temperature, or current sharing.

Power-net scoped counts and all acceptance rows are machine-readable in
`INTEGRATION_VALIDATION.json`. No severity downgrade, global rule relaxation,
blanket exclusion, synthetic connectivity, or waiver was used.

This result is a validation failure for the integrated candidate. It does not
close the integration package and does not authorize Phase 25 or Phase 26.
Return the evidence to the owning power/authority path for a bounded correction.
