# Fresh integrated SERVICE USB2 width validation — 2026-09-13

- Integrated candidate: `22d25b04`
- Toolchain: KiCad Light 10.0.6, image `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`
- ERC: 351 findings, 0 errors; same source result as before.
- DRC: 424 violations / 499 unconnected items. Classes: 119 track_width, 138 clearance, 80 silk_over_copper, 28 text_height, 16 copper_edge_clearance, 9 holes_co_located, 9 track_dangling, 7 via_dangling, 6 courtyards_overlap, 5 pth_inside_courtyard, 3 silk_overlap, 2 tracks_crossing, 2 lib_footprint_issues.
- Like-for-like prior integrated report: 433 violations / 499 unconnected; this candidate removes 30 width findings and introduces 21 clearance findings, for a net reduction of 9 DRC violations.
- DRC SHA-256: `46a849ca79ebf9bd066888f637662f75b91c9f9fc3150d548d6da7008e209148`
- ERC SHA-256: `5f2c3acfccffb8a96ac432199b688c5bfdc5297493273edfb35f42ce003b3a62`
- The parity command reported the existing fully-annotated-schematic limitation; it is recorded, not waived.

Disposition: accept this scoped width improvement as the current integrated candidate; Phase 24 remains open.
