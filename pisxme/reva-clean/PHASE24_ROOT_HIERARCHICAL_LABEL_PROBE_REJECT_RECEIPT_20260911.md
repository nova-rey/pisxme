# Root hierarchical-label substitution probe — rejected

A disposable complete-project probe changed only the root `CM5_PER0_P`
`global_label` to `hierarchical_label`. Native KiCad 10.0.5 changed the
canonical 485-warning / 0-error result to 486 findings, adding one
`pin_not_connected` and one `unconnected_wire_endpoint`; the isolated-label
count did not fall. The root/child contract was therefore damaged even though
the experiment was limited to one label.

Disposition: **REJECTED**. The current global-label contract cannot be
replaced piecemeal by hierarchical labels. Canonical CAD was not changed.
Probe evidence is retained in `.phase24_root_hlabel_probe/`.
