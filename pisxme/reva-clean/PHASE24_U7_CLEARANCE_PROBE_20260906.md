# U7 clearance-basis probe

The disposable board was saved with `m_MinClearance = 0.15 mm` and rerun
through native KiCad DRC. The generic 0.20-mm required clearance remained in
the report, so this API-only setting does not override the active board/rule
basis. The probe is rejected as a rule-authoring method, not as fabrication
evidence.

The probe still retains value: TI's official land pattern is confirmed at
0.4-mm pitch and 1.2 x 0.2-mm pads, and JLC's current six-layer capability
must be represented by an actual KiCad rule/project basis before using the
0.15-mm capability in any accepted candidate.

Raw evidence:

- `PHASE24_U7_PROJECT_FOOTPRINT_ROUTE_CLEARANCE015_20260906.kicad_pcb`
- `PHASE24_U7_PROJECT_FOOTPRINT_ROUTE_CLEARANCE015_20260906-drc.rpt`
- `phase24_set_fixture_clearance_probe.py`
