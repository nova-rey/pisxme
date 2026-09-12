# Rejected BRIDGE_3V3 U4 local link — 2026-09-12

- Base integrated candidate: `9ab4a9f4`
- Toolchain: KiCad Light 10.0.6, image `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`
- Proposed scope: two F.Cu segments from U4 pad 5 to nearby C18 pad 2 on `BRIDGE_3V3`.
- Native result: DRC return code 5, 442 violations, 499 unconnected items.
- Baseline comparison: 433 violations, 499 unconnected items.
- Decision: reject and do not integrate; no connectivity improvement and nine additional DRC violations.
- Raw report SHA-256: `17cb0dd3f28e6d73fe98c8f2bfdab84fd0d5d05e7459f909f565f2bcaba47b8d`
- Raw stdout SHA-256: `47dc5dbf8aada75707d6d66f729c187c6c2fd8175b40d213f14c5e844a3d46c8`

This is a bounded method result, not evidence that the BRIDGE_3V3 topology is impossible. A different route family or return-aware method is required.
