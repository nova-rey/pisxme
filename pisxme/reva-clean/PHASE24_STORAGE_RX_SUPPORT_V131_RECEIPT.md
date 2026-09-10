# Phase 24 storage RX support V131 receipt

V131 attempted an obstacle-aware native-pad A* escape for the direct
U11.26/27 to U12.23/22 RX support nets on the V127 parent. Native DRC
rejected the candidate at 177 violations / 499 opens, including RX pair
shorts/crossings into POWER_GND, each other, and JMS_AVDDL.

The experiment is rejected as a router/source-transition implementation
failure. It does not change the V127 CM5 USB3 route or the storage electrical
topology. The next support implementation must use explicit package-aware
source and target transitions with deliberate pair-separated layer corridors;
this coarse A* obstacle class is retired for the dense U11/U12 field.
