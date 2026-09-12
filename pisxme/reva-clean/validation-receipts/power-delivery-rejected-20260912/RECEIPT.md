# Phase 24 power delivery producer rejection — 2026-09-12

## Candidate identity

- Workstream: `power_delivery_producer`
- Committed producer base: `c8710a84cc142b6ca8a04697e40b89576591eb26`
- Qualified worker: `/home/nyx/pisxme-eda-workers/scripts/pisxme-worker`
- Image: `pisxme-kicad-light:v1`
- KiCad: `10.0.6`
- Candidate: `PHASE24_POWER_DELIVERY_CANDIDATE.kicad_pcb`
- Candidate SHA-256: `48e49ec7fcb3d2e2d511072d987a66a1026f79acade906eed7434510b1446681`

The candidate was generated in the disposable worker only. It was not
integrated into canonical CAD, and no schematic, rule, library, or global
configuration was changed.

## Bounded method

The producer added pad-center-derived F.Cu same-net joins for the U3/U4/U5
12V_PROTECTED and POWER_GND exposed fields, added a U3 protected-field leg,
and added direct F.Cu capacitor-row joins for BRIDGE_3V3 and BRIDGE_1V1.
Zone filling and native DRC were run after serialization. The branch-B input
and fused rails were deliberately not guessed into a long obstacle-filled
corridor during this attempt.

## Native result

The untouched base run was 312 violations / 499 unconnected items with zero
shorting_items. The candidate run was 336 violations / 378 unconnected items,
including 13 `shorting_items` and 13 `solder_mask_bridge` findings. The
unconnected count improvement is therefore not acceptable evidence for
promotion.

The concrete new shorts are:

- U3 `12V_PROTECTED` leg intersects its `NC` pad 15 at `(62.25,163.75)`.
- Direct BRIDGE_3V3 capacitor-row joins cross the POWER_GND pads of C16/C17.
- Direct BRIDGE_1V1 capacitor-row joins cross the POWER_GND pads of C26–C40.

The candidate is **REJECTED**. No real short or manufacturing defect may be
waived. Raw evidence is retained beside this receipt:

- `base-drc.json`, `base-drc.stdout`, `base-census.json`
- `candidate-drc.json`, `candidate-drc.stdout`, `candidate-census.json`
- `make_power_candidate.py`
- `PHASE24_POWER_DELIVERY_CANDIDATE.kicad_pcb`
- `SHA256SUMS`

## Next method

Do not retry direct same-layer capacitor-row joins or the U3 pad-16-to-pad-14
vertical leg. A materially different, obstacle-aware method is required:
reserve each regulator/capacitor launch channel from actual pad geometry, use
side-entry dogbones and ordinary through-via handoffs on an approved power
layer, and connect BRIDGE rails on a separate layer only after checking every
POWER_GND pad and existing high-speed corridor. Branch-B input/fused delivery
must likewise be routed from actual J6/F2/Q2/U2 pads through a reviewed
corridor. Revalidate every material candidate in fresh Light before any
canonical integration.

Power closure remains open: continuity, DRC, current capacity, branch sharing,
voltage drop, transient/inrush, regulator loss, thermal, and return-path
acceptance are not established by this attempt.
