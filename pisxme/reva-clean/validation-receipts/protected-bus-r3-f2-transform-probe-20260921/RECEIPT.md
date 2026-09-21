# F2 transform producer probe

Base: canonical HEAD `90a415d9`; CAD geometry base `57332e98`.
Method: qualified `pisxme-kicad-light:v1`, native pcbnew script, MPA transform `T_F2=(0,+11.25mm)`.

The transformed F2 was authored at center `(64,26.25)` with raw/fused pad centers `(57.6,25)/(66.9,25)`. The J5.2/F2 local escapes and In2 segments were emitted at y=25. Native DRC returned **977 violations** and **428 unconnected items**. The report contains shorting items involving `PWR_SRC_J5_P2` with `PWR_SRC_J5_P1`, `PWR_SRC_J5_P3`, and existing `12V_IN_A`, plus fused-lane/via conflicts. No candidate is accepted.

This is a material contradiction between the transform and existing copper/pad-field geometry. The exact board, route graph, and raw DRC report are retained. Unblocker must classify whether the F2 cohort/row must move as a bounded macro decision or whether an alternate legal corridor exists; no further transform or route variant is authorized until that review.
