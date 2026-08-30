# TDK C3225X7R1C226M250AC authority receipt

Checked: 2026-08-30. This is a local provenance receipt for the manufacturer
characteristic sheet and live distributor evidence; it is not a replacement
for the linked manufacturer document.

## Exact item

- Manufacturer: TDK Corporation
- MPN: `C3225X7R1C226M250AC`
- Case: 1210 / EIA CC3225, nominal 3.20 x 2.50 mm, max thickness 2.70 mm
- Capacitance: 22 uF, ±20%
- Dielectric: X7R, -55 to +125 C, 5% max dissipation factor
- Rated voltage: 16 Vdc (`1C` voltage code)
- Mounting: surface-mount, embossed tape, reflow compatible
- Factory pack: 1,000; cut-tape quantity-1 is available through distributors

## Current procurement evidence

The TDK product page snapshot reported 41,593 DigiKey, 48,825 Mouser,
118,000 Avnet Abacus, and 132,000 Arrow pieces on 2026-08-17/18. DigiKey
listed cut tape at about $0.73 quantity-1 and about $0.31 at quantity 1,000;
Mouser reported active production availability. These are dated snapshots and
must be refreshed before a purchase order.

## Electrical evidence and limit

The official characteristic sheet contains the exact-part capacitance-vs-
frequency, DC-bias, temperature, impedance/ESR, and ripple-temperature plots.
The graph is authoritative for curve shape but does not publish a numerical
table for the exact 16-part board operating point. Therefore the repository's
90% COUT value is a nominal Rev-A screen, while the ±20% tolerance screen and
exact DC-bias/temperature sum remain explicitly unresolved.

## Sources and provenance

- Manufacturer product page: <https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info?part_no=C3225X7R1C226M250AC>
- Manufacturer characteristic sheet: <https://product.tdk.com/en/system/files/dam/doc/product/capacitor/ceramic/mlcc/charasheet/c3225x7r1c226m250ac.pdf>
- DigiKey: <https://www.digikey.com/en/products/detail/tdk/C3225X7R1C226M250AC/1587497>
- Mouser: <https://www.mouser.com/ProductDetail/TDK/C3225X7R1C226M250AC>

Manufacturer data is retained by reference under TDK documentation terms;
distributor pages are procurement evidence only. The existing generic 1210
footprint is reused, so no third-party CAD asset is introduced.
