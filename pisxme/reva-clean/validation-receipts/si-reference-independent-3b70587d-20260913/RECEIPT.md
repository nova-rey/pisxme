# Independent SI/reference lane result

- Source head: `3b70587d`; selected PCB SHA-256 `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`.
- Scoped closure: board declares the approved six-layer roles (`F.Cu`, `In1.Cu=In1.GND`, `In2.Cu=In2.PWR`, `In3.Cu=In3.PROTECTED_12V`, `In4.Cu=In4.GND`, `B.Cu`); raw parse confirms 329 signal segments, 90 vias, 216 F.Cu and 113 B.Cu segments, zero inner-layer signal segments. This agrees with `PHASE13_STACK_RECEIPT.md` and JLC stack authority.
- Parked gap under Hard Problem Queue Issue #2: storage USB3 nets are not assigned to `HS_USB3_90R`; measured widths include 0.15/0.20 mm versus the 0.13208 mm approved starting geometry. Return-plane continuity and SI measurements remain unproven.
- No CAD edits were made. Overall `layers_routes_impedance_return` remains OPEN pending integrated storage routing and SI evidence.
