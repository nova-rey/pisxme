# R3 construction-correction blocker

The authorized insulated copper construction was added without changing branch routing, fuse identity, J1 mapping, or high-speed copper. The exact proposed construction is C11000 copper foil, 1.0 mm x 8.0 mm x 82.0 mm, 0.10 mm polyimide on both faces, six millimetres positive/return separation, and four bonded transitions per polarity.

The four-wire model gives `0.499` mOhm effective PCB neck and `8.099` mOhm complete path, within the authority targets. Model-only current density and pulse heating are retained; continuous thermal rise and joint qualification are unproven.

Native Light result: `1555` DRC violations, `426` unconnected items, return `5`; stats return `0`. DFM remains blocked by clearance, solder-mask, shorting, hole, courtyard, and co-location findings. This candidate requires Package/DFM construction review and prototype qualification; no canonical integration was performed.
