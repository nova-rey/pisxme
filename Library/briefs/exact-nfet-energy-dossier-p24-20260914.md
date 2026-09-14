# Exact reverse-protection nFET and fault-energy evidence

Package: `P24-EXACT-NFET-ENERGY-AUTHORITY`  
Retrieved: 2026-09-14  
Owner: Librarian (knowledge state; advisory)  
Decision authority: Power Integrity Engineer / Power Authority  
Status: `EVIDENCE_PACKET_READY_WITH_EXACT_GATE_AND_SYSTEM_COORDINATION_GAPS`

## Library-first result

The private Library already indexed the MAX17527A controller, the CSD19536KCS candidate, Littelfuse 0297015 fuse and SMBJ18A TVS, and Molex 5556/5569 harness data. The CSD19536KCS record does not specify RDS(on) at the MAX17527A guaranteed external gate drive. A bounded primary-source search added two manufacturer candidates with 100-V ratings and explicit 4.5-V RDS(on) data. No CAD or vendor PDF was copied.

## Controller contract

Analog Devices MAX17527A Rev. 0 (2023-03-20) specifies external nFET source to SN, drain to IN, gate to GN; external gate drive 4.45 V minimum, 4.75 V typical and 4.95 V maximum for EN=5 V with no reverse condition. The controller's current limit is 0.6–6.0 A with ±4% accuracy over 3–6 A; internal short-circuit fast trip is 20 A minimum, 26 A typical, 32 A maximum with 3 microseconds typical response. The external nFET remains on during that short-circuit fast-trip event. Thus the 6-A current-limit setting does not by itself bound the MOSFET's fault pulse. Reverse-current blocking, fuse, TVS and harness inductance must be coordinated as a system.

## Manufacturer candidates

### STMicroelectronics STL125N10LF8AG

Primary source: `DS14632 Rev 3`, May 2026, manufacturer URL recorded in `Library/provenance/sources.json`. It is an AEC-Q101-qualified automotive logic-level 100-V N-channel device in PowerFLAT 5x6. The datasheet specifies 175 °C maximum junction temperature, -55 to +175 °C operating range, 100% avalanche tested, VGS ±20 V, continuous ID 119 A at TC=25 °C and 84 A at TC=100 °C, and single-pulse avalanche rating IAS 60 A / EAS 330 mJ under the stated 30-A, 25-°C start test. RDS(on) maximum is 5.8 mOhm at VGS=4.5 V and ID=30 A, and 4.6 mOhm at VGS=10 V and ID=60 A, at TJ=25 °C. The published SOA includes a TJ=175 °C boundary and the datasheet includes a 175 °C RDS(on)-versus-VGS typical curve.

This is the strongest current candidate for a production authority review. It does **not** close the exact 4.45-V requirement: the guaranteed MAX17527A minimum is 50 mV below the device's 4.5-V RDS(on) test point. Its 4.5-V RDS(on) maximum is also a 25-°C electrical-characteristic limit; the 175-°C curve is typical, so the authority must apply a documented worst-case temperature multiplier or obtain a qualification measurement at the actual gate-drive minimum. The PowerFLAT package and its 1–3 source / 4 gate / 5–8 drain arrangement also need a package/thermal installation decision before CAD use.

### Infineon BSC096N10LS5

Primary source: `Final Data Sheet Rev. 2.1`, 2019-09-02, manufacturer URL recorded in `Library/provenance/sources.json`. It is an active logic-level 100-V N-channel device in SuperSO8, fully JEDEC-qualified for industrial applications, 100% avalanche tested, with -55 to +175 °C operating/storage range. The datasheet gives RDS(on) maximum 12.5 mOhm at VGS=4.5 V, ID=10 A and TJ=25 °C; 9.6 mOhm at VGS=10 V, ID=20 A. It gives EAS 45 mJ at ID=20 A, 100-V breakdown, SOA through 175 °C device limits, and 100-V reverse-diode test conditions.

This is a secondary candidate only. It has lower avalanche energy and less current/thermal headroom than the ST candidate, and likewise leaves the 4.45-V and temperature-bound RDS(on) gap. Its small package requires a separate copper/thermal review.

### Local TI LM74700-Q1 reference (not the active controller)

The project-local TI `LM74700-Q1` datasheet (`SNOSD17G`, revised December 2020; SHA-256 `e16b3a8c0023201fafa5825436f5f2dd6f885b92b84e65602b3f50d741c58b6f`) contains useful manufacturer MOSFET-selection guidance. It says to select VDS for the highest differential fault voltage, select body-diode current above inrush, and use RDS(on) values specified at 4.5 V. Its example 12-V reverse-battery design selects Diodes Inc. `DMT6007LFG`, rated there as 60 V VDS, ±20 V VGS, 6.5 mOhm typical / 8.5 mOhm maximum at VGS=4.5 V and Vth maximum 2 V.

This does not close PiSXMe's MAX17527A contract. LM74700-Q1 drives its FET with a charge pump up to approximately 13 V and has a different reverse-current controller. The example is a 3-A nominal 12-V design and supplies no PiSXMe six-loop SOA, fuse/TVS/harness energy proof. `DMT6007LFG` is therefore a useful precedent for a 4.5-V-rated FET requirement, not a selected or qualified PiSXMe MPN. It also does not remove the 4.45-V minimum gap.

