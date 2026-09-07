# Phase 24 Path-A U7 footprint replacement discriminator

Date: 2026-09-06  
Classification: `ROUTE_IMPLEMENTATION_DISCRIMINATOR`, not production
promotion.

## Question

The disposable SATA corridor still showed intrinsic U7 pad-field findings.
This experiment tests whether those findings came from an embedded legacy U7
footprint rather than the project-local TUSB9261 authority.

## Method

`phase24_replace_u7_with_project_footprint.py` loads the saved native
`PHASE24_PATHA_MINIMAL_SATA_CORRIDOR_MONO2_20260906` board, replaces only U7
with `PiSXMe_RevA_Clean.pretty/TUSB9261IPVP_PVP0064A.kicad_mod`, preserves
placement/orientation/reference/value and every saved pad net by native pad
identity, then reruns the existing corridor author, endpoint audit, and KiCad
DRC. No schematic, production PCB, net ownership, or DRC rule changed.

## Evidence

| Check | Result |
|---|---|
| Native U7 replacement | PASS |
| Eight SATA endpoint assertions | PASS |
| Native DRC | 12 findings, FAIL for release |
| Endpoint opens introduced | none in the endpoint audit |
| Production promotion | NO |

The replacement retains the same local route classes: TX dogbone
short/crossing, one socket-launch clearance, residual QFN pad-field
clearance, and fixture/support unconnected items. The embedded/project
footprint mismatch is therefore not the root cause. Further progress must
repair route geometry or complete the support fixture, not exchange equivalent
U7 footprint embeddings.

Raw evidence:

- `PHASE24_U7_PROJECT_FOOTPRINT_20260906.kicad_pcb`
- `PHASE24_U7_PROJECT_FOOTPRINT_ROUTE_20260906.kicad_pcb`
- `PHASE24_U7_PROJECT_FOOTPRINT_ROUTE_20260906-drc.rpt`
- `phase24_sata_native_connectivity_audit.py`
