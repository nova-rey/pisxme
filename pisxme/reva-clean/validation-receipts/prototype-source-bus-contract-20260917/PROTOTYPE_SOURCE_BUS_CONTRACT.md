# PiSXMe Rev A prototype protected source/common-bus contract

- **Package:** `P24-PROTOTYPE-SOURCE-BUS-CONTRACT`
- **Contract ID:** `PISXME-P24-PROTOTYPE-SOURCE-BUS-20260917`
- **Revision:** `1.0.0`
- **Workstream base:** `c2e0194c432e712d6f8386b9682f038dd06188e6`
- **Review source state:** `reva-clean` at the workstream base above; no CAD was edited.
- **Authority:** Product / Power Authority, within the signed selected architecture `PISXME-P24-POWER-ARCH-20260917`.
- **Assurance:** PiSXMe Rev A is a prototype/open-hardware carrier. This contract contains calculations and acceptance limits; it contains no fabricated-hardware measurement, vendor approval, or production-qualification claim.
- **Status:** `SIGNED_PROTOTYPE_SOURCE_BUS_CONTRACT`

## Binding contract

PiSXMe Rev A shall use a regulated, current-limited nominal 12 V source assembly feeding one ordinary protected common/distributed 12 V bus and the authority-mapped J1 12 V/GND contact field. The default implementation is one high-current input path. Multiple input paths are allowed only when each exact path is separately protected, ampacity-qualified, and included in the same end-to-end resistance and thermal evidence; no passive sharing credit is allowed before that evidence exists.

The contract preserves the product requirements of 300 W sustained V100 operation and a 330 W bounded peak for 100 ms. It removes the superseded six-loop precision-current premise. SXM2 contact multiplicity is used for parallel physical distribution only; it does not create equal-current or per-group regulator requirements. Undocumented standalone SXM2 sequencing, auxiliary behavior, contact thermal sharing, and the final fabricated assembly remain `REQUIRES PROTOTYPE VALIDATION`.

## Source, load, and voltage envelope

| Quantity | Binding value | Basis and status |
|---|---:|---|
| V100 sustained load | 300 W | User product requirement and NVIDIA 300 W maximum-power evidence; product behavior to be validated on prototype |
| Design peak | 330 W for 100 ms | Retained bounded product allowance; no hardware waveform claim |
| Auxiliary low-voltage load screen | 22.7 W | Existing CM5/bridge design screen: 5 V*3 A + 3.3 V*2 A + 1.1 V*1 A |
| Conversion efficiency floor | 90% | Conservative class-D design screen, not a measured board guarantee |
| Source nominal | 12.0 V regulated | Selected prototype architecture; not asserted as an NVIDIA standalone rail mandate |
| Source operating window | 11.4–12.6 V at the source terminals | Class-D carrier screen retained from the prior envelope; exact source/harness must meet it |
| Protected bus minimum | 11.05 V sustained; 11.00 V during the 100 ms peak | Derived from the 11.4 V source minimum and the drop budget below |
| Protected bus maximum | 12.60 V | OVP/source upper bound; no downstream operation above this value is credited |
| Source continuous capability | at least 40.0 A | Capability requirement with margin over the worst low-voltage load screen |
| Source bounded-peak capability | at least 45.0 A for 100 ms | Capability requirement; source transient waveform remains prototype evidence |

The source current calculation is:

```text
Pbus,sustained = (300 + 22.7) / 0.90 = 358.5555556 W
Pbus,peak      = (330 + 22.7) / 0.90 = 391.8888889 W
I at 12.0 V:      29.8796296 A sustained; 32.6574074 A peak
I at 11.4 V:      31.4522417 A sustained; 34.3762183 A peak
```

The 40 A continuous source has 8.5477583 A (27.18%) capacity above the 11.4 V sustained screen. The 45 A, 100 ms source has 10.6237817 A (30.91%) above the 11.4 V peak screen. These are source-capability margins, not permission to operate the connector, copper, or protection outside the contract.

