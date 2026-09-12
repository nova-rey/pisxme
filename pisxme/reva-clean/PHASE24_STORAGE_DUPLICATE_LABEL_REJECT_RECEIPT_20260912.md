# Phase 24 duplicate STORAGE label canonicalization rejection

The disposable probe `phase24_storage_duplicate_label_canonicalization_probe.py`
replaced 20 exact x=70 `NC_*` labels with the corresponding JMS named labels.
It was tested against the post-alias canonical source without modifying it.

Native KiCad 10.0.5 ERC changed from 311 warnings / 0 errors to 317 warnings
/ 0 errors. `multiple_net_names` fell from 23 to 6, but
`isolated_pin_label` rose from 126 to 149. This is not a net improvement and
the candidate is rejected. No canonical schematic or netlist change was
promoted. The raw probe report remains in the disposable output directory.
