# Rejected native pcbnew nine-branch producer

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Producer base: `a18d6d47`
- Toolchain: KiCad Light 10.0.6
- Candidate: `PHASE24_MOLEX_NINE_BRANCH_PRODUCER.kicad_pcb`
- Candidate SHA-256: `1e08ed0e21267c0a81e7ff758bdeaf073cc56734355dcfedc61b57236475474c`
- DRC report SHA-256: `4357016b473350f0966be902a7ac103989612a2e91163f22c9015ff9d7d76870`

The native pcbnew producer materialized J5/J6/J9, 18 contacts, F1-F9 and nine branch net pairs. Native DRC reported 1,135 violations, including real `shorting_items` and `tracks_crossing` records. The candidate is rejected and was not integrated. The reported failures include legacy protected/fused copper interactions and local branch fanout crossings; they are implementation evidence requiring a bounded routing/ownership correction, not proof that the Molex architecture is impossible.

The candidate remains historical evidence only. Any next attempt must preserve the nine-branch contract, isolate producer-owned power copper from legacy nets, and return a materially corrected candidate with fresh DRC and path-budget evidence.
