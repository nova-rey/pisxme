# Phase 24 fresh-Light JMS583/U5 recheck

Date: 2026-09-12  
Candidate ref: `837940e1`  
Validator: fresh `kicad-light` worker, KiCad 10.0.6

## JMS583 local escape

`PHASE24_JMS583_FINE_QFN_ESCAPE.kicad_pcb` was loaded from the committed
candidate. The scope audit passed: seven saved 0.10 mm XIN/XOUT escape tracks,
no fine-net vias, and no leakage outside the declared local window. The
complete JMS583 support-cohort audit passed, the REXT audit passed, and the
trace-removal negative controls passed.

Native DRC reported 612 violations and 409 unconnected items. This matches
the inherited acreage baseline and is retained as open full-board evidence;
it is not attributed to the local JMS583 escape.

## U5 native connectivity

`phase24_u5_layer_connectivity_audit.py` passed against the saved native PCB.
Its negative control removed an actual connected trace and failed the audit as
required. Connectivity was derived from KiCad's saved pads/tracks/vias/zones;
the expected member table supplied assertions only.

The KiCad 10.0.6 worker emitted known property-enum and Python via-width
assertion noise while loading/auditing; neither changed the pass/fail results.

## Boundary

This receipt closes neither full-board DRC nor Phase 24. It confirms the
bounded JMS583 implementation and U5 audit are ready inputs for controlled
acreage integration/closure.
