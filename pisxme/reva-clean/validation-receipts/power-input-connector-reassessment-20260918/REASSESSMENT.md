# High-current input connector architecture reassessment

## Binding prototype architecture

Product/Power Authority binds one Anderson Powerpole PP15/45 1x2 positive/return assembly:
`ASMPR45-1X2-RK`, housings `1327`/`1327G6`, and 45 A right-angle PCB contacts `3-5912P1`/`1336G1` and `3-5913P1`/`1337G1`. The released manufacturer data supports the 40 A continuous source contract at its CSA/TUV condition and a 45 A contact-family rating. The 40 A rating has no installation derating margin and the 45 A value is not a dedicated 100 ms pulse qualification; those remain prototype validation requirements.

The path is one positive pole and one return pole. No passive current-sharing credit is used. At the published 0.525 mOhm wire-contact screen, the connector-only drop is 21 mV / 0.84 W at 40 A and 23.6 mV / 1.06 W at 45 A per contact. These are connector screens, not a complete source-to-J1 budget.

## Footprint authority

Anderson drawing B02021S Rev. 6 and the PP15/45 datasheet provide contact variants, housing datums, mated envelope, 7.9 mm contact spacing, PCB layout datums, staple-hole locations, mounting features, contact dimensions, PCB thickness range, and the 10 AWG board-copper recommendation. They do not prescribe PiSXMe finished-hole drill, annular ring, solder-mask expansion, or project courtyard. Those values may be authored from the released contact envelope and PiSXMe fabrication rules and must be recorded in the footprint dimensional audit. A vendor KiCad footprint is not required for prototype CAD.

## Alternative comparison

Two conventional Molex Mini-Fit Jr. 5569 2x3 headers have released 4.2 mm-grid through-hole geometry, but Molex provides no current-sharing credit and the standard 5556 six-circuit screen is approximately 7 A/circuit: two headers require 6.67 A/contact at 40 A and 7.5 A/contact at 45 A, leaving no acceptable peak margin. TE ELCON Mini 2204535-1 has released hole/pitch data and a 35 A/contact rating, but the two-connector harness, branch impedance and sharing evidence are not yet a complete source contract. These remain alternatives, not the binding architecture.

## Dependency disposition

`external:vendor-footprint-authorization` is resolved for prototype CAD. Retain only production AVL/supplier approval and prototype empirical validation as non-blocking requirements. Add a `prototype-validation` dependency covering source/harness resistance and thermal rise, contact fit/pull, 40 A continuous derating, and 45 A transient validation. No canonical CAD was edited.

Sources: Anderson PP15/45 product record and datasheet; Anderson B02021S Rev. 6 drawing; Molex 5569 drawing and PS-43879; TE ELCON 2204535-1 record and customer drawing. Source URLs and hashes are recorded in the Librarian brief.
