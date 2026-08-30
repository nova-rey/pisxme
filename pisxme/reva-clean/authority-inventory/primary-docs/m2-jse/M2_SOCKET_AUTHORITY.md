# SATA M.2 B-key socket authority

Date checked: 2026-08-29.

Selected item: JAE `SM3ZS067U410ABR1000`, active SM3 series, B-key, 67
positions, 0.5 mm pitch, surface-mount right-angle, 4.10 mm body height,
0.5 A/contact, 60 mating cycles. The JAE SM3 series bulletin is saved as
`JAE-SM3-series-bulletin.pdf`, SHA-256
`d8be12322c2c68a462fae3578cf27fb799bd87423ba8599fad31ef0cfb87a8a0`.

The series authority explicitly covers SATA, PCIe Gen3, USB3 and the four
polarizing keys. The 4.1 mm height allows a 1.0 mm component on the underside
of the M.2 module. Use the standard 2280 end datum; provide an optional 2242
retention datum in the clean mechanical study, but do not require it for the
primary SSD.

Candidates considered: JAE `SM3ZS067U410ABR1000` (selected); TE
`1-2199119-0` (technically suitable but live TE page reports unavailable);
and the official CM5IO `MTSSD03-67MSW337` implementation (reference only).

Procurement snapshot: DigiKey's exact MPN record shows active status and a
manufacturer standard lead time of 15 weeks, with approximately USD 1.57
quantity 1. Mouser's exact record showed stock 0 with 5,663 on order and
expected 2026-05-29, USD 1.57 quantity 1, USD 1.34 quantity 10, USD 1.19
quantity 25, USD 1.14 quantity 100, and full-reel MOQ 2,000 at about USD
0.883 each. LCSC/JLC exact stock was not surfaced. MOQ is 1 for cut tape.
Sourcing risk is MEDIUM; TE `1-2199119-0` is the backup after a pad/height
comparison and availability recheck.

Exact-MPN drawing authority is saved locally as
`JAE-SM3ZS067U410-drawing.pdf`, SHA-256
`4b4ccf5359a38faf65b9b5eb9b1598d533dc3f57222727df58e573824480649b`, from
DigiKey's manufacturer drawing record. The drawing identifies the
`SM3ZS067U410` family and exact 4.10 mm variant. The Mouser exact-MPN page
also links the same drawing family and ECAD model.
The local JAE series bulletin remains the manufacturer source for the
ordering-code and key/height interpretation. Mouser exposes an ECAD model
link, but a third-party model is not authority until dimension-checked.

Footprint/3D: the clean project now contains
`PiSXMe_RevA_Clean.pretty/JAE_SM3ZS067U410ABR1000_BKEY.kicad_mod`, derived
from the exact drawing's 0.5 mm two-row geometry with the B-key void at
positions 12–19 per SATA-IO TP053. Its extraction test proves 67 unique
contact pads and the clean STORAGE instance references it. No JAE
manufacturer 3D file was available in the local capture; the CM5IO STEP
`../../cm5io-rev2/CM5IO.3dshapes/MTSSD03-67MSW337.STEP` remains corroboration
only. Assembly is ordinary SMT/reflow with a discrete 2280 screw/standoff
retention feature.

SATA-IO mapping authority is saved as
`SATA-IO-TP053v11-M2-card-format.pdf`, SHA-256
`9d419572e7fba7cf1c7b1207f38cae3c47c04210695293fb516c484b4fd09abf`. It
defines Socket 2 as the B-key socket, B-key notch pins 12--19, and the SATA
device-side pairs: SATA-B+/SATA-B- on pins 41/43 and SATA-A-/SATA-A+ on pins
47/49. The clean design shall label the connector `SATA ONLY / NVMe NOT
SUPPORTED` and shall not connect the PCIe or USB alternatives.

Decision: `CLOSED`. This closes the SATA-capable B-key 2280 socket and its
electrical mapping authority; 2242 is an optional retention study only. Phase
3 must generate the selected JAE footprint from the exact drawing and never
silently reuse the CM5IO M-key footprint.
