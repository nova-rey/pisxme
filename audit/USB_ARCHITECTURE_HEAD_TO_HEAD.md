# USB architecture head-to-head

| Metric | Current PiSXMe USB-C | Disposable USB-A variant | Official CM5IO reference |
|---|---|---|---|
| Ports | 2 | 2 | 2 (one stacked J12) |
| Speed/port | 5 Gbps native CM5 USB3 | 5 Gbps native CM5 USB3 | 5 Gbps native CM5 USB3 |
| High-speed mux ICs | 2 HD3SS3212 | 0 | 0 |
| CC ICs | TPS25821 integrated FAST source paths; Type-C support | 0 for fixed host | 0 for Type-A |
| USB3 ESD | 2 four-line arrays/port in active board | omitted from focused trial; future variant may retain 1/port | no USB3 ESD TPD4 identified in highspeed sheet |
| USB2 companion ESD | 1/port | omitted from focused trial | no USB3-sheet companion ESD identified |
| Signal vias | 80 total (40/port) | 0 in trial | 16 total, 1.33/conductor |
| Return/stitching | 6 categorized active GND vias | 0 in focused coupon | 476 board-wide GND vias |
| Active ICs in one FAST port | mux + VBUS controller + 3 ESD devices = 5 | 0 in trial; direct variant needs chosen VBUS/ESD protection | shared VBUS switch allocation; no mux |
| Direct SuperSpeed topology | mux plus reversible branch fanout | host launch → Type-A | CM5 → stacked Type-A |
| DRC trial quality | accepted production USB-C routing, but complex | 0/0 direct SS trial | official fabricated design |
| User functionality | reversible plug | fixed/keyed plug | fixed/keyed plug |

The Type-A variant preserves the CM5 link capability and intended SSD/NIC
function while materially simplifying the SuperSpeed topology. The active
board remains unchanged and its Type-C architecture remains the current
review artifact.
