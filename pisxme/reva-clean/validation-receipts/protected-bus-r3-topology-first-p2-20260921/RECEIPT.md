# R3 topology-first P2 feasibility probe

- Base: exact `57332e98`.
- Worker/image: `root-mediated-topology-first-probe-20260921`, `pisxme-kicad-light:v1`, KiCad 10.0.6.
- Method: one J5.2/F2 branch with occupancy-screened local F.Cu escapes, ordinary F.Cu→In2/In4 vias, ordered plane segments, and local F2 pad-field continuity.
- Occupancy result: proposed segments initially had no sampled existing-track conflicts; DRC then exposed actual pad/barrel and existing-copper conflicts.
- Native DRC: 965 violations, 428 unconnected items, exit code 5.
- Important conflicts: PWR_SRC_J5_P2/PWR_FUSED_J5_P1 and PWR_SRC_J5_P1/PWR_SRC_J5_P2 shorts, plus pre-existing corridor conflicts. No acceptance candidate.
- Disposition: preserve as one-branch topology evidence; request MPA lane-coordinate correction before expansion.
