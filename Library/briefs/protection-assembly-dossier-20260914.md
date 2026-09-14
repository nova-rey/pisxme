# Protection assembly dossier — MAX17527A / nFET / fuse / TVS

Date: 2026-09-13 (campaign packet: 20260914)  
Owner: Librarian (knowledge state; advisory)  
Queue package: `P24-PROTECTION-DOSSIER`  
Decision authority: Power Integrity Engineer and Power Authority. This brief does not select a production MPN, alter product requirements, or authorize CAD.

## Library-first result

The private Library already contained the PiSXMe `CSD19536KCS` nFET record, the provisional `0297015.U` / `178.6165.0001` fuse-holder record, and the `SMBJ18A` TVS candidate. It did not contain a MAX17527A manufacturer packet, the current Littelfuse MINI fuse I²t/time-current table, or an indexed current SMBJ-series table. The following bounded manufacturer sources were acquired by URL and parsed. No third-party or vendor PDF was copied into the Library.

## Indexed source facts

### MAX17527A

Analog Devices MAX17527A Rev. 0 datasheet (03/20/2023) is the primary component source. It specifies a 5.5–60 V input range, 0.6–6.0 A programmable current limit, ±4% accuracy from 3–6 A across temperature, and an external n-channel FET for input reverse-polarity and optional reverse-current protection. The external FET connection is source to SN, drain to IN, and gate to GN. The device's external gate drive is 4.45 V minimum, 4.75 V typical, and 4.95 V maximum under EN = 5 V with no reverse condition.

The same source specifies a 20/26/32 A minimum/typical/maximum internal fast-trip overcurrent threshold and 3 µs typical response. The external nFET remains on during the internal short-circuit fast trip, so this mechanism does not prove external-FET short-circuit SOA or I²t protection. Reverse-current protection has slow 5.4 mV typical / 17 µs typical and fast 100 mV typical / 108 ns typical thresholds and response. FLAG is open drain and asserts low for overvoltage, undervoltage, excessive internal drop, thermal shutdown, and an invalid SETI resistance; reverse-current-only events do not assert FLAG. FLAG has a 4 mA protection limit.

The device uses continuous, autoretry, or latch-off modes. The datasheet gives 22.5–25.5 ms blanking and 654–792 ms autoretry timing ranges. Latch-off reset requires EN below 0.4 V for at least 30 µs typical or an input cycle. Thermal foldback begins at 150°C and thermal shutdown is 165°C typical with 10°C hysteresis. Minimum local input bypass is 1 µF and SN bypass is 4.7 µF. The MAX17527A absolute maximum DC IN current is 6.3 A; this is a stress limit, not a qualified continuous operating target.

The six-loop candidate's 6.25 kΩ SETI value nominally selects 6.0 A. With the recorded device and resistor tolerances, the existing authority packet calculates 5.75424575–6.24624625 A. That upper value is below 6.3 A by only about 0.05375 A, so the Power Authority must treat this as a tight qualification margin and must not use the absolute maximum as the normal operating limit.

### External nFET candidate

The existing PiSXMe candidate is TI `CSD19536KCS`, 100 V N-channel TO-220. Its manufacturer datasheet gives 2.5 V typical / 3.2 V maximum threshold at 250 µA, 2.5/3.2 mΩ at VGS = 6 V and 2.3/2.7 mΩ at VGS = 10 V, ±20 V maximum VGS, 118 nC typical / 153 nC maximum total gate charge, 0.4°C/W junction-to-case thermal resistance, and a 100 V drain-source rating.

The MAX17527A gate drive is specified around 4.45–4.95 V; the CSD19536KCS datasheet does not guarantee RDS(on) at that drive range. Therefore CSD19536KCS remains a candidate evidence item, not a closed external-FET selection. Power Authority must either select an nFET with guaranteed low-voltage RDS(on) at the MAX17527A gate-drive range or obtain a bounded electrical/thermal qualification that covers the declared source range, transient, reverse-polarity, reverse-current, and short-circuit conditions. The MAX17527A's 85 V example for -55 V at VOUT = 30 V is an application example, not the PiSXMe system requirement; the selected FET VDS rating must be derived from the signed PiSXMe transient/reverse-polarity envelope.

### Fuse

