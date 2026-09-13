# Phase 24 bounded ERC source candidate: V100 PCIe labels

## Scope and base

- Producer base: `9e72fde1787db6e919d0e1b03d43ce4e7d77006b` (current exact
  branch head when this candidate was prepared).
- Source scope: `V100_PCIE.kicad_sch` only; no root schematic, child sheet
  pins, symbols, wires, UUIDs, coordinates, net names, or PCB files change.
- Warning family: the two remaining `same_local_global_label` records for
  `V100_PET0_P` and `V100_PET0_N`.

## Candidate

`phase24_promote_v100_pcie_link_labels.py` is an exact producer with fail-closed
UUID/coordinate guards. It changes these two local labels to global labels,
retaining their serialized coordinates and UUIDs:

```text
V100_PET0_P @ (100.32,102.54), UUID c0000000-0000-0000-0000-000000000002
V100_PET0_N @ (100.32,105.08), UUID c0000000-0000-0000-0000-000000000003
```

The disposable candidate was generated successfully. Candidate file SHA-256:
`92edfd89c158adb5075fe40a36c57a7088fd4d07723455572b2b5e13d5837c7d`.
`diff -u` contains exactly two `label` → `global_label` record changes.

## Current evidence and disposition

The exact-head retained ERC report
`validation-receipts/fresh-exact-current-c020b4f9/erc.json` records 24
`same_local_global_label` findings. The two V100 PCIe records are an
independent source-only cluster: root global labels already exist and the
child local labels are at the two guarded wire endpoints. Prior root-label
removal, hierarchy substitution, and duplicate-boundary deletion probes are
rejected for damaging connectivity; this candidate uses the distinct,
identity-preserving child-local promotion method.

Static producer checks pass. Native KiCad Light validation was not completed
in this producer attempt: the qualified worker clone could not be allocated
while the host filesystem was exhausted, and the host KiCad 10.0.5 process
also failed before producing a report. This is not a validation result and
must not be treated as a promotion. Root should run the candidate through a
fresh qualified KiCad 10.0.6 Light checkout, compare native netlist names and
node sets against the base, and promote only if no new ERC class/error or
semantic netlist delta appears.

