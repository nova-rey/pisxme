# PiSXMe Rev-A Branch-B Power Envelope Authority — v1.1

**Decision ID:** `PISXME-REV-A-POWER-ENVELOPE-001`
**Version:** `1.1.0`
**Decision date:** 2026-09-14
**Authority:** Power Authority, requested by Root Foreman
**Synthesis input:** Librarian brief, Researcher sack, and exact Molex application specification
**Status:** controlling decision; supersedes same-ID version 1.0.0
**CAD state:** read-only review; no schematic, PCB, library, rule, or configuration file was edited.

## Decision

The generic Molex product-page value of 13.0 A maximum per contact cannot be
used as the complete Branch-A/Branch-B assembly rating. The exact Molex
`PS-43879-001-001` section 4.3 table rates the standard 5556 Mini-Fit Jr.
wire-to-board terminal system at **8 A per circuit** for a two-circuit
16/18-AWG assembly under its 30 C maximum temperature-rise test. It requires
application derating and states that the connector system was not designed or
tested for current sharing.

The current PiSXMe selection is two 2-position `0039300020`/`39-30-0020`
5569 headers with one 12-V contact and one return contact per branch. The
selected mating terminal, wire, crimp, length, and thermal installation are
not closed. Therefore Power Authority does **not** bind the requested
250-W/25.25-A operating envelope or dual 13-A branch limit to the current
complete input assembly.

Only two indispensable fields remain D:

1. **Continuous current:** Product/architecture authority must either approve
   a lower V100 power envelope compatible with the exact selected input
   assembly, or authorize a changed contact/harness topology and its package
   contract. The organization cannot silently convert a generic contact-page
   maximum into a complete 13-A branch rating.
2. **Peak current:** Product/architecture authority must decide whether the
   330-W historical allowance or another peak requirement is retained and
   provide the corresponding qualified input architecture and transient
   contract. No V100/SXM2 load-step waveform was found.

All other fields are A, B, or C and can be set by Librarian evidence,
engineering synthesis, and Power Authority within the selected product
boundary. Issue #2 remains narrowed to these two D fields until that decision
is made. This is a narrow authority/product blocker, not a claim that all
power engineering is externally unavailable.

## Exact current evidence and arithmetic

The exact standard-terminal application limit is 8 A per circuit for the
two-circuit 16/18-AWG case. Thus the two selected two-contact branches have a
16-A pre-derating ceiling only as a connector-table arithmetic screen; it is
not a released operating rating, because Molex requires application derating
and disallows assuming current sharing.

The existing Rev-A worksheet calculates the requested envelope as:

```text
I_V100 = 250 W / (12.0 V * 0.90) = 23.14815 A
P_LV   = (5.0 V * 3.0 A) + (3.3 V * 2.0 A) + (1.1 V * 1.0 A)
       = 22.7 W
I_LV   = 22.7 W / (12.0 V * 0.90) = 2.10185 A
I_TOTAL = 25.25000 A
```

This exceeds the exact two-circuit table screen by 9.25 A before derating.
If an internal product decision were made to accept only a 16-A pre-derating
input screen, the corresponding V100 allowance after the same low-voltage
load would be approximately:

```text
P_V100 = (16.0 A - 2.10185 A) * 12.0 V * 0.90 = 150.10 W
```

That 150.10-W value is an illustrative engineering boundary, not an adopted
PiSXMe product requirement. It demonstrates why the continuous-current row is
a product decision rather than a missing routing calculation.

The historical values compare as follows:

| Value | Same 90% worksheet input current including 2.10185 A low-voltage load | Disposition |
|---|---:|---|
| 250 W V100 allowance | 25.25 A total | Requested Rev-A envelope; not bindable to the current unqualified assembly |
| 300 W V100 maximum product fact | 29.87963 A total | Retain as NVIDIA product/stress reference; not a current Rev-A requirement |
| 330 W preliminary peak allowance | 32.65741 A total | Superseded preliminary budget; not a binding requirement |
| 28.5 A / 34.3 A preliminary input values | historical design allowances | Preserve as historical evidence; do not use to widen current copper or relax connector evidence |

## Rail-by-rail power-tree review

