# Phase 24 redundant STORAGE NC-label repair rejection

Disposable candidates tested:

* coordinate-group removal: over-broad; changed netlist structure;
* exact-name removal: removed 33 records and changed netlist structure;
* exact warning-name plus `x=70` coordinate removal: removed only 20 records.

The final coordinate-exact probe reduced native ERC from 312 to 305 warnings
with zero errors, but exported netlist comparison still found 11 extra net
names and 11 changed node sets. It is therefore rejected: the `NC_*` records
participate in the current hierarchy/netlist contract despite the native
`multiple_net_names` warnings. No canonical schematic or netlist authority
was changed. The warnings remain open and unwaived.
