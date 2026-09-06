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

SHA-256:

- `HD3SS6126-datasheet.pdf`: `ce9c29d4c051738737e76a24ca40202e926db58a8b4665581bf905a4bd11b2ee`
- `HD3SS3412-datasheet.pdf`: `4013014d39f23f4d4a42fe4f918e392339488542224ebb2cd67ecd536b14e0ef`
- `JAE-SM3-series-page.html`: acquisition returned HTTP 403 and no file was represented as a false capture.
- `ASMedia-ASM2362-product-page.html`: `da194e78a04f004d75c107ca6a21c9abf983ffd7876a94ab50f5376c7e549beb`

The source page contents were inspected through the browser and the relevant
claims are reproduced in the qualification and blocker records. Manufacturer
copyright and redistribution restrictions remain applicable.
