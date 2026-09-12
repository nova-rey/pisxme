# Phase 24 selector-label source experiment — 2026-09-13

- Producer base: `99aa35ba` (integrated physical candidate `d7a8ddfa`)
- Generator: `phase24_correct_storage_selector_pin_labels.py`
- Scope: generated U12/U13 selector symbol/label names in `STORAGE.kicad_sch`; no PCB, rules, libraries, or geometry changed.
- Fresh Light KiCad 10.0.6 ERC: `351 findings`, unchanged from the integrated source baseline.
- Decision: do not promote. The one-line schematic diff changes the U13 pin-name contract without reducing ERC or providing a fresh parity/authority closure. Candidate and raw ERC are retained for review; no electrical topology change is accepted from this experiment.
