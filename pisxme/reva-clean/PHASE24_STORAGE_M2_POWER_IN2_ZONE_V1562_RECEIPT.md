# Phase 24 storage M.2 power handoff — V1562

Date: 2026-09-10  
Parent: `PHASE24_STORAGE_V79_HARMLESS_ADD.kicad_pcb`  
Status: **accepted focused power-connectivity primitive; not board promotion**

## Change

The nine native J3 `STORAGE_3V3` pads are connected by pad-derived F.Cu
dogbones to ordinary 0.8/0.4-mm through-vias. The vias join an explicit
0.60-mm `STORAGE_3V3` spine on designated `In2.PWR`; a remote source via
hands off to U14.5 without a B.Cu collector through the SATA launch field.
No signal net was added to a plane layer and no via-in-pad or microvia was
used.

## Evidence

| Check | Result |
|---|---|
| Native M.2 power-owner audit | PASS — all 9 J3 contacts reach the source-owned rail |
| Necessary-trace removal negative control | PASS — removing one required trace fails the audit |
| Native KiCad DRC | 610 violations / 342 unconnected items; inherited board remains open |
| New storage-rail shorts | None found in the V1562 shorting sections |
| New storage-rail crossings | None found in the V1562 shorting sections |
| Rule policy | unchanged; no severity relaxation |

The native DRC count is not a full-board pass. The candidate is retained as a
focused power-connectivity primitive and is not promoted until the remaining
board findings and the local DRC delta are reconciled.

Raw report: `PHASE24_STORAGE_M2_POWER_IN2_ZONE_V1562-drc.rpt`.  Generator:
`phase24_storage_m2_power_in2_zone_v1562.py`. Audit:
`phase24_storage_m2_power_owner_audit.py`.

## Decision closed

This closes the immediate classification that V79's J3 power problem is a
missing physical copper path rather than a schematic source-ownership issue.
It does not close storage routing, power integrity, or Phase 24.
