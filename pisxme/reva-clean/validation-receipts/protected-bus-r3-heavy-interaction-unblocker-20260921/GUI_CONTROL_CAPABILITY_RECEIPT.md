# Heavy GUI-control capability receipt

- Workstream: `protected-bus-r3-heavy-router-fixture-20260921`
- Scope: disposable Heavy image/runtime only; no canonical CAD or global configuration changes.
- Date: 2026-09-21
- Image: `pisxme-kicad-heavy:v1`

## Existing qualified interfaces

The installed project bridge is the qualified `kicad-codex-bridge` MCP stdio
server. Its documented live path is KiCad 10 IPC over a Unix socket exposed by
a running PCB Editor with the API server enabled. The bridge exposes board
read/write/selection methods and `kicad_run_action`, but no GUI mouse, keyboard,
interactive-router, or X11-control tool. `run_action` is explicitly documented
as an unstable KiCad-version-specific escape hatch; it does not establish a
supported interactive-router control path.

The Heavy worker starts a private TCP-disabled Xvfb display through
`/usr/local/bin/pisxme-heavy-session`; this provides rendering only. The
qualified worker interface documents no VNC, X11 socket export, GUI-control
service, or worker-side control client.

## Runtime and package probes

The prior bounded Heavy probe launched `pcbnew` under Xvfb and captured three
screenshots. `kicad-cli version` returned `10.0.6`; no board file changed and no
route candidate was produced. The container was subsequently stopped and
released. No KiCad IPC socket or editor process is currently live.

Image probe command:

```sh
sudo docker run --rm --network none pisxme-kicad-heavy:v1 bash -lc \
  'for x in xdotool wmctrl xte ydotool xvkbd xmessage xprop xwininfo Xvfb python; do
     printf "%s=" "$x"; command -v "$x" || true; done;
   ldconfig -p | grep -E "libXtst|libX11|libXi|libXext" || true;
   python -c "import importlib.util; print([(x,bool(importlib.util.find_spec(x))) for x in [\"Xlib\",\"gi\",\"tkinter\",\"wx\",\"mcp\",\"kipy\"]])"'
```

Observed:

- `Xvfb` is present; `xdotool`, `wmctrl`, `xte`, `ydotool`, `xvkbd`,
  `xmessage`, `xprop`, and `xwininfo` are absent from the qualified image.
- `libXtst.so.6`, `libX11.so.6`, `libXi.so.6`, and `libXext.so.6` are present.
- Python has `gi`, `wx`, `mcp`, and `kipy`; it has no `Xlib` or `tkinter` module.

## Capability decision

`BLOCKED: NO_SUPPORTED_GUI_CONTROL_PATH`.

A temporary Python `ctypes` wrapper around `libXtst` could be written inside a
disposable workspace and could send synthetic X events, but that would be a new,
unqualified control mechanism. It is not an existing worker interface, would not
provide KiCad-native router semantics or reliable window/focus targeting, and
cannot be promoted as a supported Phase-24 implementation path without a
separate worker-image/tool qualification. Installing an X11 utility would also
require changing the qualified image or using an unrecorded external package,
which is outside this bounded task.

The exact supported invocation for the existing bridge remains:

```sh
KICAD_PROJECT_ROOT=/workspace/project \
  KICAD_CLI_PATH=/usr/bin/kicad-cli \
  pisxme-bridge
```

It is MCP stdio and requires a live KiCad IPC socket from an API-enabled PCB
Editor; it cannot perform the requested GUI router smoke test when no socket is
available. The existing Heavy launch/Xvfb invocation proved display startup
only:

```sh
pisxme-heavy-session pcbnew /workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb
```

No supported harmless key/control smoke test can be completed in this image:
there is no qualified input utility, no bridge method for GUI input, and the
only conditional bridge action (`run_action`) needs the unavailable live IPC
server and is not a supported interactive-router contract.

## Evidence retained

The prior runtime receipt and output artifacts remain in this workspace:

- `output/pcbnew.stderr`
- `output/pcbnew.stdout`
- `output/screen.png`
- `output/screen2.png`
- `output/screen3.png`
- `receipts/workspace.json`

No canonical source, project configuration, image tag, or global app-server
configuration was changed by this probe.
