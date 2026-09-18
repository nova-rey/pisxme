# PiSXMe Rev A three-branch Molex prototype validation plan

- **Package:** `P24-POWER-INPUT-MOLEX-PROTOTYPE-VALIDATION`
- **Base state:** `ec980aa2c25a841e18026e1061c86b496d76b9d2`
- **Candidate state:** `CANDIDATE_READY`
- **Binding architecture:** three Molex Mini-Fit Jr. 2x3 through-hole headers, family `39-30-0060` / `0039300060`
- **Branch topology:** three physical header groups with nine designated positive/return contact-pair paths; each contact pair is independently current-limited or fault-isolated, as defined by the corrected V2 authority and schematic/package contract
- **Assurance:** prototype/open-hardware validation plan. No fabricated hardware was operated, no measurements are claimed, and no production AVL or supplier qualification is required by this package.

## Authority and design basis

Product/Power Authority decision `MOLEX_MULTI_CONNECTOR_AUTHORITY_V2` supersedes the earlier coarse three-branch wording and the Anderson PP15/45 footprint path for Rev A CAD. Its retained source records are the Molex 5569 sales drawing `039300040_sd.pdf`, Molex Mini-Fit Jr. specification `PS-43879-001-001.pdf`, and the `0039300060` product record. V2 rejects one 15 A fuse per connector: each of the nine positive/return contact-pair paths must be independently current-limited or fault-isolated. The authority packet hash is `132bd0c98b1b71379712112f764baef147064edb490893be81d40c5bd4e89770`; restricted/private source bytes remain in the Librarian corpus and are not copied into the public repository.

The binding source-bus contract `PISXME-P24-PROTOTYPE-SOURCE-BUS-20260917` remains in force:

- regulated nominal source 12.0 V, operating window 11.4–12.6 V;
- 40 A continuous source capability and 45 A for 100 ms;
- protected bus minimum 11.05 V sustained / 11.00 V for the bounded peak and maximum 12.60 V;
- complete source-to-J1 positive-plus-return path <=10.0 mOhm hot;
- source harness/connector effective loop allocation <=4.0 mOhm hot;
- connector, conductor, protection, copper and via rise <=30 °C above declared ambient unless a lower component limit governs;
- no passive current-sharing credit before all nine contact-pair paths are measured and accepted.

The Molex authority uses the conservative 5556 four-to-six-loaded-circuit screen of 7 A per contact at its stated temperature-rise condition. Each of the nine positive/return contact-pair paths is therefore screened at 7 A per pole; the three physical headers together provide nine positive and nine return paths, or 63 A screened capacity per polarity. The 40 A and 45 A source contract targets are 4.444 A and 5.000 A per contact pair respectively, leaving 2.556 A and 2.000 A of screen margin. These are design calculations and manufacturer application screens, not fabricated measurements or permission to omit path protection, impedance matching, copper analysis or thermal validation.

## Branch arithmetic and current-balance contract

The three headers provide nine designated positive contacts and nine designated return contacts. V2 treats each positive/return contact pair as an independent current-limited or fault-isolated path; the initial queue shorthand of three 15 A connector branches is therefore superseded for validation. A single 15 A fuse per header is not a valid sharing implementation.

For all nine paths at a 40 A continuous total:

```text
I_contact_pair,target = 40 / 9 = 4.444444 A
```

For all nine paths at a 45 A, 100 ms bounded peak:

```text
I_contact_pair,target = 45 / 9 = 5.000000 A
```

The conservative loaded-circuit screen is 7 A per contact. Thus the target screens retain 2.555556 A/contact continuous margin and 2.000000 A/contact peak margin. These are design calculations and manufacturer application screens, not fabricated measurements. No passive current-sharing credit is allowed: all nine paths and all three headers are required, and no N-1 operation is credited.

The prototype current-balance screen is:

- during the 40 A continuous run, total measured current shall be at least 40.0 A within calibrated test tolerance and each of the nine contact-pair paths shall remain at or below 7.0 A including measurement uncertainty;
- the preferred balance target is `max(I_pair) - min(I_pair) <= 10% of mean pair current`, a PiSXMe derived engineering screen and not a Molex specification;
- if the 10% screen is not met, do not credit equal sharing: retain the nine path records, stop the full-envelope run, and return the imbalance to Power/Producer authority;
- during the 45 A pulse, each contact-pair path shall remain at or below its 7 A screen and all nine waveforms shall be retained. At a measured 45 A total with nine 7 A maxima, no path may dominate the bus;
- at lower first-power currents, unequal path sharing is not itself a failure, but every path's polarity, isolation, current readback and protection behavior must be proven.

