# PiSXMe Rev-A Branch-B Power Envelope Authority

**Decision ID:** `PISXME-REV-A-POWER-ENVELOPE-001`  
**Version:** `1.0.0`  
**Decision date:** 2026-09-14  
**Authority:** Power Authority, requested by Root Foreman  
**Synthesis input:** Power Integrity Engineer and Librarian packets listed below  
**Scope:** selected Path-A production implementation; J5/J6 Branch A/B 12-V input, protection, merged protected rail, SXM2/V100 power field, and the three PiSXMe regulator rails.  
**CAD state:** read-only review; no schematic, PCB, library, or rule file was edited.

## Binding decision

The prior `external-blocker` classification is rejected. All nine requested
fields are establishable as manufacturer facts (A), conservative calculations
from those facts and explicit project assumptions (B), or internal PiSXMe
system requirements within the approved Rev-A product boundary (C). No
indispensable field is D.

The binding Rev-A operating envelope is:

| Quantity | Binding requirement |
|---|---:|
| regulated input | 12.0 V nominal, current-limited source |
| V100/SXM2 design allowance | 250 W at the 12-V input design basis |
| total protected-input current | **25.25 A maximum for the Rev-A operating envelope** |
| Branch A / Branch B continuous limit | **13.0 A maximum per branch** |
| equal-share target at the envelope | 12.625 A per branch |
| combined branch capacity | 26.0 A; 0.75 A / 2.97% margin above 25.25 A |
| branch protection | existing 15 A fuse per branch; it is protection, not a 13-A current regulator |
| supported loss-of-branch behavior | disable or inhibit V100 enable and hold the reset policy; never continue the full envelope through one 13-A branch |

The 13-A value is the hard branch operating limit. The selected mating
terminal, wire, crimp, cable length, temperature, and installation must be
procured or qualified for at least 13 A continuous at the declared ambient.
The Molex 13-A fact applies to the selected board header contact and does not
automatically qualify an unspecified harness.

## Calculation basis and margins

The project worksheet uses a conservative 90% input-power factor for the
V100 design allowance and the low-voltage converters:

```text
I_V100 = 250 W / (12.0 V * 0.90) = 23.14815 A
P_LV   = (5.0 V * 3.0 A) + (3.3 V * 2.0 A) + (1.1 V * 1.0 A)
       = 22.7 W
I_LV   = 22.7 W / (12.0 V * 0.90) = 2.10185 A
I_TOTAL = 23.14815 A + 2.10185 A = 25.25000 A
```

At equal sharing, each branch is 12.625 A. Two 13-A limits provide 26 A
combined capacity, leaving 0.75 A (2.9703%) at the combined input. At the
hard-cap corner, one branch can be 13.0 A only if the other is at least
12.25 A for a 25.25-A total; the corresponding absolute imbalance limit is
0.75 A, or 5.94% of the 12.625-A equal-share target. A branch-open event is
therefore outside the supported operating envelope and must disable V100
power rather than silently transfer 25.25 A to the remaining branch.

The 15-A fuse has 2 A (15.38% relative to the 13-A operating cap) of nominal
rating headroom. Fuse ampere rating alone does not prove time-current, I2t,
connector, harness, or thermal closure; those remain implementation and
validation gates.

For the selected `CSD19536KCS`, using the manufacturer maximum 2.7 mOhm
RDS(on) at 10-V gate drive:

```text
P_FET(12.625 A) = 12.625^2 * 0.0027 = 0.430 W per branch
P_FET(13.000 A) = 13.000^2 * 0.0027 = 0.456 W per branch
P_FET(25.250 A) = 25.250^2 * 0.0027 = 1.722 W (unsupported one-branch fault)
```

The one-branch result is retained as a fault-stress reason for shutdown; it
is not a permitted operating point. The old 62 C/W screening bound at 40 C
ambient gives approximately 66.7 C junction at 12.625 A and 68.3 C at 13 A,
but this is a component/worksheet screen, not board thermal proof. Final
board spreading, fuse-holder, connector, harness, airflow, and temperature
measurements remain required.

The three `TPSM63606RDLR` outputs are internally limited/rated at 6 A in the
project authority packet. The binding design loads use 3 A on `CM5_5V`, 2 A
on `BRIDGE_3V3`, and 1 A on `BRIDGE_1V1`, giving 50.0%, 33.3%, and 16.7%
current utilization, respectively. These are design envelopes, not measured
loads. The 1.1-V output retains a separate effective-capacitance gate:
16 x 22 uF x 0.90 = 316.8 uF nominal derated, but applying the capacitor's
20% tolerance gives 253.44 uF, below the 300-uF minimum from the conservative
1-V TI reference row. This is an open implementation/validation item and is
not hidden by this envelope decision.

