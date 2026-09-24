# Protected-bus Heavy v2 bounded attempt

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Base SHA: `9bda92d4a40b59e749891d4c090320714eef6b9b`
- Capability: `pisxme-kicad-heavy:v2`
- Image digest: `sha256:39fdae0176135aec42a0dacc8fb250bf8cbf915e01ad67a342e8f8bb2de44344`
- Workspace: `protected-bus-fcu-waypoint-20260924`
- MPA corridor: J5.2 `(16.20,25.00)` -> `(18.35,27.15)` -> `(50.00,27.15)` -> `(50.00,13.75)` -> F2.1 `(57.60,13.75)`, F.Cu only, no via.

The qualified Heavy session launched successfully under the 2.75 GiB cap and private
Xvfb. It produced `route-start.png`, `current1.png`, `waypoint1.png`, and
`after-undo.png`, but the bounded GUI attempt did not reach a saved candidate or
fresh-Light validation before the session was stopped. No canonical CAD was changed.
The disposable container was cleaned up after preserving these workspace artifacts.

Disposition: implementation attempt incomplete; do not claim candidate or validation.
Route through the normal Tier-2 Unblocker/method-change path before another Heavy
attempt. The MPA corridor remains the sole authorized geometry.
