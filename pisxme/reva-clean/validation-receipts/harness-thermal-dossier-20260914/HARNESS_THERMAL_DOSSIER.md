# P24-HARNESS-THERMAL-DOSSIER

Status: `EVIDENCE_PACKET_READY_WITH_PRODUCT_ASSEMBLY_GAPS`

Package: `P24-HARNESS-THERMAL-DOSSIER`
Scope: six independent 16-AWG source loops for the conditionally signed V2.2
power envelope; Molex 5569 header installation and connector/copper thermal
qualification.
Prepared: 2026-09-14
CAD changed: no
Fabricated hardware measured: no

## Library-first result

The private Library was searched first. It already contains the Molex 5556/
5557/5569 family brief, exact selected header authority, selected terminal
class, and the V2.2 connector qualification packet. Those records establish
family identity and manufacturer limits, but they do not contain the selected
PiSXMe wire MPN, six one-way cable lengths, complete hot loop budgets, local
ambient/airflow class, six-header installation, or temperature results.

A bounded public-source acquisition filled the reusable evidence gap. It does
not turn product-specific assembly assumptions into a qualification. No public
PDF, CAD file, or restricted reference material was copied into the public
repository or private Library.

## Indexed evidence

### E1 — Molex PS-5556-001-001, current connector system specification

- Publisher: Molex
- URL: <https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/productspecificationpdf/555/5556/PS-5556-001-001.pdf?inline=>
- Revision/date observed: PS-5556-001, current browser extraction dated 2026-06-22, 23 pages; retrieved 2026-09-14.
- Evidence: Tier 1, primary manufacturer specification.
- Local retention/hash: none; direct NYX byte retrieval was not retained.
- Applicable facts: single-wire 16-AWG stranded copper, maximum insulation diameter 3.15 mm; 16-AWG phosphor-bronze rating 8 A for 2–3 circuits, 7 A for 4–6, 6 A for 7–10, 5 A for 12–24; rating based on Molex test method at 30 °C maximum rise over ambient.
- Limitation: Molex states the rating is a guideline and requires derating for circuit size, ambient temperature, PCB copper/trace size, adjacent heating, wire size/stranding/coating/length, and crimp quality. It is not a six-loop PiSXMe qualification.

### E2 — Molex PS-5556-004-001 Rev B1, reflow-capable header specification

- Publisher: Molex
- URL: <https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/productspecificationpdf/555/5556/PS-5556-004-001.pdf?inline=>
- Revision/date: B1, ECM 851282, 2026-03-24, 17 pages; retrieved 2026-09-14.
- Evidence: Tier 1, primary manufacturer specification.
- Local retention/hash: unavailable; no substitute hash claimed.
- Applicable facts: 16-AWG stranded copper applicability; phosphor-bronze 8 A at 2–3 circuits; +30 °C maximum terminal rise basis; phosphor-bronze operating range −40 to +105 °C; current derating requires ambient, PCB copper, adjacent heating, wire length and crimp quality.
- Limitation: no PiSXMe ambient/airflow or six-header installation model.

### E3 — Molex 55560010-TS-000 dual-wire termination test summary

- Publisher: Molex
- URL: <https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/testsummarypdf/555/5556/55560010-TS-000.pdf>
- Revision/date: ECR 625162, 2019-11-01, 6 pages; retrieved 2026-09-14.
- Evidence: Tier 1, primary manufacturer test summary, but the tested wire combinations are 18–22 AWG and therefore not a 16-AWG qualification.
- Tested family: 5569 header assembly, 39012020 5557 housing, 39000079 terminal among samples.
- Contact result: initial contact resistance requirement 10 mΩ maximum; the listed 39000079 sample had mean 5.651 mΩ and maximum 5.791 mΩ in that test configuration.
- Limitation: the header part tested was 39281023 rather than the selected 0039300020, and the wire gauge/assembly is not the proposed six-loop harness. Reuse only as family/test-method evidence.

### E4 — Molex 5569 series and selected 0039300020 authority

- Series URL: <https://www.molex.com/en-us/products/series-chart/5569>
- Selected part authority: project record `authority-inventory/primary-docs/power/MOLEX_0039300020_AUTHORITY.md`; manufacturer drawing reference `039300020_sd.pdf` / `55690002-SD`.
- Evidence: Tier 1 manufacturer family data plus project package authority.
- Applicable facts: selected 0039300020 / 39-30-0020 is the 5569 two-position, dual-row, right-angle, through-hole header; 4.20 mm pitch; recommended PCB thickness 1.78 mm; family operating range −40 to +105 °C; exact hole and retention geometry is already closed in the project authority record.
- Additional current page: <https://www.molex.com/en-us/products/part-detail/39300020> reports 13.0 A maximum per contact, but that is a contact catalog ceiling and does not replace the 8 A application/derating screen for the selected 5556/5557 assembly.

### E5 — Molex 5557 series chart / 39012020 housing

- URL: <https://www.molex.com/en-us/products/series-chart/5557>
- Evidence: Tier 1 manufacturer product authority, retrieved 2026-09-14.
- Applicable facts: 39012020 is a two-circuit, dual-row 5557 receptacle housing; 4.20 mm pitch; polarized/locking family; operating range −40 to +105 °C.
- Limitation: housing rating is not a product ambient guarantee and does not qualify the harness routing or heat accumulation.

