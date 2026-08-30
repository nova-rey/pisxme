# Official CM5IO USB3 implementation

Source: official Rev 2 KiCad package in
`references/cm5/official-cm5io-rev2/`. This is the primary CM5-side reference.

## Topology

The official CM5IO uses the CM5’s two independent USB3 interfaces directly
with one stacked dual Type-A connector, `J12` `MTCONN_UBAF30-D2011`.
There is no SuperSpeed orientation mux because Type-A has one fixed
orientation. The high-speed sheet carries USB3-0 and USB3-1 directly from the
CM5 symbol to J12.

CM5 mapping:

| Port | RX P/N | USB2 D-/D+ | TX P/N | Type-A physical note |
|---|---|---|---|---|
| USB3-0 | 128/130 | 134/136 | 140/142 | A5/A6 and A8/A9 use deliberate P/N naming swaps |
| USB3-1 | 157/159 | 163/165 | 169/171 | B5/B6 and B8/B9 use the same routing aid |

The schematic contains the explicit note: `USB 3 Pairs P/N swapped to help
routing`. At J12, A5/B5 (connector SSRX-) carry the project RX_P name and
A6/B6 (SSRX+) carry RX_N; A8/B8 (SSTX-) carry TX_P and A9/B9 (SSTX+) carry
TX_N. This is a naming/routing swap, not a bandwidth change.

## Measured board evidence

From the preserved Rev 2 KiCad board:

- Four copper layers.
- Main USB3 width is 0.147 mm; some local segments are 0.127 mm.
- USB3-0: D and RX are 2 vias per conductor; TX is 1 via per conductor.
- USB3-1: D, RX, and TX are 1 via per conductor.
- All selected USB3 routes use F.Cu/B.Cu through-vias in the source board.
- The official source census records 16 USB3 signal vias over 12 USB3
  conductors, 1.33 vias/conductor average.
- The board-wide ground count is 476 vias; this is not a USB-port-only
  stitching count.

## ESD and VBUS

The USB3 high-speed sheet routes the SuperSpeed nets directly to J12. The
`TPD4EUSB30` U1/U2 parts found in the complete CM5IO source are connected to
Ethernet `TRD0..TRD3` nets, so they are Ethernet ESD, not USB3 ESD. The USB3
VBUS/control sheet includes an `AP2553W6`/`AP22653W6` current switch path and
the Type-A port VBUS net; the source has one shared dual-connector VBUS
implementation rather than one Type-C orientation switch per port.

This gives PiSXMe two separate lessons:

1. A direct fixed-orientation Type-A path can leave the CM5 with no USB3 mux.
2. ESD and VBUS are independent protection/power decisions; they should not
   be conflated with SuperSpeed fanout complexity.

## Reuse boundary

PiSXMe can reuse the CM5 pin order, the deliberate P/N naming freedom, direct
F.Cu/B.Cu escape concept, and the absence of a hub. PiSXMe cannot copy the
CM5IO connector coordinates, board-wide power design, or its unrelated
Ethernet/HDMI/M.2 circuitry.
