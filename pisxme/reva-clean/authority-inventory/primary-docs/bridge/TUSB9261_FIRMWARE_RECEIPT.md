# TUSB9261 firmware and programming receipt

Retrieved/verified: 2026-08-29.

TI product page: <https://www.ti.com/product/TUSB9261>

| TI resource | Version / date | Purpose | Local evidence |
|---|---|---|---|
| SLLC416 | 01.00.00.0M / 2018-09-03 | Default firmware, U1/U2 disabled | TI download page verified; ZIP requires TI export approval |
| SLLC421 | 01.00.00.0D / 2012-08-27 | Firmware, U1/U2 enabled | TI download page verified; ZIP URL recorded, not locally fetched |
| SLLC414 | 01.00.00.0E / 2013-10-24 | TUSB926x FlashBurner Utility | TI download page verified; ZIP requires TI export approval |

Download pages: <https://www.ti.com/tool/download/SLLC416>,
<https://www.ti.com/tool/download/SLLC421>, and
<https://www.ti.com/tool/download/SLLC414>. The old `lit/zip` links redirect
to the gated TI download workflow. No HTML error response is represented as a
firmware ZIP in the repository.

Programming model: attach SPI flash to `SPI_CS0`, load the TI default image
with FlashBurner through the documented USB/programming path, and retain the
firmware version and checksum in the manufacturing record. The chip ROM loads
the image from SPI after reset. Custom descriptors/GPIO behavior are not
needed for the initial Rev-A storage path.

The selected initial policy is SLLC416 (U1/U2 disabled), with TI's default
USB UASP/BOT and SATA AHCI behavior. Phase 7 must qualify `fstrim`, UAS
enumeration, stress I/O, USB reset, suspend/resume, and cold power-cycle
recovery on the actual CM5 image and selected M.2 SATA SSD. TI documents UASP,
BOT, SATA port reset/OOB negotiation, and the minimum 2 ms global reset, but
does not claim Linux discard semantics; that is intentionally a validation
item rather than an invented authority claim.

Provenance: TI-hosted product, firmware, programming-tool, datasheet,
implementation-guide, and DEMO-guide pages. The gated binary resources are
not redistributed here.
