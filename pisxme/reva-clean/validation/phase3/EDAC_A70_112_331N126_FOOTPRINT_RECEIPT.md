# Phase 3 EDAC A70-112-331N126 footprint receipt

Checked: 2026-08-30.

## Source and scope

The footprint is derived from the recorded EDAC authority drawing, served
through Mouser:

`https://www.mouser.com/catalog/specsheets/EDAC_A70-112-331N126.pdf`

The local authority record is
`authority-inventory/primary-docs/ethernet-magjack/EDAC_A70-112-331N126_AUTHORITY.md`
and the source metadata is in
`authority-inventory/primary-docs/ethernet-magjack/EDAC_A70-112-331N126_SOURCE_RECEIPT.md`.
EDAC Inc. is the mechanical authority; the drawing is copyrighted and is not
copied into this repository.

## Footprint/readback facts

Artifact: `PiSXMe_RevA_Clean.pretty/EDAC_A70_112_331N126.kicad_mod`.

- Namespace-safe footprint name: `EDAC_A70_112_331N126`.
- Pads 1–14: 0.90 mm drills at the EDAC layout families x = -5.715,
  -4.445, -3.175, -1.905, -0.635, 0.635, 1.905, 3.175, 4.445, 5.715 mm;
  y = -8.89, -6.35, -3.83, -2.56 mm as assigned by the drawing.
- Pads 15–18: 1.02 mm drills at (-6.63, 4.06), (-4.09, 4.06),
  (4.09, 4.06), (6.63, 4.06) mm.
- EDAC hole groups: 2x NPTH 3.25 mm at (+/-5.715, 0) mm; 2x NPTH
  1.60 mm at (+/-7.875, -3.05) mm; and 4x NPTH 1.02 mm at
  (+/-8.20, 0) and (+/-8.20, 10.75) mm.
- Body envelope is 15.90 mm wide by 21.35 mm nominal length, with fab,
  silkscreen, and courtyard geometry. No `model` entry or machine-local path
  is present.

## Explicit legacy comparison

Compared with the preserved legacy
`authority-inventory/cm5io-rev2/CM5IO.pretty/TRJG0926HENL.kicad_mod`, pads
1–18 retain the same signal/LED numbering and coordinate families, but this
artifact is not a copy: it uses the EDAC hole groups above (including 3.25
mm and 1.60 mm holes), has the EDAC body/courtyard envelope, and omits the
legacy `TRJG0926HENL` 3D model path. The legacy footprint's two 3.20 mm and
two 1.70 mm mounting holes are not accepted or reused.

Validation status: footprint text/readback and pad-count checks passed locally;
full PCB parity/placement validation remains a later Phase 3 gate.
