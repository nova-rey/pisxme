# Phase 17 Ethernet ESD replacement research

Date: 2026-09-03

## Preferred disposable candidate — Littelfuse SP3019-04HTG

The manufacturer datasheet specifies a four-channel, 5 V protection array in
an SOT-23-6L gullwing package. Protected I/O pins are 1, 3, 4, and 6; pin 2
is GND and pin 5 is NC. The datasheet reports 0.3 pF typical I/O-to-GND at
3 GHz and 0.18 pF I/O-to-I/O. This package topology removes the TPD4E004
DRY interleaved power/signal choke point and is materially easier to route and
assemble.

Procurement evidence captured 2026-09-03: Mouser listed 12,146 in stock and
DigiKey listed the exact MPN as active. Mouser showed approximately $0.67
quantity 1 and a 13-week factory lead time. Exact current pricing and stock
must be refreshed before release. This is a normal gullwing package and is
appropriate for ordinary prototype assembly. Lifecycle is Active; it is the
documented replacement path for obsolete SP3012-04HTG.

Sources:

- https://www.littelfuse.com/assetdocs/tvs-diode-array-sp3019-datasheet?assetguid=e916472b-caac-48e9-84a7-ccbd6c544a5d
- https://www.mouser.com/en/ProductDetail/Littelfuse/SP3019-04HTG
- https://www.digikey.com/en/products/detail/littelfuse-inc/SP3019-04HTG/8123983

## Secondary candidates

- Würth Elektronik `824014`: SOT-23-6L, explicit GBit LAN application,
  0.55 pF typical / 0.65 pF maximum I/O-to-GND, valid lifecycle and observed
  DigiKey/Mouser stock. Pin 5 is VDD, so it needs a local supply connection.
  https://www.we-online.com/components/products/datasheet/824014.pdf
- TI `ESDS304DBVR`: active SOT-23-5, explicitly characterized for
  1000BASE-T at 125 MHz and 2.3 pF typical, with current DigiKey/Mouser stock;
  its five-pad flow-through arrangement is attractive but less low-capacitance
  than SP3019. https://www.ti.com/lit/ds/symlink/esds304.pdf
- ST `HSP053-4M5`: active 0.5 mm µQFN with strong capacitance performance,
  but less suitable for ordinary prototype assembly. https://www.st.com/resource/en/datasheet/hsp053-4m5.pdf

## Decision boundary

SP3019-04HTG is selected for the next disposable geometry trial, not yet for
the clean schematic or production PCB. Promotion requires checking the exact
manufacturer land pattern/model, mapping both arrays across all eight MDI
signals, preserving connector-boundary ESD placement, and passing native DRC,
pair ordering, impedance, reference-plane, mechanical, and CM5IO comparison
gates. No claim of 1000BASE-T compliance is made from capacitance alone.

## Disposable geometry trial

`phase17_sp3019_trial.py` generated a board-only exploratory candidate using
the published SOT-23-6L dimensions and pin topology. Native KiCad DRC reported
335 violations and 238 unconnected items. Candidate-specific failures remain
in the J7 source escape and right-column pair approach. Because this trial footprint was
not imported from an authoritative CAD model and did not complete all
connector-side/support routing, it is evidence for continued investigation
only and is not a component or routing approval.
## TI ESDS304DBVR alternative candidate (2026-09-03)

TI’s official ESDS30x Rev. B datasheet identifies `ESDS304DBVR` as an active
production 4-channel device in the 5-pin SOT-23 DBV package. The datasheet
pin map is I/O1=1, GND=2, I/O2=3, I/O3=4, I/O4=5. It explicitly documents
10/100/1000 Ethernet, 125 MHz 1000BASE-T operation, 2.3 pF typical line
capacitance, ±30 kV IEC 61000-4-2 protection, and a passive no-supply
topology. The package addendum lists a 3000-piece reel and active-production
status.

Source: TI ESDS30x datasheet Rev. B, January 2024, official URL:
https://www.ti.com/lit/ds/symlink/esds304.pdf

The project-local disposable footprint
`PiSXMe_RevA_Clean.pretty/ESDS304DBVR_SOT23_5.kicad_mod` uses TI DBV0005A
mechanical/land-pattern values (0.6 mm × 1.1 mm pads, 0.95 mm pitch, 2.6 mm
row separation), with explicit F.Paste, F.Mask, and F.CrtYd layers. It is a
candidate artifact only: the clean schematic and production PCB have not been
changed, and the ESDS304 fixture has not yet passed native DRC or procurement
review.

The generator was subsequently aligned to the corrected pad coordinates and
the fixture was regenerated again. This candidate has 7 unconnected items
and 104 native DRC violations, so it is also rejected. The lower dangling
count confirms the endpoint correction took effect, but the remaining
crossings and shorts are still routing-topology defects.

A second, large-acreage ESDS304 escape was then constructed with remote U9/U6
placement and separated upper/lower connector shelves. Native DRC reports 92
violations and 8 unconnected items. It is rejected for crossings, connector
launch collisions, and incomplete connectivity; the part remains unpromoted.

The initial ESDS304 escape was invalid evidence because the local footprint
had the wrong pad-side distribution and overlapping pads. The footprint was
corrected to the TI DBV0005A arrangement: pads 1/2/3 on one side, pads 5/4
on the other, 2.6 mm row separation, 0.95 mm pitch, and 0.6 mm × 1.1 mm
exposed metal. The corrected rerun still fails as a routing construction:
native DRC reports 100 violations and 11 unconnected items. It is rejected
for Phase 17, but ESDS304 itself remains an electrically credible active
alternative pending a new escape construction.

## Next fallback solution class: TI ESDS311DYFR (2026-09-03)

TI lists `ESDS311` as an active one-channel unidirectional protector in the
ordinary SOD-323 package. TI explicitly identifies Ethernet 10/100/1000 Mbps
as an application, specifies 4.5 pF typical line capacitance, ±30 kV IEC
61000-4-2 protection, and a 3.6 V working standoff. Its two-terminal shunt
topology is physically simple: one pad is the protected line and the other is
a short local return to GND. Eight devices would protect all eight MDI
conductors without an interleaved multi-channel escape.

Authority: TI ESDS31x product page and Rev. C datasheet. Regional distributor
evidence captured 2026-09-03 shows Mouser `ESDS311DYFR` with 4,510 in stock
and Digi-Key with 2,745 in stock. Stock must be refreshed before release.

Sources:

- https://www.ti.com/product/ESDS311
- https://www.ti.com/lit/ds/symlink/esds314.pdf
- https://www.mouser.com/ProductDetail/Texas-Instruments/ESDS311DYFR
- https://www.digikey.jp/en/products/detail/texas-instruments/ESDS311DYFR/22462690

Decision: fallback candidate only. Its higher capacitance and eight-placement
assembly burden make it inferior to SP3019 and ESDS304 pending a fixture.