### Researcher-returned 4.5-V candidates

The bounded Researcher sack also returned two primary datasheets. TI `CSD18536KCS`, SLPS532C revised March 2024, specifies 60 V VDS, 2.2 mOhm maximum at VGS=4.5 V and ID=100 A, -55 to +175 C operation, 0.4 C/W junction-to-case, an SOA through the stated thermal boundary, and normalized RDS(on) curves explicitly including VGS=4.5 V. Diodes Inc. `DMT6007LFG`, DS37335 Rev. 2-2 (November 2015), specifies 60 V, 8.5 mOhm maximum at VGS=4.5 V and ID=15 A, -55 to +150 C, AEC-Q101/100% UIS, EAS 20 mJ at the stated 0.1-mH test, SOA at TJ max 150 C, and an RDS(on)-temperature graph at 4.5 V/15 A.

Both improve the evidence over CSD19536KCS but remain candidates, not PiSXMe selections. Their 60-V VDS ratings may be insufficient for the declared negative-input/transient envelope, and their 4.5-V specifications remain 50 mV above the MAX17527A guaranteed minimum. The temperature curves support a calculation but do not by themselves provide a guaranteed maximum RDS(on) at 4.45 V and the declared hot operating point.

### Existing CSD19536KCS

The existing TI record remains a rejected/unqualified candidate for this gate. Its published RDS(on) values are at 6 V and 10 V, not at the MAX17527A 4.45–4.95-V guaranteed drive. Do not infer 4.45-V suitability from threshold voltage or a typical transfer graph.

## Fuse, TVS, harness and fast-trip cross-correlation

The existing indexed component evidence remains applicable:

- Littelfuse 0297015 MINI is 15 A / 32 V DC / 1000 A interrupting, with 4.58 mOhm typical cold resistance and 308 A²s typical pre-arcing I²t. The manufacturer time-current table spans 0.03–0.1 s at 600% rating, 0.08–0.5 s at 350%, and 0.15–5 s at 200%; its 13-A-at-20-°C and 9-A-at-100-°C derating illustrates why the 15-A marking is not a continuous system guarantee. A distributor's 270 A²s field uses a different I²t definition and remains conflicting evidence.
- Littelfuse SMBJ18A is a unidirectional 600-W TVS, 18.0-V standoff, 20.0–22.1-V breakdown, and 29.2-V maximum clamp at 20.6-A peak pulse. The source does not specify PiSXMe pulse duration/energy for the actual harness.
- Molex 5556/5569 evidence supports 16-AWG phosphor-bronze at 8 A per circuit for 2–3 circuits on a 30-°C-rise test basis, with application derating and a -40 to +105 °C family range. The exact PiSXMe six harnesses, hot loop resistances and inductances remain unbound.

The manufacturer evidence proves component facts but not the PiSXMe system transient. In particular, the MAX17527A's 20–32-A fast trip and external-FET-on behavior require a worst-case fault model that includes source voltage, harness L/R, local capacitance, TVS clamp trajectory, fuse clearing, nFET SOA and copper. `E = 1/2 L I²`, `V = L di/dt`, and fuse/TVS/nFET energy must be evaluated against the selected assembly; a component's headline rating is not a system pass.

## Exact authority gaps

1. **Gate minimum:** no candidate found in this bounded acquisition has a guaranteed RDS(on) maximum at exactly VGS=4.45 V. STL125N10LF8AG is specified at 4.5 V and is the strongest candidate, but the 50-mV gap must be closed by a binding gate-drive tolerance/qualification approach.
2. **Temperature-bound conduction:** candidate electrical RDS(on) maxima are specified at TJ=25 °C; high-temperature curves are typical. Power Authority must bind a worst-case temperature multiplier and thermal limit or obtain measured qualification at the actual gate-drive minimum.
3. **System VDS/reverse envelope:** the 100-V candidate rating is not yet tied to PiSXMe source tolerance, negative input, harness inductance and TVS clamp. The product reverse/transient envelope and minimum VDS margin must be calculated and signed.
4. **Fast-trip energy:** no vendor source supplies the PiSXMe six-loop fault waveform. Power Authority must calculate/qualify nFET SOA/I²t, TVS pulse energy, fuse clearing, harness inductance and PCB copper for the declared 20–32-A fast-trip range and fault duration.
5. **Harness installation:** exact cable MPN/length, crimp/connector resistance allocation, six hot-loop resistance measurements, inductance, ambient/airflow and installation temperature margins remain open.
6. **Package/installation:** selection between the ST PowerFLAT 5x6, Infineon SuperSO8, or a qualified alternative must be reconciled with the existing protected input region, copper and assembly process.

## Disposition

Acquisition is complete enough for Power Authority reassessment and a bounded exact-nFET decision. The packet does not promote an MPN, authorize a footprint or CAD edit, sign the source contract, or claim hardware qualification. The original CSD19536KCS gap is narrowed to explicit authority/qualification work; it is not an evidence-exhaustion or user blocker.
