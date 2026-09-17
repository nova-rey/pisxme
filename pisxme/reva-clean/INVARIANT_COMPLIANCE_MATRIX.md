# PiSXMe Rev A Invariant Compliance Matrix

Baseline `c06876d2bb3c244d29ad04e883a253eefd35c265`; states are exactly PASS, FAIL, UNPROVEN, or NOT_APPLICABLE.

| ID | State | Evidence/contradiction | Owner |
|---|---|---|---|
| INV-PRODUCT-V100-300W | FAIL | Current selected input is 16 A pre-derating versus 29.87963 A screen. | Product/Power Authority |
| INV-PRODUCT-V100-330W-PEAK | FAIL | Current input cannot support 32.65741 A screen. | Product/Power Authority |
| INV-INPUT-12V | UNPROVEN | Selected protected-bus 12 V architecture; exact source tolerance and input assembly remain open. | Power Authority |
| INV-INPUT-CAPACITY | FAIL | Molex assembly 8 A/circuit, 16 A pre-derating. | Power Authority |
| INV-MOLEX-8A | PASS | Component limit passes itself; system envelope does not. | Package/Power Authority |
| INV-BRANCH-SHARING | UNPROVEN | Replacement rule applies only to parallel external input paths; exact assembly qualification remains open. | Power Authority |
| INV-PROTECTION | UNPROVEN | No complete transient energy and shutdown evidence. | Power Authority |
| INV-RAIL-5V | UNPROVEN | Physical copper/effective C/thermal open. | PI Authority |
| INV-RAIL-3V3 | UNPROVEN | Current integrated serialized copper absent. | PI Authority |
| INV-RAIL-1V1 | FAIL | 253.44 uF conservative screen is below 300 uF. | PI Authority |
| INV-SEQUENCING | UNPROVEN | No integrated sequencing proof. | Power/Firmware Authority |
| INV-SXM2-J1-PACKAGE | PASS | Integrated endpoint/assembly remains separate. | Package Authority |
| INV-SXM2-J1-INTEGRATION | UNPROVEN | Current integrated opens/returns remain. | PCB/Package Authority |
| INV-CM5 | UNPROVEN | Integrated route/return evidence incomplete. | Interface Authority |
| INV-PCIE | UNPROVEN | Route and return closure absent. | SI Authority |
| INV-STORAGE-PATHA | FAIL | 15 open required Path-A pairs. | Storage Authority |
| INV-STORAGE-PATHB | NOT_APPLICABLE | Must not enter production critical path. | Storage Authority |
| INV-STACKUP | PASS | Design-basis PASS only. | SI/Fab Authority |
| INV-IMPEDANCE | UNPROVEN | No coupon/tolerance closure. | SI/Fab Authority |
| INV-COPPER | FAIL | Branch-B and bridge nets zero serialized copper/vias. | PI/PCB Authority |
| INV-RETURN | UNPROVEN | 325 pads/47 segments/17 vias do not prove closure; unresolved returns. | SI/PI Authority |
| INV-THERMAL | UNPROVEN | No carrier thermal validation. | Thermal Authority |
| INV-MECHANICAL | FAIL | Courtyard/PTH/edge and missing-model findings. | Mechanical Authority |
| INV-FAB | FAIL | U11 0.15 mm fanout outside authorized local escape; release artifacts absent. | Fab Authority |
| INV-FIRMWARE | UNPROVEN | No hardware operation or vendor authorization claimed. | Firmware/Provenance Authority |

No broad CAD repair is READY until the invariant gate and every high-impact contradiction has an owned package. Scoped prior receipts remain reusable evidence.


## Power architecture amendment — 2026-09-17

The six-loop precision-limiter constraints are superseded as the governing architecture by `PISXME-P24-POWER-ARCH-20260917`; their evidence remains historical. New protected-bus rows `INV-PROTOTYPE-POWER-ARCH`, `INV-PROTOTYPE-EMPIRICAL-GATE`, and `INV-PROTECTED-BUS` are `UNPROVEN` pending source/bus closure and explicit prototype-validation procedures.
