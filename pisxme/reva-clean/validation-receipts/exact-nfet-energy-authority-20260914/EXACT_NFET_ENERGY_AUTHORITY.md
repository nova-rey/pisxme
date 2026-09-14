# P24-EXACT-NFET-ENERGY-AUTHORITY

Status: `BLOCKED_INTERNAL_QUALIFICATION_GAPS`

Package: `P24-EXACT-NFET-ENERGY-AUTHORITY`  
Review base: `ae0469bb` (`reva-clean`)  
CAD changed: **no**  
Product envelope changed: **no**

## Binding disposition

No external reverse-protection nFET is promoted to the PiSXMe production
contract. The evidence packet is sufficient to rank candidates and identify
the exact qualification gates, but it does not close the MAX17527A gate-drive,
temperature, system transient, SOA/I2t, harness, or installation requirements.
Selecting an MPN or changing the schematic/PCB would therefore be premature.

`STL125N10LF8AG` remains the strongest **unqualified candidate** for a
qualification calculation: 100 V VDS, 5.8 mOhm maximum RDS(on) at VGS=4.5 V
and ID=30 A, -55..175 C junction range, 100% avalanche tested, and published
SOA. It is not an approved selection because the MAX17527A gate-drive minimum
is 4.45 V, the candidate's guaranteed RDS(on) point is 4.5 V, and the
candidate's high-temperature RDS behavior is not a guaranteed 4.45 V value.

`BSC096N10LS5` is retained only as a lower-margin 100 V comparator. The
60 V candidates (`CSD18536KCS` and `DMT6007LFG`) are not acceptable defaults
until the complete PiSXMe negative-input and transient envelope proves a
60 V rating is sufficient; that envelope is not currently bound. The existing
`CSD19536KCS` evidence has no 4.5 V RDS(on) guarantee and is not qualified at
the controller gate.

The already selected `MAX17527AATP+T` six-loop limiter basis remains a
conditional limiter decision from the separate Power Authority signoff. This
receipt neither changes that decision nor authorizes inserting it into CAD.

## Closure matrix

| Gate | Evidence reviewed | State | Required closure |
|---|---|---|---|
| Controller gate drive | MAX17527A Rev. 0: external gate drive 4.45 V minimum, 4.75 V typical, 4.95 V maximum; candidate guaranteed data at 4.5 V | `UNPROVEN` | Bind a device with guaranteed RDS(on) at 4.45 V, or qualify gate-drive tolerance and device RDS(on) at the actual minimum over temperature. The 50 mV difference cannot be assumed away. |
| VDS and source/reverse/transient envelope | STL/BSC candidates are 100 V; lower candidates are 60 V; PiSXMe harness inductance, source fault, TVS clamp, reverse polarity and reverse-current envelope are not calculated | `UNPROVEN` | Calculate worst-case VDS at the FET including source tolerance, reverse event, harness L/R, TVS clamp and switching/fault timing, then bind VDS margin and the production MPN. |
| Temperature and RDS(on) | Candidate 25 C RDS(on) maxima; high-temperature curves are typical; installation copper/package/airflow is not qualified | `UNPROVEN` | Use a guaranteed minimum-gate, declared-junction-temperature RDS(on) bound and package/PCB thermal calculation with production derating. |
| Fast fault SOA/I2t | MAX17527A fast-trip threshold is 20 A minimum / 26 A typical / 32 A maximum, 3 us typical; external FET remains on during the short event; blanking is 22.5..25.5 ms and latch behavior is system relevant | `UNPROVEN` | Calculate the actual six-loop fault waveform and integral energy/current against FET SOA/I2t, including response tolerance, TVS pulse energy, fuse clearing, harness L/R and PCB copper. The illustrative `32^2 * 3 us = 0.003072 A^2 s` screen is not a closure proof. |
| Fuse/TVS/FET coordination | Existing fuse and TVS records are source evidence only; complete system clamp, fuse I2t, FET SOA and harness-energy coordination is absent | `UNPROVEN` | Bind exact fuse, TVS/clamp and FET parts and retain worst-case coordination calculations for normal, reverse and fault cases. |
| Harness and connector installation | Molex contract gives current/derating basis; six exact harnesses, hot loop resistance/inductance, connector installation and airflow are not proven | `UNPROVEN` | Identify six harnesses and lengths, prove hot complete-loop resistance <=20 mOhm (or approved tighter value), include inductance and installation thermal margins. |
| Package and protected copper | Candidate package options are identified; protected-input copper, thermal vias, assembly process, clearance and service access are not closed | `UNPROVEN` | Select package/land pattern only after authority calculation and MPA/Thermal installation review; validate protected copper and temperature rise. |

## Internal dependencies

1. `PA-NFET-GATE-001`: select/qualify the exact production MPN at the
   MAX17527A guaranteed 4.45 V minimum gate drive, including temperature and
   tolerance. This is an internal Power/Package authority task.
2. `PA-NFET-VDS-002`: bind the PiSXMe source, reverse, TVS and harness
   transient envelope and required VDS margin.
3. `PA-NFET-ENERGY-003`: calculate the six-loop fast-fault waveform and bind
   nFET SOA/I2t, TVS pulse, fuse clearing, harness L/R and protected copper.
4. `PA-NFET-INSTALL-004`: bind exact harnesses and the selected package's
   installation/thermal limits with MPA and Thermal Authority.
5. `PA-NFET-ADI-PROVENANCE-005`: retain the exact official MAX17527A source
   hash in the private Library if it is treated as a provenance gate. This is
   secondary to the engineering gaps above.

Until dependencies 1--4 have signed evidence, the protection assembly and
source/net/component contract must remain waiting. No CAD producer is
released by this packet.

## Source records

- `validation-receipts/exact-nfet-energy-dossier-20260914/EXACT_NFET_ENERGY_DOSSIER.md`
  and `.json`, Librarian private Library commit `4e0852a3`.
- `validation-receipts/power-authority-signoff-20260914/POWER_AUTHORITY_SIGNOFF.md`
  and `.json`.
- `validation-receipts/power-current-limiter-authority-20260914/POWER_CURRENT_LIMITER_AUTHORITY.md`
  and `.json`.
- `validation-receipts/power-connector-qualification-closure-20260914/QUALIFICATION_CLOSURE.md`
  and `.json`.
- `validation-receipts/power-envelope-authority-redesign-20260914/POWER_ENVELOPE_AUTHORITY_V2.2_CANDIDATE.md`
  and `.json`.

No vendor PDF or restricted reference material was copied into public project
history by this review. No measurement, vendor approval, or hardware
qualification is claimed.
