# Binding multi-connector source architecture correction

## Decision

Supersede the Anderson PP15/45 prototype footprint path for PiSXMe Rev A source input. Bind three Molex Mini-Fit Jr. 2x3 through-hole headers using the drawing-defined `39-30-0060` / `0039300060` family and the released 5569 interface drawing. Each header is one independently protected 12-V branch with three positive contacts and three return contacts. J5/J6 naming and the former two-connector arrangement are implementation choices and yield to this contract.

## Electrical screen

The conservative Molex 5556 four-to-six-loaded-circuit screen is 7 A per contact at the stated temperature-rise condition. Across three headers this gives nine positive contacts and nine return contacts, or 63 A screened capacity on each polarity. The 40 A continuous source contract requires 13.33 A per branch with three equal branches; the 45 A peak contract requires 15 A per branch. Set each branch protection limit to 15 A peak/maximum, with the source and harness independently rated above that limit. Each header therefore has 15 A branch protection against a 21 A conservative contact-group screen. No current-sharing credit is used to claim an individual contact rating; branch paths require matched harness/copper impedance, explicit protection and current verification during prototype bring-up.

The architecture is a conventional multi-connector GPU/Tesla-style source, not a precision-regulated six-loop system. It is suitable for prototype CAD because the manufacturer drawing defines the 4.20 mm contact grid, 1.80 mm contact holes, 3.00 mm mounting holes, 5.50 mm row spacing, and 13.80 x 8.40 mm 2x3 envelope. The 1.78 mm board-thickness recommendation, branch fuse/TVS/SW protection, copper/via capacity, and thermal margins remain integration requirements.

## Anderson disposition

Anderson PP15/45 remains electrically credible, but Footprint Authority found that B02021S Rev. 6 and DS-PP1545 do not fully define the exact project land pattern. No secondary footprint is promoted. Anderson evidence is retained as comparison material; it is superseded for the production/prototype CAD path by the drawing-defined Molex architecture.

## Prototype boundary

This decision establishes a safe design screen, not fabricated-hardware proof or production AVL qualification. Prototype validation must measure branch current balance, harness/crimp resistance, connector and fuse temperature rise, 40 A continuous operation, controlled 45 A transient response, protection action and first-power behavior. No measurements are claimed here.

## Sources

Molex 5569 sales drawing `039300040_sd.pdf`, Molex Mini-Fit Jr. specification `PS-43879-001-001.pdf`, and Molex `0039300060` product record. Source URLs and hashes are retained in the Librarian evidence packet.
