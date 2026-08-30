# SXM2 connector and land-pattern authority

Date checked: 2026-08-29.

Selected connector: Amphenol Communications Solutions `74221-101LF`, active
400-position BGA/MEG-Array receptacle, 4.0 mm stack height, 1.27 x 1.27 mm
array, 0.45 A/contact, 50 mating cycles, 30 microinch gold. Manufacturer
authority is the live product page and linked drawing `74221.pdf`, revision W,
released and printed 2025-09-24. Drawing/3D URLs and the HTTP acquisition
limitation are preserved in `SXM2_SOURCE_RECEIPT.md`.

Candidates: Amphenol `74221-101LF` (selected); the legacy custom footprint
(reference only); and commercial SXM2 adapters (not geometry authorities).
The local legacy footprint has 400 SMD pads in a 40 x 10 array, nominal 1.27
mm pitch, 0.635 mm circular pads, 0.15 mm solder-mask margin, no pad vias, and
a large courtyard. These coarse facts agree with identity/count/grid, but
the local mask/paste, A1 orientation, courtyard, and K18/K19 electrical
treatment are not manufacturer-proven.

Decision: connector identity and manufacturer mechanical authority are
`CLOSED`; local legacy geometry is not promoted into a clean design. The exact
land-pattern overlay must be regenerated from the Rev-W drawing before Phase 3
placement and compared pad-by-pad, including A1, mask expansion, paste,
courtyard, and hidden-joint assembly access. K18/K19 remain endpoint/bring-up
risks, not grounds for inventing pin functions.

Provenance: Amphenol product/drawing/3D links are manufacturer material; the
existing local footprint is a project reference and is not the manufacturer
file.
