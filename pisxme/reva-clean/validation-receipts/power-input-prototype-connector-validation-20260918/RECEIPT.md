# PiSXMe Rev A prototype high-current input connector validation plan

- **Package:** `P24-POWER-INPUT-PROTOTYPE-CONNECTOR-VALIDATION`
- **Base state:** `415e782eaaa39c14c3d55662fc4df3330be17647`
- **Candidate state:** `CANDIDATE_READY`
- **Architecture:** one Anderson Powerpole PP15/45 1x2 positive/return path
- **Assembly:** `ASMPR45-1X2-RK`; housings `1327`/`1327G6`; PCB contacts `3-5912P1` / `3-5913P1`; selected wire-side contact `261G2` pending exact mating-housing assembly record
- **Assurance:** prototype/open-hardware validation plan. No fabricated hardware was operated, no measurements are claimed, and no production AVL or supplier qualification is required by this package.

## Authority and source basis

The signed prototype source-bus contract `PISXME-P24-PROTOTYPE-SOURCE-BUS-20260917` binds a regulated nominal 12 V source, an 11.4–12.6 V source window, 40 A continuous capability, and 45 A for 100 ms. It requires the complete source-to-J1 positive-plus-return path to remain within 10.0 mOhm at the applicable hot condition, with 4.0 mOhm allocated to the source harness/connector loop. It requires connector, conductor, protection, copper, and via temperature rise no greater than 30 °C above declared ambient unless a lower manufacturer limit governs.

The connector reassessment and Anderson evidence brief identify the released manufacturer evidence used here:

- `B02021S` Rev. 6, SHA-256 `7a32189a34ff2feea3bf173c788f3dd63229ea98dfefed8009b1bc5738e8cd2c`.
- `DS-PP1545`, SHA-256 `ac39c286d44528efab30061b96df6e64e6eeafb6e154af7a03397d518f45a04f`.
- Released product data screens the PP15/45 family to 40 A continuous under its CSA/TUV condition and up to 45 A per pole in the published family data. The 40 A value has no PiSXMe installation derating margin, and the 45 A value is not a dedicated 100 ms pulse qualification; both therefore require prototype evidence below.
- The published 0.525 mOhm wire-contact screen gives a connector-only screen of 21 mV / 0.84 W at 40 A and 23.625 mV / 1.063 W at 45 A **per contact**. If both positive and return contacts meet that same screen, the pair screen is 1.050 mOhm, 42 mV / 1.68 W at 40 A and 47.25 mV / 2.126 W at 45 A. These are calculations from the published screen, not measurements or a substitute for the complete hot loop test.

The red/black housing convention is mechanical evidence only. The harness assembly record must assign board position 1/2 to positive/return, document the exact mating housing/contact combination and wire/crimp process, and prove polarity by continuity before energizing the board. No passive sharing credit is used.

## Bounded prototype procedure and acceptance limits

### 1. Assembly identity, fit, and unpowered inspection

Before any energized test, record the exact wire-side housing, `261G2` contact configuration, conductor part/gauge/stranding/length, crimp tooling and die, strip dimensions, crimp inspection method, fuse/holder and protection parts. Verify the board-side contact variant, housing keying, polarity marking, mating orientation, retention features, strain relief, bend radius, and service access against the released Anderson records and the PiSXMe assembly drawing.

Mate and unmate the exact harness with the board unpowered. Accept only complete seating, keying that prevents reverse insertion, intact latch/retention, no terminal back-out, no housing damage, and continuity from the intended source positive/return to the intended board pads. Do not claim the manufacturer's 10,000 mating-cycle rating from a prototype fit check; a limited service-cycle screen may be recorded separately.

Use the manufacturer's published retention/pull value if the exact contact and housing record supplies one. If it does not, the mechanical/DFM authority must set a declared prototype screening force before the pull test. Do not invent a force or report an unqualified pull test as a manufacturer pass. The hardware result must show no terminal withdrawal, latch release, housing damage, or polarity discontinuity at the declared force.

### 2. Harness and crimp resistance

Measure each positive and return pole, and then the complete positive-plus-return assembly, with a four-wire Kelvin method at a documented current below self-heating. Record contact, crimp, wire, board solder joint, and any fuse/holder segment separately where test access permits. Repeat or calculate at the declared hot condition using the actual conductor length, bundle, ambient, and measured temperature coefficient; nominal wire gauge alone is not an ampacity proof.

Acceptance for the selected architecture is:

