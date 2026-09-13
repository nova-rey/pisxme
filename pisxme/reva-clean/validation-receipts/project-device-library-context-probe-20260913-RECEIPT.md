# Project Device library context probe

Base: `8a8dde37` (selected integrated candidate).
Toolchain: `KiCad 10.0.6 / pisxme-kicad-light:v1`.

The project `sym-lib-table` was provisionally extended with the qualified
system `Device.kicad_sym` at `${KICAD10_SYMBOL_DIR}/Device.kicad_sym`, without
changing the schematic or PCB. Fresh Light ERC then reported **296 findings /
0 errors**: 126 `isolated_pin_label`, 121 `endpoint_off_grid`, 24
`same_local_global_label`, 22 `multiple_net_names`, and 3
`footprint_link_issues`. The prior 53 `lib_symbol_issues` disappeared.

This is a validation-context correction candidate, not a physical-design
repair. Native netlist export completed and is retained for semantic
comparison before integration. No PCB, schematic, symbol, pin, or net was
edited by the probe.
