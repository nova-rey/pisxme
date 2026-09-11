# RTL9210B Path-B working brief

The exact RTL technical copy and working layout are community evidence, not manufacturer
confirmation. Qualification facts include USB3, USB2, shared PCIe lane-0, a 25-MHz
crystal network, SPI flash, reset, and ISOLATEB. Production gates remain application
circuit, package/land pattern, SSD power/inrush, firmware provenance, and mode validation.

**Support consolidation answer:** confidence **medium** that the conceptual support
architecture is reasonably minimal: clock, reset/RSET, SPI, decoupling, mode detection,
and a switched SSD rail are ordinary distinct functions. No Tier-1 RTL9210B application
circuit has been retained proving unnecessary separation. MIC2545A is a valid rail-switch
precedent, but does not consolidate clock/reset/SPI functions. Do not redesign from this
finding; keep the support-promotion gate open.
