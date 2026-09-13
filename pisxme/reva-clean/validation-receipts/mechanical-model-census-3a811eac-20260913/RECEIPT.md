# Fresh mechanical and 3D model census

- Candidate: `3a811eac`.
- Qualified worker: `pisxme-kicad-light:v1`; image identity is recorded in `validation.json`.
- Native footprint inspection: 131 footprints total, 3 with 3D models, 128 without models.
- The no-model list is retained in `mechanical-census.txt`; it includes all major connectors and ICs as well as passives/test points.
- Native DRC family counts in the same current board context: 6 courtyard overlaps, 5 PTH-inside-courtyard, and 15 copper-edge-clearance findings, alongside the existing width/clearance/open findings.
- This is evidence for the open mechanical/DFM row and does not claim assembly readiness.
