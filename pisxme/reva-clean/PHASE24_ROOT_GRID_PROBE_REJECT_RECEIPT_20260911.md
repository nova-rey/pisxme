# Phase 24 root-grid probe — rejected

A disposable owner-preserving transform moved every root schematic coordinate
field to the nearest 1.27 mm grid location, including sheets, sheet pins,
labels, and wires. Native hierarchy structure validation passed and the
exported netlist remained exactly 338 nets with zero changed node sets.

However, native ERC remained **489 warnings / 0 errors**, with the same 201
`endpoint_off_grid` findings. The transform therefore does not address the
actual warning mechanism and was not promoted. Canonical CAD is unchanged.
