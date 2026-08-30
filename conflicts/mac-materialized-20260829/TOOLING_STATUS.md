# Tooling status at Mac handoff

## Environment

- Host: Barbarous Mac, KiCad 10.0.5.
- Project environment: `.venv311` (Python 3.11 target); `kicad-python` 0.7.1
  was present during the bridge work.
- Bridge entry points: `bridge/core.py`, `bridge/schematic_backend.py`, and
  `server.py`.
- Schematic dependency declared by the project: `kicad-sch-api==0.5.6`.
- SKiDL spike: SKiDL 2.3.0, kinet2pcb 1.1.4, Python 3.11.

## What works

- Official KiCad PCB IPC operations remain the working PCB path.
- The direct schematic backend can create/load/save basic `.kicad_sch` files,
  discover pins, assign footprints, add wires/labels/sheets, and perform an
  atomic save followed by backend reopen.
- Existing bridge and schematic unit tests previously passed (the historical
  focused set was 7–10 tests depending on fixture selection).
- KiCad 10.0.5 accepted several disposable generated/round-tripped schematics
  syntactically and native netlist/ERC commands could be invoked.
- `work/skidl_spike/golden_flat.py` generated a flat schematic/netlist and a
  disposable PCB mapping showed expected pad-net assignment.

## What is not proven

- The direct backend is not a proven authoritative schematic-to-PCB source.
- KiCad 10 has no clean headless Update PCB from Schematic command; GUI/IPC
  handoff remains the unresolved authority step.
- Project-local `PiSXMe` library resolution emitted warnings in disposable
  round trips; embedded and external symbol definitions differed for critical
  parts.
- A PiSXMe round-trip added semantic/ERC problems in one probe and changed
  project association. Existing legacy ERC violations are not a tooling gate,
  but newly introduced ones are.
- The genuine SKiDL hierarchy fixture produced four native ERC errors involving
  dangling/invalid sheet labels/pins. An auto-stub variant avoided errors by
  removing genuine sheet-pin authority, so it is not a hierarchy proof.
- Mac did not provide a usable `pcbnew` Python module for the kinet2pcb path.
- Custom symbol/footprint pin-map and schematic-derived PCB authority fixtures
  were not completed.

## Reproduction commands

Run from the repository root on Linux after verifying paths and versions:

```sh
python -m pip install -e .
python -m pytest -q tests/test_bridge.py tests/test_schematic_backend.py tests/test_schematic_integration.py
python experiments/skidl/golden_flat.py
python experiments/skidl/golden_hierarchy.py
kicad-cli sch erc <fixture>.kicad_sch --output <fixture>.erc
```

Use the Linux KiCad-bundled Python/`pcbnew` environment for `kinet2pcb` only
after a `python -c 'import pcbnew'` probe succeeds. Capture exact versions and
outputs in a disposable work directory; never write generated fixtures into
`pisxme/` until the authority gates pass.

## Installation/metadata note

The 0.5.6 wheel metadata was internally consistent, but runtime/version fields
observed in the unpacked spike were inconsistent (including `__version__` and
`VERSION_INFO`). Resolve this by installing a pinned distribution normally in
the Linux `.venv311`, recording `importlib.metadata.version()` and runtime
fields, and documenting the discrepancy. Do not fork the library merely to
rename a version string.

## Known failure modes

- Native KiCad netlist/ERC commands can hang on the resource-starved Mac;
  enforce bounded timeouts and use an isolated KiCad config directory.
- Existing PiSXMe source contains legacy ERC/library debt; compare baseline and
  introduced violations rather than declaring the legacy file a clean fixture.
- `tools/execute_m1_truth.py` is unsafe for the approved M1 boundary because it
  also mutates PCB geometry/footprints. Do not use it as a schematic-only tool.
- Never accept PCB-only imported blocks or manually invented PCB nets as proof
  of source authority.
- The Mac repository lives in an iCloud/FileProvider-backed folder. Git
  metadata became dataless and could not be materialized during handoff, so
  commit/push could not be completed safely from this checkout. A fully local
  or fully downloaded Linux clone is required for the next Git operation.

## Linux readiness gate

Return `SCHEMATIC_AUTHORING_TOOLING_READY` only after normal installation,
flat and genuine hierarchy native ERC, project-local symbol resolution,
machine-readable custom pin-map audit, zero newly introduced round-trip
semantic/ERC defects, native validation integration, flat/hierarchy/custom
schematic-to-PCB authority proofs, and full bridge regression. Otherwise return
`SCHEMATIC_AUTHORING_TOOLING_BLOCKED` with the exact blocker and leave active
PiSXMe source unchanged.
