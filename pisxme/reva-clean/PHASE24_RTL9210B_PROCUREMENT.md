# RTL9210B-CG procurement snapshot

Date checked: 2026-09-06.

Primary listing checked: https://jlcpcb.com/partdetail/RealtekSemicon-RTL9210BCG/C5143573
The listing identity is retained as the procurement lead. The public page
does not expose a reproducible live quantity-1 stock/price/lead-time receipt
in this environment, so no numeric availability claim is promoted.

| Source | Identity | Evidence | Risk |
|---|---|---|---|
| JLCPCB | RTL9210B-CG, C5143573, Realtek Semicon, QFN-68 | Current listing identity and PCBA/SMT suitability retained; live order flow is the required source for quantity and price | MEDIUM/HIGH: no reproducible quantity-1 price, stock depth, or lead time captured |
| HynixCJR CAD | RTL9210B-CG | Complete corroborating symbol/footprint/schematic; QFN 8x8, 0.4 mm pitch, EP 4.8 is represented | HIGH until independently recreated; source footprint has wrong through-hole attribute |
| Major distributors | Exact bare RTL9210B-CG | No traceable current DigiKey/Mouser/Arrow offer established in this pass | HIGH; do not assume second source |
| Community firmware | RTL9210B variants | Configs and binaries retained with commit hashes | HIGH for provenance/rights and exact variant match |

Planning cost: use a live JLC quote before BOM freeze. No verified quantity-1
price is claimed here. Add SPI flash, crystal, power filtering, SSD 3.3-V
delivery, and assembly escape cost; the single-chip reduction is likely
material but cannot be priced honestly from the retrieved page alone.
