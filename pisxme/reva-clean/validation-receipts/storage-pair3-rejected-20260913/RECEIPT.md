# Rejected F.Cu normal-width storage pair route

Base: `b02f0eaa`. A single `M2_SATA_A_P_PCIE_TXP0` U13.2→J3.49 dogleg was
attempted on F.Cu at the normal 0.20 mm width. Fresh Light DRC reported
**313 violations / 499 unconnected**, adding six clearance and five
solder-mask findings while reducing no connectivity. Candidate rejected;
canonical PCB unchanged.
