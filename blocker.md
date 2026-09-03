# PiSXMe Rev A Clean — Blocker Report

## Final state

`PISXME_REVA_CLEAN_BLOCKED`

## Earliest failed gate

Phase 17 — Ethernet routing.

Phases 0–16 are not the current blocker. Phase 3 schematic/library authority
is closed, and Phase 16 PCIe routing is closed with its documented bounded
Rev-A empirical risk.

## Blocking condition

The Phase 11/12 placement is frozen with the CM5 Ethernet source at J7 near
the left side and the Ethernet ESD and MagJack at the right edge, separated by
the V100 cooler reservation and existing regulator, power, PCIe, and connector
keepout geometry.

Under the approved six-layer contract—F.Cu primary signals, In1/In4 solid
ground, In2/In3 power, B.Cu secondary signals, ordinary through-vias, and no
ordinary signals on plane layers—the frozen placement does not admit a short,
monotonic, no-maze Ethernet route.

## Evidence

- Latest native KiCad DRC candidate: `pisxme/reva-clean/ACREAGE_ETHERNET_PHASE17-drc10.rpt`
- Latest candidate report: 319 total violations, including existing acreage
  debt.
- Representative Ethernet failures include CM5 pair crossings at J7,
  pair shorts near U6/U9, crossings against existing power/regulator tracks,
  NPTH hole-clearance violations at J7/F2/J2, and ESD pad-field clearance
  violations.
- Tested variants included perimeter routing, separated B.Cu corridors,
  via-in-pad transitions, and compact ESD placements. None passed the Phase 17
  gate.
- No rejected candidate was accepted as production routing.

## Authority status

Closed:

- Native Ethernet hierarchy and eight MDI-pair connectivity.
- EDAC `A70-112-331N126` manufacturer pad mapping.
- Complete logical-pin to physical-pad aliases for all 18 MagJack contacts.
- Native PCB mapping regression.
- CM5/J7, ESD, and MagJack net authority.

Relevant commits:

- `490ae22` — EDAC physical pad alias correction.
- `ce62f86` — Phase 17 routing rejection and blocker record.

## Impact

Phase 17 cannot close. Phase 18 USB3, Phase 19 SATA, final acreage freeze, and
external-review-ready status must not begin or be claimed.

No accepted routed design was pushed, fabricated, ordered, or published.

## Best practical resolution

Reopen the Phase 11/12 placement decision and create a compact CM5-adjacent
Ethernet island containing J7 breakout, ESD protection, EDAC MagJack, and local
shield/return and center-tap circuitry. Then regenerate and revalidate affected
downstream phases before retrying Phase 17.

Routing Ethernet on power/ground plane layers or accepting the current maze
would violate the approved plan and is rejected.

## 2026-09-03 placement-repair sprint evidence

The authorized Phase 11/12 Ethernet-only reopening was attempted with nine
compact CM5-adjacent candidates plus a complete west-edge island trial. The
most promising topology placed U9 at (25,100), U6 at (29,106), and the EDAC
MagJack at (12,119), with U9 and U6 rotated 180 degrees so the CM5 source
ordering is monotonic at each ESD package. The complete trial is preserved as
`pisxme/reva-clean/ACREAGE_ETHERNET_TRIAL_ORDERED_WEST.kicad_pcb` and its
native report as
`pisxme/reva-clean/ACREAGE_ETHERNET_TRIAL_ORDERED_WEST-drc.rpt`.

That candidate still has true Ethernet failures: same-layer crossings and
shorts in the CM5-to-ESD escape, WSON power/ground pad-field interference,
right-column escape collisions, and MDI corridor collisions with the J2 NPTH
and PTH pad field. It reports 390 total native DRC violations, including the
known acreage baseline debt, and 237 unconnected items. It is rejected and is
not a production PCB.

This closes the authorized local placement-repair attempt for the current
standard TPD4E004 two-layer topology. Phase 17 remains blocked; no Phase 18+
work was started. The smallest practical continuation is an Ethernet-local
component change. The preferred candidate for the next disposable trial is
Littelfuse `SP3019-04HTG`: its gullwing SOT-23-6L layout has I/O on 1/3/4/6,
GND on 2, and NC on 5, avoiding the current TPD4E004 power/signal choke
point. This is not yet promoted; it must first pass pin-accurate footprint,
sourcing, native DRC, and complete Phase 17 validation.
