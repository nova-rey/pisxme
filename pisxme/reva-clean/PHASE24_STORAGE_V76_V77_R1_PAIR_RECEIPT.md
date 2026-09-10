# Phase 24 storage BRIDGE_R1 pair trials — V76/V77

V76 added `BRIDGE_R1` to V75 with a direct source-field bypass. Native DRC
reported 618 violations / 348 opens and real shorts involving `JMS_AVDDL`,
`JMS_VBUS_SENSE`, and the adjacent `BRIDGE_R1RTN` transition. It was
rejected.

V77 regenerated `BRIDGE_R1` and `BRIDGE_R1RTN` together with separated
transitions. Native DRC reported 607 violations / 348 opens, including a
`BRIDGE_R1`/`JMS_VBUS_SENSE` short and an R1/R1RTN source-field short. It was
also rejected. V75 remains the preferred clean storage parent.
