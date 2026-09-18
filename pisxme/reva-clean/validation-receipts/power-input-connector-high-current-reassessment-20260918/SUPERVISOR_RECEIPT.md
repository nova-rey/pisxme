# Supervisor receipt — high-current input connector reassessment

- **Package:** `P24-POWER-INPUT-CONNECTOR-HIGH-CURRENT-REASSESSMENT`
- **Canonical queue package:** `P24-POWER-INPUT-CONNECTOR-ARCHITECTURE-REASSESSMENT`
- **Base state:** queue candidate base `ff9da674`; governing Molex correction base `6261b569`
- **Result:** `DONE`
- **Canonical CAD changed:** no
- **External dependency:** `external:vendor-footprint-authorization` **RESOLVED**

## Binding recommendation

Use three Molex Mini-Fit Jr. 5569 dual-row right-angle through-hole six-circuit headers. The existing Product/Power authority binds the family as `39-30-0060 / 0039300060` (`5569-06A2-210` bulk identity), with three positive and three return contacts per header. The current Molex drawing marks the `39-30-0060` bulk package as not recommended for new applications and lists `39-30-1060` (`5569-06A2`, tray, 94V-2 matte tin) as the current orderable equivalent; this procurement identity must be normalized before hardware purchase. `39-30-1061` is the select-gold tray variant and is not a second architecture.

All nine positive/return contact pairs are required. Each pair receives independent positive-series fault isolation/current limiting; a single fuse per connector and passive contact-sharing credit are rejected. The binding source screen is 40 A continuous and 45 A for 100 ms. With the Molex 5556 phosphor-bronze 16-AWG, four-to-six-loaded-circuit screen of 7 A/contact at 30 °C rise:

```text
40 A / 9 pairs = 4.444444 A per pair
45 A / 9 pairs = 5.000000 A per pair
9 pairs x 7 A = 63 A screened capacity per polarity
```

The design therefore retains 2.555556 A/pair continuous screen margin and 2.000000 A/pair peak screen margin. These are manufacturer application screens and design calculations, not installed-hardware qualification.

## Candidate comparison

- **Single high-current system:** Samtec PowerStrip/40 `PET-08-02-T-VT-LC` + `PES-08-02-T-VT` + configured PESS cable. The retained TC0919-2456 Rev. 2 evidence screens 48.5 A/contact after 20% derating at 30 °C rise with two energized contacts. It remains unselected because the exact configured cable/footprint bytes and local mechanical envelope were not retained.
- **Anderson PP15/45:** `ASMPR45-1X2-RK`, housings `1327/1327G6`, PCB contacts `3-5912P1`/`3-5913P1`. It is electrically credible at the published 40 A CSA/TUV and 45 A UL screens, but Footprint Authority found no released exact contact-tail drill/slot, datum, plating, pad/annulus, or mask definition. It is superseded for active CAD.
- **Selected GPU/Tesla-style architecture:** three Molex 5569 six-circuit headers. Public carrier precedent supports the multi-header form factor; no external carrier CAD or rating was imported.

## Footprint authority and dimensional audit

The project-local footprint can be authored from the released 5569 interface data. The audited candidate is `Molex_5569-06A2_2x03_P4.20mm_Horizontal.kicad_mod`, SHA-256 `014a8f9b4ad6a1583aec43a5c0fb2a603e305970adf463eea26cd6afa54c7051`. The audit records six 1.80 mm finished PTH drills on a 4.20 mm contact grid, 5.50 mm row spacing, two 3.00 mm NPTH peg holes, 8.40 mm contact span, and 13.80 mm body envelope. The Molex drawing recommends a 1.78 mm board thickness.

Pad copper size, annulus, mask expansion, courtyard margin, solder-fillet allowance, and 3D orientation are project/fabrication decisions. Final DFM must verify them against the six-layer 1.6 mm board, NPTH copper/via keepouts, wave/selective/hand-solder access, right-angle mating envelope, cable bend/strain relief, cooler and board-edge clearance, and the aggregate copper/via/thermal path. The local footprint audit does not claim production AVL or fabricated fit.

## Source provenance

The authority records cite Molex 5569 sales drawing `039300040_sd.pdf`, Molex `PS-43879-001-001.pdf`, and the `0039300060` product record. The Library retains metadata and extracted facts only; vendor bytes were not copied, so exact local SHA-256 values for those Molex sources are unavailable by design. The current official Molex drawing is `55690002-SD` (document part A2, revision B, 2023-10-23); the current specification is `PS-43879-001-001`, revision A2, ECM 851282, dated 2026-03-24. Refreshing the source manifest to the exact downloaded bytes is evidence hygiene before hardware procurement, not a footprint blocker.

Local authority hashes:

- `MOLEX_MULTI_CONNECTOR_AUTHORITY_V2.md`: `132bd0c98b1b71379712112f764baef147064edb490893be81d40c5bd4e89770`
- footprint dimensional audit: `196187868da6699ac74ea147526fddbb797dea41c6bd04da40ac63931166551c`
- prototype validation receipt: `d551e29990646cb239e28d898d9f26ce85c453a13ccf8aec6c6652268f5407c8`

Anderson comparison source hashes remain recorded as B02021S Rev. 6 `7a32189a34ff2feea3bf173c788f3dd63229ea98dfefed8009b1bc5738e8cd2c` and DS-PP1545 `ac39c286d44528efab30061b96df6e64e6eeafb6e154af7a03397d518f45a04f`.

## Remaining D fields and queue action

The dependency is removed for prototype CAD. The remaining D fields are exact header plating/orderable MPN, mating 5557 housing and 5556 terminal, conductor gauge/length/bundle/crimp, branch protection implementation, hot effective connector/harness loop <=4.0 mOhm, complete source-to-J1 loop <=10.0 mOhm, 40 A current balance and thermal rise, and controlled 45 A/100 ms behavior. These belong to the existing prototype/integration validation path and do not restore `external:vendor-footprint-authorization`.

Queue evidence shows `external:vendor-footprint-authorization`, `authority:P24-POWER-INPUT-CONNECTOR-ARCHITECTURE-CORRECTION`, and `authority:P24-POWER-INPUT-FOOTPRINT-RECONCILIATION` all `RESOLVED`; no package is waiting on vendor footprint authorization. Root may proceed with normal serialized integration and request fresh Light validation against any integrated candidate. No unrelated architecture branch is reopened.

## Validation performed

Read the live registry, queue package and dependency state, Library brief/index/provenance, Anderson failure audit, Molex V2 authority, Molex dimensional audit, nine-branch contract, and prototype validation plan. Verified the local artifact hashes above and recomputed the nine-pair current arithmetic. Current Molex drawing/specification claims were checked against the official manufacturer records. No CAD or canonical library file was edited.
