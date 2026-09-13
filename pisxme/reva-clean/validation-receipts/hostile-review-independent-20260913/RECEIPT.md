# Phase 24 independent hostile review preparation

- Review date: 2026-09-13 UTC
- Scope: bounded read-only hostile review of the current integrated candidate.
- Repository: `nova-rey/pisxme`, branch `reva-clean`
- Candidate HEAD: `e1de060962b76eabcfd4e83612326c708bd80f4f`
- Origin `reva-clean` at review: `e1de060962b76eabcfd4e83612326c708bd80f4f`
- Qualified validator: `pisxme-kicad-light:v1`
- Image ID: `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`
- KiCad: `10.0.6`
- Selected PCB SHA-256: `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`
- Canonical schematic SHA-256: `6eef63bd3d2b0b9fafc0150d3c34f636ce24a48b2ecbd3d28a5f0bfec167e9f1`
- Project/rules SHA-256: `ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e4423569` / `38e5c7521d964bfa91ee610dc6b7ca39b767b04b8990e94ea91dfe826d21f6a3`
- Sample: one integrated board in a fresh detached Light checkout; no fabricated hardware or bench measurements.
- CAD mutation: none. HEAD changes relative to its parent are `bible.md` and the earlier DFM receipt only; canonical PCB and schematic are unchanged.

## Review purpose and independence

This lane challenged whether the current acceptance evidence can be treated as a
clean integrated result. It used a fresh Light checkout from current HEAD,
native KiCad ERC/DRC/netlist generation, the existing parity and Path-A native
census scripts, and the existing power census. It did not alter schematic,
PCB, project, rule, library, or configuration files. Storage/power geometry
remains the documented `WAITING_ON #2` dependency; this review does not attempt
a route or placement solution.

## Exact commands and retained outputs

The validator was launched with the qualified worker interface:

```text
/home/nyx/pisxme-eda-workers/scripts/pisxme-worker validate \
  /home/nyx/PiSXMe e1de060962b76eabcfd4e83612326c708bd80f4f \
  hostile-review-independent-20260913 bash -lc '...'
```

Inside that fresh checkout, the following commands were run. Return codes and
stdout/stderr are retained beside this receipt:

```text
kicad-cli version
kicad-cli pcb drc --severity-all --format json --exit-code-violations \
  --output /workspace/output/hostile-current-drc.json \
  /workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb
kicad-cli pcb drc --format json \
  --output /workspace/output/default-drc.json \
  /workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb
kicad-cli sch erc --severity-all --format json --exit-code-violations \
  --output /workspace/output/current-erc.json \
  /workspace/project/pisxme/reva-clean/PiSXMe_RevA_Clean.kicad_sch
kicad-cli sch export netlist --format kicadxml \
  --output /workspace/output/current-native.xml \
  /workspace/project/pisxme/reva-clean/PiSXMe_RevA_Clean.kicad_sch
python3 phase24_schematic_pcb_pad_parity_audit.py \
  /workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb \
  /workspace/output/current-native.xml
python3 phase24_patha_native_storage_census.py \
  /workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb \
  /workspace/output/current-patha-census.json
python3 validation/phase24_power_return_census.py \
  /workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb
```

## Results

### Native ERC — OPEN

The fresh native checker reported `293` findings and returned RC `5` with
`--severity-all --exit-code-violations`. The included severities were error,
warning, and exclusion. Counts by sheet/type were `endpoint_off_grid=121`,
`isolated_pin_label=126`, `same_local_global_label=24`, and
`multiple_net_names=22`. Four checker classes are ignored by native ERC
(`single_global_label`, `four_way_junction`, `simulation_model_issue`, and
`footprint_filter`); they remain explicit evidence gaps and were not treated
as waivers. This row remains OPEN.

### Native integrated DRC and opens/shorts — OPEN

The fresh native checker reported `300` violations and `499` unconnected items,
returning RC `5` with `--severity-all --exit-code-violations`. Violation classes
were:

