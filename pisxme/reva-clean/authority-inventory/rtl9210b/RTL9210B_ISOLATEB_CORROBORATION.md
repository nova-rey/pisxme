# RTL9210B `ISOLATEB` support corroboration

Checked 2026-09-10 against `authority-inventory/rtl9210b/RTL9210B_ROOT.xml`.

The retained community schematic gives a concrete implementation direction:

- RTL9210B pin 12 (`ISOLATEBPIN`) connects to U3 pin 1 (`EN`).
- U3 is Microchip `MIC2545A-1YM`, LCSC `C637455`, a documented 3-A
  high-side power-distribution switch.
- U3 pins 6 and 8 are on the M.2 `+3V3` input net; pin 3 is GND; pin 4
  has an ILIM resistor; pins 5 and 7 are switched-output support nodes;
  pin 2 is an intentionally unconnected fault output.

This is corroborating implementation evidence, not manufacturer authority
for PiSXMe. It narrows the current `ISOLATEB` opening to a local SSD-power
switch/support review. The exact PiSXMe source rail, output capacitors,
current/inrush/thermal budget, fault policy, and authorized production
application circuit remain open. No component or production schematic was
changed by this receipt.
