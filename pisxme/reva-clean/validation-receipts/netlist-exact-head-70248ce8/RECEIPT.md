# Exact-head native netlist regeneration

- Candidate/source commit: `70248ce8`
- Worker/image: fresh detached `pisxme-kicad-light:v1`; KiCad 10.0.6
- Schematic: `PiSXMe_RevA_Clean.kicad_sch`
- Command: `kicad-cli sch export netlist --format kicadxml -o native-netlist.xml PiSXMe_RevA_Clean.kicad_sch`
- Result: native KiCad XML netlist regenerated successfully with return code 0.
- Scope: this replaces stale SATA-era checked-in export for future parity work; it does not itself prove pad coverage or routed connectivity.
- Raw output and checksum are retained here.
