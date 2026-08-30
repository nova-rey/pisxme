# TPSM63606RDLR support-network authority

Checked: 2026-08-30. Status: `CLOSED_FOR_PHASE15_LAYOUT_AUTHORITY`.

## Primary authority

The governing source is the locally preserved TI `TPSM63606` revision B
datasheet: `../TPSM63606.pdf` (SLVSGB4B, revised April 2022).

The pin descriptions on datasheet pages 3–4 require VIN1/VIN2 to be supplied
and locally bypassed, VLDOIN to be biased from an output point or otherwise
handled per the voltage condition, AGND to be joined to PGND, VOUT1/VOUT2 to
feed the output capacitors, FB to use an external divider, RT to use an
external resistor to AGND, PG to use a 10 kOhm–100 kOhm pull-up, and EN/SYNC
to have an explicit high/low or UVLO policy. CBOOT/RBOOT are optional slew
rate-control connections around the internal 100-ohm bootstrap path; they are
not a license to place a general signal on SW.

The TI reference table on datasheet page 17 establishes these design points;
the 5-V reference design on page 24 uses two 47-uF ceramic output capacitors:

| Rail | RFBT with RFBB = 10 kOhm | Suggested FSW | Minimum effective COUT | CFF |
|---|---:|---:|---:|---:|
| 5.0 V | 40.2 kOhm | 0.8–1.2 MHz | 30 uF | 22 pF; TI example is 2 x 47 uF |
| 3.3 V | 23.2 kOhm | 0.7–0.95 MHz | 50 uF | 47 pF |
| 1.0 V | short | 0.3–0.5 MHz | 300 uF | none |

The 1.1 V rail is not a table row. Rev A must not silently interpolate the
1.0 V row: its FB/FSW/COUT choice remains an explicit engineering calculation
before the Phase 5 gate can close.

## Procurement basis

For the 10-uF, 50-V input ceramic family, TI lists TDK
`C3216X7R1H106K160AC`, but current DigiKey search evidence showed it on
backorder. It is therefore not selected as a single-source production
dependency.

For the 22-uF, 16-V X7R output ceramic listed by TI, Murata
`GRM32ER71C226KEA8K` is the selected working candidate: 1210, 22 uF, 16 V,
X7R, 10%, with an exact manufacturer datasheet and current DigiKey related-
part evidence of approximately 1,404 pieces at about $0.79 each in cut tape;
Mouser also lists the exact MPN. This is a candidate pending DC-bias/effective-
capacitance confirmation at each rail voltage and the final quantity choice.

The simplest always-on EN/SYNC policy is direct connection to VIN. PG is an
open-drain output and needs a separate 20–100 kOhm pull-up; it must not be
merged with EN. The internal 100-nF bootstrap capacitor and 100-ohm resistor
mean CBOOT/RBOOT should remain open unless slew-rate tuning is intentionally
calculated. VCC is an internal LDO output and must not be externally loaded.
AGND pins 6/11 join PGND pin 19 under the module; PGND 17–20 are the power
return and thermal path.

The 0402 feedback, RT, EN, and PG resistors may use a mainstream thick-film
family such as Yageo `RC0402FR-0710KL` for 10 kOhm, with exact value variants
selected from the same family after the rail calculations. This is a
procurement-friendly placeholder family, not yet a closed exact BOM choice.

Sources checked for the current procurement snapshot:

- TI primary datasheet: `https://www.ti.com/lit/ds/symlink/tpsm63606.pdf`
- DigiKey exact/related Murata listing:
  `https://www.digikey.com/en/products/detail/murata-electronics/GRM32ER71C226KEA8K/2548186`
- Mouser exact Murata listing:
  `https://www.mouser.com/en/ProductDetail/Murata-Electronics/GRM32ER71C226KEA8K`

## Exact PiSXMe decision

The clean `TPSM63606RDLR_RDL0020` footprint now follows the TI RDL0020A
datasheet land-pattern arrangement: pins 1-16 are perimeter lands and pins
17-20 are the four central PGND thermal lands. The TI layout guidance is the
Phase 15 overlay authority: symmetric VIN/VOUT capacitor placement, short FB
route, local top-side PGND copper, and a 0.3 mm thermal-via array to the
adjacent ground plane. Exact rail values and DC-bias derating remain recorded
Phase 5 design inputs; this receipt closes the package/layout authority needed
for Phase 15 routing.

License/provenance: TI material is retained for design-reference use under
the TI datasheet terms; distributor pages are procurement evidence only. No
third-party CAD or library asset is copied by this receipt.
