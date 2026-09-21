# Molex 0039300060 geometry reconciliation

The Librarian indexed exact-variant evidence in private Library commit `91ad3be5`.

- Manufacturer product record: Molex `0039300060 / 39-30-0060 / 5569-06A2-210`.
- Manufacturer drawing: `55690002-SD`, part A2, Rev B, dated 2023-10-23.
- Six contacts, dual row, 4.20 mm pitch; maximum board thickness 1.78 mm; 23.50 mm mated-height reference; 13.80 mm body reference.
- Candidate source footprint hash: `014a8f9b4ad6a1583aec43a5c0fb2a603e305970adf463eea26cd6afa54c7051`.
- Candidate PTH centers: `(0,0)`, `(4.2,0)`, `(8.4,0)`, `(0,5.5)`, `(4.2,5.5)`, `(8.4,5.5)` mm; six 1.80 mm drills.
- Candidate NPTH peg centers: `(0,-7.3)`, `(8.4,-7.3)` mm; 3.00 mm drills.
- Candidate lands `2.70 x 3.70 mm` and courtyard are project-derived, not manufacturer-authored in the acquired drawing.

Disposition: exact pad and peg-hole basis is sufficient for a bounded prototype footprint-authority decision. Manufacturer-authored land/courtyard and verified STEP/WRL 3D parity remain UNPROVEN and must be recorded as prototype/DFM limitations; do not claim manufacturer-verified 3D closure. No restricted vendor bytes are copied into the public repository.

Private Library evidence:
- `/home/nyx/PiSXMe-Library/Library/briefs/molex-0039300060-geometry-reconciliation-20260921.md`
- `/home/nyx/PiSXMe-Library/Library/indexes/molex-0039300060-geometry-reconciliation-20260921.json`

Public sources:
- https://www.molex.com/en-us/products/part-detail/0039300060
- https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/salesdrawingpdf/556/5569/039300200_sd.pdf?inline=
