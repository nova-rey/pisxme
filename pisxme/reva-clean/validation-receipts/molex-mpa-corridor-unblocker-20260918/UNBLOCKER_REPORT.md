# Molex MPA corridor unblocker report

Outcome: SELF_UNBLOCK.

The retained candidates varied Branch-B copper on the dispersed baseline placement and never applied the binding MPA coordinates. The reports repeatedly show Q1 GATE_A at (32.54,78.00), while the binding MPA decision requires Q1 at (61,22) and Q2 at (61,54). Their 418–419 DRC failures therefore do not establish corridor impossibility.

Resume action: one clean native KiCad producer from the exact current base must assert all ten MPA placements and fixed anchors before routing the local J6->F2->D2/U2/Q2 Branch-B corridor. Preserve CM5 B.Cu corridors and transition protected output to In3 only at the post-protection merge. Validate zero shorts/crossings and complete Branch-B connectivity before integration.
