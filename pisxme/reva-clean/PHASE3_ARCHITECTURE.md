# PiSXMe Rev A Clean — Phase 3 architecture contract

Status: native project shell and contract scaffold; no placement or routing.
Authority: `Approved Plans/PiSXMe_RevA_Clean_Rebuild_Plan.md`, Phase 3.

## Clean namespace

All new custom symbols and footprints belong to `PiSXMeRevAClean`, backed by
`PiSXMe_RevA_Clean.kicad_sym` and `PiSXMe_RevA_Clean.pretty`. The preserved
CM5IO and legacy PiSXMe libraries are evidence sources only. No clean source
may contain `PiSXMe:` identifiers, absolute machine-local model paths, or
unresolved library references.

## Required hierarchy

The production schematic shall contain exactly these functional sheets:

`CORE_CM5`, `V100_PCIE`, `V100_POWER`, `POWER_INPUT`, `REGULATORS`,
`ETHERNET`, `STORAGE`, `SERVICE`, `COOLING`, and `DEBUG`.

The root sheet owns only cross-sheet interfaces and global power policy. Each
functional sheet owns its local connectivity; there is one connectivity
authority per block. No PCB-only net, proxy net, or duplicated SKiDL/native
connectivity source is permitted.

## Frozen boundaries

- CM5: PCIe Gen2 x1, native Gigabit Ethernet, one USB3 storage path, USB2
  SERVICE, required control/debug, and power only.
- STORAGE: CM5 USB3 -> TI `TUSB9261IPVP` -> SATA -> JAE B-key M.2 SATA-only
  socket; no use of CM5 USB2 SERVICE.
- SERVICE: USB2 UFP only, two 5.1 kOhm Rd resistors, connector-boundary ESD,
  host VBUS sense/test; never sources VBUS.
- POWER_INPUT: two mandatory regulated/current-limited 12 V cold-plug inputs.
- PCB layers: F.Cu signals/components, In1 GND, In2 low-voltage power, In3
  protected 12 V/high-current power, In4 GND, B.Cu secondary signals/components.

## Phase 3 exit gate

The gate requires native KiCad reopen, ERC, netlist export, a namespace scan
with zero legacy IDs or machine-local paths, machine-readable symbol-pin/
footprint-pad parity, and zero PCB-only or proxy nets. Placement and routing
remain prohibited until that evidence is recorded.
