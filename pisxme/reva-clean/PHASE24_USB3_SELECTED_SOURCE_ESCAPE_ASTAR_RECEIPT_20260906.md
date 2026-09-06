# Phase 24 USB3 source-escape A* trial

Date: 2026-09-06
Status: `REJECTED`
Failure class: `ROUTE_IMPLEMENTATION_FAILURE`

The disposable `phase24_usb3_source_escape_astar_selected.py` trial used the
actual J7/U7 pad positions and began from explicit source transitions. Native
KiCad DRC after zone refill reported:

- 180 violations
- 450 unconnected items
- 1 `tracks_crossing` finding
- 9 dangling tracks and 5 dangling vias
- 6 copper-clearance, 8 edge-clearance, and 8 co-located-hole findings

The remaining findings also include inherited assembly/silkscreen issues.
The candidate is not a production route and was not promoted. This result
does not reject the selected macro-floorplan or the official CM5IO source
anchor; it rejects this A* continuation implementation. The generated PCB is
kept as disposable local evidence, while the native DRC JSON is the saved
machine report for this trial.

Report: `PHASE24_USB3_SELECTED_SOURCE_ESCAPE_ASTAR-drc.json`.
