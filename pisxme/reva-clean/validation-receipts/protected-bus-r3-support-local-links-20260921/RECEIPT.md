# R3 Support Local-Link Candidate Receipt

- Base: `fc306298`
- Candidate SHA-256: `f60017ca95671689116b3972be6b12a19ea4badf0cb47cfbad3146cc713dcbf5`
- Worker/image: `pisxme-kicad-light:v1`, KiCad `10.0.6`
- Scope: MPA support-cohort positions plus local VCAP/input/fused/gate links; no source/J1 corridor edits
- Fresh Light DRC: 986 violations; 434 unconnected items
- DRC SHA-256: `3c51ed79b28735edb1ce2413c41535748ef321a41d155fa7e86e188004b7eb84`
- Result: isolated progress only; unconnected count improved 447→434 versus placement-only candidate, but full producer gates remain open and no canonical integration was performed.

## Extended local-link attempt

- Candidate SHA-256: `17d5603af5ecf19bf000939373e85486774641f21e2039e91b89f62cae4e3591`
- Added local In3 protected-output and In2 fused-input transitions.
- Fresh Light DRC: 1013 violations; 430 unconnected items.
- DRC SHA-256: `edfdf37295e085b9276b90d59d882c9c0e5640c68defd596e58420988542cb3c`
- Result: rejected; the shorter local-link candidate remains the better isolated checkpoint.
