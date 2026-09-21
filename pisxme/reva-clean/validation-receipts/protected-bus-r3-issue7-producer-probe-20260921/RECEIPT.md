# Issue #7 resolution reconciliation and active producer probe

- HPQ: `nova-rey/codex-config-backup#7`
- HPQ state: `resolution-ready` (Issue remains open pending canonical integration)
- Origin package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Current base: `627ec337a28ce0c732df7744dc3ba360414464db`
- Worker: `protected_bus_r3_issue7_producer_2`
- Image: `pisxme-kicad-light:v1`
- Command: `/opt/pisxme-venv/bin/python3 /workspace/project/pisxme/reva-clean/probe_power.py`
- Return code: `0`

## Reconciliation

The Sol packet for Issue #7 was an authority contradiction: the prior 2.0 mOhm Q1 allocation could not be satisfied by the fixed CSD19536KCS worst-case 2.70 mOhm device. The signed Product/Power Authority correction is already present on current HEAD in commit `627ec337`; it binds the 4.32 mOhm hot Q1 term and 8.50 mOhm complete positive-plus-return budget. The HPQ dependency is therefore resolved for scheduling, but Issue #7 is not closed because no canonical CAD candidate has passed integration and fresh validation.

## Active producer result

A fresh Light worker was launched after the package had been found READY with no owner. The native probe loaded the selected committed PCB and returned a clean process result, but exposed the exact remaining source-topology gap:

- `12V_IN_A`: 8 pads, J5/F1/U1 support only.
- `12V_IN_B`: 7 pads, J6/F2/U2 support only.
- `FUSED_12V_A`: 8 pads, F1/Q1/D1/U1 support only.
- `FUSED_12V_B`: 7 pads, F2/Q2/D2/U2 support only.
- `12V_PROTECTED`: 151 pads, existing J1 field and support loads.
- Canonical selected PCB has no J9 or F3-F9 footprint/net topology.

This is not a routing pass and no candidate is promoted. It is a reproducible source-topology finding. The producer remains RUNNING only while the next bounded source-topology authoring step is dispatched; it must not claim completion from this probe.

The retained nine-branch authority and rejected topology fixture remain evidence. The next implementation command must materialize the signed J5/J6/J9 and F1-F9 topology in an isolated producer, then use the R3 MPA geometry and micro-batch native authoring. No global rule changes or direct canonical edits are authorized.

## Source seed and bounded materialization

The retained rejected nine-branch fixture was loaded in the same fresh Light workspace and mechanically asserted to contain J5/J6/J9 and F1-F9. The assertion passed with J5/J6/J9 at (12,25)/(12,50)/(12,75) and the nine fuse references present. A disposable R3 topology materialization then moved F1-F3 to y=15, F4-F6 to y=40, and F7-F9 to y=65 at x=36/64/92, as required by the R3 MPA decision.

Native Light DRC on that materialized seed is `1077` violations and `499` unconnected items. It is rejected as a routed candidate: the result proves the seed contains the required topology but its inherited copper cannot be reused after the authoritative placement change. The next bounded step is explicit per-branch native micro-batch authoring from this topology seed, with save/reload checkpoints; no bulk nearest-neighbor mutation is authorized.
