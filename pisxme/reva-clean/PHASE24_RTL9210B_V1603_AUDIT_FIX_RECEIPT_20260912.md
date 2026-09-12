# Phase 24 RTL9210B V1603 audit correction

The V1603 native six-net audit previously removed only one source-attached
track for each negative control. `REFCLK_P` contains redundant and
zero-length saved segments, so that operation could leave the path connected.

The corrected audit still derives positive connectivity from native pads,
tracks, vias, and zones, but removes all actual saved copper objects for the
tested net in the disposable negative copy. Local KiCad 10.0.5 and fresh
KiCad Light validation pass all six positives and all six negative controls.
No PCB authority or routing was changed.
