# High-current GPU-style input assembly evidence

Request scope: Root Foreman / current prototype power-bus correction. Retrieved 2026-09-17. This is a Librarian evidence packet only; it does not select a PiSXMe connector, authorize CAD, or sign the power envelope.

## Existing Library result

The existing PiSXMe input selection is Molex `0039300020` / `39-30-0020`, a 2-position Mini-Fit Jr header. The manufacturer record gives **13 A maximum per contact**. The indexed Molex 5556/5569 specification gives an application-dependent **8 A/circuit** value for 16-AWG phosphor-bronze terminals in 2–3 circuits, on a 30 °C terminal-rise basis, with explicit application derating. This assembly cannot support the corrected 40 A continuous / 45 A 100 ms source contract as one positive/return pair. It is retained as historical evidence, not a candidate for the corrected source path.

## Candidate A — Anderson Powerpole PP15/45, discrete positive and return poles

Manufacturer evidence:

- Anderson `ASMPR45-1X2-RK` is a one-piece standard 1x2 DC two-wire assembly with red/black PP15/45 housings and 45-A right-angle PCB contacts. The manufacturer's product page lists 10-AWG-compatible wire, up to 45/55 A family capability, −20 to +105 °C housing range, 10,000 mating cycles, and hot-plug capability.
- The underlying parts are Anderson `1327` red standard housing and `1327G6` black standard housing, paired with `3-5912P1` 45-A right-angle bottom PCB contacts (or `3-5913P1` top-row contacts as geometry requires). The corresponding 10-AWG low-force wire contact is `261G2` (bulk `261G2-LPBK`); `269G3` is the high-detent alternative. Anderson's catalog lists `1309G14` as the crimp tool for the 10–14-AWG 200G/1830G contact family; the exact tool/contact pairing must be confirmed against the selected contact before procurement.
- Anderson PP15/45 DS-PP1545 manufacturer data states for a fully loaded connector and 105 °C-rated cable at 25 °C ambient: single-pole wire-to-wire 10-AWG **55 A UL / 40 A CSA-TUV**, single-pole 45-A PCB-to-wire **45 A UL / 40 A CSA**, average mated resistance **0.525 mΩ** for 45-A wire contact with 5/8 inch of 10 AWG and **0.500 mΩ** for 45-A PCB contact-to-contact. It states ratings are per position, with all positions loaded, and that application derating is required. The 45-A PCB trace recommendation is 10-AWG cross-section; the connector uses plated through-hole PCB contacts. The data sheet's 45-A UL hot-plug rating is based on two housings blocked together at 72 V DC, so it is not a PiSXMe hot-plug waiver.
- The same data sheet records a UL ground short-time test of 750 A for 4 s using 10-AWG wire and 470 A for 4 s using 12-AWG wire. This is grounding/test evidence, not a complete PiSXMe 45-A fault or surge qualification.

**Bounded interpretation:** A 1x2 PP15/45 assembly supplies one positive and one return pole. Under the conservative CSA/TUV values, each pole is exactly 40 A; the 45-A/100-ms requirement needs a documented short-time/thermal calculation and cannot be claimed from the continuous rating alone. Under UL, the 45-A pole rating has direct nominal headroom. Use 10-AWG 105 °C wire, the manufacturer-recommended crimp process/tool, and a conservative external derating for ambient, enclosure, adjacent heating, harness length, and PCB copper. The two poles must be treated as separate positive/return conductors; no current-sharing claim is needed.

Screening resistance/thermal arithmetic using the manufacturer's typical/maximum contact values:

| Case | Complete positive+return contact resistance | Connector contact loss |
|---|---:|---:|
| 40 A continuous, 0.525 mΩ/pole | 1.050 mΩ | 1.68 W |
| 45 A, 100 ms, 0.525 mΩ/pole | 1.050 mΩ | 2.13 W instantaneous, 0.213 J for 100 ms |
| 40 A continuous, 0.500 mΩ/pole PCB-contact screen | 1.000 mΩ | 1.60 W |

These are screening calculations from manufacturer contact figures, not measurements. If PiSXMe retains a 10 mΩ complete source-to-J1 positive+return budget, the 1.05 mΩ contact-pair screen leaves 8.95 mΩ for both wires, crimps, board entry, protection and distribution. The current branch must be accepted only after Power/Package Authority signs wire length, crimp, connector installation, copper/via cross-section, thermal rise and source-to-J1 resistance allocations. At 40 A the total 10 mΩ budget dissipates 16 W; at 45 A it dissipates 20.25 W, so the budget must distinguish continuous from 100-ms pulse energy and identify where heat is allowed.

## Candidate B — Amphenol FCI M-CRPS +54V family

Amphenol `10170331-360001` is an active 6-contact vertical M-CRPS boardside connector. The manufacturer product record states **40 A/contact**, 8–10 AWG wire, 0.6 mΩ maximum power contact resistance, −40 to +105 °C, 600 V AC/DC, 100 mating cycles, and high-temperature thermoplastic construction. The M-CRPS family page states 8–12 AWG cable options, 40 A/contact, keyed/latching housing and two mate-last/break-first sense contacts; the family is designed around OCP M-CRPS +54 V but the page describes retrofit use for 12-V systems.

This is a strong high-current reference and a possible compact board-entry family, but the retrieved public record does not establish a complete PiSXMe 12-V cable-side mating MPN, exact pin assignment for two positive/two return circuits, or the contact derating/thermal arrangement for the intended 12-V prototype. It remains a candidate requiring Package Authority confirmation and an exact mating assembly before use.

