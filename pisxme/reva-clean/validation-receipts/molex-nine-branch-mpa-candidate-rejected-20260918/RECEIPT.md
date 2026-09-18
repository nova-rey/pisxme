# P24 Molex nine branch direct producer receipt

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Base: `39498cc513c7428ea005209efd1baf7297f8ecc4`
- Worker workspace: `/home/nyx/eda-workspaces/p24-molex-nine-branch-direct`
- Light handle observed: `bb84d6f839ec` (KiCad CLI 10.0.6)
- Candidate commit: `fc09f8c34027d0a1540ee1e859727e947ece6f5e`
- Candidate: `pisxme/reva-clean/PHASE24_MOLEX_NINE_BRANCH_MPA_CANDIDATE_20260918.kicad_pcb`

The candidate was produced from the rejected native producer artifact, with the
binding MPA coordinates applied to J1/J5/J6/J9, F1-F9, D1/C3/U1/Q1,
U2/Q2/C4/D2 and TP2. Four explicitly legacy footprints (`OLD_J5`, `OLD_J6`,
`OLD_F1`, `OLD_F2`) were removed. No canonical checkout was edited.

Native Light checks:

- `kicad-cli pcb drc`: command return 0, but report contains **1139 violations** and **499 unconnected items**.
- Fresh detached Light validation at the candidate SHA reproduced **1139 violations / 499 unconnected items**.
- `kicad-cli pcb export netlist` is unavailable in KiCad 10 (`netlist` is not a supported PCB export subcommand); this is an execution capability result, not a passing connectivity check.
- `kicad-cli pcb export stats` passed and reports 90 through vias, 135 through hole pads, and 139 components.

Path resistance/drop, via-current, and thermal DFM acceptance evidence was not
generated because the candidate fails native connectivity/DRC. This candidate
must not be promoted; the exact blocker is the retained obsolete/under-routed
power topology in the source producer artifact despite applying the fixed
placement and legacy-footprint removal.
