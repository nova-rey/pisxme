# Protected-bus producer bounded retry result

- Package: P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER
- Base: 5d78700c70f8476ac749ead50197c3b1e9c07587
- Workspace: molex-power-bus-clean-20260918
- Toolchain: KiCad Light 10.0.6
- State: BLOCKED_FOOTPRINT_GEOMETRY_CONTRADICTION

## Work performed

Verified the clean detached checkout and exact base. The handoff-named
`PiSXMe_RevA_Clean.kicad_pcb` does not exist in this checkout; the selected
integrated repair basis is `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`.
Created an isolated candidate `PHASE24_POWER_INPUT_MOLEX39301082_CANDIDATE.kicad_pcb`
by replacing only J5/J6 with the authorized prototype Molex 39301082 8-contact
footprint and assigning four duplicated schematic pin-1 contacts to each
12V_IN branch and four duplicated schematic pin-2 contacts to POWER_GND.
No canonical file was changed.

## Validation

Command:
`kicad-cli pcb drc --exit-code-violations --output molex-candidate-drc.rpt PHASE24_POWER_INPUT_MOLEX39301082_CANDIDATE.kicad_pcb`

Result: return code 5; 418 DRC violations, 499 unconnected items. The clean
base report at this worker already had 300 violations and 499 unconnected
items. The candidate introduces a native `shorting_items` class involving
J5's NPTH mounting pad and `12V_IN_A`; equivalent connector-region clearance
issues are present at J5/J6. The released-dimension candidate's 3.6 mm NPTH
keepout overlaps the outer 2.6 mm contact land at the 2.65 mm center spacing
used by the current isolated footprint.

## Required next action

Footprint Authority must reconcile the released 39301082 drawing datum and
peg/contact spacing, or select the Anderson PP15/45 footprint route, then
regenerate the footprint and rerun focused native DRC before any protected-bus
integration. Do not promote this candidate or take credit for its connector
geometry. Existing 300-violation baseline and all raw reports are retained.
