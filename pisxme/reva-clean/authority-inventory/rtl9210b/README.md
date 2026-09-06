# RTL9210B-CG Path-B qualification evidence

Retrieved 2026-09-06 for the isolated Path-B comparison. This directory is
not production CAD and does not replace Path A.

## Evidence retained

| Artifact | Provenance | Use | Limitation |
|---|---|---|---|
| `community-lz1/rtl9210b.pdf` | HynixCJR/LZ-1-Backplane, commit `18444b9d584036ff8e0221d5eacb3fb2a0d3fbd5` | Rev. 1.1 pin, mode, power, timing and package evidence | Community-hosted copy; verify with Realtek before release |
| `community-lz1/RTL9210b_0.kicad_sch` | Same repository | Corroborating complete implementation | Repository labels the PCB WIP; not a production oracle |
| `community-lz1/easyeda2kicad.kicad_sym` | Same repository | Corroborating symbol/pin naming | Requires independent pin audit |
| `community-lz1/QFN-68...kicad_mod` | Same repository | Package geometry cross-check | Incorrectly marked `through_hole`; never reuse unchanged |
| `firmware-tools/README.md` and configs | bensuperpc/rtl9210, commit `265d4727a29e9c443f5ff567107556924c1879c2` | Firmware/config/programming/recovery procedure | Community tools, Windows-only updater, device-specific configs |
| `firmware-tools/*bin` and `RTL9210B_CG_upqi.cfg` | damnnfo/rtl9210b-firmware, commit `c381c0e56ad37ab40d5e56f690417d0942c061d7` | Demonstrates obtainable firmware artifacts | Provenance/licensing and virgin-chip compatibility remain open |

The PDF is the strongest available technical source in this qualification;
the CAD and firmware repositories are corroboration, not manufacturer
authorization. SHA-256 values for retained files are recorded in the
procurement/qualification report and should be regenerated before release.

KiCad 10.0.5 natively exported XML netlists from the retained
`RTL9210b_0.kicad_sch` and `M.2_0.kicad_sch`; the receipts are
`RTL9210B_0.xml` and `M.2_0.xml`. They confirm native parsing and expose the
community schematic's RTL9210B pin/net names and M.2 PEDET contact 69. This
is schematic parse evidence, not a completed PCB or ERC/DRC pass.
