# TI selector package review

Checked 2026-09-06 against the retained datasheets, including the package
sections rather than inferring a footprint from a family name.

`HD3SS3412` uses TI package drawing `RUA0042A`, a 42-pin WQFN with exposed
thermal pad 43. The retained datasheet provides the signal table, SEL pin 9,
and the package/land/stencil views. Its recommended VDD is 3.3 V and its
high-bandwidth port common-mode range is 0--2 V.

`HD3SS6126` has different signal ownership, including HS_OE pin 6, SEL pin 9,
and the SSA/SSB/SSC plus HSA/HSB/HSC groups, but its retained datasheet also
uses the RUA0042A land-pattern drawing. It therefore receives a separate
library name (`HD3SS6126_RUA0042A`) even though the physical pad geometry is
shared; pin function and schematic mapping are not shared by assumption.

The earlier shared-name candidate was removed. The current pair of named
footprints is based on the actual common drawing plus separate pin tables.
