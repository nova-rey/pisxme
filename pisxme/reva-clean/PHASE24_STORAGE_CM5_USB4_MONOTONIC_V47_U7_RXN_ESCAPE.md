# Phase 24 Path-A V47 U7 RX_N escape experiment

**REJECTED — non-improving local route class.** V47 starts from V46 and
regenerates only `BRIDGE_SATA_RX_N` around the U7 TX_N field using ordinary
through-vias. Complete SATA endpoint connectivity passes and native DRC has
zero shorting entries, but the result remains **601 violations / 399 opens**
and relocates the local RX_N/TX_N crossing rather than removing it.

No production PCB, schematic authority, validation severity, or layer policy
changed. V46 remains the preferred disposable parent. This candidate is
preserved as evidence that this isolated U7 RX_N move does not close the
remaining corridor.
