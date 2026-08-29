# MiSaKa / EEWorld JMS578 U5 reference extraction

Status: read-only extraction for PiSXMe M6. This is a concrete reference, not a
PiSXMe implementation and not for fabrication.

## Source and preservation

The reference clone was `/private/tmp/jmsref.bU8OeM` at commit
`2a1bb050603ba040ff3cdfc5e40612d25e3e6dca`.

Source hashes after the extraction (clone working tree restored clean):

| file | SHA-256 |
|---|---|
| `ver0.1.kicad_pcb` | `b7c7e5f4d05f9ada84f6b951037b44a7bce72d1c1a5fc5fa765ffad0e2201393` |
| `ver0.1.kicad_sch` | `00ffb168c3e76b40260559f53a4fb9aef3e5059eb3fce3261015cf86fbce4a20` |

Exact disposable copies are present beside this report as
`MiSaKa_ver0.1.kicad_pcb`, `MiSaKa_ver0.1.kicad_sch`, and
`MiSaKa_ver0.1_extracted.net`. The PiSXMe repository and Git history were not
modified. The earlier synthetic/provisional PiSXMe island is not authoritative
and must not be used as an M.2 pin-map source.

## What the reference actually is

This is a fabricated multi-drive USB-to-SATA cage: J1 USB 3.1 Type-B → U5
JMS578 → one SATA link into JMB575, then four downstream SATA connectors J4–J7.
It is useful as a concrete JMS578 bridge island, but it is **not** a direct
M.2 implementation. No M.2 electrical mapping is inferred here.

## U5 identity and package

* Reference: U5
* Value in PCB: `~` (the schematic library part is `Interface_USB:JMS578`)
* Footprint: `Package_DFN_QFN:QFN-48-1EP_6x6mm_P0.4mm_EP4.2x4.2mm_ThermalVias`
* QFN exposed pad is pad 49 with four 0.30 mm thermal vias in the source
* U5 placement: `(117.51232, 91.78798)`, rotation 180 degrees

## Exact U5 pin/net extraction

| U5 pin(s) | function | reference net | connected reference parts |
|---|---|---|---|
| 1 | TME | `Net-(U5-TME)` | C21-2, R23-1 |
| 2, 3, 5, 6 | GPIO0/1/2/3 | `/GPIO0`, `/GPIO1`, `/GPIO2`, `/GPIO3` | U4 SPI flash/control |
| 4, 10, 40 | VCCK | `/vout1.2` | C23–C30, C40, C45, L5-2 |
| 7, 14, 39, 46 | VCCO/AV33O/MODE0 | `/vout3.3` | C21-1, C32–C34, R24-1, R25-2, U4 |
| 8, 9, 11 | GPIO4/5/6 | `/GPIO4`, `/GPIO5`, `/GPIO6` | no other reference node |
| 12 | VBUS | `VBUS` | C46-2, C47-2, J1-1 |
| 13 | USB DM | `/HSD0-` | J1-2 |
| 14 | AV33O | `/vout3.3` | listed above |
| 15 | USB DP | `/HSD0+` | J1-3 |
| 16, 17, 25, 35, 48 | NC/GPIO9 | explicit U5 unconnected nets | none |
| 18, 21, 24, 29, 32 | AVDDL | `/vout1.2` | C23–C30, C40, C45, L5-2 |
| 19 | SSTXN | `/cap-SSTX1-` | C35-2 |
| 20 | SSTXP | `/cap-SSTX1+` | C36-2 |
| 22 | SSRXN | `/cap-SSRX1-` | C37-2 |
| 23 | SSRXP | `/cap-SSRX1+` | C39-2 |
| 26, 42, 43, 47, 49 | GND/NC/MODE1/exposed pad | `GND` | plane and local ground network |
| 27 | XOUT | `/XOUT` | Y1-3, C31-1 |
| 28 | XIN | `/XIN` | Y1-1, C22-2 |
| 30 | SATA RXP | `/RX_P` | C42-1 |
| 31 | SATA RXN | `/RX_N` | C41-1 |
| 33 | SATA TXN | `/TX_N` | C44-1 |
| 34 | SATA TXP | `/TX_P` | C43-1 |
| 36 | REXT | `Net-(U5-REXT)` | R26-1 |
| 37 | UAO/GPIO8 | `Net-(U5-UAO{slash}GPIO8)` | R25-1 |
| 38 | RST# | `/RST` | C38-1, R24-2 |
| 41 | GPIO7 | explicit U5 unconnected net | none |
| 44 | LXO | `/LXO` | L5-1 |
| 45 | VREG_IN | `VBUS` | C46-2, C47-2, J1-1 |
| 46 | MODE0 | `/vout3.3` | listed above |

## Local support parts to carry into an adaptation review

The following are the exact support references and values around U5 in the
reference schematic/PCB. They are evidence for a review package, not an
automatic PiSXMe BOM.

