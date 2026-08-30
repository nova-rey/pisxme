# Phase 4 SXM2 lane-0 mapping receipt

Checked: 2026-08-30. Connector: Amphenol `74221-101LF`, Rev-W.

| Function | SXM2 contact | Direction at V100 endpoint | Rev-A treatment |
|---|---|---|---|
| CM5 PCIe receive from V100 | A2/A3 | V100 TX → CM5 RX | lane 0, polarity preserved |
| CM5 PCIe transmit to V100 | G1/G2 | CM5 TX → V100 RX | lane 0, transmitter-side AC coupling on PET0 |
| PCIe reference clock | E7/F7 | CM5 host clock → V100 endpoint | differential pair, polarity preserved |
| Fundamental reset | E18 | CM5 control → V100 endpoint | active-low PERST, no high-speed stub |

The connector identity and contact labels come from the preserved connector
authority record and its Rev-W manufacturer drawing. The local symbol is an
isolated namespace copy of the prior pin-label source and contains only the
documented lane-0/control contacts plus power/ground placeholders. The local
400-pad land pattern is retained as a comparison artifact only: exact Rev-W
mask/paste/courtyard and K18/K19 auxiliary treatment remain
`REV_A_EMPIRICAL_RISK` until manufacturer-overlay and physical assembly review.

Explicit exclusions: no PER1/PER2/PER3, no x4/x8/x16 expansion, no NVLink,
no PCIe switch, no redriver, and no second AC-coupling pair. Endpoint
enumeration, reset timing, and undocumented V100 power sequencing remain
hardware-validation risks.
