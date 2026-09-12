# Phase 24 STORAGE alias-rename probe — rejected

Date: 2026-09-12  
Base: committed `4c25a8d3`  
Validator: fresh KiCad Light 10.0.6

The disposable probe renamed 21 exact co-located `NC_*` STORAGE labels to the
currently preferred JMS583/support net names. Native ERC changed the electrical
warning classes from 132/126/30/23 to 132/149/30/5 (worker-only library/link
warnings are excluded from that comparison). The alias class improved, but
isolated-label findings increased.

Semantic native netlist comparison is not preserved: baseline 338 nets versus
probe 349 nets, with 11 extra `/STORAGE/NC_*` nets and 11 changed node sets.
The candidate is therefore rejected as an electrical-authority repair. No
canonical schematic, PCB, or validation severity was changed.
