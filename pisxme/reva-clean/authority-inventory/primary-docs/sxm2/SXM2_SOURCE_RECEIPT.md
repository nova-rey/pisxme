# SXM2 source receipt

- Product: https://www.amphenol-cs.com/product/74221101lf.html
- Drawing: https://cdn.amphenol-cs.com/media/wysiwyg/files/drawing/74221.pdf
- 3D: https://cdn.amphenol-cs.com/media/wysiwyg/files/3d/s74221.zip
- Observed: Active; 400 positions; 4 mm; 1.27 mm array; 0.45 A/contact.
- Drawing observed through the manufacturer-linked browser PDF: four pages,
  revision W, Released, printed 2025-09-24.
- Direct curl retrieval on 2026-08-29 returned HTTP 403 from the CDN. This is
  an acquisition limitation, not evidence the drawing does not exist.
- Current manufacturer product page rechecked 2026-08-30: lifecycle `Active`,
  400 contacts, 1.27 mm x 1.27 mm array, 4.00 mm stack height, 0.45 A/contact,
  and Mouser distributor stock 312 (updated 2026-07-29). The linked drawing is
  Rev W, status Released, printed 2025-09-24.
- Local comparison reference:
  `../../../../footprints/PiSXMe.pretty/SXM2_74221-101LF.kicad_mod`.

Comparison against the current product page and released Rev-W metadata: the
clean pattern has 400 SMD pads in a 40 x 10 array, 1.27 mm pitch, nominal
0.635 mm circular pads, and a 4 mm-class body outline, matching the public
coarse authority. Exact land-pattern/mask/paste/A1 fields are not independently
reproducible locally because the manufacturer CDN rejects direct capture. The
local pattern remains `REV_A_EMPIRICAL_RISK` for those fields and is not treated
as a promoted manufacturer ECAD file.
