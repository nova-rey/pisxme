# Unblocker: native F2 corridor capability change

Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
Outcome: `SELF_UNBLOCK`
Base evidence: `e5ee47fc`.

The native F2 authority is internally consistent. The scripted P2 geometry is electrically illegal because it crosses existing J5.1/F1 copper and creates J5 pad and F1 fused-net shorts. Native F2 remains fixed at `(64,15,0deg)` with physical pad endpoints `(57.6,13.75)` and `(66.9,13.75)`.

Failure census: 454 clearance, 428 unconnected, 199 hole-clearance, 124 width, 113 solder-mask, and 35 shorting findings. Distinct prior route methods also failed: transform 977/428, topology-first 965/428, focused P2 961/434, clone 977/429, current-head B2 984/428, native F2 967/428.

Capability change: use a fresh isolated KiCad Heavy workspace and GUI-native interactive router for a one-branch fixture only: J5.2 to F2 raw, F2 fused to distributed join, and J5.5 to In4 return. Do not inherit or replay retained scripted P2 geometry. Preserve all R3 authority, no global rules, no J1/high-speed edits, and no waiver.
