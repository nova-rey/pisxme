# Ethernet ESD authority

Date checked: 2026-08-29.

Selected item: Texas Instruments `TPD4E004DRYR`, active four-channel 1.6 pF
Ethernet ESD array, 5.5 V, 6-pin SON/DRY, tape and reel. The six-pin contract
is four protected MDI I/O pins plus VCC and GND. Local TI datasheet
`TPD4E004.pdf` SHA-256:
`5388f4694815b497d26249fe2b0cb5ca9196840e0265fc83e60781fd611d19f0`.

Candidates: `TPD4E004DRYR` (selected); TI `TPD4E05U06DQAR` (lower-capacitance
but 10-pin and less direct for four copper pairs); and Diodes
`DESD1ETH1GXLPSQ` (one channel, T1-specific, rejected for four-pair
1000BASE-T). TI explicitly lists Ethernet for TPD4E004 and its 1.6 pF/channel
capacitance is suitable for the short MagJack-side protection path.

Procurement snapshot: DigiKey exact page showed 11,275 in stock, about USD
1.58 quantity 1, USD 0.999 quantity 10, USD 0.664 quantity 100, USD 0.520
quantity 500, and USD 0.473 quantity 1,000; reel quantity 5,000. Mouser
showed 29,014 in stock, MOQ 1, about INR 129.52 quantity 1 and INR 34.85 at
reel quantity 5,000. LCSC/JLC substitution was not needed. Package is
ordinary SMT; use TI's SON drawing and straightforward ground placement.

Decision: `CLOSED`. This closes the CM5IO-derived copper Ethernet transient
protection choice. TI datasheet/product material is manufacturer provenance;
no 3D model is mechanically material.
