# Protected-bus F2 via method unblocker

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Outcome: `SELF_UNBLOCK`
- Classification: bounded geometry/workflow failure.

Candidate `a19c403ac13897fc7515ed8d57461add61329400` failed fresh Light at 927 DRC / 434 unconnected versus 919 / 435 baseline because the final F.Cu segment placed a through-via co-located with F2.1. The next single qualified Heavy v2 route shall escape J5.2 briefly on F.Cu, place an ordinary through-via near `(24.5,24.5)`, change to In2.Cu there, and obstacle-avoid on In2.Cu to F2.1 raw `(57.6,13.75)`, finishing on the pad with no via or dangling endpoint. Preserve all anchors, layers, rules, topology, and MPA corridor constraints.