* C21 `1uF`: `/vout3.3` to U5 TME net.
* C22 and C31 `33pF`: crystal load capacitors to GND.
* C23–C30 `100nF`: `/vout1.2` local bypass capacitors.
* C32–C34 `100nF`: `/vout3.3` local bypass capacitors.
* C35 and C36 `100nF`: USB3 TX series coupling capacitors.
* C37 and C39 `0R`: USB3 RX series links in this implementation.
* C38 `1uF`: reset capacitor to GND.
* C40 `10uF`: 1.2 V bulk capacitor.
* C41–C44 `10nF`: SATA pair series coupling capacitors; C41/C42 are RX,
  C43/C44 are TX.
* C45 `0.1uF`: 1.2 V bypass capacitor.
* C46 and C47 `100nF`: VBUS bypass capacitors.
* L5 `4.7uH`: U5 LXO to `/vout1.2`.
* R23 `100K`: TME to GND.
* R24 `330K`: `/vout3.3` to `/RST`.
* R25 `4.7K`: UAO/GPIO8 to `/vout3.3`.
* R26 `12K`: REXT to GND.
* Y1: `Crystal_GND24_Small`, 30 MHz in the accompanying README and schematic.
* U4: SPI flash/control companion connected to U5 GPIO0–3 and `/vout3.3`.

The source includes external regulators for its multi-rail design and a USB
Type-B connector. Those portions must not be copied blindly into PiSXMe:
PiSXMe must independently resolve 5 V input, 3.3 V/1.2 V requirements, M.2
3.3 V power, bridge reset/configuration, and the exact SATA socket pin map.

## Reference high-speed coupling and topology

### USB side

`J1` carries `/HSD0+`, `/HSD0-`, `/SSRX0+`, `/SSRX0-`, `/SSTX0+`, and
`/SSTX0-`. U5-side nets are separated by C35/C36/C37/C39. The PCB route
statistics for all tracks on U5-related nets are:

| class | source nets | track count | summed track length | layers |
|---|---|---:|---:|---|
| USB2 | `/HSD0+`, `/HSD0-` | 12 + 10 | 18.97 + 16.11 mm | F.Cu |
| USB3 TX | `/SSTX0+`, `/SSTX0-`, `/cap-SSTX1+`, `/cap-SSTX1-` | 0 + 0 + 5 + 4 | 6.18 + 6.16 mm on U5-side nets | F.Cu |
| USB3 RX | `/SSRX0+`, `/SSRX0-`, `/cap-SSRX1+`, `/cap-SSRX1-` | 0 + 0 + 9 + 8 | 4.87 + 4.70 mm on U5-side nets | F.Cu |

The apparent zero counts on connector-side net names are because the reference
board uses several renamed/intermediate net records; inspect the exact PCB
tracks before deriving a pair-length receipt. The reliable topology fact is
that the pair runs locally on F.Cu through the four coupling components into
the U5 pins, with no signal vias in the full reference board.

### SATA side

The one JMS578 SATA pair goes through C41–C44 to JMB575 nets
`/net-RX_N`, `/net-RX_P`, `/net-TX_N`, `/net-TX_P`. The reference PCB then
fans those into JMB575 and downstream SATA connectors. For PiSXMe, keep only
the U5-side coupling pattern as a candidate and replace the JMB575 fanout with
an explicitly verified M.2 B-key socket map. The extracted data does not
authorize a direct U5-to-M.2 pad-number claim.

## Geometry and construction observations

* Full source PCB segment count: 1,471.
* Full source physical through-via count: 0 according to a direct PCB parse.
* U5-related signal tracks are F.Cu-local in the source.
* Source U5 footprint uses four thermal through-vias under the exposed pad.
* The source board is a large four-layer/multi-drive design with many unrelated
  DRC findings; it is not a PiSXMe acceptance artifact.

## Native DRC evidence

DRC was run only on an isolated copy of the cloned PCB with KiCad 10.0.5,
`--severity-all --refill-zones --save-board`:

* 2,156 violations
* 1 unconnected item

The violations are dominated by legacy whole-board geometry/library/setup
issues (499 clearance, 199 each of several via/track constraints, 137 library
mismatches, and 120 board-edge clearance findings). This DRC result is not a
claim that the reference implementation is fabrication-ready. It does confirm
that KiCad can parse and inspect the cloned source. The one unconnected item
and all unrelated whole-board findings require separate classification if the
reference board is used as a starting point.

## Boundary for PiSXMe use

Use this extraction to reproduce the **JMS578 local island**: QFN package,
USB3/SATA coupling placement concept, 30 MHz crystal, REXT, reset/configuration
support, local bypassing, exposed-pad thermal strategy, and short F.Cu signal
paths. Do not copy the multi-drive JMB575 architecture, its external SATA
connector fanout, its power tree, or any inferred M.2 mapping. The next PiSXMe
step is to build a disposable schematic/PCB island from these exact U5-side
facts plus a separately manufacturer-verified M.2 B-key socket and pin table.
