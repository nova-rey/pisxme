# R3 focused P2 branch diagnostic

- Base: `8974ce97`.
- Worker/image: `p24-protected-bus-r3-mpa-producer`, `pisxme-kicad-light:v1`, KiCad 10.0.6.
- Method: one J5.2/F2 positive and return pair with local F.Cu escapes, ordinary F.Cu→In2/In4 vias, and bounded x=106 join endpoints; no fuse pad-field bridging.
- Native DRC: 961 violations, 434 unconnected items, exit code 5.
- Result: diagnostic only; no candidate or integration claim. It shows that removing pad-field bridges reduces the added DRC burden but does not close the branch.
