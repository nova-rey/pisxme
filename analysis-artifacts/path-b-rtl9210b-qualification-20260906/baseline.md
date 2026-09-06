# Read-only inspection receipt

Date: 2026-09-06. Commands were run from `/home/nyx/PiSXMe`; generated native
reports for this inspection were directed to `/tmp/pisxme-pathb-readonly-O3bSDl`
and were not added to the repository.

## Worktree boundary

The repository was already heavily dirty before this artifact was created
(observed status summary: 61 modified paths and 3,175 untracked paths). Existing
Path-A and Phase-24 changes were preserved. No existing KiCad file, library,
report, plan, or `bible.md` entry was edited for this task. The only intended
repository mutation is this new disposable directory.

## KiCad-aware surface

- `kicad-cli`: KiCad 10.0.5
- `pcbnew`: available; KiCad Python ABI environment at
  `/home/nyx/pisxme-toolchain-environment/bin/pisxme-pcbnew-python`
- `eeschema`: available
- Flatpak app: `org.kicad.KiCad` 10.0.5 stable
- No dedicated KiCad IPC/MCP tool was exposed in the current tool surface.
- Native `pcbnew` inspection loaded the current placement candidate and
  inspected J3/U11/U12/U13 without saving it.

The KiCad CLI netlist command returned exit code zero for the direct schematic
probes but did not materialize the requested output under `/tmp` in this
Flatpak invocation. This is recorded as a tool limitation, not as netlist
proof. The retained `PHASE24_DUAL_MODE_STORAGE.net` is an existing native
Eeschema 10.0.5 export and remains historical evidence.

## Stackup and rules

The released fabrication basis is six-layer `JLC06161H-7628`, nominal 1.6 mm,
1 oz outer and 0.5 oz inner copper, with L2/L5 solid GND planes and ordinary
through vias. The released geometry is 5.2 mil width / 8 mil spacing for the
90-ohm PCIe/USB/USB2 pairs and also 100-ohm SATA/Ethernet targets; final fab
coupon measurement remains required.

The `PiSXMe_RevA_Clean.kicad_dru` file is only a placeholder rule file. The
active `PiSXMe` project rule file contains a USB3 width rule, but the isolated
Path-B fixture must receive a standalone reviewed rule basis rather than
silently inheriting the dirty production project.

## Schematic/PCB correspondence

- The current child schematic is `pisxme/reva-clean/STORAGE.kicad_sch` and
  contains the Path-A dual-mode topology: TUSB9261, JMS583, two TI selectors,
  TE J3, and J5/U14 mode control. It contains no RTL9210B component.
- The current root is `PiSXMe_RevA_Clean.kicad_sch`; retained status records
  Path-A native ERC as open and the child/root hierarchy as unfinished.
- The current placement candidate is
  `PHASE24_DUAL_MODE_STORAGE_PLACEMENT.kicad_pcb`; native `pcbnew` found 117
  footprints, 1,011 tracks, two zones, J3 with 71 pads, U11 JMS583 with 64
  pads, U12/U13 selectors with 43 pads each. This is Path-A evidence only.
- The community RTL9210B schematic instance uses a 68-perimeter-pin plus
  exposed-pad symbol and the community QFN footprint. It is not part of the
  current root/child correspondence.

## Fresh read-only validation observations

Commands:

```text
kicad-cli sch erc --format json --severity-all --output /tmp/.../storage-erc.json pisxme/reva-clean/STORAGE.kicad_sch
kicad-cli sch erc --format json --severity-all --output /tmp/.../root-erc.json pisxme/reva-clean/PiSXMe_RevA_Clean.kicad_sch
kicad-cli pcb drc --format json --severity-all --output /tmp/.../PHASE24_DUAL_MODE_STORAGE_PLACEMENT-drc.json pisxme/reva-clean/PHASE24_DUAL_MODE_STORAGE_PLACEMENT.kicad_pcb
kicad-cli pcb drc --format json --severity-all --output /tmp/.../PHASE24_DUAL_MODE_STORAGE_SUPPORT_ROUTED-drc.json pisxme/reva-clean/PHASE24_DUAL_MODE_STORAGE_SUPPORT_ROUTED.kicad_pcb
kicad-cli pcb drc --format json --severity-all --output /tmp/.../PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED-drc.json pisxme/reva-clean/PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED.kicad_pcb
```

Observed results:

| Object | Fresh native result | Interpretation |
|---|---:|---|
| `STORAGE.kicad_sch` ERC | 379 findings | Open; not an ERC pass. |
| `PiSXMe_RevA_Clean.kicad_sch` ERC | 952 findings | Open root/hierarchy baseline. |
| Path-A placement PCB DRC | 884 violations / 499 unconnected | Unrouted/partial candidate; not a release result. |
| Path-A support-routed PCB DRC | 1,159 violations / 499 unconnected | Open routing/partial-fixture result. |
| Path-A USB3 isolated PCB DRC | 211 violations / 78 unconnected | Partial fixture; route findings remain. |

Retained reports use different checkpoints and counts, including 407 ERC and
1,069/1,013 DRC observations. They are not silently reconciled with the fresh
run; the source hashes in `evidence-manifest.json` identify each current input.
None of these Path-A baselines authorizes Path-B integration.

## Community source inspection

- `RTL9210b_0.kicad_sch` contains the expected 1–69 pin names, including
  PEDET, ISOLATEB, CLKREQ, PERST, SPI, crystal, USB, shared SATA/PCIe lane 0,
  and REFCLK.
- Its instance footprint is `QFN-68_L8.0-W8.0-P0.40-BL-EP4.8` and its source
  module declares `(attr through_hole)` despite every perimeter pad being SMD.
- `RTL9210B-CG_QUALIFICATION.kicad_mod` changes the attribute to `smd`, adds
  explicit F.Fab body geometry, and uses a conservative larger courtyard. It
  remains a qualification candidate, not released manufacturer CAD.
- Community support values are present, but the retained qualification record
  explicitly treats them as corroboration only and requires the latest
  authorized application circuit.

## Native M-key inspection

Current native J3 value: `1-2199230-4`; footprint:
`TE_1-2199230-4_MKEY`. It loads as 67 contacts plus M1/M2/S1/S2 mechanical
pads. Contact 69 is named `M2_PEDET` in the current Path-A candidate. This
confirms current socket representation only; it does not close direct
RTL9210B sideband ownership.
