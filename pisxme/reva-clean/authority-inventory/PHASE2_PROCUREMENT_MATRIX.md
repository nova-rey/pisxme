# PiSXMe Rev A Clean — Phase 2 procurement matrix

Snapshot date: 2026-08-29. Prices and stock are distributor snapshots, not
guarantees.

| Function | Selected item | LCSC/JLC | DigiKey / Mouser / other | MOQ / price snapshot | Risk / backup |
|---|---|---|---|---|---|
| SATA B-key M.2 socket | JAE `SM3ZS067U410ABR1000` | Exact LCSC/JLC stock not surfaced | DigiKey exact MPN active, 15-week lead; Mouser exact MPN 3,029 in stock plus 4,000 on order on captured page; exact 4.1 mm drawing link | MOQ 1 cut tape; Mouser about EUR1.35 qty1 / EUR0.832 qty1000 / reel 2,000 | MEDIUM; TE `1-2199119-0` technical backup, recheck availability |
| Ethernet ESD | TI `TPD4E004DRYR` | Exact LCSC/JLC buy not required | DigiKey 11,275; Mouser 29,014 | MOQ 1; DigiKey ~$1.58 qty1 and ~$0.473 qty1000; reel 5,000 | LOW; TI `TPD4E05U06DQAR` package alternative |
| SXM2 receptacle | Amphenol `74221-101LF` | Direct assembly not evidenced | Official Amphenol page showed Mouser 312; JAK 2,586, MOQ1, ~$29.17 qty1, 8-week factory lead | MOQ 1; ~$27–29 each small quantity | MEDIUM/HIGH due cost, hidden-joint SMT, and lead; no drop-in assumed |
| USB-to-SATA bridge | TI `TUSB9261IPVP`, 64-HTQFP/PVP 7x7 | Exact LCSC/JLC buy not required | DigiKey exact record 2,107 in stock; Mouser exact record 469 in stock | MOQ 1; DigiKey ~$10.75 qty1 / ~$6.52 qty1000; Mouser ~$7.73 qty1 / ~$4.55 qty1000; standard pack 250 | MEDIUM due 26-week factory lead; TI `TUSB9261IPAPRQ1` is a non-drop-in automotive/package alternative |
| JMS578 evaluated/rejected | JMicron `JMS578` QFN48 6x6 | LCSC C17700079, MOQ1, ~$0.495 qty1 / ~$0.188 qty1000, **out of stock** | No dependable exact major-distributor record found | Catalog price only; no reliable lead time | HIGH / rejected |
| ASM1153E evaluated/rejected | ASMedia `ASM1153E` QFN48 6x6 | No exact current stock found | No dependable exact major-distributor record found | No reliable quote | HIGH / rejected; module evidence documents no TRIM |
| CM5 carrier connector | `10164227-1001A1RLF` | Not required; major-distributor procurement is stronger | Amphenol Active/Stocked; DigiKey 8,092 and Newark 9,449 captured | MOQ 1 cut tape; about $1.77 DigiKey / $2.10 Newark qty1; 9-week Newark lead | LOW/MEDIUM; do not substitute 1004 without drawing check |
| Ethernet MagJack | EDAC `A70-112-331N126` | Exact JLC/LCSC stock not captured; THT mixed-assembly part | Mouser exact record: 1,203 in stock, MOQ 1; EDAC drawing; DigiKey exact record; LPJG0926HENL manufacturer-direct backup | $6.97 qty1 / $5.52 qty100 / $4.12 qty1000; 20-week factory lead | MEDIUM; selected; generate EDAC layout; LPJG0926HENL backup |
| USB2 SERVICE receptacle | Amphenol `10171746-00021LF` | Exact LCSC listing found; no dependable stock snapshot used | Manufacturer page: stocked; Mouser 12,763, DigiKey 4,688, Newark 1,180, Arrow 935; exact drawing | MOQ 1 cut tape; about $0.79 manufacturer/DigiKey, $0.85 Newark; reel 12,000 | LOW; selected; ordinary SMT; parametric USB-C substitute only after mechanical check |
| USB2 SERVICE ESD | TI `TPD2EUSB30DRTR` | Exact LCSC listing not used as closure basis | DigiKey 46,516, Mouser-indexed 90,983; TI active catalog and datasheet | MOQ 1; about $1.18 DigiKey / $0.57 Mouser qty1; reel 3,000 | LOW electrical/procurement; DRT land-pattern gate remains open |
| Dual 12 V input headers | Molex `0039300020` / `39-30-0020`, two units | Not a JLC basic SMT part; use through-hole/hand or selective solder | Molex active 5569 series; DigiKey exact-family record 87,237, MOQ 1; Mouser exact family 22,793, MOQ 1; Newark 4,922, min 10 | About $0.75 DigiKey qty1, EUR0.62 Mouser qty1, $1.13 Newark qty10; 4.20 mm pitch | LOW sourcing / MEDIUM assembly; 5557 receptacle and 5556 terminals are mating-side backups |
| Branch fuse + holder | Littelfuse `0297015.U` + `178.6165.0001`, two branch sets | Not a JLC basic SMT part; through-hole serviceable holder | DigiKey exact fuse 24,049; Mouser exact holder 14,956; Littelfuse product/drawing authority | Fuse about $0.46 qty1 / $0.2066 qty1000; holder about $4.78 qty1 / $2.32 qty5000; MOQ 1 | LOW sourcing / MEDIUM assembly; rating and thermal derating remain Phase 5 calculations |
| CM5IO MagJack reference | Trxcom `TRJG0926HENL` | JLC exact extended `C9900198333`, 0 stock | Manufacturer page only; no dependable mainstream stock | JLC internal assembly price $0.0392, minimum 444, full reel 500; consign-only | HIGH; rejected as production item |
| Six-layer fabrication | `JLC06161H-7628` | JLC current public stack/calculator | JLC direct | Quote/coupon required; not a component | LOW for stack authority, normal fab tolerance risk |

The JMS578 catalog price was not treated as procurement success. The selected
TUSB9261IPVP has exact active buy paths at two major distributors and TI-hosted
firmware/programming resources. Phase 2 result: `PHASE2_AUTHORITY_CLOSED`.
