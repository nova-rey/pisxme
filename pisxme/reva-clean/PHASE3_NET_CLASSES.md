# PiSXMe Rev A Clean — Phase 3 net-class contract

These are logical constraints for schematic review. Final widths and gaps are
owned by the Phase 13 current-JLC stack receipt.

| Class | Members | Reference / rule |
|---|---|---|
| `HS_PCIE_90R` | PCIe TX/RX and REFCLK | 90 ohm differential; continuous GND reference |
| `HS_USB3_90R` | CM5 USB3 to bridge | 90 ohm differential; short local corridor |
| `HS_SATA_100R` | bridge SATA to M.2 | 100 ohm differential; no stubs |
| `HS_GBE_100R` | four MDI pairs | 100 ohm differential; ESD at connector boundary |
| `HS_USB2_90R` | SERVICE DP/DM | 90 ohm differential; direct UFP path |
| `POWER_12V_HIGH` | protected 12 V and V100 feeds | broad copper; controlled transitions |
| `POWER_LV` | CM5/bridge/storage rails | local decoupling and regulator return |
| `GND_RETURN` | grounds, shields, transition returns | solid In1/In4; deliberate stitching |
| `CONTROL` | reset, PG, fault, enable, LEDs, UART | local, short, no unnecessary vias |

No high-speed geometry is released for routing by this scaffold.
