# SERVICE USB2 ESD authority — TI TPD2EUSB30DRTR

Checked: 2026-08-30. Status: `CLOSED` for the electrical part selection;
the exact DRT land pattern remains an explicit PCB-library sub-gate.

TI identifies `TPD2EUSB30DRTR` as an active catalog two-channel USB 3.0 ESD
array in the DRT SOT-9X3 package. Its 0.7 pF typical channel capacitance,
5.5 V reverse standoff, IEC 61000-4-2 level-4 contact protection, and 5 A
surge rating are suitable for the 480 Mb/s USB2 D+/D- path. The actual device
interface is two protected I/O pins and ground; VBUS is not a device pin and is
not connected to the ESD symbol.

Procurement evidence captured 2026-08-30: DigiKey reported 46,516 in stock,
MOQ 1, about $1.18 quantity 1, and active status; Mouser-indexed records
reported 90,983, MOQ 1, about $0.57 quantity 1. TI lists a standard 3,000
piece reel and ordinary SMT reflow. TI provides the authoritative datasheet
and package information. The G4 suffix is a procurement alternative with the
same electrical/package family, subject to exact suffix verification.

The clean schematic now uses exact MPN `TPD2EUSB30DRTR`, a three-pin symbol,
and no inherited USB-C connector footprint. A DRT-specific project-local
footprint must be generated from TI's package drawing before the component is
placed on the PCB; a generic SOT-23-3 pattern is not accepted as equivalent.

Sources:

- `https://www.ti.com/lit/ds/symlink/tpd2eusb30.pdf`
- `https://www.ti.com/product/TPD2EUSB30/part-details/TPD2EUSB30DRTR`
- `https://www.digikey.com/en/products/detail/texas-instruments/TPD2EUSB30DRTR/2193486`

Exact PiSXMe decision closed: SERVICE connector-boundary ESD is TI
`TPD2EUSB30DRTR` on `SERVICE_USB2_DP`, `SERVICE_USB2_DM`, and `SERVICE_GND`.
