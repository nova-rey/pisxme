# Fresh native netlist receipt

- Candidate commit: `0d62a8f3`.
- Worker: qualified `pisxme-kicad-light:v1`.
- Command: `kicad-cli version --format plain`; `kicad-cli sch export netlist --format kicadxml` from the canonical schematic.
- Native export completed successfully in a fresh detached Light checkout.
- This supersedes stale checked-in SATA-era XML for current source inspection; it does not by itself close bidirectional coverage or physical connectivity.
- Raw netlist, version, validation metadata, and hashes are retained here.
