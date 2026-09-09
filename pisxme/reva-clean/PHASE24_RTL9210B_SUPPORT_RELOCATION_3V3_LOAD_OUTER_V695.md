# RTL9210B Path-B V695 — positive 3V3 load basis

V695 moves the U1.20 descent to x=103.2 outside the SPISI pad field, then
uses ordinary transitions to a B.Cu load collector and an upper U2 escape.
It connects U1.20, C3.1, U2.3, and U2.8 on RTL_3V3 while retaining the V685
source and V687/V693 QFN branches.

Native KiCad 10.0.5 DRC reports **0 violations** and 26 incomplete opens.
Disposition: retain V695 as the positive RTL_3V3 load-field basis.
