# MPA R3 Reassessment

- Decision ID: `PISXME-P24-PROTECTED-BUS-MPA-20260921-R3-REASSESSMENT`
- Result: `BINDING_DECISION; R3 PLACEMENT/CORRIDOR AUTHORITY RETAINED`
- CAD changed: no

B1 and B2 do not demonstrate a structural contradiction in the R3 source-local three-bank placement. B2 reduced unconnected items from 435 to 428 but worsened DRC from 919 to 984, with clearance, shorts, crossings, and width failures caused by overlapping straight F.Cu/In4 paths and an incorrectly crossing In2 join. Fixed J1/J5/J6/J9 anchors, F1-F9 positions, 28 mm spacing, 0.75 mm inter-bank gap, and reserved In2/In4 fields remain binding.

The producer must use corridor-aware native authoring, preserve separate fused arrivals, distinct return-via arrays, and the unchanged In3 J1 approach. Placement reopening requires evidence that a complete corridor-aware branch pair remains infeasible.
