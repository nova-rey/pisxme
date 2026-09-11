# Phase 24 CM5 no-connect cleanup receipt — 2026-09-11

## Finding

Native KiCad 10.0.5 reported 11 `no_connect_dangling` warnings in
`CORE_CM5.kicad_sch`. The focused audit established that each was a stale
serialized record duplicated by a correctly transformed record with the same
UUID. The stale records were not attached to real pins in the current
two-unit CM5 symbol.

## Evidence and repair

An earlier disposable probe removed exactly the 11 identified
`(coordinate, UUID)` records. The probe passed with no ERC errors and zero
remaining `no_connect_dangling` findings. The committed
`validation/phase3/test_phase24_cm5_stale_no_connect.py` is the regression
guard: it rejects reintroduction of those stale records and reruns native ERC.

The same bounded deletion was then applied to the authoritative
`CORE_CM5.kicad_sch`. No pins, labels, wires, units, or electrical nets were
changed.

## Native result

Command:

```text
kicad-cli sch erc --output PHASE24_CLEAN_SCHEMATIC_ERC_LIVE_RECHECK_20260911_v3.rpt PiSXMe_RevA_Clean.kicad_sch
```

Result: **851 violations, zero errors**. The dangling no-connect class fell
from 11 to 0; all other warning-class counts were unchanged from v2.

Raw report SHA-256:
`53efcb9244ebe6e77f93d95713f54666f3f133c509ea73f79b4896d05ed9308a`

This closes one serialization-warning cluster only. Full Phase 24 schematic
truth/ERC/netlist/parity remains open because the remaining warning clusters
are not waived.
