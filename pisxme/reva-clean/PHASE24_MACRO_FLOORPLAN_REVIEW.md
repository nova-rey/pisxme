# Phase 24 macro-floorplan review

Baseline: `PHASE24_U7_3V3_CURRENT_LOCAL.kicad_pcb` (native-loaded current integrated candidate).
All coordinates below are extracted after KiCad transforms; existing copper is not silently treated as valid after a footprint move.

| footprint | value | center (mm) | rotation | side | native body bbox |
|---|---|---:|---:|---|---|
| `J7` | `Raspberry-Pi-5-Compute-Module` | `35.00,130.00` | `0.0` | `B.Cu` | `31.44,78.44–71.56,133.56` |
| `J2` | `A70-112-331N126` | `77.50,53.00` | `180.0` | `F.Cu` | `68.53,41.74–86.47,65.30` |
| `U6` | `TPD4EUSB30` | `81.10,65.22` | `-90.0` | `F.Cu` | `77.17,64.25–82.85,66.15` |
| `U9` | `TPD4EUSB30` | `75.10,65.22` | `-90.0` | `F.Cu` | `73.58,64.25–79.03,66.15` |
| `U8` | `Texas_DRT_3` | `58.00,100.00` | `90.0` | `F.Cu` | `57.27,99.17–58.73,100.83` |
| `J1` | `74221-101LF` | `150.00,90.00` | `0.0` | `F.Cu` | `116.47,76.20–183.53,103.80` |
| `U7` | `TUSB9261IPVP` | `120.00,140.00` | `180.0` | `F.Cu` | `115.28,135.28–124.72,146.18` |
| `J3` | `JAE SM3ZS067U410ABR1000 B-key SATA socket` | `145.00,125.00` | `90.0` | `F.Cu` | `133.86,113.45–226.15,136.55` |
| `J4` | `Amphenol 10171746-00021LF USB-C USB2 SERVICE` | `45.00,100.00` | `90.0` | `F.Cu` | `40.88,93.30–49.12,106.70` |
| `J5` | `0039300020` | `12.00,25.00` | `0.0` | `F.Cu` | `10.45,16.15–14.96,31.70` |
| `J6` | `0039300020` | `12.00,45.00` | `0.0` | `F.Cu` | `10.45,36.15–14.96,51.70` |
| `F1` | `178.6165.0001` | `240.00,40.00` | `0.0` | `F.Cu` | `227.88,27.88–252.12,52.12` |
| `F2` | `178.6165.0001` | `50.00,120.00` | `0.0` | `F.Cu` | `37.88,107.88–62.12,132.12` |
| `U1` | `LM74700QDBVRQ1` | `20.00,75.00` | `0.0` | `F.Cu` | `18.27,71.87–21.73,76.72` |
| `U2` | `LM74700QDBVRQ1` | `20.00,95.00` | `0.0` | `F.Cu` | `18.27,91.87–21.73,96.72` |
| `U3` | `TPSM63606RDLR` | `60.00,165.00` | `0.0` | `F.Cu` | `57.05,161.07–62.95,167.68` |
| `U4` | `TPSM63606RDLR` | `225.00,105.00` | `0.0` | `F.Cu` | `222.05,101.07–227.95,107.67` |
| `U5` | `TPSM63606RDLR` | `235.00,105.00` | `0.0` | `F.Cu` | `232.05,101.07–237.95,107.67` |

## CM5 pin-group to island distances

| group | CM5 native pads | CM5 launch centroid (mm) | island centroid (mm) | centroid distance (mm) | nearest pad distance (mm) |
|---|---:|---:|---:|---:|---:|
| Ethernet | 8 | (34.50,99.90) | (77.76,59.56) | 59.15 | 50.70 |
| PCIe | 7 | (69.60,101.50) | (150.00,90.00) | 81.22 | 55.39 |
| USB3-storage | 4 | (70.04,105.30) | (132.11,132.11) | 67.61 | 36.06 |
| SERVICE-USB2 | 2 | (66.96,99.30) | (45.00,100.00) | 21.97 | 19.96 |

## High-speed copper census