The 10% balance screen is a test gate for this architecture. It must not be represented as a Molex rating or retroactively applied to the superseded Anderson plan.

## Bounded prototype procedure and acceptance limits

### 1. Assembly identity, polarity, and fit

Before energizing, record all three header MPNs and lot markings, exact mating 5557 housing/5556 terminal or released equivalent, conductor gauge/stranding/length, crimp tooling and die, strip dimensions, crimp inspection method, branch fuse/holder, reverse/protection switch, TVS and any branch current sensor. Record the schematic-defined positive and return contact mapping for every header; do not infer polarity from geometric appearance.

With the board unpowered, inspect all three 2x3 headers, retention features, polarization, solder joints, board edge/service access, harness bend radius and strain relief. Mate each harness fully and verify terminal seating, latch engagement, no contact back-out, no housing damage, no reverse insertion and continuity from each source pole to the intended branch pads. A prototype fit check does not claim a lifetime mating-cycle rating.

Any missing exact mating housing, terminal, conductor or crimp process is an assembly-record prerequisite for hardware testing. It is not permission to substitute a generic part or to fabricate a result.

### 2. Branch isolation and resistance

With all nine contact-pair paths disconnected from the source and the V100 absent, verify each contact-pair path independently:

- positive-to-return resistance and diode behavior at the input connector;
- no positive-to-positive or return-to-return unintended backfeed through protection;
- no branch-to-branch backfeed when one branch is energized in a safe, low-current fixture;
- continuity through each of its three positive contacts and three return contacts, with all nine positive/return pairs identified;
- fuse/holder, reverse device, TVS and branch switch orientation.

Use a four-wire Kelvin method or calibrated low-ohm meter to measure each contact-pair path's complete positive-plus-return path, separately recording connector contacts, mating terminals/crimps, harness, fuse/holder, protection switch, board pads and accessible copper. Repeat or calculate at the declared hot condition using actual wire length, bundle, ambient and measured temperature. Nominal wire gauge alone is not ampacity or resistance proof.

For the nine independent contact-pair loops `R1` through `R9`, record the effective parallel input loop using:

```text
R_effective = 1 / (1/R1 + 1/R2 + ... + 1/R9)
```

The source harness/connector allocation is closed only when the applicable effective loop is <=4.0 mOhm hot and the complete source-to-J1 path, including protection, copper, vias, planes and J1 spreading, is <=10.0 mOhm hot. Every branch result and the effective result must be retained; no sharing credit is allowed when a branch is open, out of tolerance or unmeasured.

Reference loss screens are 160 mV / 6.4 W at 40 A and 180 mV / 8.1 W at 45 A for a 4.0 mOhm effective loop. At the full 10.0 mOhm source-to-J1 cap they are 0.400 V / 16.0 W and 0.450 V / 20.25 W respectively; the actual hot extraction and lower component limit govern.

### 3. 40 A continuous branch balance and thermal rise

After cold resistance and isolation checks pass, operate a controlled 40.0 A continuous source through all nine contact-pair paths across all three headers at the declared ambient, airflow, harness bundle and mating condition. Use nine independent contact-pair current measurements, grouped by header, and a total source current measurement. Capture each path voltage at the connector and protected-bus/J1 field voltage with differential probes or Kelvin DMM connections.

Measure temperatures at every header's positive and return contact groups, all nine mating terminal/crimp paths, wires, housings, per-path protection, PCB pads and copper necks, vias, common-bus merge and worst J1 power-field transition. Run to the declared thermal steady-state and retain ambient, airflow, dwell, instrument serial/calibration and sample-rate data.

Pass only when:

- total current reaches the 40 A continuous contract within calibrated tolerance;
- each contact-pair path remains <=7.0 A including measurement uncertainty;
- the preferred 10% nine-path balance screen passes, or Power Authority explicitly records a revised engineering disposition before full-envelope credit;
- the effective and complete path resistance/drop allocations close;
- every thermal point stays within the lower of the applicable Molex/terminal/wire/protection limit or 30 °C rise above ambient;
- no connector/fuse discoloration, odor, arcing, solder damage, terminal release, unstable protection, unexpected reset or unsafe restart occurs.

