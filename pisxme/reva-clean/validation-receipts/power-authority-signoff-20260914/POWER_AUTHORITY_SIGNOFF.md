# P24-POWER-AUTHORITY-SIGNOFF

Status: `WAITING_ON_PROTECTION_ASSEMBLY_AND_INSTALLATION_QUALIFICATION`

Package: `P24-POWER-AUTHORITY-SIGNOFF`  
Review base: current committed candidates `454de823` and `373ed806`; V2.2
numerical architecture `daaf6d3b`  
CAD changed: **no**

## Binding disposition

Power Authority accepts the MAX17527A calculation and the V2.2 six-loop
numbers as conditional engineering authority evidence. The exact
`MAX17527AATP+T` remains the selected limiter candidate for one instance on
each loop A--F, programmed with a 6.25 kOhm, 0.1% SETI resistor and latch-off
CLMODE. This is a qualification basis, not authorization to insert six stages
into the schematic or PCB. The unqualified legacy 15-A fuse is not promoted.

The source contract **cannot return READY**. It still lacks the exact
reverse-protection, energy-coordination, fault-aggregation, harness, and
installation evidence needed to bind the six-loop source/net/component
contract. The producer therefore remains parked; no PCB-only source additions
are authorized.

## Numeric claims accepted within scope

These values are accepted as calculations or source-contract screens at the
stated scope. They are not bench measurements or integrated-board closure:

| Claim | Disposition |
|---|---|
| 300 W sustained / 330 W design peak V100 product envelope | Accepted Class-C product requirement; must not be reduced. |
| 11.4--12.6 V source window; 40 A continuous / 45 A bounded-peak source requirement | Accepted V2.2 contract screens; source procurement capability remains to be proven. |
| Six independent 12-V/return loops, no passive sharing | Accepted V2.2 architecture requirement; source schematic and installation are not yet implemented or qualified. |
| Molex 8 A/circuit manufacturer screen with 0.8 derating = 6.4 A hard branch screen; 5.8 A normal target | Accepted as a conservative design screen, subject to hot harness, connector, copper, and installation qualification. |
| Low-voltage peak demand 34.37621832 A; six-loop limiter minimum 34.52547453 A; arithmetic margin 0.14925621 A | Arithmetic accepted, but the margin is narrow and does not prove unbalanced-load delivery, source capability, or transient behavior. |
| MAX17527A input range 5.5--60 V and 6.0 A nominal limit with +/-4% device accuracy | Accepted vendor claim for the selected candidate, subject to retained official-source provenance. |
| 6.25 kOhm, 0.1% SETI: 5.75424575--6.24624625 A calculated branch range | Accepted calculation. The 6.24624625 A upper value is below the 6.4 A screen by 0.15375375 A and below the 6.3 A absolute DC input-current value by only 0.05375375 A. |
| Six-loop minimum calculated limit 34.52547453 A | Accepted arithmetic only; no arbitrary redistribution or passive sharing is authorized. |
| MAX17527A 20--32 A fast-trip threshold, 3 us typical response, and 22.5--25.5 ms blanking range | Accepted as device protection data; not accepted as proof of a 6.4 A instantaneous system limit or complete SOA/I2t protection. |
| V2.2 protected-bus drop screens: 0.350 V sustained and 0.400 V peak; 11.05 V and 11.00 V protected-bus minima | Accepted as Class-D design budgets pending actual harness, protection, copper, thermal, and transient qualification. |
| Molex 39012020 housing, 39000080/39000079 5556 terminal class, 16-AWG minimum, crimp/tool dimensions and 68.5 N pull requirement | Accepted manufacturer assembly contract fields. No assembly-lot evidence exists in this repository. |
| Complete harness loop resistance <=20 mOhm hot | Accepted as a binding requirement; **not proven** for six actual loops. |

## Exact remaining dependencies

1. **External reverse-protection nFET.** Package/Power must select an exact
   MPN and verify VDS, current, RDS(on), gate drive, reverse-polarity and
   reverse-current SOA over 11.4--12.6 V and the declared temperature range.
2. **Fuse, TVS/clamp, and I2t/SOA coordination.** Name exact parts and retain
   a worst-case calculation covering the MAX17527A 20--32 A fast-trip range,
   3 us response, 22.5--25.5 ms blanking/retry or latch behavior, harness
   inductance, clamp voltage, fuse I2t, nFET SOA, and PCB copper. Existing
   `0297015.U`/15-A evidence is legacy and insufficient by itself.
3. **FLAG aggregation and fail-safe control.** Bind the six open-drain FLAG
   paths, pull-up/wired logic, fault truth table, V100 inhibit/reset behavior,
   EN timing, and controlled restart. Demonstrate that any branch fault
   prevents unsafe V100 enable and cannot be masked by another branch.
4. **Fast-trip interpretation.** System authority must explicitly state that
   the 6.4 A invariant applies to the post-blanking regulated branch limit, or
   supply a separate product/system requirement for sub-3-us fault current.
   The MAX17527A data alone cannot establish the latter.
5. **Harness resistance.** Package Authority must identify wire, one-way
   length, terminals, crimp process, temperature basis, and six complete hot
   loop values or conservative calculations at or below 20 mOhm.
6. **MPA and thermal installation.** MPA must bind six nonconflicting header
   positions and associated limiter/protection cohorts, preserve protected
   corridors and assembly access, and return the geometry to Thermal Authority
   for connector, solder, copper, harness, limiter, ambient, and airflow
   margins.
7. **ADI provenance.** Librarian should index the official MAX17527A source
   and retain its exact byte hash in the private Library. This is a provenance
   condition; it does not convert the open engineering qualifications into a
   pass.

## Resume rule

When dependencies 1--6 have signed evidence, Root may update the source
contract with exact six-loop references, net names, MPNs, protection behavior,
and installation constraints, then return the producer to `READY`. The next
step remains one isolated schematic/PCB producer followed by serialized
integration, targeted native connectivity/DRC, and fresh KiCad Light
validation. This receipt authorizes no CAD edit and does not close any Phase
24 acceptance row.

## Source records reviewed

- `validation-receipts/power-current-limiter-authority-20260914/POWER_CURRENT_LIMITER_AUTHORITY.{md,json}` at `454de823`.
- `validation-receipts/power-connector-qualification-closure-20260914/QUALIFICATION_CLOSURE.{md,json}` at `373ed806`.
- `validation-receipts/power-envelope-authority-redesign-20260914/POWER_ENVELOPE_AUTHORITY_V2.2_CANDIDATE.{md,json}` at `daaf6d3b`.

No CAD, schematic, library, rule, or configuration file was edited.
