# Phase 1 reconciliation receipt

Date: 2026-08-29  
Status: `PASS_WITH_EXPLICIT_FIX_QUEUE`

## Frozen donor baseline

The legacy electrical sources remain byte-stable at the Phase 0 checkpoint:

| File | SHA-256 |
|---|---|
| `pisxme/PiSXMe.kicad_sch` | `d31ff8e96fd1df211f5528f0b4c70f8b7a7891d68383d4561bfae83116bf5bbb` |
| `pisxme/PiSXMe.kicad_pcb` | `a53e6751a59eb530afd3b522672b5ce967515710bf7eece54a5aa4242e81316e` |
| `pisxme/PiSXMe.kicad_pro` | `d3a7b822ae1cfa8eb3da075e11ff9f763c3940218c92a5acded2e4f718e858c2` |
| `pisxme/PiSXMe.kicad_sym` | `5f017fe96dfcd394939034f490e67596571583226110bd7b2ee54a9c32b2d8f8` |

Current parser-visible legacy PCB census is 62 footprints, 89 segments,
46 vias, and 0 zone records under the simple record scan. The older 165-via
and 40-zone census in `cleanup/human-routing/BASELINE.md` used a different
parser/board snapshot and is therefore stale for current-source geometry; it
is retained as historical evidence, not merged into the clean baseline.

## Reconciled stale records

- `design/CRITICAL_FOOTPRINT_AUDIT_FINAL.md` describes several items as closed,
  while `design/CRITICAL_FOOTPRINT_AUDIT_V2.md` and
  `design/FINAL_BLOCKER_REVIEW_V2.md` retain unresolved SXM2 land-pattern,
  K18/K19, and assembly/authority risks. The stricter unresolved disposition
  controls the clean rebuild.
- Historical PCIe records reporting 7 vias/129 tracks and later reports for
  the active source are not interchangeable with the Phase 0 active hashes.
  The clean project will measure its own native source rather than inherit
  either count.
- Legacy `PiSXMe:` identifiers are expected in the frozen donor and are not a
  Phase 3 clean-library pass criterion. They are explicitly forbidden only in
  `pisxme/reva-clean/`.
- Existing ERC/DRC counts are baseline evidence (94 ERC, 803 DRC, 182
  unconnected) and do not authorize routing or repair of the donor.

## Phase 1 gate decision

PASS. KEEP/FIX_WHILE_TRANSPLANTING/DISCARD dispositions exist for PCIe/SXM2,
mechanics/power, CM5, protection, regulators, footprints and rules. The only
open items are intentionally carried into later gates: exact authorities,
independent library validation, V100 empirical behavior, and clean-project
connectivity. Phase 2 authority inventory may begin.

