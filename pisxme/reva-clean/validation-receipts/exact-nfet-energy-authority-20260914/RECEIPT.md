# Evidence receipt

`P24-EXACT-NFET-ENERGY-AUTHORITY` returned
`BLOCKED_INTERNAL_QUALIFICATION_GAPS` at base `ae0469bb`.

No exact production nFET MPN is promoted. `STL125N10LF8AG` is retained as the
strongest unqualified candidate. The required 4.45 V gate-drive, temperature,
VDS/transient, SOA/I2t, fuse/TVS/harness coordination, and installation gates
remain explicitly listed in `EXACT_NFET_ENERGY_AUTHORITY.{md,json}`.

No CAD or product requirement changed. Recommended queue dependency:
`authority:exact-nfet-energy-qualification`.
