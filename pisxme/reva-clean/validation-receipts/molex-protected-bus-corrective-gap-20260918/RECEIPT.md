# Corrective protected-bus producer gap receipt

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Workstream: `molex-protected-bus-fresh-20260918-r2`
- Base: `841ee7738e21ee78e617c17507a7fb31f8e561fb`
- Toolchain: KiCad CLI 10.0.6, `pisxme-kicad-light:v1`
- Result: **BLOCKED — missing authoritative schematic topology**
- Canonical CAD: unchanged
- Candidate: none

## Bounded commissioning evidence

A fresh disposable checkout was prepared from the exact assigned base. Native
KiCad DRC ran against `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb` and
returned **300 DRC violations** with exit code 0 because `--exit-code-violations`
was not requested. Native ERC ran against `PiSXMe_RevA_Clean.kicad_sch` and
returned its raw report. Native schematic netlist export succeeded.

The authorized Molex 5569 2x3 footprint receipt was present and its source
geometry was preflighted. Its retained audit records six 1.80 mm PTH contacts,
two 3.00 mm NPTH mounting holes, 4.20 mm contact pitch, 5.50 mm row spacing,
and the derived pad/annulus choices. The source and project hashes are in
`EVIDENCE_MANIFEST.json` and `SHA256SUMS`.

## Exact topology gap

The selected current schematic/netlist cannot express the authority-required
three-header, nine independently protected positive/return contact-pair
architecture without adding new symbols, branch nets, component identities,
values, footprints, and protection contracts that are not present in the
current approved source state.

| Current source element | Native current state | Consequence |
|---|---|---|
| `J5` | 2 electrical contacts: `1=12V_IN_A`, `2=POWER_GND`; 2 NPTH pegs | one positive/return input pair only |
| `J6` | 2 electrical contacts: `1=12V_IN_B`, `2=POWER_GND`; 2 NPTH pegs | one positive/return input pair only |
| `F1` | one source fuse group: `12V_IN_A` to `FUSED_12V_A` | no branch-specific subdivision |
| `F2` | one source fuse group: `12V_IN_B` to `FUSED_12V_B` | no branch-specific subdivision |
| `D1/U1/Q1` | one A TVS / LM74700 / high-side path | one protected stage |
| `D2/U2/Q2` | one B TVS / LM74700 / high-side path | one protected stage |
| power net set | `12V_IN_A`, `12V_IN_B`, `FUSED_12V_A`, `FUSED_12V_B`, `12V_PROTECTED`, `POWER_GND` | no nine branch-positive nets, nine branch-return nets, or nine independent protection nets |

The current native power component inventory is therefore two input pairs and
two protection chains. Installing three 6-contact headers and assigning their
contacts to those six existing nets would create passive parallel contacts and
would not satisfy the binding correction requiring nine independently
current-limited or fault-isolated branches. It would also make a false
connectivity/DRC green result possible without proving branch protection.

To proceed, Product/Power Authority must provide or authorize the missing
source-level contract: nine branch net identities and the exact independently
protected/fault-isolated stage for each branch (component MPNs/values,
footprints, ratings, and schematic ownership), plus how the nine returns are
joined into the protected common return. This is an authority/topology gap,
not a KiCad footprint or routing failure.

No new component, value, or synthetic net was invented. No candidate PCB was
created and no canonical file was changed.

## Raw evidence

Raw baseline DRC/ERC/netlist and the pcbnew footprint/net inspection are
retained beside this receipt. The inspection reports the existing 2-pin J5/J6
mapping and the existing two-stage protection inventory. `EVIDENCE_MANIFEST.json`
records exact source identities and hashes.