| group | routed track items | vias | copper length (mm) | layers |
|---|---:|---:|---:|---|
| Ethernet | 189 | 0 | 534.4 | F.Cu |
| PCIe | 35 | 4 | 704.5 | B.Cu, F.Cu |
| USB3-storage | 36 | 8 | 323.8 | B.Cu, F.Cu |
| SERVICE-USB2 | 34 | 4 | 101.6 | B.Cu, F.Cu |

## Macro-placement candidates

`ETH_WEST`: move the complete Ethernet endpoint set to a west-edge neighborhood: J2 `(15,145)`, U6 `(42,88)`, U9 `(48,88)`. This keeps ESD near the CM5 GBE launch, avoids the SERVICE connector body, and gives the MagJack a natural west-edge launch; all affected Ethernet copper must be regenerated.

`ETH_SOUTH`: move the MagJack to the south edge `(75,160)` while placing U6/U9 near the CM5 launch at `(42,88)/(48,88)`. This tests a separated source/connector island without consuming the PCIe east corridor; all affected Ethernet copper must be regenerated.

`STORAGE_LOCAL`: move U7 to `(95,120)` and retain J3 as the outboard M.2 endpoint `(145,125)`, keeping the long 2280 mechanical envelope while shortening the CM5 USB3 launch. USB3/SATA copper and clock/support routes must be regenerated.

`SWAP_ETH_STORAGE`: move the complete Ethernet endpoint set to the south-west/CM5 side and move the complete storage island north-west/mid-acreage, explicitly testing whether both interfaces gain monotonic corridors without consuming the PCIe launch region.

`CM5_NEIGHBORHOODS`: place ESD/support near the GBE launch, U7/clock near USB3, SERVICE near its USB2 launch, and retain J1 at the PCIe launch. This is a placement-only topology candidate.

These are disposable placement candidates, not accepted routing. Candidate selection requires native DRC/connectivity, pair metrics, references, mechanical access, and revalidation of every affected frozen subsystem.

## Candidate centroid comparison

| candidate | Ethernet island centroid | Storage island centroid | SERVICE centroid | Ethernet source distance (mm) | USB3 source distance (mm) |
|---|---:|---:|---:|---:|---:|
| `CURRENT` | (77.8,59.6) | (132.1,132.1) | (45.0,100.0) | 59.2 | 67.6 |
| `ETH_WEST` | (28.0,121.5) | (132.1,132.1) | (45.0,100.0) | 22.5 | 67.6 |
| `ETH_WEST_OUTBOARD` | (18.5,128.4) | (132.1,132.1) | (45.0,100.0) | 32.7 | 67.6 |
| `ETH_EAST_ESD_WEST_JACK` | (42.8,128.4) | (132.1,132.1) | (45.0,100.0) | 29.7 | 67.6 |
| `ETH_SOUTH` | (62.0,129.9) | (132.1,132.1) | (45.0,100.0) | 40.7 | 67.6 |
| `STORAGE_LOCAL` | (77.8,59.6) | (121.4,123.5) | (45.0,100.0) | 59.2 | 54.5 |
| `SWAP_ETH_STORAGE` | (28.0,121.5) | (119.7,122.8) | (45.0,100.0) | 22.5 | 52.6 |
| `CM5_NEIGHBORHOODS` | (30.6,103.2) | (117.0,125.1) | (84.0,100.0) | 5.1 | 51.0 |

## Whole-board interpretation

- `J7` is on B.Cu at `(35.0,130.0)`; Ethernet exits the left mating-side column at `(32.96–36.04,99.1–100.7)`, while PCIe/USB3/SERVICE exit the right column at approximately `(66.96–70.04,99.3–106.7)`.
- PCIe `J1` is the closest high-speed endpoint to its CM5 launch and remains the anchor; moving it would spend the most sensitive validated geometry for little gain.
- SERVICE `J4` is the only currently local interface. Ethernet and storage are both materially remote; the current top Ethernet island and mid-board storage island occupy corridors that compete with PCIe/power and expose the clock/SATA congestion.
- The migration/swap candidates are topology probes only. They intentionally invalidate affected copper and require complete regeneration before any promotion.