| Segment | Source/load basis | Calculated screen or margin | Authority status and missing confidence data |
|---|---|---|---|
| 12-V source and J5/J6 branches | Regulated, current-limited 12-V cold-plug source; two Molex branches, 15-A fuse candidates, SMBJ18A/LM74700-Q1/CSD19536KCS per branch | Exact standard 5556 application table: 8 A/circuit for the two-circuit 16/18-AWG case. A 15-A fuse is not a connector rating. At the requested equal-share 12.625 A, each branch exceeds that table value by 4.625 A (57.8%) before application derating. | The source current limit, mating terminal, wire/crimp/length, ambient, harness drop, fuse I²t, TVS energy, and branch thermal path are not closed. No current sharing is assumed. |
| Protected 12 V merge to J1/V100 | Requested 250 W V100 plus 22.7 W low-voltage load, 90% conversion worksheet | `I_TOTAL = 25.25 A`; exact two-circuit table screen is 16 A, leaving a 9.25-A shortfall before derating. Static drop is `Vdrop = I × Rpath`; `Rpath` is not measured or extracted. | `12V_PROTECTED` has only six segments/one via in the current census and Branch-B input/fused nets have zero segments/vias. Physical continuity, plane impedance, loop inductance, return path, and V100 contact contract remain open. |
| U3 `CM5_5V` | 5.0-V nominal, 3-A design load; TPSM63606 6-A output authority; 5.02-V divider calculation | 3/6 A = 50% nominal utilization; minimum effective output-capacitor requirement is 30 uF. Exact DC-bias/temperature effective capacitance and thermal rise are not measured. | Vendor control/FB network is available. Rail copper, PG/EN sequencing, load-step droop/recovery, and thermal-via/reference-layout overlay remain open. |
| U4 `BRIDGE_3V3` | 3.3-V nominal, 2-A design load; TPSM63606 6-A output authority; 3.32-V divider calculation | 2/6 A = 33.3% nominal utilization; minimum effective output-capacitor requirement is 50 uF. Exact DC-bias/temperature effective capacitance and thermal rise are not measured. | Current census has zero serialized bridge-3.3-V segments/vias. Physical route and vendor-layout return/thermal evidence remain open. |
| U5 `BRIDGE_1V1` | 1.1-V nominal, 1-A design load; TPSM63606 6-A output authority; 1.0-V minimum-family calculation with 1.1-V divider | 1/6 A = 16.7% nominal utilization. `16 × 22 uF × 0.90 = 316.8 uF` nominal screen; with ±20% tolerance, `253.44 uF`, which is 46.56 uF (15.52%) below the conservative 300-uF effective-C screen. | Current census has zero serialized bridge-1.1-V segments/vias. The exact-part DC-bias curve, thermal path, loop inductance, transient droop and vendor-layout overlay remain open. |
| `POWER_GND` return and planes | 325 pads, 47 segments, 17 vias, three zones in the retained return census; native unresolved return items remain | Counts do not produce an impedance value. Return impedance and ground bounce require extracted geometry/stackup or measurement; `Vbounce = I × Zreturn` cannot be evaluated without `Zreturn`. | Ground stitching, high-current return continuity, shared-return coupling, and endpoint/package return behavior remain open. |
| Protection, control, and shutdown | LM74700-Q1 reverse blocking/EN behavior; SMBJ18A candidate 18-V standoff/29.2-V clamp; PG/EN/SYNC and reset policy | LM74700-Q1 3.2–65-V input range exceeds the candidate TVS clamp numerically, but this is not a load-dump qualification. A transient screen requires `E = ∫V(t)I(t)dt`, source impedance, fuse I²t, and MOSFET SOA. | The selected TVS, fuse, MOSFET, UV/OV thresholds, enable/reset/brownout timing, PG pull-ups and V100 inhibit policy require coordinated system review. No hardware sequencing or clamp measurement is claimed. |

The transient model remains explicitly separate from static IR drop:
`ΔV_transient ≈ ΔI × ESR + Lloop × dI/dt + ΔV_control`. The retained
evidence does not provide the V100/SXM2 load-step amplitude or slew, harness
and package inductance, PDN impedance, capacitor ESR/ESL over bias and
temperature, or converter control-loop response at the selected operating
point. Therefore no load-step pass, ground-bounce pass, or thermal pass is
implied by the nominal current arithmetic. The missing data limits confidence;
it does not justify adding capacitors without an identified transient model.

## Field-by-field classification

