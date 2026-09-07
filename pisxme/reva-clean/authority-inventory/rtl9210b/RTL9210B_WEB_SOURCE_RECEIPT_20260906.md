# RTL9210B-CG web-source receipt

Checked 2026-09-06 from the live pages below. This receipt records what the
pages establish; it does not promote community material to manufacturer
authority.

## JLCPCB / LCSC procurement lead

Source: <https://jlcpcb.com/partdetail/RealtekSemicon-RTL9210BCG/C5143573>

The current listing identifies:

- manufacturer: Realtek Semicon;
- MPN: `RTL9210B-CG`;
- JLC part: `C5143573`;
- package: `QFN-68`;
- assembly: SMT, Economic and Standard PCBA;
- MSL: 3;
- EasyEDA symbol/footprint availability; and
- PCBA-only storage: the page says purchased parts cannot be shipped
  separately.

The page does **not** provide a reproducible quantity-1 price, stock depth,
or lead-time receipt in this environment. Therefore it closes identity and
JLC assembly eligibility only. Bare-chip availability remains `MEDIUM/HIGH`
until a live BOM quote or traceable lot is obtained.

## HynixCJR/LZ-1-Backplane

Source: <https://github.com/HynixCJR/LZ-1-Backplane>

The repository explicitly describes its PCB as work in progress while
documenting RTL9210B as a USB 3.2 Gen 2 to NVMe/SATA M.2 subsystem. Its
schematic, symbol, footprint, and PDF are retained locally under this
directory as corroborating evidence. The repository is not used as sole
production authority; the imported footprint's `through_hole` metadata was
caught and a local SMD qualification footprint was recreated.

## Firmware ecosystem

Sources:

- <https://github.com/bensuperpc/rtl9210>
- <https://github.com/damnnfo/rtl9210b-firmware>

These repositories establish that RTL9210A/B firmware, configuration files,
update tooling, and recovery artifacts exist in the public ecosystem. They do
not establish Realtek authorization, exact virgin-chip compatibility, or
redistribution rights. Those remain explicit Path-B promotion gates.

## Decision impact

This receipt strengthens the procurement and ecosystem evidence for Path B;
it does not close the two productization gates: authorized initial
programming/configuration of a virgin `RTL9210B-CG`, and firmware provenance/
redistribution rights. Path A remains intact and Path B remains an isolated
parallel candidate.
