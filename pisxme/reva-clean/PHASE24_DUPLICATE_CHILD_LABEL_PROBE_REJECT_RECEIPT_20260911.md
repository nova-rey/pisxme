# Duplicate child rail-label probe — rejected

A disposable complete-project probe removed the second serialized
`BRIDGE_3V3` and `BRIDGE_1V1` hierarchical label from each of `REGULATORS`
and `STORAGE`, leaving the long source-owned wire records intact. Native
KiCad 10.0.5 changed the current 485-warning / 0-error result to 489
findings, adding four `unconnected_wire_endpoint` findings. The probe did
not provide a safe warning reduction and was not promoted.

The repeated labels occur at distinct source-owned rail contract locations;
they are not interchangeable duplicate records. Canonical CAD was not
changed. Evidence remains in `.phase24_duplicate_child_label_probe/`.
