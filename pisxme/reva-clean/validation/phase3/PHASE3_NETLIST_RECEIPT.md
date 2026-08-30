# Phase 3 native netlist export receipt

Checked: 2026-08-30. Status: `CLOSED`.

KiCad 10.0.5 exports the clean root hierarchy with the native S-expression
netlist command. The export is run in a project-local temporary working
directory because this KiCad build does not reliably write export output to an
absolute path outside the project working directory.

The generated reference export was 55,811 bytes and the BOM was 1,080 bytes.
The export emitted no annotation warning after `phase14_annotation_normalize.py`
converted underscore-bearing descriptive references to legal unique KiCad
references. `test_phase3_netlist_export.py` repeats the export in an isolated
temporary directory and checks representative references across the hierarchy.

This closes the annotation/netlist prerequisite. It does not claim that the
acreage PCB is populated or routed; those remain later plan phases.
