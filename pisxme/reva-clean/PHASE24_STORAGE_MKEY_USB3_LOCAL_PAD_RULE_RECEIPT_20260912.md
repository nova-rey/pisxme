# Phase 24 M-key USB3 local pad-clearance probe — 2026-09-12

## Disposition

**REJECTED for promotion; retained as a rule/footprint experiment.** The
candidate starts from the recovered V121 source escape, restores its USB3
tracks to the normal 0.20 mm width, and applies 0.15 mm local clearance to
the HD3SS6126 U12 pads only. The board-wide clearance and minimum-width rules
remain 0.20 mm.

## Evidence

All four J7→U12 saved-pad links and the serialized-track negative control pass.
After native zone refill, KiCad 10.0.5 reports **384 DRC violations / 427
unconnected items**. The intrinsic U12 0.4 mm-pitch pad-field clearance
findings are removed by the footprint-local clearance, but real USB3 launch
crossings and inherited-board findings remain.

Fresh KiCad Light independently reproduced all four endpoint passes and the
negative control; its KiCad 10.0.6 DRC reported **418 violations / 427
unconnected items**. The version delta is recorded and does not change the
candidate rejection.

## Classification

This is a **route integration experiment**, not a waiver or global rule
relaxation. The local pad clearance is a manufacturability candidate only and
requires footprint/assembly authority review before production use. The
remaining USB3 launch crossings must be repaired with actual obstacle-aware
geometry.
