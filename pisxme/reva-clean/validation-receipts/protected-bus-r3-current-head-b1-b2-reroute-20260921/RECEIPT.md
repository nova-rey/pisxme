# R3 Current-Head B1/B2 Joint Reroute Receipt

- Base: `05be2ec9`
- Candidate SHA-256: `ebc8c6340b9a00b76af547acf3fbf17930c2532e50b4627666a38d82db4d05d7`
- Worker/image: `pisxme-kicad-light:v1`, KiCad `10.0.6`
- Scope: replace only B1/B2 raw/fused/return geometry using MPA-identified separated lanes; preserve J1, anchors, unrelated copper
- Fresh Light DRC: 972 violations; 430 unconnected items
- DRC SHA-256: `f27bccc28cfde269498ddfa26da1a5d32ad3485621fefbb85365a7a72aac2c1c`
- Result: `REJECTED_FOR_INTEGRATION`; opens improved versus B2 (428→430) but DRC remains worse than integrated B1 baseline (919/435), and the candidate does not close the complete-path gate.
- No canonical integration performed.
