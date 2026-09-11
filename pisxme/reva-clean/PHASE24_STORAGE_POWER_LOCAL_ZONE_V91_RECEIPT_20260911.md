# Storage M.2 power local-zone V91 experiment

V91 replaced the earlier long fanout with short F.Cu dogbones from each of
the nine J3 `STORAGE_3V3` contacts to staggered ordinary through-vias and a
local In2 power zone. Native saved-board connectivity passed for all nine
contacts and the actual trace-removal negative control.

The geometry is not promotable: native KiCad DRC reported 621 violations and
341 unconnected items, including a real `STORAGE_3V3` to `JMS_AVDDL` short at
the J3 launch (`215.0,167.275`). The staggered dogbones cross adjacent
connector contacts. No canonical CAD changed. This rejects the dense
same-side fanout topology; future repair must reserve the connector launch
channels before adding power copper.
