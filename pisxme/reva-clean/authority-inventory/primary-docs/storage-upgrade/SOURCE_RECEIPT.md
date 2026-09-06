# Storage upgrade source receipt

Checked 2026-09-06. Web captures are reference snapshots; refresh procurement
before a purchase.

| Authority | Local file | Source |
|---|---|---|
| TI TUSB9261 | existing `../bridge/TUSB9261-datasheet-revI.pdf`, implementation guide, firmware receipt | https://www.ti.com/product/TUSB9261 |
| TI HD3SS6126 | `ti-switches/HD3SS6126-datasheet.pdf` | https://www.ti.com/product/HD3SS6126 |
| TI HD3SS3412 | `ti-switches/HD3SS3412-datasheet.pdf` | https://www.ti.com/product/HD3SS3412 |
| JAE SM3 family | `jae-mkey/JAE-SM3-series-page.html` | https://www.jae.com/en/connectors/series/detail/id%3D64187%26application_code%3D%26order%5B%5D%3Dsubject%3Adesc |
| ASMedia ASM2362 | `asm2362/ASMedia-ASM2362-product-page.html` | https://www.asmedia.com.tw/product/Ee1YQF9sX7yyajH5/C5cYq34qpByQ6jm6.html |
| JLCPCB ASM2362 listing | `asm2362/JLCPCB-ASM2362-part-page.html` | https://jlcpcb.com/partdetail/ASMediaTech-ASM2362/C5121260 |
| JMicron JMS583 official product brief | `jms583/JMS583-product-brief-official-1046.pdf` | https://www.jmicron.com/file/download/1046/JMS583.pdf |
| JMicron JMS583 datasheet Rev 2.1 | `jms583/JMS583-datasheet-rev2.1.pdf` and text extraction | https://snapeda.s3.amazonaws.com/datasheets/2115-PDS-17001_JMS583_Datasheet_(Rev._2.1)_20190716.pdf |
| JLCPCB exact JMS583-QHFA3A | browser capture; `C25701682` | https://jlcpcb.com/partdetail/Jmicron-JMS583QHFA3A/C25701682 |
| TE exact M-key product page | `connectors/te/TE_MKEY_AUTHORITY.md` | https://www.te.com/de/product-1-2199230-4.html |
| TE M.2 application specification Rev C | `connectors/te/TE-114-115006-application-spec-revC.pdf` | https://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocFormat=pdf&DocLang=English&DocNm=114-115006&DocType=Specification+Or+Standard&PartCntxt=1-2199230-4 |
| TE exact customer 2D CAD | `connectors/te/cad/TE-1-2199230-4-2d-dxf.zip` | https://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocFormat=2d_dxf.zip&DocLang=English&DocNm=CVM_1-2199230-4&DocType=Customer+View+Model&PartCntxt=1-2199230-4 |
| JMicron JMS581DL official product brief | `jms581dl/JMS581DL-product-brief-official.pdf` | https://www.jmicron.com/file/download/1222/JMS581DL%2BProduct%2BBrief%2B%28Rev.1.00%29.pdf |
| JMicron JMS583 official product brief | `jms583/JMS583-product-brief-official-1046.pdf` | https://www.jmicron.com/file/download/1046/JMS583.pdf |
| JMicron JMS583 datasheet Rev 2.1 | `jms583/JMS583-datasheet-rev2.1.pdf` and text extraction | https://snapeda.s3.amazonaws.com/datasheets/2115-PDS-17001_JMS583_Datasheet_(Rev._2.1)_20190716.pdf |
| JLCPCB exact JMS583-QHFA3A | browser capture; `C25701682` | https://jlcpcb.com/partdetail/Jmicron-JMS583QHFA3A/C25701682 |
| TE exact M-key product page | browser capture; `TE_MKEY_AUTHORITY.md` | https://www.te.com/de/product-1-2199230-4.html |
| TE M.2 application specification Rev C | `connectors/te/TE-114-115006-application-spec-revC.pdf` | https://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocFormat=pdf&DocLang=English&DocNm=114-115006&DocType=Specification+Or+Standard&PartCntxt=1-2199230-4 |

SHA-256:

- `HD3SS6126-datasheet.pdf`: `ce9c29d4c051738737e76a24ca40202e926db58a8b4665581bf905a4bd11b2ee`
- `HD3SS3412-datasheet.pdf`: `4013014d39f23f4d4a42fe4f918e392339488542224ebb2cd67ecd536b14e0ef`
- `JAE-SM3-series-page.html`: acquisition returned HTTP 403 and no file was represented as a false capture.
- `ASMedia-ASM2362-product-page.html`: `da194e78a04f004d75c107ca6a21c9abf983ffd7876a94ab50f5376c7e549beb`
- `JLCPCB-ASM2362-part-page.html`: `424df54a72292b32fb560bda9a7b3cf1e6513f91812641648bca0f2a220a3bd1`
- `JMS583-product-brief-official-1046.pdf`: `c472cdcb93cc02eedcdb2e31256b48c95e601fe4a98b662ae627e6d695006824`
- `JMS583-datasheet-rev2.1.pdf`: `27a491efa2361a5b3363d61ebf43b0983ce0c2407a49a5e949a3ff9b83b88529`
- `TE-114-115006-application-spec-revC.pdf`: `3919d7af08573732ab864840b67a9a8520405a29e90d886ae5fef236d76586eb`
- `TE-1-2199230-4-lcsc-datasheet.pdf`: `0b5de10c795caabfc67fa71dfb909e6b1b5a154dd45551c41e9b89840807b234`
- `TE-1-2199230-4-2d-dxf.zip`: `89ab400716590e16d7b43165ecb0e4e7835bb6b0b077d00ecca7c9af1150b787`
- `JMS581DL-product-brief-official.pdf`: `4c7516711fda2483cb827cea543270063b5077192f377f1de7c23622bc0e77b`
- `JMS583-product-brief-official-1046.pdf`: `c472cdcb93cc02eedcdb2e31256b48c95e601fe4a98b662ae627e6d695006824`
- `JMS583-datasheet-rev2.1.pdf`: `27a491efa2361a5b3363d61ebf43b0983ce0c2407a49a5e949a3ff9b83b88529`
- `TE-1-2199230-4-lcsc-datasheet.pdf`: `0b5de10c795caabfc67fa71dfb909e6b1b5a154dd45551c41e9b89840807b234`

The source page contents were inspected through the browser and the relevant
claims are reproduced in the qualification and blocker records. Manufacturer
copyright and redistribution restrictions remain applicable.

Additional M-key observations:

- JAE's current product listing identifies `SM3ZS067U215BMR1500` as a
  67-position, 0.5-mm, 2.15-mm SMT M-key connector:
  https://products.jae.com/gl/en/connectors/content-library/featured-content/cadence_clarity/
- JAE family documentation identifies the U215 drawing family as
  `SJ113567/SJ113568`; the released exact pad/courtyard drawing still needs to
  be obtained for local parity before production replacement.
- DigiKey exact-family evidence exists for the corresponding JAE M-key U215
  series with MOQ 1 and quantity-1 pricing/stock snapshots. Exact
  `BMR1500` distributor confirmation remains a BOM-release check and is not
  inferred from a nearby suffix.

Additional ASM2362 procurement observation:

- JLCPCB lists `ASM2362` as part `C5121260`, QFN-64, for its economic and
  standard SMT assembly flow, and exposes an EasyEDA symbol/footprint link.
  This is useful procurement/assembly evidence, but it is not ASMedia-
  authoritative pinout, land-pattern, reference-circuit, firmware, or
  programming authority. It therefore does not close the NVMe bridge gate.
