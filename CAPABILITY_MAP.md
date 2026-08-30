# KiCad / Codex capability map

Inventory date: 2026-08-20

## Detected installation

- KiCad application: `/Applications/KiCad/KiCad.app`
- KiCad version: `10.0.5` (from `Contents/Info.plist` and bundled `kicad-cli --version`)
- Bundled CLI: `/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli`
- `kicad-cli` is not currently on the shell `PATH`.
- Global KiCad preferences: `/Users/Cooper/Library/Preferences/kicad/10.0/kicad_common.json`
- IPC setting was initially disabled. It is now enabled as an authorized integration prerequisite.

## Supported live IPC path

The official `kicad-python` package is installed in the project Python 3.11 environment:

- Python: `/usr/local/opt/python@3.11/bin/python3.11`
- Environment: `.venv311`
- Binding: `kicad-python==0.7.1`
- Binding API build: `10.0.1-0-g2db9e5a72b`
- Dependencies: `protobuf`, `pynng`

KiCad 10's GUI IPC server uses a Unix socket. The official binding defaults to
`ipc:///tmp/kicad/api.sock`; KiCad can append its PID when multiple instances exist.
The official developer documentation identifies `KICAD_API_SOCKET` and
`KICAD_API_TOKEN` as plugin-launched environment variables. For an external client,
the bridge will discover live sockets and let the first authenticated request obtain
and cache the token through the official binding.

KiCad 10 requires a running KiCad GUI/editor for this IPC path. The installed
`kicad-cli` command has no `api-server` subcommand; the headless API-server support
described by the current kicad-python project is a KiCad 11+ capability and is not
claimed for this installation.

Live verification on 2026-08-20 succeeded after the KiCad setup wizard was completed:
`/tmp/kicad/api.sock` accepted the official binding handshake, returned KiCad `10.0.5`,
and the client cached the returned API token. The connected PCB document was the
disposable `test-fixtures/disposable/ipc_test.kicad_pcb`.

## kicad-python 0.7.1 surface observed directly

The released package exposes a substantial PCB API, including:

- version/ping, open-document enumeration, binary lookup, action dispatch;
- PCB save, save-as, revert, commits/undo grouping, create/update/delete items;
- item reads for tracks, vias, pads, footprints, shapes, dimensions, text, barcodes,
  images, zones, groups, IDs, nets, connectivity, and bounding boxes;
- selection management, layers, stackup, origins, graphics defaults, title block,
  design rules/custom rules, visible/active layer and editor appearance;
- board exports for STEP, render PNG, SVG, DXF, PDF, PS, Gerbers, drill, position,
  GenCAD, IPC-2581, IPC-D-356, ODB++, and statistics;
- project net classes and text variables.

The package's `Board` and `KiCad` classes were inspected from the installed wheel.
The installed wheel does not provide a usable schematic wrapper: importing
`kipy.schematic` fails because its generated schematic types do not contain the
imported `BusEntryType`, and no schematic command modules are present in the wheel.
This is recorded as an observed limitation, not silently worked around.

## CLI coverage available in KiCad 10.0.5

Structured wrappers can use the bundled CLI for:

- PCB DRC: `kicad-cli pcb drc`, including JSON/report output and exit-code modes;
- schematic ERC: `kicad-cli sch erc`, including JSON/report output and exit-code modes;
- PCB exports: Gerbers, drill, position, PDF, SVG, STEP, STEPZ, STL, GLB, ODB++,
  IPC-2581, IPC-D-356, GenCAD, DXF, PS, stats, and other listed exporters;
- schematic exports: BOM, DXF, HPGL, netlist, PDF, PS, SVG, and Python BOM;
- format upgrades and the remaining `fp`, `sym`, `jobset`, and render commands.

## Explicitly unsupported or conditional

- No live IPC access exists while the KiCad API server/editor is unavailable.
- Schematic live IPC editing is unavailable through the installed official wheel;
  schematic source files remain accessible to filesystem tools and can be validated
  with `kicad-cli sch erc` and exports.
- DRC/ERC are CLI-backed in this installation rather than high-level kicad-python
  methods.
- KiCad 10 does not provide the KiCad 11+ headless API-server route, so the bridge
  will not claim GUI-free live IPC control.
- UI actions not represented by the supported IPC messages remain limited to the
  documented unstable `run_action` escape hatch; raw memory access and GUI scraping
  are outside scope.
- Footprint mirroring/flip is not represented by a native KiCad 10.0.5 IPC object in
  the installed binding. The bridge does not fake a flip by merely changing layers;
  this remains an explicit unsupported operation.

## Bridge verification

- MCP registration: global `codex mcp add kicad-codex-bridge ... --env KICAD_PROJECT_ROOT=...`.
- MCP discovery: direct stdio `initialize`/`list_tools` returned 61 tools.
- Live MCP operations: board summary, layer enumeration, footprint creation and movement,
  pad inspection, text/graphic/track/via creation, save, readback, selection, and raw
  `GetVersion` call all succeeded.
- CLI operations: KiCad JSON DRC returned six fixture violations with exit code 0; Gerber
  export succeeded; ERC returned a structured report when run against the bundled KiCad
  `Arduino_Pro_Mini.kicad_sch` template without modifying that template.

## Authoritative references

- [KiCad IPC API](https://dev-docs.kicad.org/en/apis-and-binding/ipc-api/)
- [KiCad add-on developer IPC guidance](https://dev-docs.kicad.org/en/apis-and-binding/ipc-api/for-addon-developers/)
- [Official kicad-python repository](https://gitlab.com/kicad/code/kicad-python)
- [Official kicad-python API docs](https://docs.kicad.org/kicad-python-main/)
- [KiCad 10 CLI manual](https://docs.kicad.org/10.0/en/cli/cli.pdf)
