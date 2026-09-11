# Root global-label removal probe — rejected

A disposable complete-project probe removed only the root global label
`CM5_PER0_P` while leaving its root sheet-pin wire and child hierarchical
label unchanged. Native KiCad 10.0.5 ERC changed from 485 warnings / 0 errors
to 486 warnings / 0 errors and introduced one
`unconnected_wire_endpoint`; the original isolated-label warning did not
disappear. The exported netlist `(nets)` section retained exact name/node
parity, but the new dangling endpoint makes the transformation invalid.

Disposition: **REJECTED**. Root global labels are part of the live hierarchy
contract and cannot be removed individually. Probe source is retained in
`.phase24_root_global_label_probe/`; canonical schematic was not changed.