For two positive and two return poles at 40 A, the published 0.6 mΩ maximum per mated power contact gives a four-contact connector-contact screen of 2.4 mΩ and 3.84 W at 40 A (using one contact resistance per current pole). At 45 A for 100 ms, the same contact screen gives 4.86 W instantaneous and 0.486 J for 100 ms. The calculation is a screening model only; M-CRPS pin parallelization, thermal arrangement and cable assembly remain unresolved.

## Candidate C — Samtec PowerStrip/40 PET/PES/PESS

Samtec’s exact product family is a stronger board-entry/harness candidate for this prototype than the existing Mini-Fit Jr. pair:

- `PET-08-02-T-VT-LC` is an 8-position, 6.35-mm-pitch vertical locking-clip terminal. The manufacturer page lists 58.7 A max, 450 VAC / 636 VDC max, and a high-power dual-blade contact. `PET-08-02-L-VT-LC` is the 10-µin gold/tin alternative.
- Its mating board socket is `PES-08-02-T-VT` or `PES-08-02-L-VT`; Samtec lists the same 58.7-A product claim and a rugged screw-down option. The exact board/socket orientation and footprint must be checked against PiSXMe mechanics.
- The cable family is `PESS`, with 2–8 power positions, polarized latching, and 10/12-AWG cable choices. One example configurable MPN is `PESS-08-10-L-40.00-SR`; the exact cable length, plating and end configuration remain Package Authority inputs.
- Samtec product specification `pesx-petx.pdf`, Rev F (2024-12-04), gives a 50-A power-contact rating with one pin powered per row, −55 to +125 °C operation, 450 VAC, and 5-mΩ maximum LLCR delta in the qualification tests. The manufacturer power report `TC0919-2456 Rev 2` is more useful for derating: after 20% derating and at 30 °C rise it reports 58.7 A/contact for one powered contact, 48.5 A/contact for two, 41.1 A/contact for three, 38.0 A/contact for four, and 29.4 A/contact with all eight powered.

**Bounded interpretation:** If PiSXMe uses exactly one positive and one return position, the report’s two-powered-contact case gives 48.5 A/contact at its 30 °C rise/20% derating basis, above the 40-A continuous floor and leaving a 45-A/100-ms pulse to be checked by the separate pulse/thermal calculation. If two positive and two return positions are energized, the four-contact case is 38.0 A/contact and fails the 40-A continuous screen. Therefore do not assign a four-contact parallel arrangement without a new authority calculation; a two-contact positive/return assignment is the only immediately supported screen. The 8-position family also introduces a large 6.35-mm footprint, 0.25-mm mating alignment limit, mechanical height, and exact cable-side configuration gates.

The report’s 0.17–0.27 mΩ all-contact test resistance range is useful precedent, but the Rev F specification only guarantees a 5-mΩ LLCR delta under the cited tests. Use the published test result for analysis context, not as a guaranteed PiSXMe resistance allocation. At a 5-mΩ complete positive/return connector screen, 40 A dissipates 8 W and a 45-A, 100-ms pulse deposits 0.81 J; this is a screening bound and requires authority-selected contact resistance and thermal margin.

## Recommendation to authority

Use Candidate C as the first Package/Power Authority review candidate because Samtec supplies a manufacturer power-rating test report, a board terminal/socket family, and a 10-AWG cable family. Its 2-position energized case has a published 48.5-A/contact 30 °C-rise/20%-derated result, while using four energized contacts falls below 40 A/contact. Candidate A remains a viable exact two-wire fallback with a 40-A CSA/TUV floor and 45-A UL nominal rating. Candidate B remains a compact alternative requiring an exact mating cable and 12-V applicability review. No candidate is automatically selected.

Neither candidate proves PiSXMe system closure. Power Authority must bind the exact assembly, ratings/derating, protection coordination, harness length and wire MPN, positive/return resistance budget, PCB entry geometry, and thermal acceptance method. No fabricated-hardware measurements or production qualification are claimed.

## Sources and limitations

- Anderson Power, `DS-PP1545.pdf`, PP15/45 & Powerpole Pak specifications, retrieved 2026-09-17: https://www.andersonpower.com/content/dam/ideal-anderson-power-dotcom/product-assets/default/data-sheets/DS-PP1545.pdf
- Anderson Power `ASMPR45-1X2-RK` product record: https://www.andersonpower.com/product/powerpole-15-45-single-row-1x2-assemblies-dc-2-wire-standard/
- Anderson Power `1327` housing record: https://www.andersonpower.com/product/powerpole-connector-housing-red/
- Anderson Power PP15/45 product series and 10-AWG contact/tool records: https://www.andersonpower.com/product-lines/powerpole/
- Amphenol FCI `10170331-360001` product record: https://www.amphenol-cs.com/product/10170331360001.html
- Amphenol FCI M-CRPS family record: https://www.amphenol-cs.com/product-series/m-crps-54v-connectors-cable-assemblies.html
- Samtec PET terminal: https://www.samtec.com/products/pet-08-02-t-vt-lc
- Samtec PES socket: https://www.samtec.com/products/pes-08-02-t-vt
- Samtec PESS cable family: https://www.samtec.com/products/pess
- Samtec PES/PET specification Rev F: https://suddendocs.samtec.com/productspecs/pesx-petx.pdf
- Samtec PES/PET power test report TC0919-2456 Rev 2: https://suddendocs.samtec.com/testreports/tc0919--2456_report_rev_2_pwr.pdf

Only URLs and extracted factual notes are retained. Vendor PDFs, drawings, CAD, and images were not copied into the private or public project repositories; exact local byte hashes are therefore unavailable.
