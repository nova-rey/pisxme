# Fresh validation after bridge USB label integration

- Integrated source head: `8a8dde37`
- Worker: `pisxme-kicad-light:v1`, KiCad 10.0.6
- Scope: schematic-only label scope change; PCB unchanged.

Fresh Light ERC reports **349 findings / 0 errors**. Native netlist export
completed and is retained with the exact command return codes. The producer
semantic comparison remains valid: 361 net names and sorted node sets are
unchanged. This source improvement does not close integrated DRC, storage,
power, SI, DFM, or hostile-review rows.
