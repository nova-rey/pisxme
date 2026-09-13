# PiSXMe Branch-B power-envelope authority reassessment

Date: 2026-09-13  
Owner: Librarian (knowledge state; advisory)  
Request: reassess Hard Problem Queue Issue #2 `external-blocker` classification field by field.  
Scope: Branch-B input and protected-rail envelope for the selected Path-A PiSXMe implementation.  
Decision authority: Power Integrity Engineer synthesizes; Power Authority sets and signs the binding PiSXMe requirements. Librarian does not set numeric requirements and did not edit CAD.

## Existing Library sufficiency and acquisition

The private `Library` branch was searched first. Existing records already contain:

- `amphenol-74221101lf-product` and `amphenol-gs-12-100-rev-r`: J1/SXM2 connector contact evidence, including the 0.45 A MEG-Array contact rating and its temperature-rise test basis. This applies to J1 contact-field calculations, not to the J6/J5 input header.
- `mic2545a-ds20006921a`: MIC2545A USB/storage switch facts; it is not the Branch-B 12 V path authority.
- `subsystem-power-protection`: explicit warning that exact regulator, switch, TVS, fuse, connector, return, thermal, and inrush limits remain selected-part/fabricator questions.
- Project-derived `PHASE5_POWER_CALCULATIONS.md` and `PHASE5_POWER_NETWORK_SPEC.md` on `nova-rey/pisxme` `reva-clean` at source SHA `eab799b1f12d8b0cad8a6db31add18576eb8056a`; SHA-256 values are `82c34b6a4b2b4878f7e74c7f7873ad68ba4d10ebfa6a7c33d742fa2a632b60e6` and `9e29ef646d4af5199a9e745a0fe8d6a140144acc67540c5956b98d0579e446df`. These are internal design-basis records, not manufacturer claims.

The Library did not contain the exact Molex input-header record or a current LM74700/load-sharing packet. Those gaps were researched against manufacturer sources and indexed in `Library/provenance/sources.json` under:

`molex-0039300020-product-20260913`, `ti-lm74700-q1-ds-snosd17g`, `ti-lm74700-q1-product-20260913`, `ti-lm74700-load-sharing-sszt272`, `ti-csd19536kcs-ds-slps485c`, and `littelfuse-0297015-ato-holder-20260913`.

A bounded external researcher commission was issued for exact harness/terminal derating and any authoritative V100/SXM2 load profile. The returned evidence sack (session `d3dd71d7-b412-435d-8dbb-a12cac7174bd`, 2026-09-13) found a cached NVIDIA V100 datasheet and the project Molex authority note, but no numeric harness derating, mating-terminal curve, SXM2 rail breakdown, V100 transient waveform, or load-step profile. Its live web search was unavailable in that worker, so these are unresolved search results rather than claims that the wider public corpus is empty. The report is indexed as `researcher-power-envelope-gap-20260913`. Its result is not needed to classify the fields below because the approved Rev-A design basis permits Power Authority to set internal requirements; if later retrieval returns materially stronger evidence, Librarian will append it as a source revision and notify the authority.

No third-party PDFs, CAD, or restricted material were copied into the private Library.

## Source facts and limits

### Connector and harness

PiSXMe J6/J5 is the project-selected Molex `0039300020` / `39-30-0020` 2-position Mini-Fit Jr header. Molex's current part record gives 13.0 A maximum per contact and 600 V maximum. The contact fact is direct manufacturer evidence for the connector (source ID `molex-0039300020-product-20260913`). It does not rate an unselected mating terminal, wire gauge, crimp, harness length, or thermal installation. The exact harness is therefore a procurement/assembly input; Power Authority may set a minimum harness requirement within the already approved regulated, current-limited 12 V cold-plug product envelope.

The existing project design basis requires two mandatory branches and records a 15 A fuse per branch. The public schematic identifies J5/J6 as `0039300020`, F1/F2 as `0297015.U`/`178.6165.0001`, and Q1/Q2 as `CSD19536KCS`. These are project-derived facts, not a claim that the present PCB routes or thermally closes them.

### Protection and current sharing

TI's LM74700-Q1 product page identifies 3.2–65 V operation, load-dump compatibility, reverse-current blocking, reverse-polarity protection, and -40 to +125 C operation. Datasheet Rev G records a typical 20 mV regulated forward-drop threshold, typical -11 mV reverse-current threshold, and design considerations including input operating voltage under load dump plus nominal and maximum load current. The datasheet explicitly places the high-current path in the external MOSFET and requires customer validation of the system implementation.

TI's SSZT272 article shows two LM74700-Q1 controllers used to share load current between sources and warns that FET selection affects conduction loss and transient response. It does not establish a numeric PiSXMe branch-imbalance limit. The selected CSD19536KCS datasheet provides 100 V VDS, 2.7 mOhm maximum RDS(on) at 10 V gate drive, 150 A package-limited product data, -55 to +175 C operating range, and a 0.4 C/W theta-JC metric. These component limits do not prove board copper, connector, fuse, harness, airflow, or shared-load closure.

The Littelfuse catalog identifies `0297015` as a 15 A ATO fuse option. Fuse ampere rating alone does not close I2t, harness protection, branch transient, or load-sharing behavior.

The cached NVIDIA V100 product datasheet (December 2019, SHA-256 `ca694a4789eae7feb9ce9090f2207cbe82f5da1448922d4855e346680c59d3`) states maximum power consumption of 300 W for V100 SXM2. It does not state rail voltage, continuous/peak current, branch allocation, or load-step behavior. The 250 W/12 V/90% worksheet envelope is therefore a PiSXMe design assumption and its 25.25 A arithmetic is transparent engineering synthesis, not an NVIDIA claim.

