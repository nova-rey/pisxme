# Schematic-authoring tooling report

Status: `SCHEMATIC_AUTHORING_TOOLING_BLOCKED`.

The bridge has a hybrid architecture: official KiCad PCB IPC plus a direct
`kicad-sch-api` 0.5.6 backend. Basic create/load/save, symbols, wires, labels,
sheets, connectivity helpers, transactional saves, and unit tests exist.

The gate is not closed. KiCad 10.0.5 has no clean headless Update PCB from
Schematic command. Project-local PiSXMe library resolution emitted warnings in
round trips, embedded and external symbol definitions differed for critical
parts, and one existing-schematic probe introduced semantic/ERC changes and
changed project association. Flat syntax and native parsing are not enough:
hierarchy, custom pin-to-pad mapping, and schematic-derived PCB authority must
be proven on Linux. Do not use PCB-only proxy nets for M6.
