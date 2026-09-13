# PiSXMe Rev A power envelope authority — v2.0 candidate

**Decision ID:** `PISXME-REV-A-POWER-ENVELOPE-001`
**Candidate version:** `2.0.0-candidate`
**Base source state:** `dd4b2c80785ca1fc82c84bd0da48ff612147690a`
**Scope:** source/contact/harness/protection/distribution authority only
**CAD state:** read-only; no schematic, PCB, footprint, rules, or configuration file was edited
**Status:** `CANDIDATE_READY_FOR_POWER_AUTHORITY_SIGNATURE`
**Supersession:** proposes superseding v1.1 only for the two product-envelope D fields and the incompatible two-connector implementation. v1.1 remains provenance for the rejected 8-A/two-branch screen.

## Binding product boundary

PiSXMe Rev A shall support a V100/SXM2 load of **300 W sustained** and retain a
**330 W design peak allowance** at the 12-V product input. The existing two-circuit
8-A-per-circuit input topology is not a product constraint. It is an implementation
that fails this boundary and is `SUPERSEDED_BY_INVARIANT INV-PRODUCT-V100-300W`.

The arithmetic screen includes the existing low-voltage design loads of 22.7 W
(5 V x 3 A, 3.3 V x 2 A, and 1.1 V x 1 A) and a 90% conversion screen:

| Condition | Calculation | Required input current |
|---|---:|---:|
| 300 W sustained at 12.0 V | (300 + 22.7)/(12.0 x 0.90) | 29.87963 A |
| 330 W peak at 12.0 V | (330 + 22.7)/(12.0 x 0.90) | 32.65741 A |
| 300 W sustained at 11.4 V | (300 + 22.7)/(11.4 x 0.90) | 31.45224 A |
| 330 W peak at 11.4 V | (330 + 22.7)/(11.4 x 0.90) | 34.37622 A |

The 11.4-V cases are the design-low-voltage screen for source and distribution
sizing. They are engineering requirements, not a claim about an NVIDIA
V100 waveform or a fabricated-board measurement.

## Proposed source and contact architecture

Replace the two-branch input with **six independent 12-V circuits**. The
preferred low-risk implementation is three Molex `0039300020` two-position
headers, each header carrying one 12-V circuit and one return circuit. A
mechanically equivalent six-circuit connector assembly may replace the three
headers only after Package Authority verifies the exact mating terminal, wire,
crimp, retention, footprint, and envelope. The existing two-header layout is
not retained merely for historical continuity.

Each circuit shall have:

1. a separately identified 12-V and return conductor;
2. a qualified 16-AWG minimum harness conductor (18-AWG is not accepted for
   the new system-level screen without a separate thermal/voltage-drop signoff);
3. independent reverse-current blocking;
4. an active current limit with a hard maximum of **6.4 A per circuit**;
5. secondary short-circuit protection coordinated to the connector, wire, PCB,
   and MOSFET I2t/SOA; and
6. a monitored `BRANCH_POWER_GOOD` contribution to the V100 enable interlock.

The exact Molex application evidence remains applicable: the standard 5556
16/18-AWG two-circuit system is rated **8 A per circuit at its 30 C maximum
rise test**, requires application derating, and is not qualified for assumed
passive current sharing. The proposed 6.4-A limit is an 80% screen of that
8-A value. It is not a claim that the connector assembly is qualified until
mating parts, wire, crimp, length, ambient, and thermal installation are
closed.

Six circuits provide a derated arithmetic capacity of `6 x 6.4 = 38.4 A`.
That exceeds the 34.37622-A design-low-voltage peak screen by 4.02378 A
(11.71%) and the 31.45224-A sustained screen by 6.94776 A (22.09%).
This margin is a capacity screen, not permission to omit path-drop, thermal,
transient, or fault validation.

## Source and distribution limits

The external regulated source shall be specified as:

- 12.0 V nominal;
- 11.4 V minimum and 12.6 V maximum at the input connector during the declared
  operating envelope;
- at least 40 A continuous source capability;
- at least 45 A available for the declared 330-W peak interval and startup
  transient; and
- current limiting that does not rely on passive sharing between the six
  circuits.

The protected-board bus shall meet these limits before V100 enable:

- six branch limits, each `I_branch <= 6.4 A`;
- normal shared operation target `I_branch <= 5.8 A` sustained after startup;
- total protected-input current `<= 38.4 A` by independent branch limits;
- source-to-J1 protected-bus drop `<= 0.25 V` at 300-W sustained screen and
  `<= 0.35 V` during the 330-W peak screen;
- each branch harness loop resistance `<= 20 mOhm` at its maximum operating
  temperature; and
