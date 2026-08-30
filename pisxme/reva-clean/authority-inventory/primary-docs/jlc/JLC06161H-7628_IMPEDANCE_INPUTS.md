# Reproducible JLC06161H-7628 impedance inputs

Checked: 2026-08-30. This is the saved input record for the current public JLC
six-layer calculator. It is separate from the fabrication coupon: the order
remains authoritative for final stack tolerance.

## Stack and fields

- Stack option: `JLC06161H-7628`, six layers, nominal 1.6 mm finished board.
- Copper: 0.035 mm nominal outer layers; 0.0152 mm nominal inner layers.
- L1-L2 and L5-L6: 0.21040 mm 7628 prepreg, nominal Dk 4.4.
- L2-L3 and L4-L5: 0.40000 mm core, nominal Dk 4.6.
- L3-L4: 0.20280 mm 7628 prepreg, nominal Dk 4.4.
- Reference planes: L2 and L5 GND; no ordinary plane-layer signal routing.
- Include solder mask only for coated outer-layer checks.

The current JLC impedance-template API response for the exact request
`{"cuprumThickness":1.0,"insideCuprumThickness":0.5,"stencilLayer":6,"stencilPly":1.6}`
is saved as `JLC06161H-7628-stack-api-20260830.json`, SHA-256
`d05b35679338f41986ca756bafe88ee655775b37a86a07cf2bbc107fbb6e58e0`. The
selected object is `JLC06161H-7628`, not the similarly named 3313/2116/1080
options; its raw lamination records prove the three 7628 prepregs and two
0.4 mm cores listed above.

## Design targets

| Interface | Target | Routing reference |
|---|---:|---|
| PCIe Gen2 | 90 ohm differential | L1 over L2 GND or L6 over L5 GND |
| USB3 | 90 ohm differential | L1 over L2 GND or L6 over L5 GND |
| SATA | 100 ohm differential | L1 over L2 GND or L6 over L5 GND |
| 1000BASE-T | 100 ohm differential | L1 over L2 GND or L6 over L5 GND |
| USB2 | 90 ohm differential | L1 over L2 GND or L6 over L5 GND |

The prior project receipt contains a live 90-ohm solver result of width
0.13208 mm (5.2 mil), pair gap 0.085328 mm (3.359375 mil), calculated 89.995806
ohm and coated cross-check 90.14944 ohm. It is retained as starting geometry,
not as a promise that every JLC stack tolerance produces that value.

The Phase 13 calculator capture is now attached as
`JLC06161H-7628-calculator-20260830.json` and
`pisxme/reva-clean/PHASE13_STACK_RECEIPT.md`. It records the current inverse
calculation result for both target classes. The eventual order must still
specify controlled impedance and include a fabrication coupon; coupon data is
not available before fabrication.

Sources: `JLC06161H-7628_IMPEDANCE_BASIS.md`,
https://jlcpcb.com/impedance, and
https://jlcpcb.com/help/article/user-guide-to-the-jlcpcb-impedance-calculator.
