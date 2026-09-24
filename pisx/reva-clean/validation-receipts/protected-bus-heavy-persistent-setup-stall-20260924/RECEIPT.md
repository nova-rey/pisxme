# Protected-Bus Heavy Persistent-Shell Setup Stall

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Base: `a7b802d3`
- Worker: `pisxme-kicad-heavy:v2` (`sha256:39fdae0176135aec42a0dacc8fb250bf8cbf915e01ad67a342e8f8bb2de44344`)
- Method: documented persistent `bash` shell plus `heavy-gui launch --timeout 120`.
- Result: no candidate, no validation artifact, no canonical mutation.

The persistent-shell method acquired `gui-session.json` and a live `pcbnew`,
but repeated first-run KiCad Setup dismissal actions did not reach a usable
routing state. Retained screenshots: `root-setup.png`, `root-setup2.png`,
`root-setup3.png`, and `root-setup3_000.png`. The workspace produced no PCB
candidate or route receipt during more than one hour of live session time.
The supervisor was stopped and the worker was cleaned up/released through the
supported lifecycle.

Prior bounded failures are retained in:
- `protected-bus-heavy-launch-stall-20260924`
- `protected-bus-heavy-direct-launch-timeout-20260924`

This is capability/setup-control exhaustion, not evidence that the corrected
MPA corridor is physically impossible.
