# Protected-bus R3 Heavy interaction Unblocker receipt

- Date: 2026-09-21
- Base: canonical HEAD `26d5051d`
- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Dependency: `other:protected-bus-r3-heavy-interactive-control-20260921`
- Outcome: `HARD_BLOCK` for this package only

Heavy/Xvfb/pcbnew launched successfully with KiCad 10.0.6 and the disposable
R3 board open. The scoped KiCad bridge exposes item-level PCB IPC, movement,
and the unstable `run_action` escape hatch, but no supported interactive-router
cursor/path request. The Heavy image has no qualified xdotool, ydotool, xte,
xvkbd, Xlib, VNC, or equivalent controller. No CAD file or canonical artifact
was changed.

The six prior scripted/direct geometry attempts remain rejected evidence; no
new geometry was replayed. Issue #7 remains `OPEN` with `resolution-ready`; its
authority packet is already reconciled and is not the current queue dependency.

Required next capability: a qualified Heavy GUI-control path or supported
KiCad interactive-router IPC API, with an exact invocation and harmless smoke
test, before the one-branch obstacle-aware route fixture is retried.
