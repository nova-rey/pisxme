# CM5 accidental-overimplementation audit

Requirement boundary: CM5 host, one V100 PCIe x1 endpoint, two fast USB host
ports, one service/recovery USB2 port, boot/storage, power, cooling, and
debug/control.

| CM5 capability | PiSXMe state | Classification |
|---|---|---|
| PCIe x1 | One lane-0 link to SXM2 | REQUIRED |
| USB3 port 0 | FAST-A | INTENTIONALLY_EXPOSED |
| USB3 port 1 | FAST-B | INTENTIONALLY_EXPOSED |
| Independent USB2 | SERVICE with TUSB320/recovery | REQUIRED |
| eMMC | Recommended CM5 SKU; no extra carrier logic | REQUIRED deployment choice |
| native Ethernet | absent; commodity USB NIC on FAST-B | UNUSED_AND_NOT_IMPLEMENTED |
| HDMI | absent | UNUSED_AND_NOT_IMPLEMENTED |
| MIPI camera/display | absent | UNUSED_AND_NOT_IMPLEMENTED |
| SD/microSD | absent | UNUSED_AND_NOT_IMPLEMENTED |
| HAT/general GPIO header | absent | UNUSED_AND_NOT_IMPLEMENTED |
| extra PCIe lanes | absent | UNUSED_AND_NOT_IMPLEMENTED |
| RTC support | no dedicated carrier block found | UNUSED_AND_NOT_IMPLEMENTED |
| Wi-Fi external circuitry | absent; optional CM5 SKU only | UNUSED_AND_NOT_IMPLEMENTED |
| USB hub | absent | REQUIRED simplification |
| UART/debug | J8 internal header | REQUIRED |
| recovery control | nRPIBOOT/TP3/service-role support | REQUIRED |

No accidentally implemented CM5 feature was found. The only material
overimplementation candidate is not a CM5 feature itself: reversible Type-C
FAST-port support adds mux/branch/CC complexity that fixed-host Type-A does
not need.
