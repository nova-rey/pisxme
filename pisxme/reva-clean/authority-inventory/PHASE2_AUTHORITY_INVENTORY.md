# PiSXMe Rev A Clean — Phase 2 authority inventory

Date: 2026-08-29  
Gate: `PHASE2_AUTHORITY_BLOCKED`

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
| JMS578 / SATA bridge | `BLOCKED` | JMicron `JMS578`, QFN-48 6 x 6, brief Rev 1.0.1 | Electrical candidate only; bare-chip procurement and firmware ecosystem not closed |
| ASM1153E alternative | `REJECTED_FOR_CLOSURE` | ASMedia `ASM1153E` | No better bare-chip procurement/firmware path; known module TRIM limitation |
| Current JLC six-layer stack | `CLOSED` | `JLC06161H-7628`, 1.6 mm class, 1 oz outer / 0.5 oz inner, ordinary through vias | Reproducible 90/100-ohm calculator basis saved locally |
| CM5 carrier connector | `CLOSED_FOR_REFERENCE` | Official CM5IO archive `10164227-1001A1RLF` and local STEP | Do not substitute the old 1004 placeholder without drawing check |
| Ethernet MagJack | `CLOSED_FOR_REFERENCE` | Official CM5IO `TRJG0926HENL`, footprint and STEP in archive | Clean BOM must revalidate lifecycle/stock |

## Evidence index

- CM5IO Rev 2 archive: `cm5io-rev2/`, extracted from official archive;
  SHA-256 `48b14a6757b0edc0ac110331445f35a4212b5ce432bdcec6605c99431b59496b`.
- JMicron brief: `primary-docs/JMS578.pdf`, SHA-256
  `3c59d77780a50314462e8967ec91e9fe532d1356becd31a7b9945b66410e1ae0`.
- M.2: `primary-docs/m2-jse/M2_SOCKET_AUTHORITY.md`, TE family drawing, and
  JAE series bulletin.
- SXM2: `primary-docs/sxm2/SXM2_74221-101LF_AUTHORITY.md` and
  `primary-docs/sxm2/SXM2_SOURCE_RECEIPT.md`.
- Ethernet ESD: `primary-docs/ethernet-esd/TPD4E004.pdf` and
  `TPD4E004_AUTHORITY.md`.
- Fabrication: `primary-docs/jlc/JLC06161H-7628_IMPEDANCE_BASIS.md` and the
  locally saved current calculator page.
- Mechanics: `primary-docs/mechanics/V100_COOLER_BACKPLATE_AUTHORITY.md`.
- Bridge gap: `primary-docs/bridge/JMS578_PROCUREMENT_AND_FIRMWARE_EVIDENCE.md`.

## Gate rationale

The gate is blocked by one exact unresolved authority: a bare JMS578 cannot be
released because the exact current buy path is not dependable and the public
firmware/configuration ecosystem does not provide an image, configuration
format, redistribution rights, or device-specific Linux/UAS/TRIM/reset proof.
The LCSC listing proves catalog existence, not obtainable supply. ASM1153E does
not remove that blocker. The practical replacement is a purchased, assembled
USB-to-M.2-SATA module with explicit firmware/Linux support, or removal of
integrated SATA bridging from Rev A; either requires an explicit architecture
decision before Phase 3.

The cooler and local SXM2 pattern are explicitly classified as
`REV_A_EMPIRICAL_RISK`, with the public-source reason and required physical or
pad-by-pad verification recorded. No datasheet or procurement question was
hidden under that label.

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

`PHASE2_AUTHORITY_BLOCKED`. Do not begin Phase 3 schematic synthesis, clean
PCB placement, footprint transplant, or routing until the JMS578 blocker is
resolved by an exact purchasable/programmable bridge choice or an explicit
architecture replacement decision.
