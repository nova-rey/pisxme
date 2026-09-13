# AUTO_PEDET corridor producer receipt

- State: producer candidate; never integrated into canonical branch.
- Base commit: `333d8db5fcce5134ea2117ea2c2018b9e57e53c1`
- Base PCB: `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- Worker: `mpa-autopedet-corridor`, qualified `pisxme-kicad-light:v1` worker.
- KiCad CLI: `10.0.6`.
- Image digest: unavailable from host because Docker API access is denied; qualified image tag recorded.
- Scope: only `AUTO_PEDET`, native pads `J3.69` to `J8.2`; no placement, rules, schematic, or other copper edits.

## Native implementation

Producer command:

```sh
python3 /workspace/project/pisxme/reva-clean/produce_autopedet_corridor.py
```

Native pad coordinates:

- `J3.69` / `AUTO_PEDET`: `(227.750,159.725)` mm
- `J8.2` / `AUTO_PEDET`: `(246.270,148.730)` mm

Added ordinary control-width `0.20 mm` F.Cu segments:

1. `(227.750,159.725)` -> `(227.750,157.500)`
2. `(227.750,157.500)` -> `(255.000,157.500)`
3. `(255.000,157.500)` -> `(246.270,148.730)`

## Native connectivity

```text
native_connectivity True
source AUTO_PEDET dest AUTO_PEDET source_items 5
```

The native saved-board graph connects `J3.69` to `J8.2`. This is scoped connectivity evidence only.

## Native DRC

Command:

```sh
kicad-cli pcb drc --format json --severity-all --exit-code-violations \
  -o /workspace/output/autopedet-drc.json \
  /workspace/project/pisxme/reva-clean/validation-receipts/mpa-autopedet-corridor-producer-20260913/AUTO_PEDET_CORRIDOR_CANDIDATE.kicad_pcb
```

Return code: `5` (violations present).

Raw report: `autopedet-drc.json`.

Result: `312` violations, `499` unconnected items, `0` reported `shorting_items`.
Violation families: clearance `141`, track_width `125`, copper_edge_clearance `15`, track_dangling `9`, via_dangling `7`, courtyards_overlap `6`, pth_inside_courtyard `5`, tracks_crossing `2`, lib_footprint_issues `2`.

The three added AUTO_PEDET tracks introduce clearance findings against the existing top `POWER_GND` zone (actual clearance `0.0000 mm` on the long and source segments). This producer is therefore not an integration candidate or acceptance closure. Do not promote without authority review of the corridor/zone treatment.

SHA-256:

f8f59f7305fb356590dbd5496335b3266fa9c636c9756900a4ed74147223e8aa  pisxme/reva-clean/validation-receipts/mpa-autopedet-corridor-producer-20260913/AUTO_PEDET_CORRIDOR_CANDIDATE.kicad_pcb
f5dfccd8772167cb355f072afe2146783a1ba37fb75711924b9eef1300c0b416  pisxme/reva-clean/validation-receipts/mpa-autopedet-corridor-producer-20260913/autopedet-drc.json

## Disposition

Native endpoint connectivity passed, but targeted full-board DRC failed and increased the violation census from the 300-violation baseline to 312. This is a bounded rejected producer result, not a structural impossibility proof. Return to MPA for corridor/zone disposition; do not run speculative route variants in this workstream.
