# Phase 4 V100 lane-0 receipt

Checked: 2026-08-30. Status: `PISXME_REVA_CLEAN_PHASE4_CLOSED`.

The V100 child sheet now contains only the approved schematic island:

- CM5 PCIe lane 0 PER0/PET0;
- two transmitter-side PET0 220 nF coupling capacitors;
- differential REFCLK;
- active-low PERST;
- selected Amphenol `74221-101LF` Rev-W contact mapping A2/A3, G1/G2,
  E7/F7, and E18;
- explicit V100 power and ground contract labels.

The machine-readable audit is `test_phase4_v100_audit.py`. It proves one
SXM2 instance, exactly two PET0 capacitors, all required lane-0 labels, and
zero PER1+, x16, NVLink, switch, or redriver baggage. Native KiCad 10.0.5
reopen/ERC passes with zero violations; the regenerated netlist is non-empty.

The SXM2 connector identity is Amphenol `74221-101LF`, Rev-W. Its local
400-pad land pattern remains the explicitly recorded `REV_A_EMPIRICAL_RISK`
from Phase 2 because public sourcing did not provide a directly downloadable
manufacturer CAD land-pattern file; no physical fit or endpoint enumeration
claim is made. Undocumented V100 endpoint reset/power-sequencing behavior is
also `REV_A_EMPIRICAL_RISK` pending hardware validation.

No PCB placement, routing, or conventional island was modified.
