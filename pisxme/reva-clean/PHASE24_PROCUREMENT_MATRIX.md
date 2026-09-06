# Phase 24 dual-mode storage procurement matrix

Checked 2026-09-06. Prices are observed planning values, not quotations.

| Function | Selected/reference item | Qty-1 evidence | MOQ/assembly | Lifecycle | Risk | Decision |
|---|---|---|---|---|---|---|
| SATA bridge | TI `TUSB9261IPVP` | DigiKey/Mouser records, approx. $8--10 | MOQ 1; SMT | ACTIVE | MEDIUM | Retain; SATA Gen1/2 only, up to 3 Gb/s |
| USB A/B selector | TI `HD3SS6126RUAR` | DigiKey/Mouser snapshots, approx. $3--4 | MOQ 1; QFN SMT | ACTIVE | MEDIUM | Design-review qualified |
| SATA/PCIe selector | TI `HD3SS3412RUAR` | distributor snapshots, approx. $3--5 | MOQ 1; QFN SMT | ACTIVE | MEDIUM | Design-review qualified |
| NVMe bridge | JMicron `JMS583-QHFA3A` | JLC exact `C25701682`, displayed $6.06 qty 1 but 0 stock; broker snapshots 1k--11k | Min 1 on JLC; SMT | Current catalogue candidate; exact lifecycle suffix confirmation required | HIGH | Preferred technical candidate; mask-ROM baseline CLOSED, authorized supply OPEN |
| Dual-protocol bridge alternative | JMicron `JMS581DL` | JLC assembly `C9900187649`; no dependable stock/price captured | 144TFBGA, X-ray required; assembly evidence only | Current official catalogue entry | HIGH | Rejected pending ball map, design pack and firmware; see `jms581dl/JMS581DL_REVIEW.md` |
| M-key socket | TE `1-2199230-4` | DigiKey exact MPN approx. $2.11, factory lead shown; TE directs availability inquiry | MOQ 1; SMT/reflow specified | ACTIVE | MEDIUM | Preferred connector; exact customer CAD/pad parity OPEN |
| SPI NVRAM | JMS583-compatible flash, exact device TBD by JMicron | no final price | TBD | TBD | HIGH | Do not select from a family guess |
| Mode control | power-off selector/jumper and buffer | commodity, <$1 estimate | MOQ 1; SMT | N/A | LOW | Implement after both bridge truth tables are documented |

## Alternatives

ASM2362 has apparent JLC assembly support but no public exact pin/land/
reference/firmware design pack. RTL9210B has community firmware/reference
material but no retained Realtek-authoritative bare-chip package and its
community ecosystem documents firmware instability risk. JMS586/JMS580 and
other families did not provide a better complete authority and firmware path.

## Cost delta

The earlier $20--30 additional-board estimate remains planning-only. Quote
the complete controller, selector, socket, flash, crystal, power, protection
and support BOM after firmware and connector CAD close. No purchase was made.

## Added support and mode-control items

| Function | Selected item | Evidence/price basis | Risk | Decision |
|---|---|---|---|---|
| JMS583 support | 25-MHz crystal, 12-kOhm 1% REXT, 4.7-uH inductor, decoupling, reset RC, VBUS divider, USB/PCIe AC caps | JMS583 Rev 2.1 retained authority; commodity planning values | MEDIUM | Materialized in schematic; exact BOM quote pending |
| Mode control | J4 power-off 3-position selector + SN74LVC1G17DBVR U14 | commodity planning estimate, MOQ 1 | LOW | FORCE_SATA / AUTO_PEDET / FORCE_NVME, common MODE_IN |

The factory mask-ROM JMS583 baseline does not require project-supplied SPI
firmware; external NVRAM remains DNP until a JMicron-authorized device is
selected. No purchase was made.
