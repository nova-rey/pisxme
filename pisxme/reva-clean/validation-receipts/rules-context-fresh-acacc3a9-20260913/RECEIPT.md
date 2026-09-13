# Fresh native rule-context receipt

- Candidate: `acacc3a9`.
- Qualified worker: `pisxme-kicad-light:v1`; image identity is recorded in `validation.json`.
- Native DRC loaded `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_dru`; result was 300 violations, 499 unconnected items, and zero shorts. Ignored checks are listed in the raw JSON and are not treated as waivers for required defects.
- Rule file contains one 0.10-mm clearance/width rule conditioned on net names `XIN`/`XOUT`.
- A native `pcbnew` scope probe found all XIN/XOUT segments within the localized envelope x=135.0–138.4 mm, y=125.55–131.4 mm; no out-of-region segments exist on this board.
- Context correction: the rule is net-scoped rather than an explicit geometric region rule. Current geometry makes its effective footprint local, but future use must not assume a global exception is equivalent to a region restriction. Normal constraints remain in force for other nets; no global rule relaxation or physical repair was made.