## Connector, conductor, protection, and return requirements

The exact input connector/harness MPN is an implementation deliverable. It shall meet all of the following at the declared ambient, installation, mating, crimp, bundle, and airflow conditions:

1. The complete positive/return input assembly shall be rated for at least 40 A continuous and 45 A for 100 ms, with a source prospective-fault/interruption rating appropriate to the selected protection.
2. Conductors and crimps shall have a calculated ampacity of at least 40 A continuous and shall be selected by the qualified assembly's current, temperature-rise, bend, bundle, and length data. A nominal wire gauge alone is not an ampacity proof.
3. A single default input path shall be preferred. If the mechanical design uses multiple paths, each path shall have independent fault isolation and its own positive and return resistance/thermal record. The design must not claim equal sharing from nominally parallel connectors or wires.
4. The source-to-J1 complete positive-plus-return resistance shall be no greater than 10.0 mOhm at the applicable hot operating condition. The allocation is: source harness/connector loop 4.0 mOhm; fuse/reverse/fault-isolation loop 2.0 mOhm; PCB input positive-plus-return 2.5 mOhm; J1 common-plane/spreading to the worst mapped power field 1.5 mOhm. Every allocation includes its return contribution.
5. The protection chain shall include input fault isolation (fuse or an equivalent qualified protection), reverse-polarity/ideal-diode protection, OVP/UVLO policy, TVS or equivalent surge clamp, bounded inrush, and controlled shutdown. Exact parts and thresholds belong to the producer package and must satisfy these electrical/thermal budgets.
6. The reverse/protection path is included in the 2.0 mOhm allocation; no high-resistance limiter or precision current-servo loss is assumed.
7. The protected bus shall be a low-impedance positive and return distribution field. High-current returns shall not depend on signal traces, connector shields, or an unqualified shared neck. The J1 power field shall use only authority-mapped 12 V and GND contacts; unknown contacts remain unknown/no-connect until separately established.
8. The protection policy shall inhibit V100 enable and hold reset/inhibit when the protected bus is outside the declared operating window, during a detected input fault, or when a qualified protection device asserts a fault. Threshold hysteresis and timing require schematic/authority review and prototype observation.
9. TVS standoff shall exceed the 12.6 V normal maximum, and its clamp/energy rating shall be demonstrated against the selected source transient and harness inductance. No load-dump or surge waveform is claimed by this contract without that evidence.

## Drop, copper, via, and thermal budgets

The 10.0 mOhm complete path cap gives these worst-case screens:

| Condition | Current basis | Maximum path drop | Calculated drop at 10.0 mOhm | Bus lower bound from 11.4 V source | Margin to bound |
|---|---:|---:|---:|---:|---:|
| 300 W sustained | 31.4522417 A | 0.350 V | 0.314522 V | 11.085478 V | 35.478 mV |
| 330 W / 100 ms | 34.3762183 A | 0.400 V | 0.343762 V | 11.056238 V | 56.238 mV |

The extracted hot positive-plus-return PCB copper and via network shall satisfy the 4.0 mOhm combined PCB input plus J1 field allocation, with the 2.5 mOhm input segment and 1.5 mOhm J1 spreading allocation kept separately visible in the extraction. A single via may not be the sole 40 A path. The aggregate via array and every copper neck shall be calculated for at least 39.3153021 A continuous (1.25 times the 11.4 V sustained screen) and 37.8138401 A for the bounded peak (1.10 times the 11.4 V peak screen), with current sharing and temperature rise based on actual geometry, copper weight, stackup, and via construction.

Continuous connector, conductor, protection, copper, and via temperature rise shall be no greater than 30 degC above the declared ambient unless the exact manufacturer installation limit is lower. Power semiconductors shall remain below their applicable derated operating limit with at least a 20 degC junction margin under the 40 A continuous screen; the 100 ms peak shall remain within the manufacturer's pulsed/SOA limit. These are design limits, not measurements. Any selected component or assembly with a lower limit governs.

