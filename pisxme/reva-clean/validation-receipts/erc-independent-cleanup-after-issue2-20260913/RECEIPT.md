# Independent ERC/source lane result

- Base: `3b70587d`.
- One exact guarded source repair was tested: remove only `NC_62` at `STORAGE.kicad_sch` coordinate `(70,127.535)`, UUID `f1000000-0000-0000-0000-0000000000a2`; paired `JMS_CC1_NC` label, symbol pins, and wires were retained.
- Fresh KiCad Light 10.0.6 ERC: baseline 293 findings; candidate 294. `multiple_net_names` fell 22→21, but `isolated_pin_label` rose 126→128.
- Native netlist export succeeded, but semantic parity failed: the base `U11.62 ↔ J3.62` node split into separate `JMS_CC1_NC` and `NC_62` nets.
- Candidate rejected; no canonical files changed. This is a bounded no-candidate result, not a waiver or blocker for unrelated rows.
