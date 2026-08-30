# PCIe Placement Root Cause

The >100 mm PCIe routes were not caused by pair matching. They were caused by the
CM5 connector pad field being at approximately x=200 mm while the SXM2 lane-0
launch is around x=102–109 mm. The current CM5 connector root at `(165,100,0)`
also leaves its mating CM5 STEP envelope in the right-side I/O area, so a direct
route must traverse the full cooler-to-I/O separation.

The fixed cooler boundary at x=160 mm is the governing mechanical constraint. A
simple 0° translation can move the CM5 pad field only about 5 mm before the
connector/courtyard reaches the cooler-owned region. Rotating the combined
connector footprint 180° places the CM5 PCIe field at approximately x=162.5 mm
while keeping the connector body/courtyard east of x=160 mm. This is why the
180° candidate is materially better without moving J1 or invading the cooler
volume.

The original two-via-per-conductor routes are therefore classified as:

* **FIXED_MECHANICAL:** the SXM2 connector and cooler boundary;
* **MOVABLE_COMPONENT:** CM5 connector orientation and USB support parts;
* **ROUTING_CHOICE:** long detours and layer changes used to preserve the old
  orientation;
* **TOOL/AUTOROUTER_ARTIFACT:** none established as the primary cause.

The next route should start from candidate C and use the L1/L2 corridor directly.