The contract requires a complete positive-and-return resistance extraction, not a pad count or net-name census. It must include connector/crimp, harness, fuse/holder, reverse device, copper, vias, planes, and the J1 contact-field transition. The same extraction must feed loss and temperature calculations. No source/bus candidate becomes an integrated candidate until those artifacts exist.

## Prototype validation contract

The following are required after the exact source assembly and integrated candidate exist:

1. Verify source polarity, protective earth/return policy, isolation, cold resistance, connector keying, crimp integrity, and absence of 12 V shorts before installing the V100.
2. Use a current-limited source and external fault protection. Start with the V100 disabled and the lowest practical current limit; enable low-voltage rails in a staged ramp while observing voltage, current, reset, power-good, and temperature. Increase the limit only after each stage is stable.
3. Capture four-wire differential voltage at source terminals and at the worst J1 power field, total current, and temperatures at input connector/crimps, protection devices, PCB input neck, via array, and J1 field. Retain raw instrument files, settings, calibration identity, timestamps, and shutdown events.
4. Verify the 11.4–12.6 V source window, protected-bus 11.05/11.00 V minima, 12.60 V maximum, and the 10.0 mOhm/0.35 V/0.40 V drop limits. A 300 W sustained run and 330 W/100 ms transient are prototype validation goals; neither is claimed here.
5. Confirm that any input fault, reverse condition, source brownout, OVP/TVS event, or protection trip disables V100 enable/holds reset and leaves no unsafe restart. Standalone SXM2 auxiliary/sequence behavior is explicitly `REQUIRES PROTOTYPE VALIDATION`.
6. Stop immediately for protected-bus voltage below 11.00 V, voltage above 12.60 V, source current above 40 A continuous or 45 A for the bounded 100 ms interval, any uncontrolled inrush/fault current, connector/copper/protection rise above 30 degC or a lower component limit, unexpected reset/enable behavior, visible damage, or thermal runaway.

The first-power procedure must use a staged, externally current-limited test; it must not claim fabricated-hardware results before the hardware exists. This package deliberately does not demand production supplier guarantees, lifetime calibration, population statistics, or mass-production fixtures for the prototype gate.

## Authority and dependency disposition

- `PWR-LOOP-001` through `PWR-LOOP-006` remain `SUPERSEDED` by `PISXME-P24-POWER-ARCH-20260917`.
- `PWR-LOOP-007` remains `UNPROVEN`; no contact-group current is assigned.
- `PWR-BUS-001` is `HARD`: the common protected bus must close the declared product envelope and the budgets in this contract.
- `PWR-BUS-002` is `HARD`: no unqualified passive-sharing credit across multiple input paths.
- `PWR-BUS-003` is `UNPROVEN / REQUIRES PROTOTYPE VALIDATION`: undocumented standalone SXM2 sequencing and auxiliary behavior.
- This contract releases `P24-PROTOTYPE-POWER-BUS-PRODUCER` to proceed to exact connector/protection selection and isolated CAD production. It does not itself edit or authorize a public PCB.
- The former HPQ #5 limiter subtree remains historical/superseded. It must not be reintroduced through a source-bus implementation.

## Evidence and limits

The decision is based on the signed architecture decision, bounded six-loop provenance audit, SXM2 authority audit, private carrier-sanities, the existing 300/330 W product decision, and the prior 90% load screen. Exact connector/terminal/harness identity, board extraction, source transient waveform, protection energy/SOA, and V100 endpoint sequencing are still implementation or prototype-validation work. No public reference CAD or restricted vendor material is copied here.

**Signature:** Product / Power Authority — `SIGNED_PROTOTYPE_SOURCE_BUS_CONTRACT` — 2026-09-17
