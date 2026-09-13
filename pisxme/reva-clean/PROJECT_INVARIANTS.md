# PiSXMe Rev A Foundational Invariants

Governing contract at `c06876d2bb3c244d29ad04e883a253eefd35c265`; audit pauses new physical implementation. Classes A-F follow the JSON.

| ID | Statement | Value | Class | Result | Authority |
|---|---|---|---|---|---|
| INV-PRODUCT-V100-300W | Rev A supports V100/SXM2 300 W sustained at product input | 300 W sustained | C | FAIL | Product/Power Authority |
| INV-PRODUCT-V100-330W-PEAK | Retain 330 W design peak allowance | 330 W peak | C | FAIL | Product/Power Authority |
| INV-INPUT-12V | Nominal regulated/current-limited 12 V source with declared tolerance | 12 V nominal; tolerance and current limit to be bound | B | UNPROVEN | Power Authority |
| INV-INPUT-CAPACITY | Input system carries product envelope after efficiency and low-voltage loads | 29.87963 A sustained; 32.65741 A peak at 12 V, 90% screen | D | FAIL | Power Authority |
| INV-MOLEX-8A | Selected PS-43879-001-001 standard two-circuit assembly is limited to 8 A/circuit before derating | 8 A/circuit; 16 A arithmetic screen | B | PASS | Package/Power Authority |
| INV-BRANCH-SHARING | No assumed passive branch current sharing; each branch independently limited/fault handled | sharing prohibited absent qualification | B | UNPROVEN | Power Authority |
| INV-PROTECTION | Reverse block, OVP/UVLO, TVS, fuse I2t, MOSFET SOA and shutdown inhibit are bounded | thresholds/energy/I2t required | A | UNPROVEN | Power Authority |
| INV-RAIL-5V | CM5 5 V rail supports declared current and effective capacitance | 5.0 V, 3 A; TPSM63606 6 A; >=30 uF effective | B | UNPROVEN | PI Authority |
| INV-RAIL-3V3 | Bridge 3.3 V rail supports declared current and effective capacitance | 3.3 V, 2 A; >=50 uF effective | B | UNPROVEN | PI Authority |
| INV-RAIL-1V1 | Bridge 1.1 V rail meets effective capacitance screen | 1.1 V, 1 A; >=300 uF effective; current screen 253.44 uF | D | FAIL | PI Authority |
| INV-SEQUENCING | Enable/PG/reset/V100 inhibit meet endpoint timing | thresholds and timing to be bound | B | UNPROVEN | Power/Firmware Authority |
| INV-SXM2-J1-PACKAGE | J1 contact package/net authority maps 393 pads to A1-K40 and preserves unknowns NC | 74221-101LF 400-position 10-row 1.27 mm; mapping contract | B | PASS | Package Authority |
| INV-SXM2-J1-INTEGRATION | Integrated J1 endpoints, power field, returns and assembly are physically closed | all required contacts/routes; no unknown assigned | D | UNPROVEN | PCB/Package Authority |
| INV-CM5 | CM5 power/interface and logic levels are compatible | CM5 declared rails and supported interfaces | B | UNPROVEN | Interface Authority |
| INV-PCIE | PCIe lane/generation/REFCLK/PERST and impedance meet endpoint contract | CM5-supported Gen2 x1; 90 ohm target | B | UNPROVEN | SI Authority |
| INV-STORAGE-PATHA | Path A selected production storage mode has required mapping and inactive isolation | power-off mode selection; 15 current open endpoint pairs | B | FAIL | Storage Authority |
| INV-STORAGE-PATHB | RTL9210B Path B is unpromoted alternative | production scope: not applicable | E | NOT_APPLICABLE | Storage Authority |
| INV-STACKUP | Declared six-layer roles and fabrication stack are the selected basis | 6 layers; nominal 90/100 ohm targets | B | PASS | SI/Fab Authority |
| INV-IMPEDANCE | Controlled impedance tolerance/coupon and extracted geometry are proven | 90/100 ohm with fab tolerance/coupon | D | UNPROVEN | SI/Fab Authority |
| INV-COPPER | Copper/via/plane current density, drop and temperature rise meet input/rail budgets | per INV-INPUT-CAPACITY and rail loads | A | FAIL | PI/PCB Authority |
| INV-RETURN | POWER_GND and reference returns are continuous and low-inductance | impedance/drop/ground-bounce limits to be bound | A | UNPROVEN | SI/PI Authority |
| INV-THERMAL | Connector, protection, regulators, copper and cooler remain within temperature limits | limits by component/product/ambient; sustained and peak | A | UNPROVEN | Thermal Authority |
| INV-MECHANICAL | Anchors, cooler/backplate, SSD/cable/service envelopes and keepouts are manufacturable | envelopes/clearances per authority records | B | FAIL | Mechanical Authority |
| INV-FAB | Trace/space, copper, drill/via, fine escape and assembly process are within qualified capability | JLC capabilities; U11 local escape limit | B | FAIL | Fab Authority |
| INV-FIRMWARE | Configuration/programming/procurement provenance is sufficient; undocumented V100 behavior remains empirical risk | required firmware/configuration records | C | UNPROVEN | Firmware/Provenance Authority |

Historical implementation choices are subordinate to these invariants. Where the existing two-branch input ceiling conflicts with `INV-PRODUCT-V100-300W`, it is `SUPERSEDED_BY_INVARIANT`.
