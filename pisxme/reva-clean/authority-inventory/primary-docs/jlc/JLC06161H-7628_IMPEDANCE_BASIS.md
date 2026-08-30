# Current JLCPCB six-layer and impedance basis

Date checked: 2026-08-29. Selected stack: `JLC06161H-7628`, six layers,
nominal 1.6 mm finished board, outer copper 1 oz, inner copper 0.5 oz,
ordinary through vias.

| Region | Nominal thickness | Material / Dk |
|---|---:|---|
| L1-L2 prepreg | 0.21040 mm | 7628 / 4.4 |
| L2-L3 core | 0.40000 mm | core / 4.6 |
| L3-L4 prepreg | 0.20280 mm | 7628 / 4.4 |
| L4-L5 core | 0.40000 mm | core / 4.6 |
| L5-L6 prepreg | 0.21040 mm | 7628 / 4.4 |

The current JLC calculator model uses 0.035 mm outer and 0.0152 mm inner
copper. Targets are PCIe Gen2 90 ohm differential, USB3 90 ohm differential,
SATA 100 ohm differential, 1000BASE-T 100 ohm differential, and USB2 90 ohm
differential. Future high-speed pairs use F.Cu over L2 GND or B.Cu over L5
GND; no old 85-ohm trial geometry is authoritative.

Historical project evidence recorded a live 90-ohm result for width 0.13208 mm
(5.2 mil) and pair gap 0.085328 mm (3.359375 mil), calculated 89.995806 ohm
with a coated cross-check of 90.14944 ohm. This is prior evidence, not a
substitute for the order's fab-returned coupon. The 100-ohm requests must be
entered in the current JLC calculator/order flow before routing. Specify
controlled impedance and request the coupon/field-solver result at fabrication.

Sources saved locally: `JLC06161H-7628_IMPEDANCE_INPUTS.md` records the
current calculator fields and the public-source URLs are
`https://jlcpcb.com/impedance`,
`https://jlcpcb.com/help/article/user-guide-to-the-jlcpcb-impedance-calculator`,
and `https://cart.jlcpcb.com/client/template/placeOrder/impedanceCalculation.html`.

Decision: `CLOSED` as the current stack/impedance authority, with normal fab
coupon/tolerance verification required at order. No clean PCB or schematic
was modified.
