# Protected-bus material-selection authority

- **Package:** `P24-PROTECTED-BUS-MATERIAL-SELECTION`
- **Authority ID:** `PISXME-P24-PROTECTED-BUS-MATERIAL-SELECTION-20260921`
- **Decision state:** `SIGNED_ENGINEERING_AUTHORITY`
- **Scope:** material/fabrication selection only; no schematic, PCB routing, placement, or rule edits authorized
- **Candidate under review:** `c574c287` / fresh Light ref `86568f8b`
- **Candidate evidence:** `protected-bus-r3-distributed-mesh-producer-20260921/DFM_THERMAL_RESISTANCE.md`, `FRESH_VALIDATION_RECEIPT.md`

## Decision

The ordinary selected 1 oz outer / 0.5 oz inner six-layer construction is not
adequate for the present protected-bus mesh. The candidate extracts an
**effective PCB neck of 0.977 mOhm** against the `0.650 mOhm` effective
allocation and a complete hot path of **8.577 mOhm** against the hard `8.500
mOhm` limit. The candidate also fails its independent native Light result
(`1526` DRC violations, `426` unconnected items) and is not an integrated
candidate.

Authorize one bounded material-selection change before any new routing:

> Use a local, insulated copper reinforcement/parallel-copper source field,
> electrically bonded at the source/fuse and protected-bus transition, sized
> and laid out so the extracted effective PCB neck is no greater than `0.650
> mOhm` at the hot operating condition. Retain the six-layer signal stack and
> the ordinary through-via contract. Use heavier copper as a substitute only
> if the fabrication authority supplies a revised, order-specific stackup and
> impedance basis that passes the SI/DFM checks.

The minimum required reduction from the current mesh is `0.327 mOhm`
(`33.47%`). If the selected reinforcement achieves the effective `0.650 mOhm`
limit without increasing any other term, the modeled complete path is at most
`8.250 mOhm`, leaving `0.250 mOhm` below the hard cap.

A lower-resistance fuse/holder is authorized only as supplementary margin. It
cannot replace the reinforcement because recovering the `0.077 mOhm` total
overage does not cure the `0.327 mOhm` PCB-allocation overrun. No additional
routing or placement variant is authorized until the material construction is
specified and independently extracted.

## Retained requirements

The material change shall preserve:

- source `11.4–12.6 V`;
- `300 W` sustained and `330 W / 100 ms` peak product envelope;
- source capability `40 A` continuous / `45 A` bounded peak;
- protected-bus minima `11.05 V` sustained / `11.00 V` peak;
- nine independently protected positive/return paths, with no unqualified
  passive-sharing or N-1 credit;
- `7 A` contact screen and measured branch-balance limit of `10%`;
- complete source-to-J1 hot path `<=8.50 mOhm`;
- selected six-layer signal/reference architecture unless a fabrication
  authority signs a replacement stackup;
- ordinary through-vias, protected high-speed corridors, J1 mapping, and
  required DFM/mechanical clearances.

The `0.650 mOhm` value is an effective nine-branch PCB-neck allocation. It is
not a requirement that every branch individually measure `0.650 mOhm`.
However, every branch must still be separately extracted/qualified before any
parallel-equivalent credit is applied.

## Material options