## Field-by-field authority classification

The classification describes how the binding requirement is established:

- **A:** direct authoritative external specification;
- **B:** conservative derivation from authoritative data plus declared
  assumptions;
- **C:** PiSXMe internal system requirement set by Power Authority within the
  approved product boundary;
- **D:** indispensable input that cannot be established by the organization.

| Required field | Class | Binding requirement and evidence | Margin / unresolved limit |
|---|---|---|---|
| Connector limit | A + C | Molex `0039300020` manufacturer record gives 13.0 A maximum per contact. Bind each J5/J6 power contact to <=13.0 A continuous and do not treat J1's separate Amphenol 0.45-A contact rating as input-header evidence. | 13.0 A is the hard contact limit; 12.625 A is the equal-share operating target. Exact mating terminal and installed harness remain separate assembly evidence. |
| Harness limit | C | Require a selected mating terminal, wire gauge, crimp, cable length, and installation qualified for >=13.0 A continuous per branch at the declared ambient; require the harness voltage-drop and temperature-rise record before release. | No exact harness has been selected. This is an internal procurement/assembly requirement, not a D evidence gap. |
| Continuous current | B + C | Bind total protected-input current <=25.25 A. Derivation is the 250-W V100 design allowance plus 22.7 W low-voltage load at the documented 90% factor. | 0.75 A / 2.97% combined margin to two 13-A limits. `25.25 A` is a design envelope, not a V100 vendor guarantee or bench result. |
| Peak current | C | Bind the supported protected-input peak/operating envelope to <=25.25 A total and <=13.0 A per branch. Any requested over-envelope peak is a fault/stress case requiring current limiting or V100 shutdown, not an accepted Rev-A operating point. | No V100 transient waveform is claimed. Peak duration and slew are defined by the load-step requirement below and must be validated. |
| Branch imbalance | B + C | Equal-share target is 12.625 A/branch. At 25.25 A total, bind `abs(I_A-I_B) <=0.75 A`, `I_A <=13 A`, and `I_B <=13 A`; the worst allowed corner is 13.0 A / 12.25 A. Use the two LM74700-Q1 ideal-diode branches as the sharing topology. | TI supports the topology but gives no PiSXMe numeric imbalance. Path resistance, FET drop, connector/harness resistance, and transient mismatch remain calculated/measured validation inputs. |
| Shutdown behavior | A + C | Use LM74700-Q1 reverse-current blocking/enable behavior and the existing separate branch nets as component/topology facts. Bind any branch open, branch overcurrent, input UV/OV, or protection fault to inhibit V100 enable and hold the reset policy; no full-envelope single-branch continuation. | Exact monitor thresholds, latch/retry implementation, and V100 endpoint sequencing remain `REV_A_EMPIRICAL_RISK`; no hardware behavior is claimed. |
| Surge/load-dump limits | A + C | LM74700-Q1 is specified for 3.2–65 V input and advertises load-dump compatibility. For the Rev-A product boundary, bind operation to a regulated current-limited 12-V source and do not claim automotive load-dump compliance. The selected SMBJ18A screen is 18-V standoff and 29.2-V maximum clamp at its rated 20.6-A pulse; this is below the 65-V controller and 100-V MOSFET ratings by 35.8 V and 70.8 V, respectively. | TVS pulse energy, harness inductance, fuse I2t, source waveform, and MOSFET SOA still require the actual fault model. Automotive load-dump support would require a new product decision and is outside this Rev-A binding envelope. |
| Thermal limits | A/B + C | Use the manufacturer component ranges and the calculations above. Bind the assembly to a declared ambient/airflow envelope, no component/harness/connector/fuse temperature over its selected rating, and a documented temperature-rise margin at 13 A/branch. Use 40 C ambient as the existing screening reference only. | Board copper, connector contact, fuse holder, harness, regulator, return-plane, and airflow thermal results are not present. The 62-C/W FET screen is not a release measurement. |
| Current sharing | A + B + C | TI's LM74700-Q1 load-sharing precedent establishes the topology. Bind the branch model and validation to the 12.625-A target, 13-A hard cap, 0.75-A maximum full-load difference, branch-loss shutdown, and measured/calculated path resistance. | No passive-sharing assumption closes the row. The two branch paths must be routed and independently validated against these limits. |
| Load-step requirement | C + B | Require a fixture/model sweep from 0 to 25.25 A total with equal 12.625-A branches and the worst allowed 13.0/12.25-A split; exercise a 0.1–1.0 A/us edge and >=10 ms plateau, while keeping each branch <=13 A. At the 12-V protected/SXM2 entry, require 11.4–12.6 V during the supported step and no V100 reset/disable; apply each TPSM vendor transient limit at its rail. | No public V100/SXM2 waveform was found. The step magnitude, edge range, plateau, and 5% input band are internal C requirements for Rev-A validation, not measured hardware evidence. |

