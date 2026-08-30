# PiSXMe Rev A Clean — Phase 2 authority inventory

Date: 2026-08-29  
Gate: `PHASE2_AUTHORITY_CLOSED`

This is the final Phase 2 authority disposition for this sprint. No clean
schematic or clean PCB was modified. Legacy and CM5IO designs remain
reference-only.

## Authority dispositions

| Authority | Disposition | Selected authority / exact reference | Decision closed |
|---|---|---|---|
| SATA M.2 socket | `CLOSED` | JAE `SM3ZS067U410ABR1000`, B-key, 67-position, 4.10 mm | SATA-capable 2280 socket; optional 2242 retention datum |
| SXM2 connector identity | `CLOSED` | Amphenol `74221-101LF`, Rev-W drawing/product page | 400-position, 1.27 mm array, 4 mm receptacle identity |
| SXM2 local land-pattern reuse | `REV_A_EMPIRICAL_RISK` | Manufacturer Rev-W drawing is authority; legacy footprint is comparison-only | Phase 3 must regenerate and pad-by-pad compare mask/paste/A1/courtyard |
| V100 cooler/backplate | `REV_A_EMPIRICAL_RISK` | Conservative 150 x 95 mm XY plus +45 mm top reservation and matching underside reservation | Safe Rev-A collision envelope without claiming proprietary CAD fit |
| Ethernet ESD | `CLOSED` | TI `TPD4E004DRYR`, active, 4-channel, 1.6 pF, 6-pin SON | CM5IO-derived copper MagJack protection choice |
| SATA bridge | `CLOSED` | TI `TUSB9261IPVP`, active 64-pin HTQFP/PVP, 7 x 7 mm | Replaces JMS578 after exact procurement, firmware, package, and behavior review |
| JMS578 evaluation | `REJECTED` | JMicron `JMS578`, QFN-48 6 x 6, brief Rev 1.0.1 | LCSC exact listing out of stock; firmware/configuration and Linux discard evidence inadequate |
| ASM1153E evaluation | `REJECTED` | ASMedia `ASM1153E`, QFN-48 6 x 6 | No materially better bare-chip procurement/firmware path; module evidence documents no TRIM |
| Current JLC six-layer stack | `CLOSED` | `JLC06161H-7628`, 1.6 mm class, 1 oz outer / 0.5 oz inner, ordinary through vias | Reproducible 90/100-ohm calculator basis saved locally |
| CM5 carrier connector | `CLOSED` | Amphenol `10164227-1001A1RLF`, manufacturer page/drawing plus live DigiKey/Newark records | Do not substitute the old 1004 placeholder without drawing check |
| Ethernet MagJack | `REV_A_EMPIRICAL_RISK` | CM5IO `TRJG0926HENL` is reference-only; JLC extended listing is currently unavailable and no authoritative manufacturer record was found | Phase 3 must select a fully documented mechanical/electrical replacement or obtain a manufacturer/sample authority |

## Evidence index

- CM5IO Rev 2 archive: `cm5io-rev2/`, extracted from official archive;
  SHA-256 `48b14a6757b0edc0ac110331445f35a4212b5ce432bdcec6605c99431b59496b`.
- JMicron brief: `primary-docs/JMS578.pdf`, SHA-256
  `3c59d77780a50314462e8967ec91e9fe532d1356becd31a7b9945b66410e1ae0`.
- M.2: `primary-docs/m2-jse/M2_SOCKET_AUTHORITY.md`, SATA-IO TP053v11,
  exact-MPN JAE/Mouser drawing URL, TE family drawing, and JAE series bulletin.
- SXM2: `primary-docs/sxm2/SXM2_74221-101LF_AUTHORITY.md` and
  `primary-docs/sxm2/SXM2_SOURCE_RECEIPT.md`; the Rev-W manufacturer drawing
  remains the authority and the legacy geometry remains comparison-only.
- Ethernet ESD: `primary-docs/ethernet-esd/TPD4E004.pdf` and
  `TPD4E004_AUTHORITY.md`.
- Fabrication: `primary-docs/jlc/JLC06161H-7628_IMPEDANCE_BASIS.md` and
  `JLC06161H-7628_IMPEDANCE_INPUTS.md`; the current public calculator and
  guide URLs are recorded there.
- Supporting CM5 component authority: `primary-docs/cm5io-component-authority.md`.
- Mechanics: `primary-docs/mechanics/V100_COOLER_BACKPLATE_AUTHORITY.md`.
- Bridge: `primary-docs/bridge/SATA_BRIDGE_AUTHORITY.md`,
  `primary-docs/bridge/TUSB9261_FIRMWARE_RECEIPT.md`, and
  `primary-docs/tusb9261/`.

## Gate rationale

The previous JMS578 blocker is resolved by an explicit replacement: TI
`TUSB9261IPVP`. TI publishes the exact active device/package authority,
implementation guide, EVM guide, default firmware resources, and FlashBurner
utility; DigiKey and Mouser both show current exact-MPN stock. JMS578 remains
rejected, not silently substituted. Phase 7 still owns actual Linux
UAS/BOT/TRIM/suspend/reset testing against the selected firmware and SSD.

The cooler, local SXM2 pattern, and exact legacy MagJack procurement are explicitly classified as
`REV_A_EMPIRICAL_RISK`, with the public-source reason and required physical or
pad-by-pad/replacement verification recorded. The MagJack classification is
not being used to excuse an obtainable datasheet: the exact manufacturer
identity and lifecycle record were not publicly recoverable, and JLC reports
the extended listing unavailable. No other datasheet or procurement question
was hidden under that label.

## Source URLs

- [JMicron JMS578](https://www.jmicron.com/products/list/1)
- [LCSC JMS578 exact listing](https://www.lcsc.com/product-detail/C17700079.html)
- [ASMedia ASM1153E](https://www.asmedia.com.tw/Web2/product/7B6yQ54sX7YiFhGD/d1Eyq85QN8GhBwRC.html)
- [JAE](https://www.jae.com/en/)
- [TE M.2 application specification](https://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocFormat=pdf&DocLang=English&DocNm=114-115006&DocType=Specification+Or+Standard&PartCntxt=1-2199119-0)
- [Amphenol 74221-101LF](https://www.amphenol-cs.com/product/74221101lf.html)
- [TI TPD4E004DRYR](https://www.ti.com/product/TPD4E004/part-details/TPD4E004DRYR)
- [Current JLC six-layer stack](https://jlcpcb.com/impedance)
- [Current JLC calculator guide](https://jlcpcb.com/help/article/user-guide-to-the-jlcpcb-impedance-calculator)

## Stop rule

`PHASE2_AUTHORITY_CLOSED`. The Phase 2 authority gate is now closed. The next
permitted work is Phase 3 schematic architecture and library isolation; it
must use `TUSB9261IPVP`, its 1.1 V/3.3 V rails, SPI flash, 40 MHz clock, reset
requirements, and the TI USB/SATA routing constraints recorded locally.
