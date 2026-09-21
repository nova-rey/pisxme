# MPA effective-network architecture — distributed laminated source bus

- **Originating work package:** `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- **Decision ID:** `PISXME-P24-PROTECTED-BUS-MPA-EFFECTIVE-NETWORK-20260921-R1`
- **Authority:** Macro Placement Authority, implementing Product / Power Authority `PISXME-P24-PROTECTED-BUS-POWER-AUTHORITY-20260921-R2`
- **Status:** `BINDING_DECISION_FOR_PRODUCER; REQUIRES_PROTOTYPE_VALIDATION`
- **CAD changed by this decision:** no
- **Hardware operated:** no

## Decision

The rejected candidate's three-group parallel trace-only equivalent was about
1.43 mOhm and cannot close the provisional 0.65 mOhm effective nine-branch PCB
network allocation. The sole replacement is a **distributed laminated copper
mesh**. Each source branch remains an independent positive/return pair through
its own fuse. The copper network is widened and paralleled across the existing
six-layer contract before and after the fuse bank; it is evaluated as a
resistive network, not as nine equal passive shares.

The previous source-local fuse-bank placement is treated as an inherited pad
island only; this decision does not repeat or reselect its y-row geometry. The
material change is the current path architecture and corridor ownership.

## Physical topology and fixed relationships

- J1, J5, J6, J9, the nine fuse-holder identities, the protection cohort, and
  the mapped J1 contacts remain fixed by the preceding authority records.
- Each J5/J6/J9 positive pad owns one branch cell through its corresponding west
  fuse pad. Each return pad owns the paired return cell. No branch cell crosses
  another branch cell before its fuse.
- The three source-header cells occupy the west source-entry acreage. The
  common post-fuse mesh occupies the central protected-bus acreage west of the
  primary U1/Q1 cohort. The J1 transition remains on the east side of Q1.
- J7, J1 high-speed/clock/USB3/Ethernet/storage/CM5 copper, validated return
  structures, and all mechanical outlines remain protected.

## Layer-owned effective-network mesh

### Independent raw branch cells

For every positive branch from a connector pad to its fuse raw pad:

1. Escape the PTH pad on F.Cu and B.Cu as two parallel local copper paths. The
   pad fanout may start at the released 2.2 mm PTH geometry, then expand to a
   minimum **4.0 mm effective copper width per layer** immediately after the
   native clearance bottleneck. The short pad bottleneck must be included in
   extraction; the 4.0 mm value is not a waiver of pad clearance.
2. Use In2.Cu as a third positive parallel plane/strap within the west power
   acreage. Connect F.Cu, B.Cu, and In2.Cu at the connector and fuse ends with
   separate ordinary through-via arrays. No via-in-pad or blind/buried via is
   authorized.
3. Keep the three positive cells ordered by connector pad number. The raw
   positive cells remain electrically distinct until their fuse elements.

For every paired return cell:

1. Use a broad In1.Cu plus In4.Cu return mesh from the connector return pad to
   the distributed `POWER_RETURN_JOIN` field. Local B.Cu return copper is
   permitted only in apertures where it does not conflict with the positive
   mesh or validated high-speed corridors.
2. Use a separate ordinary through-via array at the connector-side and join-
   field transitions. Return cells remain distinct until the authorized return
   join; no single via or neck carries the aggregate source current.
3. Do not route a return through signal copper or a fuse-holder pad.

The positive and return local meshes are separated by native clearance and
remain distinct through the branch pair. The producer must use the actual
released stackup and copper thickness; widths are implementation minima for the
mesh, not evidence of resistance closure.

### Fused common field

After each fuse's east pad group, the nine fused outputs enter a **distributed
In2 positive field**, not nine long narrow lanes:

- Reserve an In2 polygon/mesh from the east fuse-bank acreage to the U1/Q1
  input field, with at least four distributed positive transition columns.
- Each fuse east pad has its own local F.Cu/B.Cu/In2 launch and its own via
  group before it touches the common field. The net becomes the authorized
  `12V_BRANCH_JOIN` only at this post-fuse field.
- Use an orthogonal comb/polygon with no single central tie. The field shall
  have two physically separated feed corridors to U1/Q1 so the effective path
  is not dominated by one neck.
- The matching In4 `POWER_RETURN_JOIN` field is broad and separately stitched
  to In1. Positive and return fields do not share a transition column.

The common field ends at the primary U1/Q1 cohort. Q1's post-protection output
uses a separate distributed via field to In3, then the existing mapped J1
12-V contact field. No B.Cu J1 terminal, via-in-pad, unknown J1 contact, or
narrow F.Cu protected trunk is authorized.

## Via geometry and current ownership

The producer shall instantiate the following minimum ordinary through-via
pattern, then increase counts if the released fab current model requires it:

- **Raw positive cell:** two rows of three 0.60/0.30 mm vias at the connector
  launch and two rows of three at the fuse raw-pad launch, placed adjacent to
  the PTH pads with native annular and courtyard clearance. The arrays are
  branch-owned and may not be shared before the fuse.
- **Raw return cell:** the same two-by-three pattern at the connector return
  launch and at the In4 return field entry; it is electrically separate from
  the positive array.
- **Fused join:** four distributed columns, each with at least two-by-four
  0.60/0.30 mm ordinary vias, spanning the In2 join field; the producer must
  report the actual count, barrel resistance, annulus, copper thickness, and
  current allocation.
- **Return join:** a matching four-column In4/In1 stitch field, physically
  offset from the positive columns and with the same extraction requirements.
- **Q1 to In3:** a distributed array sized from the released stackup and Q1
  thermal/current model; no single via carries the protected-bus path.

No arbitrary via-count credit is allowed. The via pattern is a starting
geometry that must pass native DRC, DFM, current-density, temperature-rise, and
resistance extraction.

## Governing electrical constraints

Retain the Power Authority R2 contract:

- 11.4–12.6 V source; 300 W sustained; 330 W for 100 ms.
- 40 A continuous and 45 A for 100 ms source capability.
- 11.05 V sustained and 11.00 V peak protected-bus minima.
- Complete hot positive-plus-return path <=8.50 mOhm.
- Effective nine-branch PCB neck allocation <=0.65 mOhm, pending the signed
  extraction of this new architecture.
- 7 A loaded-contact screen and <=10% qualified branch imbalance.
- No N-1 credit, no unqualified passive-sharing credit, and no six-loop revival.

The producer shall build the actual copper/via network into a resistor or field
solver model with nine independent source ports. It shall report:

1. each branch positive and return resistance;
2. the full nine-branch effective network equivalent at the common field;
3. worst-case branch and source-path resistance without assuming equal current;
4. current density and temperature rise at 40 A and the 45 A pulse;
5. the complete R3 budget including harness, fuse/holder, Q1, protected bus,
   J1 field, and residual terms.

A trace-only sum, nominal trace width, or passive equal-share calculation does
not close this gate. The output must be a native candidate plus a reproducible
extraction receipt tied to the exact stackup, copper thickness, via model, and
source SHA.

## Why this is materially new

The rejected 1.43 mOhm result came from a trace-dominated three-group network.
This decision changes both the cross-section and the topology: three positive
copper layers feed each independent branch cell, the return uses two dedicated
plane layers, each fuse launch is locally arrayed, and the common field is a
multi-column mesh rather than a narrow join or long ordered lanes. The effective
network is therefore evaluated as a distributed parallel conductance with
explicit neck, pad, barrel, and field terms.

This plan does not permit global rule relaxation, same-geometry route replay,
J1 remapping, connector remapping, or passive-sharing assumptions. If the
released fabrication stack and the specified native geometry still extract above
0.65 mOhm, the remaining product/architecture decision is precise: Product /
Power must authorize either a heavier-copper/busbar source-field fabrication
process or a lower-resistance fuse/holder package. MPA cannot claim that an
ordinary 1 oz/0.5 oz six-layer board meets the allocation without that measured
extraction.

## Producer handoff

Implement this mesh in an isolated producer workspace from Root's exact base.
Return the changed-scope manifest, native DRC/connectivity, branch/pad/fuse
census, via/copper geometry, field/resistor extraction, thermal/current evidence,
and DFM review. Root performs serialized canonical integration and fresh KiCad
Light validation. This authority packet is design evidence only and makes no
fabricated-hardware claim.

**AUTHORITATIVE BASELINE DECLARATION:** For
`P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`, use the distributed laminated
F.Cu/B.Cu/In2 positive mesh, In1/In4 return mesh, branch-owned ordinary-via
arrays, four-column post-fuse positive field, offset four-column return field,
and distributed Q1-to-In3 transition. This is the sole effective-network
architecture authorized for the corrected 0.65 mOhm allocation.
