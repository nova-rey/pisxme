# Phase 18 USB3 routing receipt

Status: `PHASE18_USB3_LOCAL_CANDIDATE_PASS_WITH_INHERITED_BASELINE`

Candidate: `ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb`

## Authority and mapping

The native schematic export `phase18-net.xml` proves the role-correct USB
device-link mapping:

| CM5/J7 | TUSB9261 U7 | Copper contract |
|---|---:|---|
| USB3 RX_N pad 128 | USB_SSTXM pin 42 | pair preserved |
| USB3 RX_P pad 130 | USB_SSTXP pin 43 | pair preserved |
| USB3 TX_N pad 140 | USB_SSRXM pin 45 | pair preserved |
| USB3 TX_P pad 142 | USB_SSRXP pin 46 | pair preserved |

The corrected SATA/M.2 mapping is also materialized on the candidate: J3
pads 1/2/3/4 map to U7 pins 57/56/60/59, and J3 pad 5 is `M2_3V3`.

## Routing evidence

The route uses 0.13208 mm (5.2 mil) copper, the selected PiSXMe JLC six-layer
100-ohm basis. All four pairs use only F.Cu/B.Cu, with ordinary 0.50/0.30 mm
through-vias outside the J7 and U7 pad fields. No plane-layer signal routing
or via-in-pad is used. The CM5 RX pair and TXN escape around the existing
PCIe fanout; TXP uses the lower local return corridor. The resulting summed
track lengths are RX_N 36.175 mm, RX_P 36.010 mm, TX_N 37.003 mm, and TX_P
38.896 mm. Pair skew is bounded by the local geometry and remains subject to
the final field-solver audit.

## Native KiCad DRC

Report: `ACREAGE_PHASE18_USB3_LOCAL-drc.rpt`

| Check | Result |
|---|---:|
| `shorting_items` | 0 |
| `tracks_crossing` | 0 |
| `clearance_violations` | 0 |
| `unconnected_items` | 430 total, inherited acreage baseline 427 plus 3 corrected storage-pad records |
| `via_dangling` | 5, all inherited regulator support vias |

The Phase 18 Ethernet/USB3-local gate therefore passes. The remaining DRC
items are explicitly inherited or outside this routing island and remain in
the global final-cleanup ledger; they are not silently treated as zero.

## Mechanical and return-path review

U7 is moved to the open acreage region at (110,105) mm and rotated 180°;
J7, CM5, PCIe, V100/SXM2, and power architecture remain unchanged. The
underside remains available under the Rev-A contract except for verified
connector, mounting, CM5/M.2, and enclosure constraints. The route has no
layer transitions without local return-via pairs; each transition is an
ordinary through-via outside a pad field.

## Decision

Phase 18 USB3 routing is accepted as a disposable acreage candidate and is
the next ancestor for the remaining approved phases. No Phase 19+ work was
started in this checkpoint.
