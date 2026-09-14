# P24-EXACT-NFET-DOSSIER

Status: `EVIDENCE_PACKET_READY_WITH_EXACT_GATE_AND_SYSTEM_COORDINATION_GAPS`  
Queue package: `P24-EXACT-NFET-DOSSIER`  
Owner: Librarian  
Private Library: `nova-rey/pisxme-private`, branch `Library`, commit `4e0852a3`  
Indexed brief: `Library/briefs/exact-nfet-energy-dossier-p24-20260914.md`

## Scope

This bounded acquisition searched the private Library and project-local authority
inventory first, then acquired targeted primary manufacturer evidence. It did
not change CAD, product requirements, or public restricted/reference material.

## Evidence returned

- Analog Devices MAX17527A Rev. 0 (2023-03-20) establishes the external nFET
  topology and 4.45 V minimum / 4.75 V typical / 4.95 V maximum gate drive.
  Its internal fast trip is 20 A minimum / 26 A typical / 32 A maximum with
  3 us typical response, and the external nFET remains on during the short
  circuit event.
- STMicroelectronics `STL125N10LF8AG`, DS14632 Rev 3 (May 2026), is the
  strongest candidate: AEC-Q101, 100 V VDS, 5.8 mOhm maximum at VGS=4.5 V and
  ID=30 A, -55 to +175 C junction range, 100% avalanche tested, 60 A / 330 mJ
  stated single-pulse avalanche rating, and a published SOA through TJ=175 C.
  Its 175 C RDS(on) curve is typical, and its guaranteed 4.5 V data point is
  50 mV above the controller's guaranteed minimum.
- Infineon `BSC096N10LS5`, Final Data Sheet Rev 2.1 (2019-09-02), is a lower
  margin comparator: 100 V, 12.5 mOhm maximum at VGS=4.5 V and ID=10 A,
  -55 to +175 C, 100% avalanche tested, 45 mJ EAS at the stated test point,
  and SOA/reverse-diode curves through 175 C.
- Local TI `LM74700-Q1`, SNOSD17G Rev G (December 2020), gives useful
  manufacturer guidance to use 4.5 V RDS(on) data and selects DMT6007LFG for a
  different 12 V / 3 A ideal-diode design. It does not close PiSXMe: that
  controller uses a charge-pump gate drive up to about 13 V and has a different
  reverse-protection contract. Local PDF SHA-256:
  `e16b3a8c0023201fafa5825436f5f2dd6f885b92b84e65602b3f50d741c58b6f`.
- Researcher-returned Diodes `DMT6007LFG`, DS37335 Rev. 2-2 (November 2015),
  specifies 60 V, 8.5 mOhm maximum at VGS=4.5 V and ID=15 A, -55 to +150 C,
  AEC-Q101/100% UIS, EAS 20 mJ at the stated 0.1-mH test, SOA at TJ max 150 C,
  and a 4.5-V RDS(on)-temperature graph.
- Researcher-returned TI `CSD18536KCS`, SLPS532C revised March 2024, specifies
  60 V, 2.2 mOhm maximum at VGS=4.5 V and ID=100 A, -55 to +175 C, 0.4 C/W
  junction-to-case, and SOA/normalized RDS(on) curves including 4.5-V gate data.
  Both are candidates only: their 60-V VDS ratings may be insufficient for the
  declared negative-input/transient envelope, and 4.5-V data remains 50 mV above
  the MAX17527A guaranteed minimum.
- Existing indexed Littelfuse 0297015 and SMBJ18A manufacturer records provide
  fuse rating/time/I2t and TVS standoff/breakdown/clamp facts. Existing Molex
  records provide 16-AWG 8 A/circuit and 30 C rise test basis with derating.

## Exact gaps returned to Power Authority

1. No acquired candidate has a guaranteed RDS(on) maximum at exactly VGS=4.45 V.
   Select a device with that guarantee, or bind a gate-drive tolerance/qualification
   method that closes the 50 mV gap to the STL 4.5 V specification.
2. Candidate RDS(on) maxima are 25 C electrical limits; high-temperature curves
   are typical. Bind a worst-case temperature multiplier and installation limit,
   or obtain qualification at the actual minimum gate drive and declared TJ.
3. Calculate the PiSXMe source/reverse/transient envelope and tie the required
   VDS margin to harness inductance and TVS clamping. A 100 V headline rating
   alone is not a system proof.
4. Calculate/qualify the six-loop fast-fault waveform: nFET SOA/I2t, TVS pulse
   energy, fuse clearing, harness L/R, and PCB copper for the MAX17527A 20–32 A
   fast-trip behavior and actual fault duration.
5. Bind the exact six harnesses, lengths, crimp/contact allocation, hot loop
   resistance, inductance, ambient/airflow, and installation thermal margins.
6. Select and package the production FET (PowerFLAT 5x6, SuperSO8, or another
   qualified MPN) against the protected-input copper and assembly process.

Acquisition is complete enough for Power Authority reassessment. This packet
is evidence only; it does not promote an MPN, authorize a footprint/CAD edit,
sign the source contract, or claim hardware qualification.
