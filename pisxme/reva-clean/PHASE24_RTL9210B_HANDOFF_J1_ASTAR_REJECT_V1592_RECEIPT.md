# RTL9210B corrected handoff-to-J1 router rejection — V1592

Date: 2026-09-10

V1592 corrected the launch planner's endpoint model by exempting the actual
source and target pad rectangles, rather than only one grid cell. Starting
from the accepted V1590 QFN handoffs, it found complete saved-board paths for
all six high-speed nets to the actual J1/M.2 contacts, with two to four layer
transitions per net.

Native KiCad 10.0.5 DRC rejected the generated geometry with **594
violations**, dominated by sub-0.2 mm clearances between the independently
searched centerlines/vias and the tightly spaced connector launch. No result
was promoted. The endpoint model is retained as a generator correction, but
the centerline/transition reservation strategy remains invalid for production
routing and must be corrected before another full launch attempt.
