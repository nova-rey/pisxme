# Crossing repair producer rejection

- Workstream: `crossing-repair-producer`
- Producer base: `563b5769c560021db4deb825685151f84371a437`
- Candidate: `PHASE24_CROSSING_REPAIR_CANDIDATE.kicad_pcb` (rejected; never integrated)
- Toolchain: `pisxme-kicad-light:v1`, KiCad `10.0.6-10.0.6~ubuntu24.04.1`
- Method: KiCad `pcbnew` API removed the two B.Cu `JMS_AVDDL` segments implicated by native `tracks_crossing` findings and added a left-side detour for the segment from `(141.8,140.0)` to `(154.5,150.5)` plus a right-side detour for `(168.0,132.6)` to `(168.0,150.5)`. No schematic, project rules, anchors, planes, USB, storage, power, J1, or high-speed geometry was intentionally edited.

## Baseline

Command:

```text
kicad-cli pcb drc --format json --severity-all -o /workspace/output/base-drc.json --exit-code-violations /workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb
```

Result: return code `5`; `312` violations, `499` unconnected items; `tracks_crossing=2`; `shorting_items=0`.

## Candidate validation

Command:

```text
kicad-cli pcb drc --format json --severity-all -o /workspace/output/candidate-drc.json --exit-code-violations /workspace/project/pisxme/reva-clean/PHASE24_CROSSING_REPAIR_CANDIDATE.kicad_pcb
```

Result: return code `5`; `318` violations, `499` unconnected items; `tracks_crossing=0`; `shorting_items=1`.

The new short is `JMS_AVDDL` B.Cu track `(141.8,140.0)` to `(141.8,138.0)` against the `JMS_AVDD33` via at `(142.2,139.5)`. This is a real net short, so the candidate is rejected. No candidate commit or canonical integration was made.

Raw outputs and the rejected board are retained here. SHA-256 values are in `SHA256SUMS`.
