# Phase 24 live-port coherent-grid probe rejection — 2026-09-11

The current live-port contract reconciliation and coherent-grid transform
were combined in a fresh disposable workspace. Native KiCad 10.0.5 ERC
reported 749 findings, including 284 `endpoint_off_grid`, 232
`isolated_pin_label`, 149 `unconnected_wire_endpoint`, and seven hierarchy
`pin_not_connected` errors.

Disposition: **REJECTED**. Canonical schematic and child sources were not
modified. The result shows that text-level reconciliation of contract pin
counts followed by coordinate transformation does not reproduce a valid
native hierarchy for the current live port sets. The next required path is
native-authored hierarchy regeneration with the complete live port mapping,
then native reopen/ERC/netlist comparison before any production promotion.
