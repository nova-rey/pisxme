# Fresh Light delta analysis

- Baseline: 919 DRC / 435 unconnected
- Candidate: 926 DRC / 434 unconnected
- Delta: +7 DRC / -1 unconnected

baseline {'solder_mask_bridge': 111, 'track_width': 117, 'courtyards_overlap': 6, 'pth_inside_courtyard': 5, 'clearance': 427, 'hole_clearance': 199, 'shorting_items': 29, 'tracks_crossing': 2, 'silk_over_copper': 2, 'hole_to_hole': 2, 'track_dangling': 12, 'via_dangling': 7}
candidate {'solder_mask_bridge': 111, 'track_width': 117, 'courtyards_overlap': 6, 'pth_inside_courtyard': 5, 'clearance': 433, 'hole_clearance': 199, 'shorting_items': 30, 'tracks_crossing': 2, 'silk_over_copper': 2, 'hole_to_hole': 2, 'track_dangling': 12, 'via_dangling': 7}

Candidate added classes: clearance +6, shorting_items +1; hole/other classes unchanged by count. The new short reports nets `PWR_SRC_J9_P1` and `12V_PROTECTED`.
