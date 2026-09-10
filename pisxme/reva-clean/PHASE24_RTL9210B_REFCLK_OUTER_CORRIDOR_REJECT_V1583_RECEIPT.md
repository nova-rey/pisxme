# RTL9210B outer REFCLK corridor rejection — V1583

Date: 2026-09-10

V1583 retained the Claude-selected 0-degree U1 orientation and the accepted
V1517 local basis, then routed REFCLK P/N through an outer board corridor with
ordinary through-vias. Native KiCad 10.0.5 DRC reported **27 violations**.
The violations include source-field clearance/crossings, REFCLK_N shorting
LANE0_TXN, multiple REFCLK conflicts with the J1-side LANE0_TXP launch, and
REFCLK P/N transition conflicts. This route class is rejected; the four
REFCLK endpoint group remains open.

The result is a route-implementation failure of an isolated overlay, not a
reason to reopen U1 orientation or Path-A. A valid next attempt must
co-author the crystal, REFCLK, rail, and adjacent lane fanout as one saved
source-field implementation.