- each connector-to-bus PCB branch resistance and thermal path calculated for
  6.4 A, with the common bus calculated for 38.4 A. IPC-2152 or an equivalent
  documented thermal model is required; a generic minimum-width rule is not
  sufficient.

A main protected-bus limiter/fuse may be used as secondary protection, but it
shall not be used to replace the six branch current limits. The existing 15-A
per-branch fuse choice is not a valid 6.4-A branch limiter and is superseded
for this architecture until a time-current/I2t review selects a replacement.

## Branch imbalance and fault policy

Passive equal sharing is prohibited. The implementation must actively limit
and observe each circuit. After a bounded startup ramp and 100-ms settling
interval, the normal current-balance target is:

- every live branch remains `<= 6.4 A`;
- the branch spread is `max(I_i)-min(I_i) <= 20% of the mean` while every
  branch is above the measurement floor; and
- any open, overcurrent, overtemperature, reverse-current, or power-good
  fault causes V100 enable to deassert and reset/inhibit to remain asserted.

A branch fault is fail-safe: the product shall not continue to claim the
300-W/330-W envelope on five branches. Recovery is latched until a controlled
restart/service action. The six-branch architecture is therefore sized for
normal operation margin, not single-branch fault-tolerant full-power operation.

## Protection, transient, and load-step requirements

Each branch retains the LM74700-Q1 reverse/reverse-current blocking concept
with an external MOSFET only if the selected MOSFET SOA, gate timing, and
thermal path are rechecked at 6.4 A. The final protection set shall include:

- branch overcurrent/current limit at `6.4 A maximum`;
- source UVLO/OVLO thresholds bound against the 11.4–12.6-V product window;
- TVS standoff and clamp selected against the declared source transient, with
  the LM74700 3.2–65-V input capability and MOSFET/TVS/fuse energy model
  checked together;
- branch and common-bus fuse I2t below the qualified conductor/connector/PCB
  damage threshold; and
- V100 inhibit before protected-bus undervoltage or protection fault can
  propagate to the endpoint.

The 330-W peak is a carrier design peak. Until a product waveform is supplied,
this authority uses a bounded engineering acceptance screen of a step from
300 W to 330 W for **100 ms**, with source and bus sized for longer duration
at the 40-A continuous source limit. This is an internal acceptance requirement,
not vendor V100 load-step evidence.

For the 300-W to 330-W step:

- nominal 12-V input-current increment screen: `(330-300)/(12 x 0.90) = 2.77778 A`;
- 11.4-V input-current increment screen: `(330-300)/(11.4 x 0.90) = 2.92398 A`;
- protected bus shall remain within the declared absolute 11.4–12.6-V steady
  window after the step and recover to that window within 1 ms; and
- measured or extracted `deltaV = deltaI x ESR + Lloop x dI/dt + deltaV_control`
  evidence shall include harness/package inductance, capacitor ESR/ESL over
  bias and temperature, converter control response, and return impedance.

No hardware pass is claimed by this candidate. If the V100 endpoint authority
later supplies a stricter waveform or voltage band, that evidence supersedes
these derived screens through a new authority version.

## Corridor and implementation inputs

The later isolated producer shall reserve, before routing, one independent
power/return corridor per input circuit from the connector to its protection
stage, then six protected branch corridors to the common protected bus and J1
power field. The corridor contract is:

- six 12-V branch current nets, each designed for 6.4 A maximum;
- six corresponding low-inductance returns; no return may be inferred from
  signal copper or a generic unconnected zone;
- common protected 12-V bus sized for 38.4 A and the declared drop/temperature
  limits;
- protection, sensing, and `BRANCH_POWER_GOOD` kept outside protected
  high-speed corridors and cooler/backplate keepouts;
- no passive branch-merge assumption, synthetic connectivity edge, or global
  rule relaxation;
- preserve validated PCIe/REFCLK/USB3/Ethernet corridors until MPA explicitly
  reauthorizes a crossing or local placement; and
- validate actual copper, vias, planes, returns, fuse/pad ownership, and thermal
  geometry on the integrated candidate.

This artifact does not choose exact placement, route layers, via count, or J1
contact assignment. Those remain Package/Power/MPA implementation decisions
bounded by the numeric current, drop, thermal, and protected-corridor limits.

## Required follow-up and status

This candidate is ready for role-level Power Authority signature and Package
Authority mechanical requalification. It intentionally makes no schematic or
PCB change. After signature:

`Power Authority v2 -> Package Authority connector/harness qualification ->`
`MPA corridor/placement decision -> isolated producer -> serialized integration`
`-> targeted connectivity/DRC -> fresh Light validation`.

The HPQ Issue #2 corridor investigation remains separate and is not duplicated
here. The original v1.1 external-blocker disposition is narrowed by the explicit
300-W/330-W product decision; no user-supplied V100 waveform is fabricated.
