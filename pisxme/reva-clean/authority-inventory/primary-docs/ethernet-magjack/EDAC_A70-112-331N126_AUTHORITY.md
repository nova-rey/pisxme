# Ethernet MagJack authority — EDAC A70-112-331N126

Checked: 2026-08-30. This record closes the exact legacy MagJack sourcing gap
by selecting a documented replacement. It does not authorize reuse of the
legacy `TRJG0926HENL` footprint.

## Candidates considered

| Candidate | Evidence | Disposition |
|---|---|---|
| Trxcom `TRJG0926HENL` | Manufacturer product page identifies the original 10/100/1000 PoE+ tab-down green/yellow part; local CM5IO STEP/footprint retained | Reference only: exact major-distributor stock and lifecycle evidence were not established; JLC exact extended listing is 0 stock and consign-only. |
| EDAC `A70-112-331N126` | EDAC drawing and exact Mouser record/datasheet link | **Selected clean Rev-A part.** |
| LINK-PP `LPJG0926HENL` | Manufacturer/distributor page claims compatibility with EDAC and Trxcom families and provides a model/datasheet path | Backup candidate only; no independent mainstream-distributor stock snapshot captured. |

## Selected item and electrical authority

- Exact MPN: `A70-112-331N126`; manufacturer EDAC Inc.; series A70.
- 1x1 shielded RJ45, 10P/8C, integrated magnetics and green/yellow LEDs,
  tab down, through-hole right angle.
- The EDAC drawing specifies 10/100/1000 Mbps filtering with PoE, 1:1 turns
  ratios, 350 uH minimum primary inductance at 100 kHz/8 mA DC bias, 1.2 ohm
  maximum DC resistance, insertion loss no worse than 1.0 dB from 1–100 MHz,
  2250 Vdc PHY-to-line isolation, and 600 mA maximum PSE pin current.
- CM5IO remains the logical authority for PHY pair, center-tap, LED, and
  shield net naming. EDAC is the authority for connector pin labels, pad
  coordinates, hole sizes, and body envelope.

## Mechanical and footprint comparison

The EDAC drawing gives a 15.90 mm body width, 21.35 +/- 0.25 mm length,
13.28 mm height, 11.43 mm contact pitch, 14 signal holes at 0.90 mm, two
3.25 mm mounting holes, and four 1.02 mm guide/mounting holes. Its recommended
layout identifies P1–P14 and LED/shield pins P15–P18.

The preserved legacy `TRJG0926HENL.kicad_mod` has the same 14 signal-pad and
four LED/shield-pad numbering pattern and matching 1.27/2.54/2.56/3.83/4.06/
6.35/8.89 mm coordinate families, but its non-plated mounting-hole set is two
3.20 mm holes plus two 1.70 mm holes. It is therefore **not** accepted as an
exact EDAC land pattern. Phase 3 must create a project-local EDAC footprint
from the recommended layout. Until independently validated, the legacy STEP
is not attached to the selected EDAC footprint.

## Procurement and lifecycle evidence

The captured exact Mouser record (Mouser # `587-A70-112N126`) reports:

- Lifecycle: “New Product”; EDAC; factory pack 1; minimum 1 and multiples 1.
- Stock snapshot: 1,203 immediately shippable; 1,835 and 1,520 on order;
  estimated factory lead 20 weeks above displayed stock.
- USD pricing: $6.97 qty 1, $6.31 qty 10, $5.96 qty 25, $5.52 qty 100,
  and $4.12 qty 1,000. US tariff may apply.
- Through-hole/right-angle assembly requires wave/selective solder or hand
  insertion; it is not an SMT-only placement.
- DigiKey, LCSC/JLC, and Newark/Arrow exact-MPN stock was not established in
  this capture. Mouser is the reputable prototype channel; LPJG0926HENL is
  the practical manufacturer-direct backup subject to incoming qualification.

Sourcing risk: `MEDIUM`. The exact part is obtainable with MOQ 1 and immediate
Mouser stock, but it is a new product with a long factory lead and no second
mainstream distributor snapshot in this capture.

## Local references and provenance

- `EDAC_A70-112-331N126_SOURCE_RECEIPT.md` records exact source URLs, capture
  date, and web-captured drawing facts.
- `../../cm5io-rev2/CM5IO.pretty/TRJG0926HENL.kicad_mod` and its STEP are
  immutable CM5IO donor comparison assets, not selected production assets.
- The EDAC drawing is manufacturer copyrighted. The local receipt stores
  source metadata and derived design facts; the clean footprint must retain
  source URL and attribution.

## Exact PiSXMe decision closed

The former `TRJG0926HENL` procurement gap is closed by selecting EDAC
`A70-112-331N126` as the documented Rev-A replacement. Phase 3 must implement
and parity-check a new `PiSXMeRevAClean` EDAC footprint; the legacy footprint
may not be reused by visual similarity.

