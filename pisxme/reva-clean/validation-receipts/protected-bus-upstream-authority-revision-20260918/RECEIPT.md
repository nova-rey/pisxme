# Protected-bus upstream authority revision receipt

## Result

`DONE` / `BINDING_DECISION` for package
`P24-PROTECTED-BUS-UPSTREAM-AUTHORITY-REVISION`.

The authority packet reconciles HPQ Issue #6's `resolution-ready` result and
supersedes only the contradictory R1 local fuse geography and narrow join
constraint. It emits no PCB, schematic, footprint, rule, or canonical queue
edit. The isolated producer is released to implement exactly the R2 plan after
Root records the queue dependency transition.

## Evidence basis

- HPQ resolution: `validation-receipts/hpq-issue6-resolution-20260918/RESOLUTION.md`
- Prior nine-branch MPA R1: `validation-receipts/molex-mpa-nine-branch-revision-20260918/MPA_DECISION.md`
- Nine-branch source contract: `validation-receipts/power-input-nine-branch-contract-20260918/NINE_BRANCH_SCHEMATIC_CONTRACT.md`
- Molex source authority: `validation-receipts/power-input-connector-reassessment-20260918/MOLEX_MULTI_CONNECTOR_AUTHORITY_V2.md`
- Protected-bus product/Power correction: `validation-receipts/protected-bus-corrective-authority-20260918/PROTECTED_BUS_CORRECTIVE_AUTHORITY.md`
- Current selected PCB: `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`

## Geometry validation

`GEOMETRY_AUDIT.py` was run with Python 3 against the corrected 24.25 mm
holder-envelope screen, current J7 courtyard/holes, audited Molex courtyard,
board edge, and J1 approach. It returned `PASS` and wrote
`GEOMETRY_AUDIT.json`.

The audit proves placement-level separation only. It does not prove native
KiCad DRC, routed connectivity, resistance, thermal rise, fuse I2t/SOA, or
fabricated-hardware operation. Those remain producer and fresh-Light
validation gates.

## Handoff

Root should remove only `package:P24-PROTECTED-BUS-UPSTREAM-AUTHORITY-REVISION`
from the protected-bus producer's waiting dependencies and replace it with
this decision artifact. The producer remains a separate candidate state and
must not be marked done until serialized integration and fresh validation pass.

No R1 replay, rejected-board reuse, route variant search, or Phase 25/26 work
is authorized.
