# Phase 24 JMS583 support-cohort V1 receipt

Candidate: `PHASE24_STORAGE_MKEY_USB3_FULL_SUPPORT_COHORT_V1_20260912.kicad_pcb`

This disposable cohort was generated from the pushed U14-repaired V6 base with
the existing project support-cohort authoring path. It connects the documented
JMS583 support cohort (reset, AVDD33, AVDDL, VCCO, VCCK, VDDREG_5V, LXO,
XAVDDH, and associated local support) and passes the support-cohort audit,
including its trace-removal negative control. The complete ten-link USB3 audit
also passes.

Native KiCad 10.0.5 DRC reports 453 violations / 401 unconnected items. The
cohort reduces open connectivity but is not promoted because its moved support
placement creates additional clearance/route findings. It is retained as
implementation evidence for the next support repair; no architecture,
RTL9210B orientation, or USB3 topology changed.
