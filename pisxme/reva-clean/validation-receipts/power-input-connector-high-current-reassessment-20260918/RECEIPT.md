# High-current input connector blocker reassessment

## Binding result

The prototype source requirement is 40 A continuous / 45 A peak. A single Anderson PP15/45 pole pair is electrically plausible from released manufacturer ratings, but the retained first-party land-pattern record does not fully bind PiSXMe's exact finished-hole, annular-ring, mask, courtyard, polarity, and mating installation data. It remains a reference/alternative and is not the active CAD choice.

The selected prototype architecture is three Molex Mini-Fit Jr. 5569 six-circuit right-angle headers, `39-30-0060 / 0039300060` (procurement normalization to `39-30-1060` tray MPN before purchase), at J5/J6/J9. Three positive and three return contacts per header provide nine explicit positive/return paths. No passive current-sharing credit is used; each positive path is separately fault-isolated by the existing nine-branch contract. The arithmetic is 40/9 = 4.444 A continuous and 45/9 = 5.000 A peak per contact-pair, below the retained 7 A loaded-circuit screen (63 A aggregate screen).

Molex released geometry defines the 4.20 mm grid, contact and mounting-hole locations, row spacing, polarity and 2x3 envelope. The project-local footprint is therefore engineering-authorized for prototype use, subject to the dimensional audit and DFM/mechanical checks already recorded in `validation-receipts/power-input-molex-5569-footprint-20260918/`. A vendor KiCad footprint is not required.

## Dependency disposition

`external:vendor-footprint-authorization` is RESOLVED for prototype CAD. No production AVL, supplier population assurance, or production qualification is required before Rev A prototype CAD. Remaining requirements are prototype validation: exact mating harness/crimp identity, contact fit/retention, 40 A continuous thermal/derating, bounded 45 A transient, and complete source-to-J1 resistance/drop and protection validation. These are validation gates, not an external blocker.

This result does not reopen the nine-branch electrical contract or the MPA corridor decision. It authorizes the producer to use the audited Molex footprint once the MPA plan is integrated.