```text
clearance                    138
track_width                  118
copper_edge_clearance         15
track_dangling                 9
via_dangling                   7
courtyards_overlap             6
pth_inside_courtyard           5
tracks_crossing                2
shorting_items                 0
```

Zero `shorting_items` is a scoped observation. It does not satisfy the zero
violation or zero required-open gate. The checker ignores five classes
(`missing_courtyard`, `track_not_centered_on_via`,
`tuning_profile_track_geometries`, `footprint_filters_mismatch`, and
`footprint_type_mismatch`); these are retained as acceptance gaps.

The hostile command comparison is a negative control for a false green: the
same board with native DRC's default command returned RC `0` despite the same
`300` violations and `499` unconnected items. Therefore a closure gate must
retain `--exit-code-violations` and inspect the JSON counts; command success
alone is not a pass.

### Native netlist and pad ownership — scoped PASS; acceptance row remains OPEN

Native schematic export returned RC `0`. The independent parity audit returned
RC `0` with `814` authoritative schematic nodes, `1,262` PCB pads, and zero
expected-pad mismatches. It recorded exclusions `nonphysical_x=65`,
`j1_placeholder=2`, `j3_key_gap=8`, and aliases `J2=18`, `F1=2`, `F2=2`,
`J4=6`. Three nonfatal `PROPERTY_ENUM` assertions were emitted while loading
the board. This is ownership parity only; it does not prove surplus-pad
correctness, physical connectivity, SI, power, or manufacturing readiness.
The corresponding acceptance row remains OPEN.

### Path-A physical endpoint census — OPEN and dependent on #2

The native connectivity census returned RC `0`, inspected `292` storage pads,
and reported `15` open required endpoint pairs out of `26`. This is a physical
connectivity result, not a synthetic expected-edge result. It remains under
`WAITING_ON #2`; no Path-B RTL9210B production integration was performed.

### Power/return census — OPEN and dependent on #2

The native power census returned RC `0`. It confirms zero routed segments and
zero vias for `12V_IN_B`, zero routed segments and zero vias for `FUSED_12V_B`,
and zero copper for bridge rails `BRIDGE_1V1` and `BRIDGE_3V3`, while the
existing measured `POWER_GND`/protected/storage/JMS counts are retained in the
raw JSON. This is design census evidence only; it proves no current, transient,
thermal, or hardware operation result. Physical power closure remains
`WAITING_ON #2`.

## Hostile governance and evidence-integrity findings

The current acceptance matrix has `13` rows and all are `OPEN`. Its candidate
field is `47364e6d`, which does not equal current HEAD
`e1de060962b76eabcfd4e83612326c708bd80f4f`; the machine-readable comparison is
retained in `matrix-audit.json`. Several earlier receipts also identify older
bases or older PCB hashes, including the previous hostile review at `cdd5a381`
with PCB SHA beginning `9938f35c`. Those scoped receipts remain useful for the
candidate they tested, but must not be relabeled as current-HEAD closure
without a fresh integrated validation. This identity drift is an OPEN
acceptance-artifact correction for Root/integration ownership.

All matrix rows currently have an evidence path, except the private Library
provenance reference, which is intentionally not present in the public repo.
No project-level DRC exclusion or waiver token was found in the checked-in
`.kicad_pro` or `.kicad_dru`; native ignored-check classes above remain open
findings rather than silently authorized dispositions.

## Disposition

**FAIL / OPEN.** This bounded hostile review found no independent basis to
advance any acceptance row to PASS. It supplies current-HEAD raw evidence,
exposes the default-DRC false-green behavior, preserves checker ignored-class
limits and PROPERTY_ENUM assertions, and identifies candidate/evidence
identity drift for correction. The queued storage/power corridor problem
remains the only reason for the dependent subtree to be `WAITING_ON #2`; the
campaign still has independent acceptance work available. Phase 25 is not
authorized and Phase 26 remains out of scope.

Raw reports, return codes, versions, candidate validation metadata, current
state, matrix audit, and SHA-256 manifest are retained in this directory.
