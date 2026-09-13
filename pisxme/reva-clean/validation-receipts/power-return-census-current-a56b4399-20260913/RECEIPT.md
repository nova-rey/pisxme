# Current power and return native census

- Candidate: `a56b4399`.
- Script: `validation/phase24_power_return_census.py` (read-only parser; no CAD writes).
- Board totals: 131 footprints, 329 segments, 90 vias, 3 zones.
- Required measured nets include: `POWER_GND` 325 pads / 47 segments / 11 vias / 3 zones; `12V_PROTECTED` 151 pads / 6 segments / 1 via; `STORAGE_3V3` 18 pads / 22 segments / 4 vias; `JMS_AVDDL` 18 pads / 7 segments / 3 vias; `JMS_AVDD33` 2 pads / 3 segments / 2 vias; `JMS_VDDREG_5V` 4 pads / 4 segments / 2 vias.
- Branch-B and bridge-rail gaps are explicit: `12V_IN_B` and `FUSED_12V_B` have zero segments/vias; `BRIDGE_1V1` and `BRIDGE_3V3` have zero segments/vias.
- This is physical ownership evidence for the open power/storage rows. It does not claim current, transient, voltage-drop, thermal, or routed-connectivity closure.