| Field | Class | Binding interpretation |
|---|---|---|
| Connector/harness limits | A + C | Molex `PS-43879-001-001` exact application table gives 8 A/circuit for the standard 5556 two-circuit 16/18-AWG wire-to-board case, with required derating. Molex’s `0039300020` page gives 13 A maximum per contact, but that generic value does not qualify the mating assembly. Power Authority requires a selected, documented mating terminal/wire/crimp/length/ambient assembly before any branch current is bound. |
| Continuous current | **D** | The requested 25.25-A total cannot be established for the current exact assembly. Product authority must lower the V100 envelope or authorize changed input contacts/harness and a new package contract. |
| Peak current | **D** | No authoritative V100/SXM2 transient contract exists in the current corpus, and the selected exact assembly cannot be assumed to carry the historical 330-W allowance. Product authority must choose the peak envelope and compatible input architecture. |
| Branch imbalance | A + C | Do not assume equal sharing. Molex explicitly says this connector system was not designed or tested for current sharing. Each branch must be independently limited and monitored/fault-isolated after the D fields are resolved. |
| Shutdown behavior | A + C | LM74700-Q1 provides enable/shutdown and reverse-current blocking mechanisms. Bind branch fault, overcurrent, input UV/OV, or protection fault to V100 enable inhibit and reset hold; exact thresholds and endpoint sequencing remain `REV_A_EMPIRICAL_RISK`. |
| Surge/load-dump limits | A + B + C | LM74700-Q1 supports 3.2–65 V input and requires a suitable TVS for a declared waveform. SMBJ18A is an 18-V standoff/29.2-V clamp screening candidate. Rev-A remains a regulated current-limited 12-V product boundary with no automotive load-dump claim until a waveform and energy model are accepted. |
| Thermal limits | A + B + C | Molex’s 8-A table is based on a 30 C maximum rise; semiconductor temperature and resistance facts are retained. Power Authority can set board, harness, connector, fuse, regulator, ambient, and airflow acceptance limits, but no thermal measurement is claimed. |
| Current sharing | A + C | The Molex specification rejects an assumed current-sharing qualification. Require independent branch limiting/fault handling and a measured or calculated path-resistance model after the product decision. |
| Load-step requirements | C | Power Authority can define a carrier-level step test after the product current decision, including amplitude, slew, plateau, protected-entry voltage band, rail droop, recovery, and instrumentation. No V100 waveform is claimed. |

## Power-tree findings that remain independent of the D fields

- The current integrated PCB has zero serialized `12V_IN_B` and
  `FUSED_12V_B` copper/vias, zero `BRIDGE_1V1` and `BRIDGE_3V3` copper/vias,
  and a sparse `12V_PROTECTED` network. This is physical open evidence, not a
  connector-capacity decision.
- The current return census records `POWER_GND` with 325 pads, 47 segments,
  17 vias, and three zones while native validation still reports unresolved
  return connectivity. Static object counts do not prove impedance, ground
  bounce, or transient performance.
- The TPSM63606 design loads remain 3 A on `CM5_5V`, 2 A on `BRIDGE_3V3`, and
  1 A on `BRIDGE_1V1` against the project’s 6-A regulator authority. The
  1.1-V effective-capacitance gate remains open: 16 x 22 uF x 0.90 x 0.80 is
  253.44 uF, below the conservative 300-uF screen.
- Static IR drop, transient droop, loop inductance, return impedance, ground
  bounce, fuse I2t, harness voltage drop, and thermal rise remain validation
  requirements. Adding capacitors alone is not an analysis.

## Resume and escalation

The Power/MPA Supervisor must keep only the actual D dependency parked:

```text
Issue #2 / product-authority decision
  -> choose lower V100 envelope or changed input contact/harness topology
  -> Power Authority reissues this decision with a new version
  -> derive corridor limits
  -> isolated producer
  -> serialized integration
  -> fresh KiCad Light validation
```

Other acceptance work remains independently actionable. No CAD, library, rule,
or configuration change is authorized by this receipt.

## Sources

- Molex `PS-43879-001-001`, revision A1, section 4.3 current table and
  current-sharing warning: <https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/productspecificationpdf/438/43879/PS-43879-001-001.pdf>
- Molex `0039300020` product page, generic maximum contact value:
  <https://www.molex.com/ja-jp/products/part-detail/39300020>
- Molex `MOLEX_0039300020_AUTHORITY.md`, project part/land-pattern record.
- TI `LM74700-Q1` datasheet, revision G, and product page.
- TI `CSD19536KCS` datasheet, revision C.
- Littelfuse `0297015.U` / `178.6165.0001` authority record and SMBJ18A
  authority record.
- PiSXMe `PHASE5_POWER_CALCULATIONS.md`, `PHASE5_POWER_NETWORK_SPEC.md`,
  and the Librarian/Researcher packets under the private Library.

## Authority signature

This is a role-signed project decision: **Power Authority**, review agent
`/root/power_authority_review_envelope`. The machine-readable companion and
SHA-256 manifest are in this receipt directory. Any change requires a new
decision version; v1.0 is retained only as superseded provenance.
