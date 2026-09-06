# RTL9210B-CG corroborating support-netlist extraction

Status: **CORROBORATING ONLY — NOT production authority**  
Generated from the native KiCad XML export
`RTL9210B_0.xml` on 2026-09-06.

The source is the WIP `HynixCJR/LZ-1-Backplane` RTL9210B implementation. It
is useful because KiCad has parsed the actual symbol, components, nets, and
pin identities. It is not sufficient to release a PiSXMe design: the source
does not provide Realtek production authorization, a released land pattern,
firmware rights, or a validated M-key sideband/power implementation.

## What the native netlist actually contains

| Area | Native evidence | Engineering interpretation |
|---|---|---|
| USB | U2.37/38 USB2 and U2.41/42/46/47 USB3 nets | The controller is wired as a combined USB2/USB3 bridge. |
| Shared storage lane | U2.64/65 and U2.67/68 are named PCIe lane-0 nets | The community design corroborates the shared SATA/PCIe lane identity from the retained technical document. |
| PCIe sideband | U2.61/62 REFCLK, U2.13 CLKREQ#, U2.14 PERST# | Sideband ownership is exposed, but the source does not prove the PiSXMe M-key behavior. |
| Mode/power | U2.8 `/PDET`, U2.12 `/ISOLATEB`, U3/U12 MIC2545 load switches | The WIP design uses PEDET and separate switched rails; exact mode sequencing and load/inrush remain open for PiSXMe. |
| Reference | U1 25-MHz crystal, C10/C17 16 pF, U2.52 clock supply | Confirms a concrete oscillator implementation, not its suitability for our final layout without application-circuit review. |
| SPI | CN3 W25Q128FVIQ connector and U2.18/19/21/22/23/24 | Provides accessible flash signals and a plausible programming boundary. Flash MPN, image, configuration, and rights remain open. |
| Analog/support | R17 12 kOhm RSET, R15/R16 76.8 Ohm current-limit resistors, L5 1 uH internal-switch inductor | These are corroborating candidate values only; they must not be promoted without an authorized/current application circuit. |
| Power | U2 5-V input pins 17/33, local 1.1-V and 3.3-V nets, U3/U12 switched SSD rails | Shows the source's power partition. It does not close the Rev-A SSD current, inrush, thermal, or inactive-interface analysis. |
| Unused pins | U2.5/6/9/10/27/28/43/44/48/49 are explicitly unconnected in the export | Preserve as review findings. They are not automatically safe no-connect decisions for PiSXMe. |

## Reproducible audit

Run:

```text
python3 pisxme/reva-clean/phase24_rtl9210b_corroborating_support_audit.py
python3 pisxme/reva-clean/phase24_rtl9210b_corroborating_support_audit.py --negative-control
```

Both commands pass at this checkpoint. The negative control mutates the
RTL9210B component identity and verifies that the audit fails rather than
accepting an expected list as synthetic evidence.

## Gates this narrows, but does not close

- **B1 support circuit:** narrowed by a native parsed implementation; still
  open because the source is WIP/corroborating and not a current authorized
  Realtek application circuit.
- **B2 M-key sidebands:** still open. The extracted source has controller
  sideband nets but is not the PiSXMe M-key socket mapping.
- **B3 land pattern:** still open. The retained community footprint has bad
  `through_hole` metadata and is not reused unchanged.
- **B4 SSD power/inrush/thermal:** still open. The WIP rails are not a
  validated Rev-A SSD power budget.
- **B5 provisioning:** still open. The source's flash connector is useful
  for a future fixture, but does not establish authorized firmware/config or
  virgin-chip programming rights.

The next valid Path-B experiment remains a standalone, disposable native
bring-up fixture only after B1–B5 are sufficiently documented. No production
schematic or PCB was changed by this extraction.