| Option | Construction and quantitative target | Electrical result | Stackup / SI impact | DFM / thermal / assembly impact | Authority disposition |
|---|---|---|---|---|---|
| Heavier outer copper | Change 1 oz outer copper (`35 um`) toward 2 oz (`70 um`) while retaining inner layers only if a revised fab stack supports it. Ideal homogeneous trace term scales by `35/70 = 0.50`; current `0.977 mOhm` would be approximately `0.489 mOhm` only if all dominant resistance scales with outer copper. | Potentially passes `<=0.650 mOhm`; not proven because inner copper, pads, vias, and transitions do not scale with outer copper. | Current selected basis is JLC06161H-7628, 1 oz outer / 0.5 oz inner. A heavier stack changes dielectric/etch/impedance inputs; PCIe/USB3/SATA/Ethernet channels require a new order-specific field/stack calculation and coupon plan. | Larger etch/annular constraints, solder-mask/paste and thermal-spreading changes; exact fab capability and cost are not retained. | **CONDITIONAL**: valid only with a signed revised stackup, SI calculation, via/DFM review, and manufacturer capability evidence. Not the default construction.
| Local insulated copper reinforcement | Add a mechanically retained, insulated copper bar/foil/strap across the local positive and return source/fuse/mesh transition, with separate positive/return clearances and bonded pads/via fields. Size for extracted `>=0.327 mOhm` reduction and final effective neck `<=0.650 mOhm`. | Preferred: does not require changing the high-speed stack. Must be proven by four-wire resistance model including bonds, pads, vias, and temperature coefficient. | Leaves the six-layer signal stack unchanged; reinforcement must stay outside controlled-impedance corridors and not interrupt reference planes or return vias. | Requires insulation, creepage/clearance, attachment, assembly sequence, rework/service access, mechanical envelope, and thermal-current sharing review. Copper bar/strap temperature rise remains unproven until calculated or measured. | **AUTHORIZED PREFERRED PATH**, subject to exact package/DFM/material drawing and resistance/thermal extraction. This is an engineering implementation choice within the prototype product requirement, not a new product behavior.
| Parallel PCB copper | Add a second legal copper path on permitted power layers and increase transition/via arrays without changing the signal stack; preserve return continuity and required clearances. | Potentially reaches `<=0.650 mOhm`; must demonstrate at least `0.327 mOhm` improvement. The current mesh already uses F.Cu/B.Cu/In2 positive and In1/In4 return, so gains must be shown rather than assumed. | May alter plane/reference continuity and controlled-channel return paths; exact layer and via changes require SI/return review. | Larger arrays may worsen courtyard/hole/clearance conflicts; current candidate already fails DRC. Requires DFM extraction and thermal review. | **CONDITIONAL**: may be part of the preferred reinforcement if it satisfies the quantitative target without reopening protected signal corridors.
| Busbar/source-field construction | Use a defined copper busbar or laminated source field at the connector/fuse-to-mesh transition, with insulated mounting and explicit positive/return separation. A 1 mm-thick copper element has roughly one order more cross-section than a 35 um PCB trace of the same width, but exact length/width/bonds must be documented. | Strong candidate for the `>=0.327 mOhm` reduction; no credit until exact geometry and joint resistance are extracted. | Signal stack remains unchanged if physically local; may affect connector keepouts, enclosure, assembly and field service. | Requires mechanical/package authority, insulation, fastener/solder/joint reliability, creepage, thermal path and assembly instructions. | **AUTHORIZED ALTERNATIVE** to local foil/strap when Package/DFM authority confirms fit and prototype assembly method.
| Lower-resistance fuse/holder | Select a released fuse/holder whose complete hot positive/return contact and fuse resistance reduce the modeled path by at least `0.077 mOhm` to reach `8.500 mOhm`. Exact MPN and resistance revision are not retained in this packet. | Can recover the current total overage only; it does not reduce the `0.977 mOhm` PCB neck to `0.650 mOhm`. | Usually no signal-stack effect; exact current interrupt/I2t, holder temperature rise, derating and contact resistance remain required. | Mating, serviceability, fault isolation, fuse clearing, heat and availability must be checked. | **SUPPLEMENTARY ONLY**; cannot be selected as the sole correction.

## Quantitative contract and calculations

The complete hot path remains the sum of effective source-side and common
terms. The fixed terms retained from the R3 authority are:

```text
Q1 hot channel                         4.320 mOhm
Q1 leads/pads/positive transition     0.150 mOhm
protected copper/vias to J1           0.250 mOhm
J1 field/spreading                     0.250 mOhm
residual                               0.080 mOhm
fixed subtotal                         5.050 mOhm
```

Therefore the source-side effective network has at most `3.450 mOhm` under the
`8.500 mOhm` total limit. The selected material correction targets the PCB
neck allocation of `0.650 mOhm`; the remaining source harness, mating, fuse,
holder, branch joins and transitions must still fit their signed allocations.
No term may be counted twice, and no residual may be consumed without being
removed from the authority table.

At the source-cap screen, the retained total limit gives:

```text
40 A: 0.340 V maximum drop; 11.060 V from an 11.4 V source
45 A: 0.3825 V maximum drop; 11.0175 V from an 11.4 V source
```

The protected minimums therefore remain satisfied on the arithmetic screen,
but margins are only `10 mV` and `17.5 mV` at the source-cap extremes. The
material package must report both static IR drop and temperature-dependent
resistance; it must not substitute a capacitor claim for low-resistance copper.

## Required evidence before release

The material producer must return one bounded package containing:

1. exact material, thickness, width, length, insulation, attachment and joint
   drawings;
2. source/revision/hash for any fabrication, copper, connector, fuse or holder
   data used;
3. complete positive and return four-wire resistance extraction, including
   pads, vias, bonds/joints, temperature coefficient and all nine branches;
4. current density, continuous temperature-rise calculation, and 100 ms peak
   thermal/pulse screen;
5. SI/return-plane review proving protected high-speed corridors and
   impedance assumptions remain valid;
6. connector, fuse/holder, package, courtyard, creepage/clearance, assembly,
   service and mechanical-envelope review;
7. updated complete budget proving `<=8.500 mOhm` with explicit margin;
8. fresh KiCad Light DRC/connectivity only after the material geometry is
   integrated into a new isolated candidate.

No fabricated-board, load-step, connector temperature, SXM2 contact, or
prototype hardware result is claimed here. Those remain
`REQUIRES_PROTOTYPE_VALIDATION`.

## Authority conclusion

The preferred authorized correction is **local insulated copper
reinforcement or a defined busbar/source field**, preserving the selected
six-layer signal stack. Heavier copper is acceptable only after a revised
fabrication/SI basis is signed. A lower-resistance fuse/holder may provide
supplementary margin but is not sufficient alone.

This package is **DONE as an authority decision** and releases no CAD route.
The protected-bus implementation package remains **WAITING** on the bounded
material construction and evidence listed above.

**Signature:** Product / Power Authority — `SIGNED_ENGINEERING_AUTHORITY` — 2026-09-21
