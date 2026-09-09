# RTL9210B V735/V1279 native geometry comparison

Coordinates are read after KiCad transforms from native PCB pads; no schematic ordering or synthetic connectivity is used.

## V735
- PCB: `PHASE24_RTL9210B_SPI_U1_ROTATE90_SPICS_SPISO_V735.kicad_pcb`
- U1 position: (36.0, 150.0) mm
- U1 orientation: 90.0 degrees

| Pad | Net | X (mm) | Y (mm) |
|---:|---|---:|---:|
| 8 | PEDET | 101.95 | 70.4 |
| 13 | CLKREQ_N | 101.95 | 68.4 |
| 14 | PERST_N | 101.95 | 68.0 |
| 18 | SPISI | 101.2 | 66.05 |
| 19 | SPICLK | 100.8 | 66.05 |
| 20 | RTL_3V3 | 100.4 | 66.05 |
| 22 | SPISO3 | 99.6 | 66.05 |
| 23 | SPISO | 99.2 | 66.05 |
| 24 | SPICS | 98.8 | 66.05 |
| 25 | RTL_1V1 | 98.4 | 66.05 |
| 33 | RTL_5V | 95.2 | 66.05 |
| 34 | RTL_3V3 | 94.8 | 66.05 |
| 51 | RSET | 94.05 | 73.2 |
| 52 | RTL_3V3 | 94.8 | 73.95 |
| 53 | XTAL_IN | 95.2 | 73.95 |
| 54 | XTAL_OUT | 95.6 | 73.95 |
| 64 | LANE0_RXP | 99.6 | 73.95 |
| 65 | LANE0_RXN | 100.0 | 73.95 |
| 67 | LANE0_TXN | 100.8 | 73.95 |
| 68 | LANE0_TXP | 101.2 | 73.95 |

## V1279
- PCB: `PHASE24_RTL9210B_XTAL_IN_LIVE_PAD_V1279.kicad_pcb`
- U1 position: (18.0, 8.0) mm
- U1 orientation: 0.0 degrees

| Pad | Net | X (mm) | Y (mm) |
|---:|---|---:|---:|
| 8 | PEDET | 97.6 | 73.95 |
| 13 | CLKREQ_N | 99.6 | 73.95 |
| 14 | PERST_N | 100.0 | 73.95 |
| 18 | SPISI | 101.95 | 73.2 |
| 19 | SPICLK | 101.95 | 72.8 |
| 20 | RTL_3V3 | 101.95 | 72.4 |
| 22 | SPISO3 | 101.95 | 71.6 |
| 23 | SPISO | 101.95 | 71.2 |
| 24 | SPICS | 101.95 | 70.8 |
| 25 | RTL_1V1 | 101.95 | 70.4 |
| 33 | RTL_5V | 101.95 | 67.2 |
| 34 | RTL_3V3 | 101.95 | 66.8 |
| 51 | RSET | 94.8 | 66.05 |
| 52 | RTL_3V3 | 94.05 | 66.8 |
| 53 | XTAL_IN | 94.05 | 67.2 |
| 54 | XTAL_OUT | 94.05 | 67.6 |
| 64 | LANE0_RXP | 94.05 | 71.6 |
| 65 | LANE0_RXN | 94.05 | 72.0 |
| 67 | LANE0_TXN | 94.05 | 72.8 |
| 68 | LANE0_TXP | 94.05 | 73.2 |

## Independent evidence

- V735 native DRC report: zero DRC violations (its unconnected-pad findings remain explicitly open).
- V735 audit: SPICS and SPISO native endpoints plus source-trace negative controls pass.
- V735 is a rotated-U1 support comparison, not evidence that the current four-lane V1279 routing can be copied without regeneration.
