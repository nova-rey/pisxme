# Corrected binding Molex source contract

This receipt supersedes the earlier coarse three-branch wording in `MOLEX_MULTI_CONNECTOR_AUTHORITY.md`.

Bind three Molex `39-30-0060 / 0039300060` 5569 six-circuit right-angle headers. Each header uses three positive and three return contacts, yielding nine positive and nine return contact paths. Each positive/return contact pair is an independently current-limited or fault-isolated branch. A single 15 A fuse per connector is rejected because the Molex specification disallows passive current-sharing credit.

The governing arithmetic is:

- 40 A / 9 branches = 4.444 A per contact continuously;
- 45 A / 9 branches = 5.000 A per contact at the peak screen;
- 9 branches x 7 A conservative loaded-circuit screen = 63 A aggregate screen;
- continuous margin to the screen = 2.556 A/contact (36.5%);
- peak margin to the screen = 2.000 A/contact (28.6%).

The 13 A product-page value is not used as the design rating. The 7 A loaded-circuit screen governs until the exact terminal, wire, crimp, ambient, harness length, thermal rise and protection implementation are qualified. The protected common 12 V bus must support the full 40 A / 45 A contract. All nine branches and all three headers are required; no N-1 credit is allowed.

Molex 5569 released geometry defines the 4.20 mm grid, contact holes, mounting holes, row spacing and 2x3 envelope. Footprint Authority must audit source revision/hash, pads, drills, pegs, polarity, board-thickness limit, mask/annulus, courtyard and mating envelope. Prototype validation must cover branch current balance, contact/harness resistance, connector and protection thermal rise, PCB/common-bus drop, protection overload/I2t, 40 A continuous operation and controlled 45 A peak behavior. No hardware measurements are claimed.

Anderson remains superseded for active CAD because its exact land pattern is not fully specified by retained first-party records.
