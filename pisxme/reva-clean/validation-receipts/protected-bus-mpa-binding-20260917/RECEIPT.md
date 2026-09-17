# Receipt — protected-bus MPA binding decision

- Package: `P24-PROTOTYPE-POWER-BUS-PRODUCER`
- Decision: `PISXME-P24-PROTOTYPE-POWER-BUS-MPA-20260917-R1`
- Base: `31b30dc0ccb28fe341f9bffb26005b5f50cd7641`
- PCB SHA-256: `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`
- Result: **BINDING_DECISION**

The decision fixes J5/J6/J1 anchors and binds one relocated two-row source/protection cohort, an In3.Cu protected-bus plane, separate pre-merge A/B corridors, and a J1-side power-field approach. It preserves the source-bus 10.0 mOhm, ampacity, via, and thermal constraints. No CAD, schematic, project rules, or queue file was modified by this authority action. The producer may now implement this exact plan from the stated base and return a candidate for serialized integration and fresh Light validation.

Power Integrity advisory was reconciled: the current long Branch-A geometry is explicitly replaceable, and source-assembly rating remains a separate qualification dependency.
