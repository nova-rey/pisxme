# PiSXMe architecture minimality audit

Status: complete, read-only audit of the active review board

Baseline: `c3e009f` / active-board SHA-256 recorded in `BASELINE_HASHES.md`

## Result

The active electrical architecture is minimal with respect to the stated
compute-appliance requirement: one CM5 host, one V100 SXM2 receptacle, one
PCIe Gen2 x1 lane, two independent CM5 USB3 ports, one USB2 service port,
power, cooling, and debug/recovery. No second GPU, NVLink, x16 PCIe, or
card-edge baggage was found in the active net structure.

The board is not yet *component-minimal*: the two Type-C FAST ports each pay
for an orientation mux and duplicate connector-side SuperSpeed branches. The
disposable USB-A trial in `experiments/usb-a-simplification/` demonstrates a
credible lower-complexity alternative. That is an architecture recommendation
for a future variant, not a mutation of this active review board.

## PCIe scope audit

| Check | Evidence | Classification |
|---|---|---|
| One lane electrically used | Active high-speed nets are `/PER0_P`, `/PER0_N`, `/PET0_P`, `/PET0_N`, `/REFCLK_P`, `/REFCLK_N`; control is `/PERST_N` and `/CM5_CLKREQ_N` | REQUIRED |
| Lane index | `design/PCIE_X1_INTERFACE_CONTRACT.md` and active CM5/SXM2 pin map identify lane 0 | REQUIRED |
| Lanes 1-15 | No active board net, segment, coupling capacitor, or footprint support block with lane 1-15 naming was found | ABSENT |
| Unused-lane AC coupling | C1/C2 are the two V100 TX coupling capacitors for lane 0; no additional PCIe lane coupling network remains | ABSENT |
| x16 support | No PCIe switch/bridge, x16 edge connector, lane fanout, or lane-specific support IC exists | ABSENT |
| Reference-clock scope | One differential REFCLK pair only | REQUIRED |

The raw PET0-side names are `/PET0_P_RAW` and `/PET0_N_RAW` at the two
source-side coupling capacitors; they are not additional lanes.

## SXM2/NVLink audit

- Exactly one `J1` `74221-101LF` exists.
- No second SXM2 connector, NVLink lane net, NVLink switch, retimer, or
  second-module power/control block exists.
- `MECH1` is a non-populated mechanical envelope annotation for the one V100
  module/cooler contract. It is not a second connector or an electrical net.
- The active connector net inventory contains no dead NVLink or second-module
  names.

Conclusion: the single-module scope is electrically respected.

## Suspicious or optional footprints

| Item | Current purpose | Classification | Disposition |
|---|---|---|---|
| D1 `SMBJ18A` | PCB-only provisional 12 V source TVS placeholder; excluded from BOM | UNKNOWN / pre-fabrication gate | Must be given schematic/BOM provenance or removed before fabrication; unchanged in this audit |
| TP1 | PERST# debug access marker | OPTIONAL_BUT_INTENTIONAL | Retain for bring-up; no high-speed stub |
| TP2 | REFCLK access marker/documentation point | OPTIONAL_BUT_INTENTIONAL | Retain only as a marker; no probe stub |
| TP3 | CM5 nRPIBOOT/recovery access | REQUIRED for recovery, optional for production assembly | Retain as the internal recovery path |
| R1 | DNP/POP CLKREQ link option | OPTIONAL_BUT_INTENTIONAL | Keep as a documented population option; do not populate without the defined strap decision |
| MECH1 | V100/SXM2 cooler/backplate envelope | OPTIONAL_BUT_INTENTIONAL | Keep as a mechanical contract annotation, never as a BOM item |

No item was proven to be legacy x16/NVLink baggage. D1 is a real release
closure issue, but its defect is provenance/implementation status rather than
evidence of a second-GPU architecture.

## CM5 feature minimality

| Feature | Active implementation | Classification |
|---|---|---|
| PCIe | One x1 lane plus clock/reset/request control | REQUIRED |
| USB3 | Two independent native ports, exposed as FAST-A/B Type-C | REQUIRED / intentionally exposed |
| USB2 | One SERVICE Type-C with DRP/recovery support | REQUIRED / intentionally exposed |
| eMMC | Consumed inside the CM5; no carrier circuitry needed | REQUIRED by recommended CM5 SKU, not separately routed |
| UART | Internal J8 header | REQUIRED debug |
| Recovery | nRPIBOOT and service-role circuitry | REQUIRED debug/recovery |
| Cooling | Two fans and optional pump header | REQUIRED for a 300 W-class appliance |
| Native Ethernet | Not implemented on PiSXMe | INTENTIONALLY_UNUSED; USB NIC is the selected modular path |
| HDMI/MIPI | Not implemented | UNUSED_AND_NOT_IMPLEMENTED |
| microSD | Not implemented | UNUSED_AND_NOT_IMPLEMENTED; eMMC/USB cover boot/storage |
| HAT/general GPIO expansion | Not implemented as a user connector | UNUSED_AND_NOT_IMPLEMENTED |
| Wi-Fi external circuitry | None | UNUSED_AND_NOT_IMPLEMENTED; Wi-Fi remains SKU-dependent |
| RTC/extra CM5 reference-board blocks | None identified | UNUSED_AND_NOT_IMPLEMENTED |

## Audit conclusion

The active board does not contain a hidden x16 or multi-GPU architecture. The
main inherited complexity is the chosen reversible Type-C implementation, not
unused accelerator circuitry. The USB-A disposable variant is therefore a
legitimate simplification candidate, but it should be treated as a new
architecture revision rather than silently applied to the current RC1.
