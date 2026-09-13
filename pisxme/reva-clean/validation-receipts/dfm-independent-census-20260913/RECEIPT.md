# Independent DFM and assembly release census — 2026-09-13

Scope: read-only review of the current integrated candidate `47364e6d`, kept disjoint from the MPA-owned storage/power corridor.

- Current PCB SHA-256: `75d2d370…181bf7c`; 131 references.
- Legacy tracked BOM is stale (50 rows, omits 90 current references and includes 9 obsolete references).
- Prior regenerated BOM covered 117/131 on an older PCB; exclusions TP1–TP13 and MECH_M2_2280 remain explicit and must be rechecked on the final SHA.
- Current release directory lacks current CPL, Gerbers, drills, assembly drawings, and fabrication parameter package.
- Only four 3D model records are present; connector models J1/J2/J3/J4/J5/J6/J8 remain missing.
- Integrated DRC still has courtyard, PTH/courtyard, and edge-clearance families; these remain open.
- Final integrated candidate must regenerate BOM/CPL and fabrication outputs in fresh KiCad Light after electrical/DFM closure, retaining commands, return codes, image identity, and hashes.

This receipt classifies the gap; it does not close DFM or mechanical acceptance rows and makes no CAD edits.