No row is D. The absence of an exact harness assembly and a public V100
load-step waveform is recorded as an implementation/evidence limitation, not
as a reason to require Rey to invent values. Power Authority is empowered to
set these internal requirements under the approved Rev-A boundary.

## Rail-by-rail implementation constraints

These constraints are binding inputs to the subsequent power/corridor work;
they do not certify the current PCB:

1. **J5/J6 raw input:** two independent Molex branches, each one 12-V
   contact and one return contact. Preserve independent fuses, TVS,
   LM74700-Q1 controllers, external FETs, and explicit branch test points.
   No branch may be treated as an interchangeable cosmetic duplicate.
2. **Fused/protected 12 V:** route each branch for the 13-A hard cap and
   return it through a low-impedance adjacent path. Merge only after the two
   protection paths; avoid one narrow neck to the 130-contact SXM2 field.
3. **SXM2/V100 field:** preserve the selected J1 12-V/GND contact contract,
   distribute current across the assigned power contacts, preserve the
   existing high-speed return corridors, and provide measurement access at
   the protected entry and return. The current census is physical ownership
   evidence only.
4. **CM5 5 V:** design load 3 A, TPSM 6-A class, 50% utilization. Follow the
   TI input-capacitor, output-capacitor, FB/RT/EN/PG, AGND/PGND, and thermal
   via guidance. Validate static IR drop and load-step droop separately.
5. **Bridge 3.3 V:** design load 2 A, 33.3% utilization. Keep the U4
   switch-node loop and return local; do not route it through PCIe/REFCLK or
   storage high-speed corridors.
6. **Bridge 1.1 V:** design load 1 A, 16.7% utilization. Close the effective
   >=300-uF COUT requirement across tolerance, DC bias, temperature, and
   frequency before treating this rail as power-ready; nominal 316.8-uF
   arithmetic is insufficient by itself.
7. **Return/ground:** preserve the three `POWER_GND` return zones and local
   regulator AGND/PGND joins, but require native connectivity and impedance
   evidence. The current 325-pad / 47-segment / 17-via census and 171
   unconnected return items do not close the return gate.
8. **Sequencing:** branch validity and protected input must precede V100
   enable; V100 power-good and branch-fault policy must be resolved before
   CM5 releases the applicable PCIe reset. Exact SXM2 endpoint sequencing is
   retained as `REV_A_EMPIRICAL_RISK`.

## Legacy value disposition

The older 300-W and 330-W values are not silently deleted; they are
reclassified:

| Legacy value | Calculation at the same 90% factor | Disposition |
|---|---:|---|
| 300 W V100 allowance | `300/(12*0.90) + 2.10185 = 29.87963 A` total; 14.9398 A/branch equal share | Not a supported Rev-A operating envelope: exceeds the 26-A dual-13-A capacity by 3.8796 A and the 13-A branch cap by 1.9398 A/branch. Retain only as an empirical/stress reference tied to NVIDIA's separate 300-W maximum-power product fact. |
| 330 W preliminary peak allowance | `330/(12*0.90) + 2.10185 = 32.65741 A` total; 16.3287 A/branch equal share | Rejected as a binding Rev-A requirement: exceeds dual-13-A capacity by 6.6574 A and the branch cap by 3.3287 A/branch. It is a superseded preliminary budget number, not vendor or product authority. |
| 28.5 A / 34.3 A preliminary input budget | Existing `FINAL_POWER_BUDGET.json` values | Superseded by this signed 25.25-A / dual-13-A envelope for Phase 24 routing and validation; preserve the old file as historical evidence and do not use it to widen copper or relax the branch gate. |

This disposition does not claim that every V100 SXM2 module behaves at 250 W,
nor that a 300-W product is impossible with a different connector, harness,
protection, copper, thermal, and product architecture. It binds only the
approved PiSXMe Rev-A acreage campaign.

