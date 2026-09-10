# Rejected V1523 support/source-handoff integration

Date: 2026-09-10  
Status: REJECTED — disposable implementation evidence

The native-clean V1523 RTL_3V3 support baseline was tested with the accepted
V1603 launch. Retaining the existing RTL_1V1 corridor creates source-field
crossings against REFCLK_P. A trial that escaped LANE0_RXP to B.Cu with a
0.60 mm through-via introduced RXP/RXN and RXP/TXN shorts because the QFN
south-edge pair spacing is too tight for that via placement. Native DRC
reported six errors and four crystal opens; the candidate was not promoted.

This result narrows the next repair: co-author the RTL_1V1 source-field
departure and the six-net handoff together, with vias outside the QFN south
edge pair envelope. The V1603 launch primitive and frozen U1 orientation are
unchanged; the authoritative clean checkpoint remains `21b6c1f0`.
