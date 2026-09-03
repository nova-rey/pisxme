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
