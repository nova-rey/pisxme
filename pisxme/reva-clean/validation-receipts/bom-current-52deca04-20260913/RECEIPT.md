# Current-source BOM and PCB reference coverage receipt

- Candidate commit: `52deca04`.
- Qualified worker: `pisxme-kicad-light:v1`; image digest is in `validation.json`.
- Native command: `kicad-cli sch export bom --format-preset CSV` from the canonical schematic, followed by native `pcbnew` reference comparison.
- Result: 117 BOM rows / references; 131 PCB references; no BOM-only references.
- PCB references absent from BOM: `MECH_M2_2280`, `TP1`–`TP13`. These are the existing explicitly excluded mechanical/test-point items and remain an open assembly/DFM disposition, not silently removed.
- This confirms the prior BOM gap against the current source and does not close DFM or assembly acceptance.
- Raw CSV, coverage output, command output, metadata, and hashes are retained here.