### E6 — Belden 39116 16-AWG wire reference

- Publisher: Belden
- URL: <https://catalog.belden.com/index.cfm?event=pd&p=PF_39116&rs=>
- Evidence: Tier 1 manufacturer product record for a possible wire class, not a PiSXMe selection.
- Applicable facts: 26x30 tinned copper, 16 AWG, nominal conductor DCR 4.0 Ω/1000 ft, 600 V RMS, 105 °C UL rating, −40 to +105 °C dry operating range, 2.1 mm nominal insulation diameter.
- Limitation: no selected cable MPN has been approved for PiSXMe; the free-air 26 A field is not a harness or connector rating and is not used as one.

### E7 — Southwire P50002-1A 16-AWG two-conductor reference

- Publisher: Southwire
- URL: <https://www.southwire.com/wire-cable/hvac/cu-300v-hvac-wire-shielded-thermostat-plenum-rated/p/P50002-1A>
- Evidence: Tier 1 manufacturer product record, retained as a resistance reference only.
- Applicable facts: 19-strand 16-AWG copper, two conductors, DC resistance 4.181 Ω/1000 ft at 25 °C; approximate 0.185 in overall diameter; product is a 300 V plenum-rated HVAC cable.
- Limitation: it is not selected for PiSXMe and its application/jacket construction must not be silently substituted for the final harness.

### E8 — NIST Copper Wire Tables

- Publisher: National Institute of Standards and Technology
- URL: <https://nvlpubs.nist.gov/nistpubs/Legacy/hb/nbshandbook100.pdf>
- Evidence: Tier 1 government reference.
- Applicable fact: standard copper temperature coefficient is 0.00393 per °C at 20 °C over the cited 10–100 °C range.
- Use: temperature correction of a manufacturer-supplied wire resistance value. This is a calculation method, not a cable qualification.

## Bounded resistance screen

For the Southwire reference value only, using the NIST linear temperature
coefficient:

`R(T) = R25 * [1 + 0.00393*(T−20)] / [1 + 0.00393*(25−20)]`

The resulting conductor resistance is 4.181 Ω/1000 ft at 25 °C,
4.906 Ω/1000 ft at 70 °C, 5.148 Ω/1000 ft at 85 °C, and 5.470 Ω/1000 ft at
105 °C. If the V2.2 `R_harness_loop <= 20 mΩ` limit refers to copper wire only,
then the maximum one-way wire length before any terminal/crimp allowance is:

| Conductor temperature | Maximum one-way length for 20 mΩ copper loop | Basis |
|---:|---:|---|
| 25 °C | 2.392 ft / 0.729 m | 2 × length × 4.181 Ω/kft |
| 70 °C | 2.038 ft / 0.621 m | 2 × length × 4.906 Ω/kft |
| 85 °C | 1.943 ft / 0.592 m | 2 × length × 5.148 Ω/kft |
| 105 °C | 1.828 ft / 0.557 m | 2 × length × 5.470 Ω/kft |

These are screening calculations for the cited reference cable. They are not
six measured values and exclude terminal contact, crimp, fuse, connector,
board and any splice resistance. The V2.2 packet separately budgets a 20 mΩ
connector loop; the authority must explicitly state whether the 20 mΩ harness
limit is wire-only or a complete external loop. If complete-loop scope is
intended, terminal/crimp/contact resistance must be subtracted from the 20 mΩ
budget before any cable length is accepted.

At 6.4 A, a 20 mΩ loop dissipates 0.819 W; at 5.8 A it dissipates 0.673 W.
Those are calculated screens only and must be allocated between the wire,
crimps, contacts and any approved splices in the thermal model.

## Thermal and installation interpretation

The manufacturer evidence establishes a 30 °C terminal-rise test basis and a
−40 to +105 °C phosphor-bronze/header/housing operating range. It does not
establish PiSXMe's ambient temperature, forced-air velocity, neighboring heat
sources, six-header spacing, local PCB copper temperature rise, solder joint
margin, or limiter/fuse thermal interaction. The exact six-loop installation
therefore remains an internal Package/Power/MPA qualification task.

The qualification must declare, for each loop A–F:

1. exact wire MPN, insulation and temperature rating;
2. one-way length and routing/ bundling condition;
3. hot copper resistance and complete resistance budget, including two
   connector contacts, crimp, fuse/limiter and any splice according to the
   signed V2.2 scope;
4. PiSXMe ambient and airflow class, adjacent heat sources and allowable
   component/contact/PCB temperatures;
5. six 0039300020 header positions/orientations, solder access, retention and
   protected copper corridor from MPA;
6. calculated or measured temperatures at 5.8 A sustained and 6.4 A bounded
   branch current, with margin below the applicable part and insulation limits;
7. a six-row hot-loop evidence table and acceptance signoff.

No external source found in this bounded pass supplies those PiSXMe-specific
installation values. This is a product-specific internal authority gap, not
evidence that the connector family is unavailable or that the product is
externally blocked.

## Disposition

Reusable evidence is indexed and ready for Package/Power Authority review.
The package remains `WAITING_ON package:exact-harness-and-installation-qualification`.
It is not a CAD authorization and does not close the V2.2 power envelope.

Resume when the exact six-loop harness schedule and installation/thermal
authority packet are signed. Do not invent cable lengths, airflow, or
fabricated temperature measurements.
