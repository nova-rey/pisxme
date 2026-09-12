# Rejected BRIDGE_3V3 U7 local stitch — 2026-09-12

- Base integrated candidate: `9ab4a9f4`
- Toolchain: KiCad Light 10.0.6, image `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`
- Proposed scope: one F.Cu 0.20-mm segment between native U7.30/U7.31 pads on `BRIDGE_3V3` at (98.2,120.2)–(98.6,120.2).
- Native result: 433 DRC violations and 499 unconnected items; the open moved to the next U7.24-to-field connection.
- Decision: reject and do not integrate; no net-count reduction.
- Candidate PCB SHA-256: `26023275831bd789fedc9a65a3003380e549a16fb3057b1b48bb66139fcb3e97`
- DRC JSON SHA-256: `20e5b760d62e07795ea60110d9f16688717ec996d55db99a9efb3ff6c8725fde`

This bounded local-return test confirms a native pair can be joined but does not close the integrated rail. Choose a return-aware multi-pad route or another independent acceptance lane; do not replay this stitch.
