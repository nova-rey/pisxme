# R3 B2 Raw Pad-Edge Primitive Receipt

- Base: `2ae9af05`
- Candidate SHA-256: `e9c977f7fd965b0df7b130cfd7629cfd833ebd43be0c4ee51562d0318a9c3a8b`
- Worker/image: `pisxme-kicad-light:v1`, KiCad `10.0.6`
- Primitive: one F.Cu segment from the loaded J5 pad-2 east edge `(17.55,25.0)` to `(20.0,25.0)` on `PWR_SRC_J5_P2`
- Save/reload: PASS; pad 2 retained `PWR_SRC_J5_P2`; exactly one primitive track
- Fresh Light DRC: 938 violations, 435 unconnected
- DRC SHA-256: `553d57b6aa88d6a412ff9fef6f68f9e53ec9bcb2eb41c2e89473bfdb4bc10b05`
- Result: primitive checkpoint did not improve the open count and is not an integration candidate; retain as method evidence only.
