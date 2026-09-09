# RTL9210B Path-B V699 — positive RTL_5V source basis

V699 removes the redundant overpass via from V698. The split F.Cu/B.Cu
overpass avoids the RTL_1V1 barrier and connects U1.33 RTL_5V to C5.1 using
ordinary transitions.

Native KiCad 10.0.5 DRC reports **0 violations** and 25 incomplete opens.
Retain V699 as the positive RTL_5V source basis; U1.17 remains open.