Littelfuse MINI 297 official datasheet, revised 2024-09-27, identifies the 0297015._ family as 15 A, 32 V DC, 1000 A interrupting at 32 V DC, recommended environmental temperature −40°C to +125°C. It gives 4.58 mΩ typical cold resistance and 308 A²s typical I²t for 0297015._. The manufacturer states this I²t is an average from breaking-capacity tests using melting time before arcing. Its time-current table gives 15 A opening intervals of 0.15–5 s at 200% rating, 0.08–0.5 s at 350%, and 0.03–0.1 s at 600%; typical derating is 13 A at 20°C and 9 A at 100°C for the 15 A item. The table explicitly says the final recommendation depends on terminals and wire size.

The manufacturer table therefore supplies a fuse identity, rating, typical cold resistance, typical pre-arcing I²t, and time-current/temperature context. It does not close coordination with the MAX17527A 3 µs fast trip, external-FET SOA, TVS pulse energy, harness inductance, or PiSXMe copper. A distributor listing reports a different 270 A²s melting-I²t field; preserve that as a conflicting definition rather than silently merging it with the manufacturer's 308 A²s typical pre-arcing value.

### TVS

Littelfuse SMBJ-series official datasheet identifies unidirectional `SMBJ18A` as a 600 W SMB/DO-214AA class part with 18.0 V standoff, 20.0–22.1 V breakdown at 1 mA, 29.2 V maximum clamp at 20.6 A peak-pulse current, and 1 µA maximum reverse leakage at standoff. These values support the existing 12 V clamp candidate at the nominal source level, but they do not establish allowable pulse duration/energy for the PiSXMe harness, source, fuse, or external nFET. The 29.2 V clamp must be checked against the selected FET's transient rating, the MAX17527A absolute limits, and the actual source/harness inductance.

## Cross-correlation and classification

| Requirement | Evidence status | Classification | Authority action still required |
|---|---|---|---|
| MAX17527A current-limit and SETI behavior | Manufacturer datasheet plus existing 6.25 kΩ calculation | A/B | Accept the calculation with explicit 6.3 A absolute-limit margin and thermal qualification |
| External nFET topology and gate drive | Manufacturer datasheet | A | Bind exact source/drain/gate contract and qualify an MPN at 4.45–4.95 V drive |
| Current-limiter fast trip | Manufacturer datasheet | A | Interpret 20–32 A IOCP and 3 µs response in the system fault model; do not treat it as a 6.4 A instantaneous limiter |
| FLAG/inhibit behavior | Manufacturer datasheet | A for per-device behavior | Define six-loop wired aggregation, pull-up domain, fail-safe polarity, branch-loss handling, and reset/latch policy |
| Fuse rating/time/I²t | Manufacturer datasheet | A | Coordinate with harness, TVS, external FET SOA, and PCB copper; resolve the 270 vs 308 A²s definition conflict explicitly |
| TVS clamp/pulse rating | Manufacturer datasheet | A | Select branch placement and prove pulse energy, source tolerance, inductance, FET SOA, and downstream absolute-limit margin |
| Six-loop simultaneous fault behavior | No manufacturer system source | C/D engineering requirement | Power Authority must set the PiSXMe fault policy and obtain calculations or measurements; this is not a Library gap after the component facts are indexed |
| Exact installed harness and thermal installation | No selected assembly record | C/D | Harness/Thermal Authority must bind part, crimp, loop resistance, ambient/airflow, and installation limits |

## Gaps returned to authority

1. `CSD19536KCS` is not qualified at the MAX17527A's guaranteed 4.45–4.95 V external gate drive; select a low-voltage-qualified nFET or produce direct qualification evidence.
2. The MAX17527A external nFET remains on during the internal 20–32 A fast-trip event; external-FET SOA/I²t under the actual branch fault must be calculated and accepted.
3. The exact system-level fuse/TVS/FET/harness energy coordination is not a vendor-provided number and must be synthesized by Power Authority.
4. Six FLAG outputs and branch shutdown/reset behavior require an explicit fail-safe aggregation contract; the device datasheet only defines one device's open-drain behavior.
5. The 0297015 I²t fields from Littelfuse (308 A²s typical pre-arcing) and a distributor (270 A²s melting I²t) use different definitions and must not be treated as interchangeable.

Acquisition is complete enough for Power Authority reassessment. The packet does not claim production qualification, a signed source contract, hardware operation, or CAD readiness.
