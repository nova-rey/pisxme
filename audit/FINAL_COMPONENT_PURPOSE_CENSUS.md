# Final component-purpose census

All 54 active PCB footprints are listed. “Remove candidate” means a future
variant question, not authorization to modify the active board.

| Ref | Part/value | Block | Purpose | Required? | Historical origin | Remove candidate? |
|---|---|---|---|---|---|---|
| J1 | Amphenol 74221-101LF | SXM2 | One V100 module receptacle | Yes | SXM2 interface | No |
| J2 | 2× Amphenol 10164227-1004A1RLF | CM5 | CM5 host connectors | Yes | CM5 carrier | No |
| J3,J4 | Molex 39301082 | 12 V input | Dual high-current input | Yes | power architecture | No |
| J5,J6 | Molex 22-23-2041 | cooling | Four-wire fan headers | Yes | cooling contract | No |
| J7 | Molex 22-23-2041 | cooling | Optional pump/auxiliary fan | Intentional | cooling contract | Optional |
| J8 | JST B4B-PH-K-S | debug | Internal UART | Yes | bring-up contract | Optional only after hardware maturity |
| J9,J10 | Amphenol 10137064-00011LF | FAST USB3 | USB-C external fast host ports | Current design yes | modular Type-C decision | Future USB-A variant candidate |
| J11 | Amphenol 10171746-00021LF | SERVICE | USB2 DRP/service port | Yes | recovery/service requirement | No |
| U1 | TPSM63606RDLR | CM5 power | CM5 5 V buck | Yes | power tree | No |
| U2,U3 | LM74700QDBVRQ1 | 12 V protection | ideal-diode/reverse protection | Yes | power tree | No |
| U4,U8 | TPS25821DSSR | FAST USB3 power | Type-C host VBUS/source control | Current Type-C design yes | modular Type-C decision | Removed in fixed-host Type-A variant |
| U5,U9 | HD3SS3212IRKSR | FAST USB3 | reversible SuperSpeed mux | Current Type-C design yes | Type-C orientation requirement | Removed in fixed-host Type-A variant |
| U6,U7,U10,U11 | TPD4EUSB30 | FAST USB3 | four-line ESD arrays for Type-C orientations | Current protection yes | Type-C branch implementation | Reduce/re-evaluate in Type-A variant |
| U12 | TUSB320LAIRWBR | SERVICE | USB-C DRP/CC controller | Yes | service recovery design | No |
| U13 | TPS2553DBVR | SERVICE | USB2 VBUS limiter | Yes | service power safety | No |
| U14 | SN74LVC1G04DCKR | SERVICE | VBUS role interlock inverter | Yes | service dual-role design | No |
| U15 | TPD2EUSB30A | SERVICE | USB2 ESD | Yes | service protection | No |
| U16 | TPSM63606RDLR | USB power | dedicated USB peripheral 5 V buck | Yes | modular USB power budget | No |
| U17,U18 | TPD2EUSB30A | FAST USB3 | USB2 companion ESD | Current Type-C design yes | fast-port protection | Re-evaluate in Type-A variant |
| Q1,Q2 | CSD19536KCS | 12 V protection | low-loss power MOSFETs | Yes | ideal-diode path | No |
| F1,F2 | Littelfuse 178.6165.0001 / 0297015.U | 12 V input | per-input fusing | Yes | high-current safety | No |
| C1,C2 | GRM21BR71H224KA01# | PCIe | V100 TX AC coupling | Yes | PCIe endpoint contract | No |
| C3,C4 | 10 uF 50 V | buck input | local buck input bypass | Yes | regulator layout | No |
| C5,C6 | 22 uF 25 V | buck output | local buck output bypass | Yes | regulator layout | No |
| C7 | 100 nF VLDOIN | CM5 power | regulator VLDOIN bypass | Yes | TI layout | No |
| C8,C9 | 100 nF LM74700 VCAP | 12 V protection | controller charge-pump bypass | Yes | ideal-diode layout | No |
| R1 | 0R CLKREQ link | PCIe control | documented DNP/POP option | Intentional option | PCIe bring-up | Yes, if strap is frozen |
| R2 | 40.2 k | CM5 power | buck feedback | Yes | regulator setting | No |
| R3 | 10.0 k | CM5 power | buck feedback | Yes | regulator setting | No |
| R4 | 13.0 k | CM5 power | buck RT | Yes | regulator setting | No |
| R5,R6 | 100 k | FAST USB3 | TPS25821 REF support | Current Type-C design yes | Type-C controller support | Removed with Type-C path |
| R7 | 52.3 k | SERVICE | TPS2553 current limit | Yes | service power safety | No |
| D1 | SMBJ18A | 12 V input | provisional un-netted TVS placeholder | Unknown/provisional | source protection study | Yes after replacement/provenance closure |
| TP1 | PERST# marker | debug | low-speed reset observation | Optional intentional | bring-up | Optional |
| TP2 | REFCLK marker | debug | documentation/access marker without probe stub | Optional intentional | bring-up | Optional |
| TP3 | nRPIBOOT marker | recovery | internal CM5 recovery access | Yes for recovery | bring-up contract | No |
| MECH1 | V100/SXM2 envelope | mechanical | cooler/backplate contract | Intentional mechanical | mechanical validation | Not a BOM item; may be omitted from release library |

The grouped rows expand to 54 physical references. No footprint’s only reason
was an x16 carrier, second GPU, NVLink, card-edge, Ethernet, HDMI, MIPI, or
microSD feature. The Type-C-specific rows are the only broad simplification
cluster identified.
