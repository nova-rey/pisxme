# PiSXMe Rev A Clean — Phase 2 closure receipt

Checked: 2026-08-30. This receipt records why the gate is allowed to pass under
the explicit rule: every required authority is `CLOSED` or explicitly
`REV_A_EMPIRICAL_RISK`. It does not claim fabricated-hardware validation.

| Requirement | Current disposition | Proof |
|---|---|---|
| SATA M.2 B-key socket | `CLOSED` | JAE exact local drawing plus JAE bulletin, Mouser/DigiKey procurement, SATA-IO TP053v11 mapping |
| SXM2 connector identity | `CLOSED` | Amphenol active product and Rev-W drawing receipt |
| SXM2 clean land-pattern transplant | `REV_A_EMPIRICAL_RISK` | Manufacturer drawing exists; legacy geometry is comparison-only and Phase 3 must regenerate/pad-compare |
| V100 cooler/backplate | `REV_A_EMPIRICAL_RISK` | Public production CAD unavailable; measured conservative envelope is sufficient for Rev-A collision control |
| Ethernet ESD | `CLOSED` | TI active `TPD4E004DRYR`, 1.6 pF/channel, four-line SON authority and multi-distributor evidence |
| SATA bridge | `CLOSED` | Active exact `TUSB9261IPVP`, two major distributors, TI datasheet/implementation/EVM/firmware-tool records |
| JMS578 / ASM1153E | `REJECTED` | Exact bare-chip procurement and firmware/Linux evidence fail; rejection and replacement are explicit |
| Current JLC six-layer stack and impedance basis | `CLOSED` | Current JLC API response saved locally for exact `JLC06161H-7628`; current calculator guide accepts the 90/100-ohm targets; Phase 13 owns route geometry/coupon |
| CM5 carrier connector | `CLOSED` | Amphenol active authority and DigiKey/Newark stock evidence |
| Exact legacy CM5IO MagJack | `REV_A_EMPIRICAL_RISK` | JLC exact listing is unavailable/consign-only and no authoritative manufacturer/lifecycle record was found |

The three empirical-risk classifications are permitted residual physical or
legacy-endpoint uncertainty, not substitutes for obtainable semiconductor,
connector drawing, or calculator authority. The next gate may start only after
this receipt and the inventory/matrix agree.
