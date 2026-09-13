# Rejected single Path A storage pair route

Base: `3ff559fd`. A B.Cu dogleg was added for only the native
`M2_SATA_A_P_PCIE_TXP0` U13.2→J3.49 pair. Fresh Light DRC reported **309
violations / 499 unconnected items** with no shorts, but added four track-width
and two track-dangling findings and did not reduce connectivity. The candidate
was rejected and no copper was integrated.
