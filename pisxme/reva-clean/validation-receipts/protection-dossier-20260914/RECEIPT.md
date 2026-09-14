# P24-PROTECTION-DOSSIER

Status: `ACQUISITION_COMPLETE_AUTHORITY_GAPS_REMAIN`  
Queue package: `P24-PROTECTION-DOSSIER`  
Owner: Librarian  
Private Library commit: `989e7b8c4e101f9d5a4be7841de2078aba8c9624` (`nova-rey/pisxme-private`, branch `Library`)

## Scope and disposition

The private Library was searched first. It already contained the PiSXMe `CSD19536KCS` candidate, `0297015.U` / `178.6165.0001` fuse-holder record, and `SMBJ18A` candidate, but lacked an indexed MAX17527A manufacturer record and current fuse/TVS coordination facts. The Librarian acquired and indexed only targeted manufacturer evidence. No vendor PDF, CAD, restricted, or copyrighted material was copied into the Library or public repository.

Indexed brief: `Library/briefs/protection-assembly-dossier-20260914.md`.  
Indexed sources: `adi-max17527a-ds-20260913`, `littelfuse-0297015-mini-ds-20260913`, `littelfuse-smbj-series-ds-20260913`, and the existing `ti-csd19536kcs-ds-slps485c`.

## Established evidence

- Analog Devices MAX17527A Rev. 0 (03/20/2023): 5.5–60 V input; 0.6–6.0 A programmable limit; external nFET source to SN, drain to IN, gate to GN; external gate drive 4.45 V minimum / 4.75 V typical / 4.95 V maximum under EN = 5 V; IOCP 20/26/32 A min/typ/max; 3 µs typical internal fast trip; external nFET remains on during the internal short-circuit trip; reverse-current slow/fast thresholds and timing; open-drain FLAG behavior; 22.5–25.5 ms blanking; 654–792 ms autoretry; latch-off reset behavior; 150°C foldback and 165°C thermal shutdown; 6.3 A absolute maximum DC IN current.
- Existing CSD19536KCS evidence: 100 V VDS, RDS(on) characterized at 6 V and 10 V gate drive, not at the MAX17527A's guaranteed 4.45–4.95 V drive; 0.4°C/W θJC.
- Littelfuse MINI 297 official datasheet (revised 2024-09-27): 0297015._ 15 A / 32 V DC / 1000 A interrupting; 4.58 mΩ typical cold resistance; 308 A²s typical I²t defined as average pre-arcing melt I²t; temperature/time-current derating and opening intervals.
- Littelfuse SMBJ official datasheet: SMBJ18A 600 W class, 18.0 V standoff, 20.0–22.1 V breakdown, 29.2 V clamp at 20.6 A peak-pulse current.

## Returned authority gaps

1. `CSD19536KCS` is not closed as the external nFET because its RDS(on) is not guaranteed at 4.45–4.95 V gate drive. Power Authority must select a low-voltage-qualified MPN or provide direct qualification.
2. The MAX17527A external nFET remains on during the internal 20–32 A fast-trip event. External-FET SOA/I²t under the actual branch fault is still required.
3. Fuse/TVS/FET/harness energy coordination is not established by component ratings alone. The 0297015 manufacturer value is 308 A²s typical pre-arcing; a distributor reports 270 A²s melting I²t under a different field definition. Power Authority must preserve and resolve this distinction.
4. Six-loop FLAG/inhibit/reset aggregation is not specified by the MAX17527A datasheet. Power Authority must define fail-safe aggregation, branch-loss behavior, and reset/latch policy.

Acquisition is complete enough for Power Authority reassessment. This receipt does not promote an MPN, sign the source contract, authorize CAD, or claim hardware validation.
