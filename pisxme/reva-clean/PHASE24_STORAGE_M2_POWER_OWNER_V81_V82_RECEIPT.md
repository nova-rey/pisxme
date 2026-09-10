# Phase 24 storage M.2 power-owner route trials — 2026-09-10

## Current finding

The source correction in `1d51775` is valid: the nine J3 power contacts are
owned by the regulator rail `STORAGE_3V3`, and the saved-board V79 parity audit
passes.  Native connectivity additionally showed that V79 had no physical
route/zone to those contacts; the earlier net-name/parity PASS was therefore
not a physical power-connectivity PASS.

## Disposable trials

* V81 (`PHASE24_STORAGE_M2_POWER_ZONE_V81.kicad_pcb`) added a broad F.Cu
  storage-rail zone.  It did not reach the fine-pitch J3 field.  Native DRC:
  603 violations / 356 unconnected items.
* V82 (`PHASE24_STORAGE_M2_POWER_TRUNK_V82.kicad_pcb`) added real F.Cu
  pad escapes, ordinary through-vias, and an acreage B.Cu power trunk.  The
  native audit passed all 9 J3 contacts and its trace-removal negative control,
  but native DRC rejected the candidate: 628 violations / 335 unconnected
  items, with new STORAGE_3V3 shorting and crossing findings.  V82 is rejected
  and is not a production ancestor.

## Audit authority

`phase24_storage_m2_power_owner_audit.py` derives reachability only from
KiCad's saved pads, tracks, vias, and filled zones via native connectivity.
Expected endpoint lists are assertions only.  On V82 it reports:

```
PASS M.2 power owner native connectivity: 9 J3 contacts
PASS trace-removal negative control
```

The next route attempt must preserve that proof while moving the power trunk
into an actually free storage corridor or using a reviewed power-plane access
strategy.  No DRC rule was weakened.

* V83 (`PHASE24_STORAGE_M2_POWER_PLANE_V83.kicad_pcb`) moved the long trunk to
  In1 power copper while retaining F.Cu pad dogbones and ordinary through-vias.
  Native connectivity and the negative control passed, but the existing B.Cu
  signal field made the through-via locations collide; native DRC reported 613
  violations / 341 unconnected items and real `STORAGE_3V3` shorts. V83 is
  rejected. This is a route-corridor failure, not evidence against source
ownership.

* V84/V85 moved the drops to a south edge corridor. Both retained native
  nine-contact connectivity. V84/V85 still introduced one real short each to
  nearby Ethernet center-tap support (`ETH_CT_BRANCH_3`/`4`); rejected.
* V86 moved the drop farther outboard, but the same class moved to
  `ETH_CT_BRANCH_4`; it also exposed a weak negative-control choice in the
  audit because the first removed segment was redundant.
* V87 moved beyond that support pad. Native connectivity and the improved
  negative control both pass; native DRC is 608 violations / 341 unconnected
  items, with no new STORAGE_3V3 shorting entry. It is not yet accepted: the
  remaining seven-vs-V79 added violations are principally QFN/source-escape
  clearances and must be isolated before production promotion.
* V88 replaced the U13 source dogbone with a local F.Cu filled pickup zone
  feeding the same outboard In1 trunk. The nine-contact audit and negative
  control pass, but native DRC remains 608 / 341 and adds selector-field
  shorting around the local zone. V88 is rejected.
