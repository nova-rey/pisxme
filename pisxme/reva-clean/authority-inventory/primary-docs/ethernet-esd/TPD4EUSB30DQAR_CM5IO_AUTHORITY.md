# Ethernet ESD authority — TI TPD4EUSB30DQAR

Checked: 2026-09-03. This record supersedes the earlier TPD4E004 choice for
the CM5IO-derived Phase 17 topology after the official Raspberry Pi CAD was
inspected.

## Authoritative identity

- Manufacturer: Texas Instruments.
- Exact orderable MPN: `TPD4EUSB30DQAR` (DQA package, USON-10).
- TI product status: `ACTIVE`.
- Four unidirectional channels, 5.5 V reverse standoff, 0.8 pF typical I/O
  capacitance, 8 kV IEC 61000-4-2 contact rating, and 5 A 8/20 us surge
  rating.
- TI datasheet Rev G is saved locally as `TPD4EUSB30DQAR.pdf`, SHA-256
  `a2c0dd845043a5bbfe610f673879c29e38649544385dea51dbe0a4c49df39136`.
- TI's DQA pinout is flow-through: D1+/D1− on 1/10 and 2/9, GND on 3/8,
  D2+/D2− on 4/7 and 5/6. The CM5IO source uses the same topology for
  Ethernet TRD pairs.

## Candidates considered

| Candidate | Disposition |
|---|---|
| TI `TPD4E004DRYR` | Previous Phase 2 selection; electrically suitable, but its 6-pin WSON escape is not the official CM5IO flow-through topology and caused the current Phase 17 choke point. Retained as historical evidence, not the promoted CM5IO-derived solution. |
| TI `TPD4EUSB30DQAR` | **Selected for CM5IO-derived Phase 17 adaptation.** Official CM5IO uses the value/package; TI confirms active exact orderable MPN and package/pin authority. |
| Bourns `CDDFN10-3324P-13` | Rejected as the official source's hidden metadata only; no exact CM5IO electrical/land-pattern equivalence is inferred. |

## Current procurement evidence

- Mouser exact MPN `595-TPD4EUSB30DQAR`: 28,850 in stock in the captured
  current listing, MOQ 1, cut-tape pricing about EUR 1.21 qty 1, EUR 0.763
  qty 10, EUR 0.506 qty 100; full reel multiple 3,000.
- Newark exact MPN `33AH5152`: 2,641 in stock in the captured listing,
  MOQ 1, about USD 2.14 qty 1, USD 1.42 qty 10, and USD 1.00 qty 100.
- DigiKey exact MPN `296-28063-1-ND`: exact stock 0 in the captured listing,
  backorder accepted, 16-week manufacturer lead time, about USD 1.61 qty 1
  cut tape / USD 0.673 qty 100; full reel multiple 3,000.
- LCSC exposes the exact TI family through its current listing/substitution
  path; this is not relied upon as the sole procurement channel.

Sourcing risk: `MEDIUM`. The exact active part is available from two major
distributors with MOQ 1 and a documented manufacturer lead time; DigiKey is
temporarily out of stock and full-reel assembly uses a 3,000-piece multiple.

## Assembly and footprint

USON-10 DQA is ordinary SMT but has 0.5 mm pitch and small 0.3 mm × 0.55 mm
signal lands. The official CM5IO native board uses KiCad's
`Package_SON:USON-10_2.5x1.0mm_P0.5mm` footprint with no via-in-pad MDI
escape. Use the manufacturer/package drawing and the official CM5IO footprint
as the source for the project-local clean asset; the CM5IO PCB remains a
reference, not an unreviewed library import.

## Exact PiSXMe decision closed

The official source establishes a materially easier, documented Ethernet ESD
topology. Promote `TPD4EUSB30DQAR` only for the CM5IO-derived Phase 17
adaptation after the disposable fixture passes native mapping, DRC,
connectivity, pair metrics, and support/return review. Until that gate passes,
the clean production ESD selection is not changed.

Sources:

- <https://www.ti.com/product/TPD4EUSB30>
- <https://www.ti.com/product/TPD4EUSB30/part-details/TPD4EUSB30DQAR>
- <https://www.ti.com/lit/ds/symlink/tpd4eusb30.pdf>
- <https://www.mouser.fr/ProductDetail/Texas-Instruments/TPD4EUSB30DQAR>
- <https://canada.newark.com/texas-instruments/tpd4eusb30dqar/esd-protection-array-4ch-son-10/dp/33AH5152>
- <https://www.digikey.com/en/products/detail/texas-instruments/TPD4EUSB30DQAR/2503665>
