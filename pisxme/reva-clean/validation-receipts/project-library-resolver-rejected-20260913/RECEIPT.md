# Project-library resolver context candidate — rejected

- Base: `ad261db9`
- Worker workspace: `project-library-resolver-context`
- KiCad image: `pisxme-kicad-light:v1`, KiCad 10.0.6
- Scope: disposable `sym-lib-table`/`fp-lib-table` context only; no canonical CAD edits.

The candidate resolved official `Device`, `Capacitor_SMD`, and
`Package_TO_SOT_SMD` paths using the image environment. ERC changed from 351
findings to 410 findings, and the exported native netlist changed bytewise.
Both ERC and netlist commands returned zero because the commands completed;
that return code is not a clean-result claim. The candidate is rejected because
it worsens findings and lacks a semantic-preservation proof. The before/after
reports, resolver tables, environment, and return codes are retained here.
