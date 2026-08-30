# SERVICE USB2 ESD authority — TI TPD2EUSB30DRTR

Checked: 2026-08-30. Status: `CLOSED` for the electrical and PCB-library
selection.

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
and the project-local `Texas_DRT_3` footprint; the inherited USB-C connector
footprint is prohibited. The footprint uses the documented 1.0 x 0.8 mm body,
0.7 mm pitch, 0.30 mm pads, and TI pin order (D+, D-, GND). Its geometry is
the maintained KiCad Texas DRT-3 implementation, cross-checked against TI's
package identity and dimensions; it is not presented as redistributed TI CAD.

Sources:

- `https://www.ti.com/lit/ds/symlink/tpd2eusb30.pdf`
- `https://www.ti.com/product/TPD2EUSB30/part-details/TPD2EUSB30DRTR`
- `https://www.digikey.com/en/products/detail/texas-instruments/TPD2EUSB30DRTR/2193486`
- `https://sources.debian.org/src/kicad-footprints/6.0.11-1/Package_TO_SOT_SMD.pretty/Texas_DRT-3.kicad_mod`

Local evidence:

- `../../../../PiSXMe_RevA_Clean.pretty/Texas_DRT_3.kicad_mod`
- `../../../../validation/phase3/test_phase14_service_authority.py`

The KiCad footprint source is Debian-packaged KiCad library content under the
Debian Sources AGPL notice; the local file is a clean-project-derived copy
with the MPN and provenance recorded here. No TI symbol or CAD file is
redistributed.

Exact PiSXMe decision closed: SERVICE connector-boundary ESD is TI
`TPD2EUSB30DRTR` on `SERVICE_USB2_DP`, `SERVICE_USB2_DM`, and `SERVICE_GND`.
