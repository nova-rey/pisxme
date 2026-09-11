# Phase 24 coherent-grid probe rejection — 2026-09-11

The existing coherent-grid transformation was re-run in a fresh disposable
workspace against the current live sources. Native KiCad 10.0.5 ERC reported
746 findings, including 284 `endpoint_off_grid`, 232
`isolated_pin_label`, 151 `unconnected_wire_endpoint`, and two hierarchy
`pin_not_connected` errors. It therefore does not qualify as a production
repair.

Disposition: **REJECTED**. The probe did not modify canonical sources. It
confirms that moving the old contract coordinate families without incorporating
the current live port-set mapping is insufficient. The active implementation
path remains a single coherent root/child regeneration with explicit live
ports, followed by native hierarchy/ERC/netlist validation.
