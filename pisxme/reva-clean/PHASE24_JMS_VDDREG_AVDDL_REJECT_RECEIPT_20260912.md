# Phase 24 JMS VDDREG cumulative rejection

Candidate: `PHASE24_STORAGE_MKEY_USB3_VDDREG_AVDDL_BASE_20260912.kicad_pcb`

The candidate restored native U11.1/U12.1-to-L10.2 connectivity and passed its
trace-removal negative control, but the proposed B.Cu rail corridor crossed
the accepted VCCK route and produced a real `USB_TXP1`/`JMS_AVDDL` short under
native DRC. Native census was 617 violations / 410 unconnected items.

This is rejected route implementation evidence. No VDDREG copper from this
candidate is promoted; the validated cumulative AVDDL/LXO/REXT support base
remains the active basis.
