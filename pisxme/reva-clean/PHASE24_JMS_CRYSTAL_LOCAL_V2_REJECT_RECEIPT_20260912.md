# Phase 24 JMS crystal local V2 rejection

Candidate: `PHASE24_STORAGE_MKEY_USB3_CRYSTAL_LOCAL_V2_20260912.kicad_pcb`

The combined REXT/crystal trial was rejected as a route implementation. Native
pad connectivity and the trace-removal negative control passed for XIN/XOUT
and JMS_REXT, but KiCad DRC found local QFN escape/solder-mask conflicts at
the XIN/XOUT segments and the candidate increased the inherited census to
566 violations / 414 unconnected items. It is not a production or support
closure candidate. The validated REXT base remains the active basis.
