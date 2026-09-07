# RTL9210B-CG procurement snapshot

Date checked: 2026-09-06. A live-page receipt is retained at
`authority-inventory/rtl9210b/RTL9210B_WEB_SOURCE_RECEIPT_20260906.md`.

Primary listing checked: https://jlcpcb.com/partdetail/RealtekSemicon-RTL9210BCG/C5143573
The current page identifies Realtek `RTL9210B-CG`, JLC part `C5143573`,
QFN-68, SMT assembly, Economic/Standard PCBA, and MSL 3. It also states that
JLC-held parts are for PCBA orders and cannot be shipped separately. The page
does not expose a reproducible live quantity-1 stock/price/lead-time receipt in
this environment, so no numeric availability claim is promoted. This is a
real PCBA sourcing lead, not proof of a standalone small-quantity chip lot.

| Source | Identity | Evidence | Risk |
|---|---|---|---|
| JLCPCB | RTL9210B-CG, C5143573, Realtek Semicon, QFN-68 | Current live listing confirms identity, QFN-68, SMT, Economic/Standard PCBA, MSL 3, and PCBA-only storage; receipt saved locally | MEDIUM/HIGH: no reproducible quantity-1 price, stock depth, or lead time captured; not a standalone chip-shipping path |
| HynixCJR CAD | RTL9210B-CG | Complete corroborating symbol/footprint/schematic; QFN 8x8, 0.4 mm pitch, EP 4.8 is represented | HIGH until independently recreated; source footprint has wrong through-hole attribute |
| Major distributors | Exact bare RTL9210B-CG | No traceable current DigiKey/Mouser/Arrow offer established in this pass | HIGH; do not assume second source |
| Community firmware | RTL9210B variants | Configs and binaries retained with commit hashes | HIGH for provenance/rights and exact variant match |

Planning cost: use a live JLC quote before BOM freeze. No verified quantity-1
price is claimed here. Add SPI flash, crystal, power filtering, SSD 3.3-V
delivery, and assembly escape cost; the single-chip reduction is likely
material but cannot be priced honestly from the retrieved page alone.
