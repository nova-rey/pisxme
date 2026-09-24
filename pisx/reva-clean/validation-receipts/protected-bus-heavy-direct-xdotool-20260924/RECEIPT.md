# Protected-bus Heavy direct-control attempt

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Base SHA: `0a381242`
- Capability: `pisxme-kicad-heavy:v2`
- Image digest: `sha256:39fdae0176135aec42a0dacc8fb250bf8cbf915e01ad67a342e8f8bb2de44344`
- MPA corridor: J5.2 `(16.20,25.00)` -> `(18.35,27.15)` -> `(50.00,27.15)` -> `(50.00,13.75)` -> F2.1 `(57.60,13.75)`.

A third materially distinct Heavy control attempt explicitly handled the KiCad Setup
modal with xdotool, loaded the board, opened Route -> Route Single Track, calibrated
the view/grid, and entered `PWR_SRC_J5_P2` routing. It reached a first waypoint,
then the route could not be advanced to a saved candidate and was undone. Retained
screenshots include `start.png`, `route-menu.png`, `route-start05.png`, `wp1.png`,
`wp1-move407.png`, `tooltip416.png`, and `undo.png`.

No candidate was saved, no fresh-Light validation exists, and no canonical CAD
changed. The disposable Heavy container was cleaned. This is a capability-level
implementation failure after MPA authority and multiple bounded Heavy methods;
route through the hard-problem queue rather than replaying the same GUI path.
