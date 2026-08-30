# PiSXMe Rev A Clean — Phase 5 power architecture receipt

Checked: 2026-08-30. Status: `PISXME_REVA_CLEAN_PHASE5_CLOSED`.

The schematic-only power architecture contains two mandatory cold-plug 12 V
inputs, two TI `LM74700QDBVRQ1` reverse-current branches, one protected merged
12 V rail, and three `TPSM63606RDLR` converters for CM5 5 V, bridge 3.3 V,
and bridge 1.1 V rails. MPNs are present on every generated power-stage
instance; the bridge IC is not reused as a regulator.

`validation/phase3/test_phase5_power_audit.py` proves the dual-input policy,
protected merge, required rails, and absence of a 12 V-to-M.2 cross-connection.
Native KiCad 10.0.5 ERC reports zero violations. Regulator feedback values,
thermal margins, current-density, and vendor-layout overlays remain required
for the later routing/PI phases.

No PCB placement or routing was introduced.
