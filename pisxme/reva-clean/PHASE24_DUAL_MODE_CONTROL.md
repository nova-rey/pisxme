# Phase 24 storage mode control

## Selected control part

`U14 SN74LVC1G17DBVR` is an active TI single Schmitt-trigger buffer in DBV
SOT-23-5. TI's Rev Y datasheet (local SHA
`c76fa723fac4502423967a1aa087dd669106b52b8de620c024b26e56f5d59309`) defines
DBV pins 1 NC, 2 A, 3 GND, 4 Y, and 5 VCC. The input is Schmitt-qualified,
the output is non-inverting, and the part supports 1.65–5.5 V supply with
Ioff/partial-power-down behavior.

## Rev-A mode circuit

J3 contact 69 (`M2_PEDET`) is pulled up locally to `STORAGE_3V3`. A SATA
module grounds PEDET/CONFIG1; an NVMe module leaves it open. A three-position
power-off configuration selector chooses `M2_PEDET`, a hard SATA strap, or a
hard NVMe strap at the buffer input. The selector is changed only with board
power removed. RC filtering is sized from the selector's worst-case leakage
and the buffer input thresholds; it is not used as a protocol-time signal.

`U14.Y` drives both TI selector SEL pins. From the retained TI truth tables:

| `STORAGE_SEL` | U12 HD3SS6126 | U13 HD3SS3412 | Mode |
|---:|---|---|---|
| 0 | A↔B (TUSB9261), USB2/SS | A↔B (TUSB SATA) | SATA |
| 1 | A↔C (JMS583), USB2/SS | A↔C (JMS PCIe) | NVMe |

U12 `HS_OE` is tied low for normal operation. While the configuration is
settling, bridge reset/SSD power-enable remains held inactive; there is no
live protocol switching or hot-plug claim. The empty socket reads the pull-up
state and therefore defaults to NVMe without connecting the SATA bridge to
the M-key lane-0 contacts.

## Required implementation checks

The selector/jumper footprint must provide mutually exclusive force straps,
visible AUTO/SATA/NVMe markings, and no path that shorts a grounded SATA
PEDET module against a forced-high strap. Native ERC/DRC must prove the three
states. Mode-aware tests must cover SATA module, NVMe module, empty socket,
reset, and both bridges unpowered/selected.

This is a mode-control authority and sourcing decision; it is not a claim that
the native schematic/PCB implementation is complete. The actual U14,
selector, pull-up, filter, reset gating, and power sequencing components still
must be placed and routed in the storage island before promotion.