- source harness plus connector complete hot positive-plus-return loop **≤4.0 mOhm**;
- complete source-to-J1 positive-plus-return path, including protection, copper, vias, planes, and J1 field transition, **≤10.0 mOhm**;
- no unexplained pole imbalance, intermittent contact, open, or polarity reversal;
- calculated 40 A and 45 A drops and losses are included in the same record. For reference, 4.0 mOhm is 160 mV / 6.4 W at 40 A and 180 mV / 8.1 W at 45 A; the actual hot result governs.

This step is a design/assembly measurement after hardware exists and remains `REQUIRES PROTOTYPE VALIDATION`.

### 3. 40 A continuous derating and thermal rise

After the cold checks pass, drive a controlled 40.0 A continuous current through the complete input assembly using a regulated 12.0 V source and an externally current-limited electronic load or equivalent safe fixture. Run at the declared ambient, airflow, harness bundle, mating condition, and board copper installation. Capture source voltage/current, connector-pole voltage, protected-bus voltage, complete path drop, and temperatures at both contacts, wire crimps, housing, conductors, fuse/holder, reverse/protection devices, PCB input copper/neck, via array, and worst J1 power-field transition.

Use calibrated thermocouples or a calibrated thermal camera plus an electrical current measurement. Record instrument IDs, calibration status, sample rate, ambient, airflow, dwell/steady-state definition, and raw files. Pass only when every measured point remains within the lower of the applicable manufacturer limit or **30 °C rise above declared ambient**, the complete hot-loop allocations close, there is no discoloration/odor/arcing/creep, and source/protected-bus values remain in the signed contract window. A component-specific lower limit governs.

The released 40 A rating is not installation derating evidence. This test is the required prototype derating evidence and is not claimed before fabrication.

### 4. 45 A bounded transient

Only after the 40 A continuous check passes, apply a controlled **45.0 A for 100 ms** pulse with a characterized current-limited source/load fixture. Capture the current waveform, source and protected-bus differential voltage, pulse duration, protection status, and any reset/inhibit response with a calibrated scope or transient recorder. Use a fixture that prevents an uncontrolled short or source overshoot; do not use an unbounded bench supply or deliberate hard short on the board.

Accept only a measured pulse that reaches the declared 45 A / 100 ms capability within the instrument uncertainty and control tolerance, remains within the approved source/protection limits, produces no uncontrolled overcurrent, contact release, arcing, visible damage, or unsafe restart, and leaves the assembly ready for inspection. A single family rating does not prove this transient; the raw waveform and post-pulse inspection are mandatory. If the current source cannot bound overshoot, the test is invalid and must be redesigned.

### 5. Protection and first-power checks

Use the existing `PISXME-P24-V100-FIRST-POWER-20260917` staged procedure. With V100 and removable loads absent, first verify polarity, isolation, fuse continuity, reverse protection, no 12 V short, and no back-power through service USB. Start at 12.0 V and the 1 A ceiling, then use the contract's staged 2 A/5 A CM5-only and 1 A/5 A inhibited-V100 ceilings before any enabled endpoint test. Observe raw input, protected bus, EN/PG/reset/PERST#/inhibit, current, inrush, and temperatures.

Do not proceed to a 300 W sustained or 330 W/100 ms system run until the complete source/harness/connector, protection, copper, thermal, and sequencing evidence is accepted. Abort for protected bus below 11.00 V during the bounded peak, above 12.60 V, source current above 40 A continuous or 45 A during the bounded pulse, persistent current limiting, uncontrolled inrush/fault current, unexpected enable/reset behavior, temperature above the governing limit, visible damage, or thermal runaway.

## Evidence package required from the eventual hardware run

Retain the exact assembly BOM and lot/part markings, crimp-tool and inspection records, four-wire resistance files, pull/fit records, current/voltage waveforms, thermocouple or thermal-camera files, source/load settings, instrument serial/calibration records, ambient/airflow, timestamps, operator, shutdown events, raw-file hashes, and the signed acceptance disposition. A design-only plan or calculation cannot be upgraded to a measured PASS.

## Explicit prototype dispositions

- Connector/harness/crimp resistance, contact fit/pull, 40 A continuous derating, thermal rise, 45 A/100 ms transient, protection response, and first-power behavior: **REQUIRES PROTOTYPE VALIDATION**.
- Production AVL, supplier population assurance, lifetime calibration, 10,000-cycle lifetime qualification, and mass-production fixtures: **not required to authorize Rev A prototype CAD**; retain as later release concerns.
- Exact wire-side mating housing, contact plating/lot, conductor, crimp tooling, length, bundle, and strain-relief record: **must be bound before hardware testing**, but is an assembly/procurement record rather than a reason to fabricate measurements.
- No hardware was available or operated for this receipt. No thermal, resistance, pull, transient, or first-power result is asserted.

**Result:** `CANDIDATE_READY_WITH_REQUIRES_PROTOTYPE_VALIDATION`
