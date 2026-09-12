# Phase 24 JMS AVDDL U12 local receipt

Candidate: `PHASE24_STORAGE_MKEY_USB3_AVDDL_U12_LOCAL_20260912.kicad_pcb`

Starting from the U11-to-C83 AVDDL primitive, U12.36 escapes outward through
ordinary 0.60/0.30 mm through-vias and returns to the shared C83.1 node. The
existing U11 AVDDL leg, cumulative support joins, and USB3 copper are retained.

Native KiCad 10.0.5: U11.20-to-C83.1 and U12.36-to-C83.1 endpoint
connectivity both PASS, with independent trace-removal negative controls PASS.
The corrected cumulative candidate reports 592 DRC violations / 412
unconnected items, with no AVDDL short/crossing finding. Other same-net
U11/U12/U13/J3 fanout connections remain open; this is not full support
closure.

The first generated version accidentally removed the existing U11 branch while
adding U12. That generator defect is corrected in the saved candidate and in
`phase24_route_jms_avddl_u12.py`; the earlier file state is rejected evidence.
