# Phase 24 dual-mode storage pin and mode matrix

Status: `IMPLEMENTATION REVIEW — forced modes defined; automatic mode open`

This document is the reviewed ownership record for the storage island. It is
not a substitute for native schematic connectivity or bench validation.

## Data path

| Segment | SATA mode | NVMe mode |
|---|---|---|
| CM5 USB2/USB3 to U12 | U12 port A to U7 USB | U12 port A to U11 USB |
| U12 inactive path | U11 path isolated by U12 | U7 path isolated by U12 |
| bridge to U13 | U7 SATA TX/RX to U13 port B | U11 PCIe lane 0 to U13 port C |
| U13 to J3 | U13 port A lane-0 contacts 41/43 and 47/49 | U13 port A PCIe lane 0 contacts 41/43 and 47/49 |
| additional PCIe lanes | unpopulated/NC | lanes 1–3 and sidebands are direct U11-to-J3 nets |

The shared lane-0 contacts must never be driven simultaneously by U7 and U11.
U12 and U13 are passive high-speed switches; their control pins are not
interchangeable and must be driven from the same settled logical mode after
any required inversion.

## M-key contacts

The contact names below follow SATA-IO TP-053 Rev 1.1. The slash names are
dual-use contacts, not permission to join unrelated sources.

| Contact | M-key function | Rev-A ownership |
|---:|---|---|
| 41/43 | SATA-B+/SATA-B- or PERn0/PERp0 | U7 RX pair or U11 PCIe RX0 through U13 |
| 47/49 | SATA-A-/SATA-A+ or PETn0/PETp0 | U7 TX pair or U11 PCIe TX0 through U13 |
| 50 | PERST# | U11 only; asserted while NVMe path is inactive |
| 52 | CLKREQ# | U11 only; pulled/isolated per bridge reference |
| 53/55 | REFCLK-/REFCLK+ | U11 only; routed as a differential pair |
| 54 | PEWAKE# | U11 only; inactive in SATA mode |
| 10 | DAS/DSS | SATA-side support only |
| 69 | PEDET / CONFIG1 | SATA module grounds it; PCIe/NVMe module leaves it open; host pull-up and mode logic |
| 2,4,12,14,16,18,70,72,74 | 3.3 V | storage SSD rail |
| 3,9,15,27,33,39,45,51,57,71,73 | GND | local ground and return vias |

Unused PCIe lanes 1–3 are not connected to the SATA bridge. Their behavior in
SATA mode and when the socket is empty is a required inactive-state review.

## Mode control decision

`FORCE_SATA` and `FORCE_NVME` are valid power-off bring-up modes. They drive a
single logical `STORAGE_MODE_NVME` signal to both selectors, with a documented
per-device polarity mapping. Mode changes are power-off operations.

The older M.2 Socket 3 interface-detect definition identifies contact 69 as
PEDET/CONFIG1: SATA grounds it and PCIe/NVMe leaves it open, with a platform
pull-up. The retained TP-053 table names the same contact CONFIG1. Rev A will
use that contact through a Schmitt-qualified input and a power-off mode latch;
the signal selects protocol, not proof that a drive is functional. DAS/DSS is
not used as the detector. The latch must treat an empty socket as PCIe/NVMe
default and the manual override must force either mode. TI's selector truth
tables make one shared polarity possible: U12 selects its B port at SEL=0 and
C port at SEL=1; U13 selects its B port at SEL=L and C port at SEL=H. Thus
`STORAGE_SEL=0` is SATA and `STORAGE_SEL=1` is NVMe, while U12 HS_OE is held
low for normal operation.

## Support-circuit obligations

JMS583-QHFA3A requires, from the retained Rev 2.1 datasheet:

- 25 MHz crystal on XIN/XOUT;
- REXT 12 kOhm, ±1% on pin 39;
- external 4.7 uH inductor on LXO;
- 5 V VDDREG input, AVDD33 on pin 19, and local AVDDL/VCCO/VCCK decoupling;
- active-low RST with the documented power-on reset timing;
- VBUS detect divider on GPIO6;
- 100 nF USB3 TX capacitors and 220 nF PCIe TX capacitors at the indicated
  transmitter ends;
- TME held low;
- SPI NVRAM DNP for Rev A unless JMicron supplies a specific configuration and
  programming path.

The SATA bridge remains limited to SATA Gen1/Gen2 (up to 3 Gb/s). The M-key
connector is TE 1-2199230-4, with its exact application drawing and customer
CAD retained under `authority-inventory/primary-docs/storage-upgrade/`.

## Closure criteria

The island cannot be promoted until forced SATA, forced NVMe, empty socket,
reset/startup, and inactive-path tests pass in a native mode-aware fixture.
AUTO additionally requires a real, authoritative detection implementation.