## Acceptance and resume conditions

This authority receipt removes the premise for Issue #2's
`external-blocker`. It does not close `power_current_transient_thermal`,
`native_drc`, `physical_opens_shorts`, or `storage_mode_behavior`.

The Power/MPA Supervisor may return the dependent package to `READY` and must
derive its corridor constraints from this receipt. The required sequence is:

```text
Power Authority receipt
  -> MPA/Unblocker corridor reassessment
  -> one isolated producer candidate
  -> targeted connectivity/DRC
  -> serialized canonical integration
  -> fresh KiCad Light validation at the exact integrated SHA
```

The current integrated PCB still has Branch-B and bridge-rail zero-copper
gaps, a sparse protected-12-V network, unresolved return connectivity, and
open regulator/thermal evidence. No claim of routing, fabrication, measured
load-step, or hardware operation is made here.

## Inputs and provenance

Private Librarian brief and Researcher sack (kept outside the public repo):

- `/home/nyx/PiSXMe-Library/Library/briefs/power-envelope-authority-reassessment-20260913.md`
  SHA-256 `eabb119fee38a4d4efd97744f85cc31594aa0efac7c38754aa944a4b64558542`.
- `/home/nyx/PiSXMe-Library/Library/briefs/researcher-power-envelope-gap-20260913.md`
  SHA-256 `e3f8bc9c2e588f38caddc8166f405b399f5a5ff3afff6419c491888984610368`.
- Private source index `/home/nyx/PiSXMe-Library/Library/provenance/sources.json`,
  SHA-256 `c88e2ffacac3a3f23b56700a9616eb31f4f22ef12aab544bd1c07e83531bdbff`.

Public-repo design-basis records and current validation evidence:

| Input | SHA-256 |
|---|---|
| `PHASE5_POWER_CALCULATIONS.md` | `82c34b6a4b2b4878f7e74c7f7873ad68ba4d10ebfa6a7c33d742fa2a632b60e6` |
| `PHASE5_POWER_NETWORK_SPEC.md` | `9e29ef646d4af5199a9e745a0fe8d6a140144acc67540c5956b98d0579e446df` |
| `PHASE5_POWER_RECEIPT.md` | `1eb265999294c0c696c0071cf484af1db5f58ab0fd808356a2fdeca936978f56` |
| `authority-inventory/primary-docs/power/MOLEX_0039300020_AUTHORITY.md` | `37d7642bf413385e3980aabb6b63ef758b9d3398a69f500a45b0bf2b861608c3` |
| `authority-inventory/primary-docs/power/LITTELFUSE_0297015U_17861650001_AUTHORITY.md` | `d2e617125ae28bef0e977f69211e3c5a08eabce184f172b91e5d4bc20fcab389` |
| `authority-inventory/primary-docs/power/SMBJ18A_TVS_AUTHORITY.md` | `4e63353741e69f7f6186e314f8caf93b4b62265166f97e2a32445d1d25280158` |
| `authority-inventory/primary-docs/power/TPSM63606_SUPPORT_AUTHORITY.md` | `6bc179162c0d42d089b6df0fd9cd2823ce77c1f5b9587d4b7178cac297d9341d` |
| `authority-inventory/primary-docs/power/TDK_C3225X7R1C226M250AC_AUTHORITY.md` | `a3321e37be0c7a122fc246c49a175c64438aa3656613283fa56da413796f5960` |
| `validation-receipts/power-return-census-current-a56b4399-20260913/power-census.json` | `f677f05be1994a8910d6bc8f17299b6616be1fcf7487dee5f8dc3a34c0209e7c` |
| `validation-receipts/power-return-census-current-a56b4399-20260913/RECEIPT.md` | `cabb8d0a93aa9ba2cd6345611413970ae8108167cad93d63b87c201071b1f002` |
| `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb` | `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c` |
| `PiSXMe_RevA_Clean.kicad_sch` | `6eef63bd3d2b0b9fafc0150d3c34f636ce24a48b2ecbd3d28a5f0bfec167e9f1` |

Manufacturer source IDs, revisions, and URLs are maintained in the private
Library source index. No restricted PDFs, CAD, or reference corpus material
was copied into this public development repository.

## Authority signature

This is a role-signed project decision, not a cryptographic claim of a human
signature. The canonical artifact digest is recorded after commit in
`SHA256SUMS`; the signing role is **Power Authority** and the review agent is
`/root/power_authority_review_envelope`. Future changes require a new decision
version and a new digest; this version must not be rewritten in place.
