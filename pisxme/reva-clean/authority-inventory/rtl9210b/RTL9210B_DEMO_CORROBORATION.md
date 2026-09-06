# RTL9210B demo schematic corroboration

Checked 2026-09-06. Source: the secondary-hosted RTL9210 68-pin demo
schematic, revision V203, which explicitly includes an RTL9210B-CG variant:
<https://www.scribd.com/document/969564441/RTL9210-VB-CG-DEMO-V203-pdf>.

This is corroborating application evidence only. It is not promoted to
manufacturer authority and does not close the Path-B production gate.

The indexed schematic text provides useful candidate values and topology:

- 5 V input to the internal LDO/SWR inputs;
- 2.2 uH switching-inductor path for the internal 1.1 V regulator;
- 12 kOhm, 1% RSET;
- 10 kOhm and 4.7 kOhm pull/support resistors on selected control/debug
  functions;
- separate controller rail bypassing and a switched SSD 3.3 V rail driven by
  ISOLATEBPIN;
- SPI flash footprint and test/UART/JTAG access;
- 25 MHz crystal support and M.2 PCIe sideband labels.

These values may seed the future disposable bring-up fixture, but the
retained datasheet itself says to follow the latest schematic circuit. The
demo is a different host design and does not establish the PiSXMe SSD power
budget, M-key empty-socket behavior, firmware rights, or exact Realtek
release land pattern. Those remain open gates.
