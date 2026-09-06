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

SHA-256:

- `HD3SS6126-datasheet.pdf`: `ce9c29d4c051738737e76a24ca40202e926db58a8b4665581bf905a4bd11b2ee`
- `HD3SS3412-datasheet.pdf`: `4013014d39f23f4d4a42fe4f918e392339488542224ebb2cd67ecd536b14e0ef`
- `JAE-SM3-series-page.html`: acquisition returned HTTP 403 and no file was represented as a false capture.
- `ASMedia-ASM2362-product-page.html`: `da194e78a04f004d75c107ca6a21c9abf983ffd7876a94ab50f5376c7e549beb`
- `JLCPCB-ASM2362-part-page.html`: `424df54a72292b32fb560bda9a7b3cf1e6513f91812641648bca0f2a220a3bd1`

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
