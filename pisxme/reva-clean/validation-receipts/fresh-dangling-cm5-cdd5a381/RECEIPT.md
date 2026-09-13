# Fresh Light validation — dangling CM5_5V track removal

Candidate: `cdd5a381`; KiCad 10.0.6 / `pisxme-kicad-light:v1`.

Fresh validation reports ERC **296 findings / 0 errors** and DRC **302
violations / 499 unconnected items**. The removal reduced total DRC and
`copper_edge_clearance` by one without changing unconnected count or creating
shorts. Remaining physical acceptance is open.
