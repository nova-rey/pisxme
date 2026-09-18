# Authority receipt — nine-branch Molex source contract

- Package: `P24-POWER-INPUT-NINE-BRANCH-SCHEMATIC-CONTRACT`
- Decision: `PISXME-P24-NINE-BRANCH-SCHEMATIC-20260918` revision 1.0
- Assigned base: `369b28f67dfb371589a73e8eda1e5dc166eedb3b`
- Result: `CANDIDATE_READY_WITH_REQUIRES_PROTOTYPE_VALIDATION`
- Canonical schematic/PCB changed: **no**
- User-owned decision required: **no**

The exact three-header, eighteen-contact source contract is now bound for the isolated producer. J5/J6/J9 each provide three positive contacts and three return contacts. B1–B9 are explicitly paired and named; F1–F9 are one positive-series 15 A Littelfuse 0297015.U fuse in 178.6165.0001 per pair. This is nine independent fault-isolation paths; the fuse is not a 5 A current limiter, and the 4.444 A / 5.000 A targets plus 7 A contact screen remain current-balance and thermal acceptance gates.

A single common protection cohort is authorized for producer evaluation using existing U1/Q1/D1/C3 parts and footprints. U2/Q2/D2/C4 are not credited as a parallel common stage. The producer must prove the 2 mΩ protection allocation, complete 10 mΩ source-to-J1 path, fuse/TVS/FET energy coordination, and control/shutdown behavior before integration.

The JSON/Markdown contract and machine queue candidate are the durable handoff. No schematic or PCB edits were made by this authority package.
