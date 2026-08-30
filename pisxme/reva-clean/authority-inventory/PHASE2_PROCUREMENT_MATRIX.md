# PiSXMe Rev A Clean — Phase 2 procurement matrix

Snapshot date: 2026-08-29. Prices and stock are distributor snapshots, not
guarantees.

| Function | Selected item | LCSC/JLC | DigiKey / Mouser / other | MOQ / price snapshot | Risk / backup |
|---|---|---|---|---|---|
| SATA B-key M.2 socket | JAE `SM3ZS067U410ABR1000` | Exact LCSC/JLC stock not surfaced | DigiKey active, 15-week standard lead; Mouser 0 stock / 5,663 on order | MOQ 1 cut tape; about $1.57 qty1; full reel 2,000 at ~$0.883 | MEDIUM; TE `1-2199119-0` technical backup, recheck availability |
| Ethernet ESD | TI `TPD4E004DRYR` | Exact LCSC/JLC buy not required | DigiKey 11,275; Mouser 29,014 | MOQ 1; DigiKey ~$1.58 qty1 and ~$0.473 qty1000; reel 5,000 | LOW; TI `TPD4E05U06DQAR` package alternative |
| SXM2 receptacle | Amphenol `74221-101LF` | Direct assembly not evidenced | Official Amphenol page showed Mouser 312; JAK 2,586, MOQ1, ~$29.17 qty1, 8-week factory lead | MOQ 1; ~$27–29 each small quantity | MEDIUM/HIGH due cost, hidden-joint SMT, and lead; no drop-in assumed |
| JMS578 bare bridge | JMicron `JMS578` QFN48 6x6 | LCSC C17700079, MOQ1, ~$0.495 qty1 / ~$0.188 qty1000, **out of stock** | No dependable exact DigiKey/Mouser/Arrow/Newark record found | Catalog price only; no reliable lead time | HIGH / BLOCKED; assembled certified module or remove bridge |
| ASM1153E bare bridge | ASMedia `ASM1153E` QFN48 6x6 | No exact current stock found | No dependable exact major-distributor record found | No reliable quote | HIGH / rejected; StarTech module documents no TRIM |
| CM5 carrier connector reference | `10164227-1001A1RLF` | Official CM5IO archive only | Archive includes STEP/footprint; clean procurement recheck required | Not quoted in this sprint | MEDIUM; do not substitute 1004 without drawing check |
| CM5IO Ethernet MagJack reference | `TRJG0926HENL` | Official archive only | Archive includes STEP/footprint | Not quoted in this sprint | MEDIUM; revalidate active supply before BOM freeze |
| Six-layer fabrication | `JLC06161H-7628` | JLC current public stack/calculator | JLC direct | Quote/coupon required; not a component | LOW for stack authority, normal fab tolerance risk |

The JMS578 catalog price is not procurement success. The Phase 2 result is
`PHASE2_AUTHORITY_BLOCKED` until that row has a real buyable and programmable
solution.