The 7 A/contact Molex application screen is not a measured board/harness result. The nine-path, three-header run is the required prototype installation derating evidence.

### 4. 45 A bounded transient

Only after the 40 A run passes, apply a controlled 45.0 A total pulse for 100 ms using a characterized current-limited source or electronic-load fixture. Measure each contact-pair current independently and capture source voltage, each path voltage, protected-bus/J1 differential voltage, total current, pulse duration, branch protection status and enable/reset/inhibit response.

Acceptance requires the measured total to reach the declared 45 A / 100 ms capability within instrument/control tolerance, every contact-pair path to remain at or below its 7 A screen including uncertainty, no uncontrolled current overshoot, no branch protection misoperation except the intended behavior, no arc/contact release/visible damage and no unsafe restart. If the fixture cannot bound current overshoot or independently observe all nine contact-pair paths, the test is invalid. Retain the waveform and post-pulse inspection; no family rating alone closes this gate.

### 5. Independent branch protection and fault behavior

Using a safe external fault fixture and the exact source/protection setup, test each of the nine contact-pair fault paths one at a time with the V100 disabled. Verify that the affected path isolates within its declared protection behavior, that the other eight paths remain within their 7 A screen, that no path backfeeds the faulted path, and that the controlled shutdown policy holds V100 enable/reset/inhibit as specified. Do not create an uncontrolled hard short on the assembled board.

Verify source OVP/UVLO window, reverse-polarity protection, TVS/surge policy, inrush behavior, fuse or equivalent interruption coordination, branch protection SOA and post-fault restart lockout. The transient energy, source impedance, fuse I²t, clamp waveform and semiconductor SOA must be calculated or measured for the exact implemented parts; this plan does not invent those values.

### 6. Staged first-power and V100 bring-up

Follow `PISXME-P24-V100-FIRST-POWER-20260917` after the three-header/nine-path source assembly and integrated CAD gates exist. Begin with all three headers and all nine contact-pair paths connected but V100 inhibited and the source set to 12.0 V with a 1 A ceiling. Verify polarity, isolation, no 12 V short and no service-USB back-power. Check each contact-pair path one at a time at safe low current, then enable all three headers and verify all nine current readbacks and balance before increasing the ceiling.

Use the contract stages: unloaded board 1 A; CM5-only 2 A then 5 A after stable review; V100 installed/inhibited 1 A then 5 A; first enabled low-load 10 A then 20 A. Full 40 A/45 A operation requires accepted branch, resistance, protection, thermal, copper, return and sequencing evidence.

Abort for protected bus below 11.00 V during the bounded peak, above 12.60 V, any contact-pair path above 7 A, total source current above 40 A continuous or 45 A during the bounded pulse, persistent source limiting, uncontrolled inrush/fault current, unexpected enable/reset behavior, connector/fuse/protection rise above the governing limit, visible damage or thermal runaway.

## Required hardware evidence package

Retain the exact three-header BOM and lot markings, mating housing/terminal and wire records, crimp-tool setup and inspection, per-branch four-wire resistance files, polarity/isolation records, current-balance waveforms, thermal files, fault/protection captures, first-power logs, source/load settings, instrument serial/calibration records, ambient/airflow, timestamps, operator, shutdown events, raw-file hashes and signed acceptance disposition. A design-only plan cannot be upgraded to measured PASS.

## Explicit prototype dispositions

- Nine-path current balance, contact-pair isolation, harness/crimp resistance, connector/fuse/protection thermal rise, 40 A continuous operation, controlled 45 A/100 ms response, protection action and first-power behavior: **REQUIRES PROTOTYPE VALIDATION**.
- Production AVL, supplier population assurance, lifetime crimp statistics, lifetime mating-cycle qualification and mass-production fixtures: **not required to authorize Rev A prototype CAD**.
- Exact mating housing/terminal/conductor/crimp/length/bundle and branch protection records: **must be bound before hardware test**.
- No hardware was available or operated for this receipt. No resistance, balance, thermal, transient, protection or first-power result is asserted.

**Result:** `CANDIDATE_READY_WITH_REQUIRES_PROTOTYPE_VALIDATION`
