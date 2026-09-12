# Integrated power native census receipt

- Source commit: `dbec6047` lineage, exact validation checkout at current HEAD.
- Toolchain: KiCad Light 10.0.6, image `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`.
- Native full-board DRC: 364 violations / 499 unconnected items.
- Violation classes: clearance 138, track_width 118, silk_over_copper 52, copper_edge_clearance 16, holes_co_located 9, track_dangling 9, via_dangling 7, courtyards_overlap 6, pth_inside_courtyard 5, tracks_crossing 2, lib_footprint_issues 2.
- This confirms the integrated baseline; rail-specific pad/track/zone ownership remains open and requires the next native rail census script before copper repair.