## Field classification for Power Authority

The letters classify what kind of authority can establish the field; they are not a signed final requirement. Numeric values below are existing design-basis inputs or calculation relationships and must be reviewed by Power Authority before becoming binding.

| Field | Class | Evidence and derivation available now | What Power Authority must sign |
|---|---|---|---|
| Connector limit | A | Molex 0039300020 manufacturer record: 13.0 A maximum per contact, 600 V maximum. J1's separate Amphenol 0.45 A/contact rating is not substituted for J6/J5. | Applicable derating versus ambient, mating state, PCB copper, and selected contact/harness assembly. |
| Harness limit | C (exact assembly still open) | No selected mating terminal/wire/cable is in the Library. The internal product envelope is regulated, current-limited 12 V cold-plug with two mandatory input branches. | Minimum wire gauge/length/crimp/terminal/contact temperature-rise requirement, or a selected purchasable harness part and derating. |
| Continuous current | C with B arithmetic | Existing internal worksheet sets a 250 W V100/SXM2 design envelope at 12 V, 90% conversion, plus CM5/bridge loads, yielding 25.25 A calculated input design envelope; it explicitly labels these as `DESIGN_ENVELOPE`, not measured hardware. Two 15 A branches require at least 12.81 A/branch under the recorded sharing policy. | Accept/revise the design-envelope loads, branch current target, fuse policy, and source current limit. This is an internal Rev-A requirement within the approved product scope. |
| Peak current | C | No authoritative V100 transient waveform is in the current corpus. LM74700 and MOSFET sources provide protection/device behavior, not the V100 load profile. A conservative peak definition can be set from the internal cold-plug/PDN model and later bench-tested. | Peak magnitude, duration, slew, and whether peak is branch-local or shared; specify test/simulation evidence required. |
| Branch imbalance | C with B method | TI load-sharing precedent supports the topology. Branch currents can be derived from measured/estimated path resistance and controller/FET forward-drop behavior; no TI numeric PiSXMe imbalance limit exists. | Maximum continuous and transient A/B imbalance, allowed loss of one branch, and shutdown policy. |
| Shutdown behavior | A for component mechanisms; C for system policy | LM74700 documents enable/shutdown and reverse-current blocking; the project schematic has separate `12V_IN_B`, `FUSED_12V_B`, `12V_PROTECTED`, and `GATE_B` nets. System under/overvoltage, fuse-open, branch-loss, and GPU disable policy are not vendor-specified. | Fault thresholds, latch/retry behavior, branch-loss response, and whether unsupported single-branch operation is enforced. |
| Surge/load-dump | A for controller capability; C for product requirement | TI identifies LM74700 load-dump compatibility and 65 V input capability, but the Rev-A project basis is a regulated current-limited 12 V bench supply, not an automotive electrical environment. The source/TVS waveform and clamp policy are therefore product-level requirements. | Declare supported input transient class (or explicitly bench-only/no automotive load-dump claim), TVS standoff/clamp, source limit, and MOSFET SOA evidence. |
| Thermal limits | A/B for parts; C for product environment and board | Amphenol J1 and Molex J5/J6 operating/contact limits, LM74700 -40..125 C, and CSD19536KCS -55..175 C/thermal metrics are available. Copper/contact-field temperature, fuse holder, harness, airflow, cooler and board thermal rise require calculation against the selected assembly. | Ambient/airflow class, allowable contact/PCB/component temperature rise, copper and via thermal criteria, and accepted analysis method/margins. |
| Current sharing | A for topology precedent; B/C for numeric requirement | TI SSZT272 supports two LM74700-Q1 ideal-diode controllers for shared sources. Sharing can be calculated from branch resistance and forward-drop mismatch, but the article gives no PiSXMe tolerance. | Sharing model, minimum/maximum branch fraction, path-resistance measurement/assumption, and evidence required before closure. |
| Load-step requirement | C with B calculation | No V100/SXM2 public load-step waveform was found in the existing corpus. The internal PDN model can calculate ΔV from the signed step, slew, ESR/ESL, capacitance, and path impedance once Power Authority selects the step. | Step amplitude, slew, duration/repetition, allowable voltage deviation, source impedance, simulation/bench method, and acceptance margin. |

## Result of reassessment

No indispensable field is presently Class D. The exact harness part and V100 transient waveform are evidence gaps, but they do not require user invention under the approved Rev-A product boundary: harness minimums and electrical stress/load-step requirements are Class C internal system requirements that Power Authority is empowered to set, while component and connector limits supply Class A inputs and the current design worksheet supplies transparent Class B arithmetic.

The existing Issue #2 `external-blocker` classification is therefore unsupported by this field-by-field review. The appropriate next action is:

1. Power Integrity Engineer reviews the source packet and calculations.
2. Power Authority signs a versioned internal Branch-B envelope table, marking each field A/B/C and preserving `REV_A_EMPIRICAL_RISK` for unknown V100 behavior and unmeasured hardware.
3. The Supervisor removes `external-blocker` from Issue #2/campaign state and returns the power/corridor package to READY.
4. The normal MPA → isolated producer → serialized integration → targeted and fresh Light validation sequence resumes.

This brief does not claim that the envelope is already signed, that the PCB is routed, or that hardware passed.
