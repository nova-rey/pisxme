# JMS583 design authority

Checked 2026-09-06. This record separates manufacturer design facts from
procurement and firmware evidence. It does not authorize a production PCB by
itself.

## Selected candidate

`JMS583-QHFA3A` (JMicron JMS583, QFN64 8 x 8). This is the current preferred
NVMe bridge candidate for the storage island. It is a USB 3.1 Gen 2 to PCIe
Gen3 x2/NVMe bridge and is electrically usable behind the fixed CM5 USB 5-Gbps
connection; the design must claim no more than the host link can deliver.

## Manufacturer-authoritative facts

Sources:

- `JMS583-product-brief-official-1046.pdf`, JMicron PDB-18001 Rev 1.00;
  https://www.jmicron.com/file/download/1046/JMS583.pdf
- `JMS583-datasheet-rev2.1.pdf`, JMicron PDS-17001 Rev 2.1. The retained copy
  is a JMicron document mirrored by SnapEDA; the official JMicron brief is
  retained separately and is the provenance anchor.
  https://snapeda.s3.amazonaws.com/datasheets/2115-PDS-17001_JMS583_Datasheet_(Rev._2.1)_20190716.pdf

The Rev 2.1 datasheet provides a complete QFN64 pin assignment and JEDEC
land-pattern dimensions. The electrically relevant map is:

| Function | Datasheet pins |
|---|---|
| USB2 | `VBUS 16`, `DM 17`, `DP 18` |
| USB3 RX | `U_RXP2 29`, `U_RXN2 28`, `U_RXN1 27`, `U_RXP1 26` |
| USB3 TX | `U_TXP2 24`, `U_TXN2 23`, `U_TXN1 22`, `U_TXP1 21` |
| PCIe RX | `P_RXN1 34`, `P_RXP1 35`, `P_RXN0 41`, `P_RXP0 42` |
| PCIe TX | `P_TXN1 37`, `P_TXP1 38`, `P_TXN0 44`, `P_TXP0 45` |
| PCIe clock/control | `CLKP 48`, `CLKN 47`, `P_RSTN 54`, `P_CLKREQN 55` |
| Crystal/reference | `XIN 50`, `XOUT 51`, `XAVDDH 52` |
| Reset/test | `RST 15` active-low with external RC; `TME 60` tied logic 0 |
| SPI flash | `GPIO0 3=SO`, `GPIO1 4=SCK`, `GPIO2 5=SI`, `GPIO3 7=CE0#` |
| USB VBUS detect | `GPIO6 10` through the datasheet voltage-divider circuit |
| Analog/digital rails | `VCCO 6,11,32,56`; `VCCK 2,31,53`; `AVDDL 20,25,30,33,36,40,43,46,49`; `XAVDDH 52` |
| Internal regulator | `VDDREG 1` = 5-V input, `LXO 64` to external 4.7-uH inductor, `GND 63` |
| Type-C-only controls | `CC1 62`, `CC2 61`; must be handled explicitly when the fixed CM5 USB path is used |

The datasheet calls for 220-nF PCIe TX AC-coupling capacitors, 100-nF USB3
TX AC-coupling capacitors, 12-kOhm +/-1% REXT, a 25-MHz crystal up to 55-ohm
ESR and +/-30-ppm crystal tolerance, the specified regulator inductor and
decoupling, and the stated reset/power-on timing. These values are design
inputs, not permission to omit the full reference circuit review.

## Firmware/configuration decision

The ordering-code section of the manufacturer datasheet includes a mask-ROM
version field and defines `Z0` as no mask ROM. The selected `JMS583-QHFA3A`
is therefore a factory-programmed mask-ROM device; baseline operation does
not require this project to author or redistribute firmware. The datasheet
scopes external SPI NVRAM to vendor VID/PID information and shows GPIO0--3 as
serial-flash pins after power-on detection. SPI NVRAM is optional for Rev A
and is provisioned as a DNP bring-up/customization footprint, not a boot
dependency.

JMicron also documents a USB firmware-update utility for future maintenance.
Rev A does not depend on that utility or copy a proprietary image. Any future
upgrade must use a JMicron-authorized image/tool matching the ordered variant.
This closes the firmware prerequisite for baseline design.

## Procurement

JLCPCB lists the exact `JMS583-QHFA3A` as `C25701682`, minimum 1, SMT,
economic/standard PCBA, with a quantity-1 displayed price of about $6.06;
the page currently reports `In Stock: 0`, so this is assembly suitability,
not current availability. Independent broker snapshots report 1,000--11,350
pieces and 2--3 day quoted lead times, but those are unverified broker stock
and carry MEDIUM/HIGH counterfeit and continuity risk. No exact DigiKey,
Mouser, Arrow, or Newark listing was verified.

Status: **PROCUREMENT OPEN / sourcing risk HIGH** until an authorized
prototype-quantity quote or traceable factory-programmed supply is obtained;
the firmware prerequisite is CLOSED for baseline operation.

## Decision

JMS583 replaces ASM2362 as the preferred NVMe candidate because it has the
strongest retained package/pin/land-pattern authority and a clear published
reference-component set. It is eligible for promotion into the clean
schematic/PCB; authorized prototype supply remains a procurement gate. The
existing TUSB9261 SATA leg remains retained.

## Provenance and license

The PDFs are retained for engineering traceability under JMicron's copyright
and distribution terms. No proprietary firmware or leaked binary is included.
The mirrored datasheet is used as a reference capture; the manufacturer brief
and JMicron URLs remain the primary provenance record.
