# Phase 24 Path-A SATA router deduplication receipt

## Scope

This is a disposable routing-generator correction. It does not alter the
authoritative schematic, the Path-A storage architecture, or the integrated
candidate. The router now suppresses repeated native vias at the same
coordinate and repeated zero-length/identical segments emitted by one A*
path.

## Evidence

The corrected router was run from the unchanged support-routed Path-A base:

`PHASE24_DUAL_MODE_STORAGE_SUPPORT_ROUTED.kicad_pcb`

Output:

`PHASE24_PATHA_SATA_NATIVE_ASTAR_DEDUP_20260906.kicad_pcb`

Native KiCad DRC was run with all severities enabled. It exited zero as a
reporting command, but the board is rejected:

- 1,240 DRC violations
- 499 unconnected items
- track-crossing findings remain

The previous un-deduplicated disposable output reported 1,246 violations and
499 unconnected items. The six-count reduction confirms that the generator
change is active, but it is not sufficient to make this route valid.

## Disposition

`REJECTED — ROUTE_IMPLEMENTATION_FAILURE`

The output is preserved as evidence only. It must not be promoted to the
integrated board or used to reject the Path-A electrical architecture. The
remaining route work requires correcting obstacle-aware path emission and
terminal escape behavior, not relaxing DRC or manufacturing rules.

Raw report: `PHASE24_PATHA_SATA_NATIVE_ASTAR_DEDUP_20260906-drc.rpt`
