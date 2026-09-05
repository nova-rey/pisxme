# Ethernet support-passive authority

Checked: 2026-09-05.

| Function | Selected exact MPN | Package | Current procurement evidence |
|---|---|---|---|
| CT capacitor, four | Murata `GRM188R72A223KAC4J` | 0603 X7R, 22 nF, 100 V | Murata reference sheet; Mouser exact listing captured 25,533 stock, MOQ 1, about $0.10 qty 1 / $0.015 qty 1,000 |
| CT resistor, four | Vishay Dale `CRCW040275R0FKEDC` | 0402, 75 ohm, 1%, 1/16 W | DigiKey exact record; Mouser exact-family listing captured 27,057 stock, MOQ 1; Newark exact listing also captured |
| Shield return capacitor | KYOCERA AVX `1206GC102KAT2A` | 1206 X7R, 1 nF, 2 kV | Mouser exact listing captured 376,303 stock, MOQ 1, about $0.24 qty 1 / $0.056 qty 4,000; DigiKey and Newark exact listings captured |
| LED current limit, two | KOA Speer `RK73G1ETTP4700D` | 0402, 470 ohm, 0.5%, 0.1 W | CM5IO native BOM uses this exact MPN; DigiKey captured ACTIVE, 17,243 stock, MOQ 1, $0.24 qty 1 / $0.04383 qty 5,000; Mouser exact listing and ECAD model captured |

## Electrical and package basis

The EDAC A70-series manufacturer-family drawing requires:

`VC1..VC4 -> 22 nF / 100 V -> 75 ohm -> common termination node`

The common node returns through `1 nF / 2 kV` to the connector shield/return.
The CM5IO native design feeds both EDAC LED anodes from 3.3 V and sinks the
yellow/green cathodes through 470 ohm resistors to J7 pads 15 and 17,
`ETH_LEDY` and `ETH_LEDG` respectively.

0603 is selected for the 100 V CT capacitors and 1206 for the 2 kV shield
capacitor. These are standard SMT packages suitable for ordinary prototype
assembly. Substitutes must preserve value, voltage, package, and placement
rules. Distributor stock and pricing are dated snapshots.

## Sources and provenance

- EDAC electrical source: `../ethernet-magjack/EDAC_A70-112-331N126_AUTHORITY.md`.
- CM5IO source: `../../cm5io-rev2/CM5_GPIO.kicad_sch` and `CM5IOBOM.txt`.
- Murata datasheet: <https://search.murata.co.jp/Ceramy/image/img/A01X/G101/ENG/GRM188R72A223KAC4-01A.pdf>
- Murata family: <https://www.murata.com/products/capacitor/ceramiccapacitor/overview/lineup>
- Vishay distributor record: <https://www.digikey.com/en/products/detail/vishay-dale/CRCW040275R0FKEDC/7928421>
- KYOCERA AVX distributor records: <https://www.mouser.com/ProductDetail/KYOCERA-AVX/1206GC102KAT2A> and <https://www.digikey.com/en/products/detail/kyocera-avx/1206GC102KAT2A/3247523>
- KOA distributor record: <https://www.digikey.com/en/products/detail/koa-speer-electronics-inc/RK73G1ETTP4700D/9852608>

The EDAC and CM5IO source files are copyrighted source material retained for
design provenance; this record derives only the values, mappings, and
procurement facts needed by PiSXMe.

## PiSXMe decision

`PHASE24_ETHERNET_SUPPORT_PASSIVES = AUTHORITY_SELECTED`

These parts may replace provisional fixture fields. Production schematic
repair and native hierarchy/netlist/parity validation are still required.
