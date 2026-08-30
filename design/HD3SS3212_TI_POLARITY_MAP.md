# HD3SS3212 polarity map in TI TIDA-00987

Date: 2026-08-23  
Primary evidence: `references/usb3/TIDA-00987/TIDRND0A-schematic.pdf`,
`TIDUC55A-design-guide.pdf`, and `HD3SS3212-datasheet.pdf`.

The table below is transcribed from the TI schematic. `P/N` in a TI net name
describes the intended USB signal identity; it is not a requirement that every
physical mux pin be approached in the nominal visual order.

## Mux mapping

### Direct TI design-guide observation

TI's design guide identifies the apparent polarity mismatch as deliberate. In
its HD3SS3212 table, the B0/C0 TX paths are named with the opposite polarity
from the nominal mux pin suffixes, and the corresponding A-side TX polarity is
switched as well. This is the precise mechanism used to keep the mux-to-ESD-
Type-C fanout straight; it is not a transcription error. The B1/C1 RX paths
retain the corresponding non-inverted relationship.

| HD3SS3212 port/pin | TI net | Physical Type-C signal | TI polarity relative to nominal name | Corresponding relationship |
|---|---|---|---|---|
| A0P pin 3 | `SSRX_P` | host/device receive path | normal | A0 vs B0/C0 is consistent |
| A0N pin 4 | `SSRX_N` | host/device receive path | normal | same |
| A1P pin 7 | `SSTX_N` | host/device transmit path | intentionally inverted | A1 inversion is also represented on the B/C TX paths |
| A1N pin 8 | `SSTX_P` | host/device transmit path | intentionally inverted | same |
| B0P pin 19 | `SSTX2_N` | Type-C B orientation TX | intentionally inverted | matches A1 TX polarity relationship |
| B0N pin 18 | `SSTX2_P` | Type-C B orientation TX | intentionally inverted | same |
| B1P pin 17 | `SSRX2_P` | Type-C B orientation RX | normal | matches A0 RX polarity relationship |
| B1N pin 16 | `SSRX2_N` | Type-C B orientation RX | normal | same |
| C0P pin 15 | `SSTX1_N` | Type-C A orientation TX | intentionally inverted | matches A1/B0 TX relationship |
| C0N pin 14 | `SSTX1_P` | Type-C A orientation TX | intentionally inverted | same |
| C1P pin 13 | `SSRX1_P` | Type-C A orientation RX | normal | matches A0/B1 RX relationship |
| C1N pin 12 | `SSRX1_N` | Type-C A orientation RX | normal | same |

## Type-C/ESD correspondence

TI’s J3 labels are:

| Type-C pins | TI signal |
|---|---|
| A2/A3 | `SSTX1_P/N` |
| A10/A11 | `SSRX2_N/P` |
| B2/B3 | `SSTX2_P/N` |
| B10/B11 | `SSRX1_N/P` |

The two TPD4E05U06 DQA arrays use the signal pads as follows:

| TI ESD device | D1+ pin 1 | D1− pin 2 | D2+ pin 4 | D2− pin 5 |
|---|---|---|---|---|
| U5, Type-C B branch | `SSTX2_N` | `SSTX2_P` | `SSRX2_P` | `SSRX2_N` |
| U6, Type-C A branch | `SSTX1_N` | `SSTX1_P` | `SSRX1_P` | `SSRX1_N` |

The TPD4E05U06 NC pins 6/7/9/10 are not electrically connected to those
signals. They are available to permit a straight physical trace path through
the package area when the layout uses them as a pass-through corridor.

## B/C selection constraint

The HD3SS3212 select input still defines which side is selected: Port B for
the low select state and Port C for the high select state. The polarity study
therefore does **not** swap the B and C branch identities. It only changes the
P/N relationship within a differential channel. A B/C branch swap would also
require an explicit select/control change and is outside this study.

## What is being reused

PiSXMe does not copy TI net names or coordinates. It reuses the validated
electrical principle: choose the polarity relationship across A versus B/C so
the physical branch order is straight, then make the remap explicit in the
schematic. The PiSXMe channel assignment and endpoint geometry are different,
so its optimized mapping is documented separately and remains trial-pending.
