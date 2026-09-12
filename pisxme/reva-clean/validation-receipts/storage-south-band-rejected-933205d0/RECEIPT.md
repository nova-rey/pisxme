# Rejected South-Band Path-A Storage Producer

- Base: `933205d0`
- Toolchain: `pisxme-kicad-light:v1`, KiCad 10.0.6
- Scope: disposable Path-A U7/C30-C33/U13/J3 route attempt
- Baseline: 312 DRC violations, 499 unconnected items, 0 shorts, 2 crossings
- Candidate: 454 DRC violations, 499 unconnected items, 12 real shorts, 8 crossings
- New classes: 42 solder-mask bridges, 14 hole-clearance defects, 18 dangling tracks
- Root cause: authoring used U13.34/.33/.32/.31 instead of native SATA pads U13.2/.3/.6/.7; these are JMS PCIe pads.
- Disposition: rejected; no canonical CAD change or integration.
- Next method, if reattempted: derive native pad coordinates programmatically, use correct pads, and place layer transitions outside pad fields and J3 via-clearance geometry.

Raw worker outputs were disposable and not retained after release; counts and root-cause evidence above are the durable rejection record.
