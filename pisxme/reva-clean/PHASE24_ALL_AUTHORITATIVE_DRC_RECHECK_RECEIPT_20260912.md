# Phase 24 all-authoritative PCB DRC recheck

Date: 2026-09-12  
Candidate ref: `436f4625`  
Candidate: `PHASE24_ALL_AUTHORITATIVE_PARTS.kicad_pcb`  
Validator: fresh KiCad Light 10.0.6

Fresh KiCad Light validation from the exact candidate ref reports 680
violations and 406 unconnected items. The
largest classes are 297 clearance, 199 track-width, 63 solder-mask-bridge,
and 406 unconnected findings; these remain open and unwaived. The candidate
also has 2 footprint-library issues.

Raw recheck workspace:
`validation-phase24-all-authoritative-fresh-20260912T150914Z`.
Command:
`kicad-cli pcb drc --exit-code-violations --output all-authoritative-drc.rpt PHASE24_ALL_AUTHORITATIVE_PARTS.kicad_pcb`

The same checkout passes `phase24_full_reference_set_audit.py`: 78 schematic
references, 101 PCB references, and exactly 23 documented mechanical/test-point
extras. This DRC baseline is a separate all-authoritative candidate and does
not replace the retained 612/409 acreage evidence for other candidate files.
