# PiSXMe Rev A Clean — Phase 3 authority manifest

| Asset / contract | Authority | Local evidence | Status |
|---|---|---|---|
| CM5 pinout/carrier | Raspberry Pi CM5/CM5IO | `authority-inventory/primary-docs/cm5io-datasheet.pdf` and archive | selected reference |
| SXM2 connector | Amphenol `74221-101LF`, Rev-W | `authority-inventory/primary-docs/sxm2/` | identity closed; land-pattern review required |
| SATA M.2 mapping | SATA-IO TP053v11 | `authority-inventory/primary-docs/m2-jse/SATA-IO-TP053v11-M2-card-format.pdf` | closed |
| SATA M.2 socket | JAE `SM3ZS067U410ABR1000` | `authority-inventory/primary-docs/m2-jse/` | closed; regenerate footprint |
| USB/SATA bridge | TI `TUSB9261IPVP` | `authority-inventory/primary-docs/bridge/`, `tusb9261/` | closed; Phase 7 Linux validation remains |
| Ethernet ESD | TI `TPD4E004DRYR` | `authority-inventory/primary-docs/ethernet-esd/` | closed |
| MagJack | EDAC `A70-112-331N126`; CM5IO topology only for net mapping | `authority-inventory/primary-docs/ethernet-magjack/EDAC_A70-112-331N126_AUTHORITY.md` plus CM5IO authority | selected; regenerate EDAC manufacturer land pattern; legacy footprint comparison only |
| Cooler/backplate | conservative clean-room envelope | `authority-inventory/primary-docs/mechanics/` | Rev-A empirical risk |
| Six-layer stack | JLC `JLC06161H-7628` | `authority-inventory/primary-docs/jlc/` | stack closed; solver/coupon later |

All donor assets must be copied individually into the clean namespace only
after source, hash, footprint pads, model path, and pin/pad mapping are recorded.
