# CM5/Ethernet edge DFM candidate R2

Package: `P24-MECHANICS-CM5-ETHERNET-EDGE-DFM`

- Dispatch base recorded by Root: `7280badc`
- Actual current canonical base used: `ef1dcbfb2fe44a33b80d0a6c2f73f91f045854ab` (the branch had advanced by documentation-only commits)
- Candidate commit (isolated producer): `a09c181b1dc065ac4711026f897b984baad73e48`
- Candidate board SHA-256: `5bd896bfaa1f56717c2f11166b3aad6e00418900820cc0b69c2d679851da2f57`
- Changed-scope manifest SHA-256: `5a4ea81ce45985cc018b655939617599ecbc4372ef95bf32d112b329ada2ad8a`
- KiCad Light: `pisxme-kicad-light:v1`, image `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`, KiCad `10.0.6`
- Canonical context hashes: rule `d5473e6262fdf3b53d5de051626f0ed76dedf7257ba591f79ab8ad55f5b411ec`, fp-lib-table `864698c14e65cd70a5b5a08d23a22477919bf29f167d26fc0eda73dd43b3be61`, sym-lib-table `3bb180e251be1f62b2be5bbe486b29263c56c6a49b7a26103a27bef29b80c311`

Changed scope is limited to C48–C51 y=178.5, C8 y=172.5, and the retained seven CM5_5V track/two-via local lower-edge delta. Producer metadata records exact endpoints. No protected-bus, J1, high-speed, or global-rule edits occurred.

Fresh Light refill DRC: **264 violations, 393 unconnected**, with 120 clearance, 117 track-width, 9 track-dangling, 7 via-dangling, 5 PTH/courtyard, 4 courtyard-overlap, and 2 crossing findings. It reports **zero shorting items, zero library-footprint issues, zero XIN/XOUT width findings, and zero copper-edge-clearance findings**. The C7/C8 courtyard overlap is absent.

The baseline from the same current source and context was 280 violations / 393 unconnected, including 15 copper-edge-clearance findings and 5 courtyard overlaps. The candidate introduces no count regression in unconnected items or shorts; remaining DRC findings are outside this package.

Return: `CANDIDATE_READY`. Root must perform serialized canonical integration and independent validation before DONE.
