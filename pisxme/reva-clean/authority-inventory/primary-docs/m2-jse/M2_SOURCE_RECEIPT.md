# M.2 source receipt

Checked: 2026-08-29.

- JAE manufacturer series bulletin: local
  `JAE-SM3-series-bulletin.pdf`, SHA-256
  `d8be12322c2c68a462fae3578cf27fb799bd87423ba8599fad31ef0cfb87a8a0`.
- Exact-MPN distributor drawing:
  https://www.mouser.com/catalog/specsheets/SM3%20drawing%204.1.pdf
  (JAE drawing title `SM3ZS067U410`, 4.10 mm variant; one page; accessed via
  Mouser exact MPN `SM3ZS067U410ABR1000`). A direct local CDN download was
  unavailable, so the URL and extracted dimensions are retained here rather
  than claiming a fabricated local PDF.
- Exact-MPN procurement page:
  https://www.mouser.de/en/ProductDetail/JAE-Electronics/SM3ZS067U410ABR1000
  (captured exact MPN, active stock snapshot, MOQ 1, factory pack 2,000, and
  ECAD-model link).
- SATA-IO authority: local `SATA-IO-TP053v11-M2-card-format.pdf`, SHA-256
  `9d419572e7fba7cf1c7b1207f38cae3c47c04210695293fb516c484b4fd09abf`.

The selected clean interface is Socket 2 / B-key / SATA-only. SATA device
pairs are pins 41/43 and 47/49; the key notch is pins 12--19. The CM5IO
`MTSSD03-67MSW337` model remains reference-only and is not electrically or
mechanically substituted.
