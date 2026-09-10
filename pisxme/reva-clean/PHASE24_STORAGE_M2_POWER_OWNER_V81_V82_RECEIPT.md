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
