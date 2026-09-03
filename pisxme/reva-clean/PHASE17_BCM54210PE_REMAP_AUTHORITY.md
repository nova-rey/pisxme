# Phase 17 BCM54210PE Ethernet remap authority

Date: 2026-09-03

## Authoritative evidence

Broadcom's public BCM54210 product authority identifies the device family as
an active single-port 10BASE-T/100BASE-TX/1000BASE-T PHY and states that the
PHY detects and corrects common wiring problems. The public page does not
publish the BCM54210PE register-level pair-swap table or authorize arbitrary
per-conductor reassignment.

The official Raspberry Pi CM5IO Rev 2 design files and datasheet expose the
Ethernet interface as four intact differential pairs `TRD0` through `TRD3`
between the CM5 and magnetics. The reference design is the wiring authority,
not evidence that individual conductors may be mixed.

Sources:

- Broadcom BCM54210 product page:
  https://www.broadcom.com/products/ethernet-connectivity/phy-and-poe/copper/gigabit/bcm54210
- Raspberry Pi CM5IO Rev 2 design files:
  https://pip.raspberrypi.com/categories/1098-design-files
- Raspberry Pi CM5IO datasheet and circuit diagrams:
  https://pip-assets.raspberrypi.com/categories/1097-raspberry-pi-compute-module-5-io-board/documents/RP-008182-DS-2-cm5io-datasheet.pdf
- Local CM5IO authority copy:
  `authority-inventory/cm5io-rev2/CM5_GPIO.kicad_sch`

## Legal remap table for disposable trials

The following table is the fail-closed remap boundary used for experiments:

| Operation | Allowed for trial | Constraint |
|---|---:|---|
| Keep each differential pair intact | Yes | Never mix one conductor with another pair |
| Invert P/N within a pair | Conditional | Only as PHY polarity-correction behavior; preserve pair integrity |
| Swap complete pair units | Conditional | Must be treated as MDI/MDIX or documented wiring-pair correction, not arbitrary MAC reassignment |
| Arbitrary four-pair permutation | Not yet authoritative | BCM54210PE-specific public register/table evidence is missing |
| Swap individual conductors between pairs | No | Not a legal Ethernet pair mapping |
| Change the CM5IO logical TRD contract | No | Requires new schematic authority and PHY-specific proof |

For a copper trial, the conservative candidate set is therefore the reference
mapping and complete-pair MDI/MDIX swap variants only. A permutation is not
promoted to production merely because a link partner might recover it.

## 1000BASE-T and polarity boundary

1000BASE-T uses all four pairs as bidirectional channels. A 10/100 MDI/MDIX
transmit/receive distinction must not be used to justify arbitrary 1000BASE-T
pair routing. Polarity correction, where supported by the PHY, can only repair
the sign of an intact pair; it does not legalize conductor mixing. Broadcom's
public product page is insufficient to claim a specific BCM54210PE manual
permutation beyond this boundary.

## Decision

The PHY hypothesis removes the need to preserve a particular external cable
polarity, and it may permit complete-pair MDI/MDIX alternatives. It does not,
on the currently public authoritative evidence, prove arbitrary pair
permutation. The clean authority remains unchanged until a candidate passes
native DRC, pair metrics, and a BCM54210PE-specific mapping proof.

## Closure decision — 2026-09-03

The requested lateral-thinking check is complete. The PHY feature summary is
real, but it is not a public authorization for arbitrary PCB pair routing:
MDI crossover concerns the supported MDI/MDIX relationship, polarity applies
within an intact pair, and skew correction is timing compensation. The exact
CM5IO reference still uses `TRD0..TRD3` intact and a 1:1 MagJack.

The detailed candidate matrix is in
`PHASE17_ETHERNET_REMAP_CANDIDATES.md`. No remapped fixture is promoted and
no clean design asset was changed. A new empirical mapping risk would require
either exact BCM54210PE documentation or an explicit user decision to accept
link-validation risk beyond the approved authority gate.
