# Phase 24 official CM5IO Rev 2 USB3 CAD extraction

Source: `pisxme/reva-clean/authority-inventory/cm5io-rev2/CM5IO.kicad_pcb` (native KiCad PCB).
This receipt is generated from saved native pads/tracks/vias; it is not a schematic-drawing or pin-list inference.

Official CM5 footprint: `Module1` value `ComputeModule5-CM5`, position `(195.5, 73.5)`, rotation `180.0°`.

| Net | Native track objects | Widths (mm) | Layers | Vias | Via positions (mm) |
|---|---:|---|---|---:|---|
| `USB3-0-RX_N` | 26 | `{0.147: 24}` | `{'F.Cu': 17, 'B.Cu': 7}` | 2 | `[(180.7362, 140.4391), (169.0485, 115.7515)]` |
| `USB3-0-RX_P` | 28 | `{0.147: 26}` | `{'F.Cu': 19, 'B.Cu': 7}` | 2 | `[(168.5515, 116.2485), (180.2391, 140.9362)]` |
| `USB3-0-TX_N` | 22 | `{0.147: 21}` | `{'F.Cu': 7, 'B.Cu': 14}` | 1 | `[(168.6485, 120.1515)]` |
| `USB3-0-TX_P` | 29 | `{0.147: 24}` | `{'F.Cu': 7, 'B.Cu': 17}` | 1 | `[(168.1515, 120.6485)]` |

Interpretation: the official source uses F.Cu and B.Cu signal segments with ordinary through-vias; no In1/In4 signal tracks are present in these four nets. The exact saved geometry remains the implementation oracle for pair ordering and launch/transition semantics.

This extraction does not claim that the official CM5IO coordinates transplant unchanged to PiSXMe; the PiSXMe adaptation must still pass native DRC, connectivity, impedance, and mechanical gates.
