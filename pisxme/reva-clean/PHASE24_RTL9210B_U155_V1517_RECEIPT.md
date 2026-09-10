# RTL9210B U1.55 rail rehome receipt: V1517

V1517 is the accepted isolated RTL_1V1 support-field rehome from V1508.
The former U1.55 leftward F.Cu escape and dangling tail were removed. U1.55
now exits west only to `(92.8,68.0)`, descends on F.Cu to the existing
RTL_1V1 via pocket at `(92.8,69.8)`, and retains the rest of the validated
RTL_1V1 network.

Native KiCad DRC: **0 violations**, 6 inherited opens. Native connectivity
joins U1.55 and U1.63. Removing the U1.55 source segment fails the saved-board
negative control. This is an isolated support primitive; crystal, REFCLK,
firmware, procurement, integration, and full Path-B gates remain OPEN.
