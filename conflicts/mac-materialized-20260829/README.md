# KiCad Codex Bridge

`kicad-codex-bridge` is a local MCP server that gives Codex a broad, observable control surface for KiCad 10. It uses the supported KiCad IPC API through `kicad-python` for live PCB work, the bundled `kicad-cli` for validation and exports, and a project-root-scoped file layer for KiCad source and generated files.

## Architecture

```text
Codex desktop / CLI
        |
        | Codex MCP config (stdio)
        v
server.py (FastMCP, 61 tools)
   |             |                  |
   |             |                  +--> scoped .kicad_* / libraries / outputs
   |             +--> bundled kicad-cli (DRC, ERC, exports, upgrades)
   +--> kicad-python 0.7.1 --> /tmp/kicad/api.sock --> KiCad PCB Editor
```

## Detected installation

- KiCad: `10.0.5`
- Application: `/Applications/KiCad/KiCad.app`
- CLI: `/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli`
- Runtime: `/Users/Cooper/Documents/ChatGPT/sxm2/.venv311/bin/python` (Python 3.11)
- Binding: `kicad-python==0.7.1` (API build `10.0.1-0-g2db9e5a72b`)
- Project root: `/Users/Cooper/Documents/ChatGPT/sxm2`

`kicad-cli` is bundled but is not on the shell `PATH`. The bridge uses its absolute path and accepts `KICAD_CLI_PATH` as an override.

## Prerequisites and installation

KiCad must be installed. On this Mac, Homebrew Python 3.11 is used because the available KiCad Python binding and its dependency wheels are compatible with it.

```sh
cd /Users/Cooper/Documents/ChatGPT/sxm2
/usr/local/bin/python3.11 -m venv .venv311
.venv311/bin/python -m pip install -r requirements.txt
```

The checked-in environment was installed with `cryptography==44.0.3` because the newer source distribution attempted a Rust build on this Intel Mac. The pin is in `requirements.txt`.

## Start KiCad and the bridge

1. Start KiCad and open the target `.kicad_pcb` in PCB Editor.
2. In KiCad preferences, enable the KiCad API server under the Plugins/API settings.
3. Start the bridge as an MCP stdio process:

```sh
cd /Users/Cooper/Documents/ChatGPT/sxm2
KICAD_PROJECT_ROOT=/Users/Cooper/Documents/ChatGPT/sxm2 \
  .venv311/bin/python server.py
```

The process speaks MCP over stdin/stdout. Logs from FastMCP and KiCad are kept on stderr so the protocol stream remains clean.

## Codex registration

The supported local Codex mechanism is the `codex mcp` command, which writes the current user's MCP configuration. Register this exact server with:

```sh
codex mcp add kicad-codex-bridge \
  --env KICAD_PROJECT_ROOT=/Users/Cooper/Documents/ChatGPT/sxm2 -- \
  /Users/Cooper/Documents/ChatGPT/sxm2/.venv311/bin/python \
  /Users/Cooper/Documents/ChatGPT/sxm2/server.py
codex mcp list
```

The equivalent configuration is a `[mcp_servers.kicad-codex-bridge]` entry in `~/.codex/config.toml` with the same `command`, `args`, and an `[mcp_servers.kicad-codex-bridge.env]` table containing `KICAD_PROJECT_ROOT`. Codex desktop/CLI/IDE clients share this MCP configuration. A newly registered server may require a new Codex task or restart before its tools appear in an already-running task.

## Socket discovery and authentication

The bridge checks `KICAD_API_SOCKET` first, then discovers Unix sockets matching `/tmp/kicad/api.sock*` and the platform temporary directory. It connects with the official `kicad-python` client. If no token is supplied, the client follows KiCad's normal handshake: the first request has an empty token, KiCad returns the session token, and the bridge caches it for reconnects. `KICAD_API_TOKEN` can be supplied when an externally provisioned token is required.

KiCad 10's external IPC server requires the GUI/editor. The installed CLI has no headless `api-server` command; the headless API-server path is not claimed here.

## MCP surface

The server exposes 61 tools in the tested build:

- connection, version, open documents, open/reload/save/save-as, actions, selection;
- board summaries, dimensions, layers, stackup, design rules, net classes, nets, region queries;
- named list/inspect tools for footprints, pads, tracks, vias, zones, graphics, plus a generic item inspector;
- native footprint creation, movement, rotation, property edits, deletion, board text, graphics, tracks, vias, and item deletion;
- DRC, ERC, unrouted-item reports, CLI capability discovery, and structured CLI exports;
- scoped project-file list/read/write/validation;
- protobuf descriptor listing, object/method descriptions, property validation, and a raw protobuf call escape hatch.

All live edits use KiCad's create/update/delete and commit APIs where available, preserving native undo transactions. Failures are returned as explicit MCP errors.

The raw layer is descriptor-driven rather than arbitrary shell or memory access. Use `kicad_list_api`, `kicad_describe_object`, `kicad_describe_method`, `kicad_get_property`, `kicad_set_property`, and `kicad_raw_call` with fully qualified protobuf names when needed.

## Filesystem layer and validation

The root is restricted to `KICAD_PROJECT_ROOT`; path traversal outside it is rejected. `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, library files, project tables, rule files, and generated outputs can be listed/read/written. Direct edits are atomic, but they are not assumed valid: run `kicad_validate_file`, `kicad_drc`, or `kicad_erc` afterward.

The installed official `kicad-python` wheel has broad PCB bindings, but importing its schematic wrapper fails because the generated schematic types are incompatible (`BusEntryType` is missing), and no schematic command modules are shipped in the wheel. Schematic files are therefore available through the scoped file layer and KiCad CLI, not live schematic IPC editing, for this installation.

## End-to-end test

With the disposable board open in PCB Editor and the bridge registered or launched directly:

```sh
cd /Users/Cooper/Documents/ChatGPT/sxm2
.venv311/bin/python scripts/e2e_mcp_test.py
```

The test inspects the active board and layers through MCP, confirms footprint/pad/track/text state, saves, runs JSON DRC, reads the board back, invokes the raw version call, and generates Gerbers with `kicad-cli`. The disposable project is under `test-fixtures/disposable/`.

## Troubleshooting

- `no Unix socket was found`: start KiCad, open PCB Editor, and enable the API server.
- socket present but handshake fails: check that the socket belongs to the intended KiCad instance, close stale KiCad processes, or set `KICAD_API_SOCKET` explicitly.
- no PCB document: open a `.kicad_pcb`; the API server can be alive while the required editor/document is unavailable.
- CLI errors: call `kicad_cli_capabilities` and use the exact KiCad 10 help surface. Some exporters require an output directory, a layer list, or an operation-specific flag such as `--mode-single`.
- schematic IPC errors are expected for the installed `kicad-python==0.7.1` wheel; use scoped source edits plus `kicad-cli sch erc`/exports.

See [`CAPABILITY_MAP.md`](CAPABILITY_MAP.md) for the inventory and authoritative API references.
