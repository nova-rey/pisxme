# Phase 24 all-authoritative PCB DRC recheck

Date: 2026-09-12  
Candidate ref: `78532426`  
Candidate: `PHASE24_ALL_AUTHORITATIVE_PARTS.kicad_pcb`  
Validator: fresh KiCad Light 10.0.6

Native KiCad DRC reports 680 violations and 406 unconnected items. The
largest classes are 297 clearance, 199 track-width, 63 solder-mask-bridge,
and 406 unconnected findings; these remain open and unwaived. The candidate
also has 2 footprint-library issues.

The same checkout passes `phase24_full_reference_set_audit.py`: 78 schematic
references, 101 PCB references, and exactly 23 documented mechanical/test-point
extras. This DRC baseline is a separate all-authoritative candidate and does
not replace the retained 612/409 acreage evidence for other candidate files.
