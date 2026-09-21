# Heavy interactive-router runtime receipt

Base: dispatch commit `aa16e8b4`.
Qualified image: `pisxme-kicad-heavy:v1`.

The Heavy container and Xvfb display launched successfully. `kicad-cli version` returned `10.0.6`; `pcbnew` remained live under Xvfb. The producer session did not create a candidate or route receipt because no supported GUI-control/interactive-router bridge was available from this Root context. No CAD file was changed or accepted.

This is a bounded implementation-runtime capability gap. The next action is Unblocker review for a supported GUI-control or equivalent obstacle-aware method; do not replay scripted P2 geometry.
