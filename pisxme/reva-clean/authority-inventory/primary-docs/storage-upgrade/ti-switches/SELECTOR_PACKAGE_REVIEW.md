# TI selector package review

Checked 2026-09-06 against the retained datasheets, including the package
sections rather than inferring a footprint from a family name.

`HD3SS3412` uses TI package drawing `RUA0042A`, a 42-pin WQFN with exposed
thermal pad 43. The retained datasheet provides the signal table, SEL pin 9,
and the package/land/stencil views. Its recommended VDD is 3.3 V and its
high-bandwidth port common-mode range is 0--2 V.

`HD3SS6126` is not promoted onto that footprint by analogy. Its device
information identifies a 9.00 mm x 3.50 mm TQFN package and its pinout has
different signal ownership, including HS_OE pin 6, SEL pin 9, and the
SSA/SSB/SSC plus HSA/HSB/HSC groups. Its package drawing and land pattern
must be authored separately from its retained datasheet before the native
dual-mode schematic/PCB is regenerated.

This review intentionally removed the initially generated shared selector
footprint candidate. Package-family resemblance is not pin/land authority.
