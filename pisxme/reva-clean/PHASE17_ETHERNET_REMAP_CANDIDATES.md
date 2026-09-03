# Phase 17 Ethernet remap candidates

Date: 2026-09-03

## Authority boundary

The CM5 datasheet is authoritative for the BCM54210PE feature summary:
automatic MDI crossover, pair-skew correction, and pair-polarity correction.
The official CM5IO reference is authoritative for the board-level wiring:
four intact `TRD0` through `TRD3` differential pairs to a standard 1:1
MagJack. No public BCM54210PE-specific register map or application schematic
was found that authorizes arbitrary four-pair reassignment at the PCB.

MDI/MDIX is not a general four-pair router. At 1000BASE-T all four pairs are
bidirectional, so the familiar 10/100 TX/RX pair swap cannot be expanded into
an arbitrary physical permutation. Polarity correction applies only to the
two conductors of an intact pair. Pair-skew correction changes timing
alignment; it does not make crossing copper acceptable.

## Candidate matrix

| ID | Physical mapping | Evidence class | Disposition |
|---|---|---|---|
| `REF_1TO1` | TRD0→pair 0, TRD1→pair 1, TRD2→pair 2, TRD3→pair 3; P/N straight | Raspberry Pi CM5IO reference | Authoritative baseline |
| `PAIR_SWAP_01` | Complete TRD0↔TRD1 pair units; TRD2/3 unchanged | Generic MDI/MDIX interpretation only | Disposable experiment only |
| `PAIR_SWAP_23` | Complete TRD2↔TRD3 pair units; TRD0/1 unchanged | Generic MDI/MDIX interpretation only | Disposable experiment only |
| `PAIR_SWAP_BOTH` | Complete TRD0↔TRD1 and TRD2↔TRD3 pair units | Generic 1000BASE-T MDI-X pattern, not BCM54210PE-specific | Disposable experiment only |
| `PAIR_PERMUTE_ARBITRARY` | Any other complete-pair permutation | No exact-device authority | Rejected |
| `CONDUCTOR_MIX` | Any conductor split across pairs | Violates pair integrity | Rejected |

For each conditional candidate, either P/N orientation may be considered only
as an intact-pair inversion. It is not a license to exchange one conductor
with another pair. A candidate would still need exact PHY-specific proof and
the complete native DRC/length/reference/connector-launch gate before it could
affect clean authority.

## Result

The remap hypothesis does not currently close the Phase 17 blocker. The only
authoritative production mapping remains `REF_1TO1`; the conditional pair
swaps are not sufficiently documented to accept as a new Rev-A empirical
risk, and they do not establish that the CM5/J7-to-MagJack crossing geometry
is electrically legal. No clean PCB or schematic was modified.

Sources:

- Raspberry Pi CM5 datasheet, Ethernet section: <https://pip.raspberrypi.com/categories/944-raspberry-pi-compute-module-5/documents/RP-008180-DS/cm5-datasheet.pdf>
- Raspberry Pi CM5IO design files: <https://pip.raspberrypi.com/categories/1098-design-files>
- Raspberry Pi CM5IO datasheet: <https://pip-assets.raspberrypi.com/categories/1097-raspberry-pi-compute-module-5-io-board/documents/RP-008182-DS-2-cm5io-datasheet.pdf>
- Broadcom BCM54210 product authority: <https://www.broadcom.com/products/ethernet-connectivity/phy-and-poe/copper/gigabit/bcm54210>
- IEEE 802.3ab standard landing page: <https://standards.ieee.org/ieee/802.3ab/1086/>
