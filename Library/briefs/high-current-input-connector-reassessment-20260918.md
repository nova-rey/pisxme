# High-current input connector reassessment — released-interface basis

Requesting package: `P24-PROTOTYPE-POWER-BUS-INTEGRATION-VALIDATION` / high-current input connector blocker reassessment. Retrieved 2026-09-18. Librarian evidence only; Product/Power and Footprint Authorities select and authorize the architecture.

## Existing Library result

The current J5/J6 choice is Molex `0039300020` / `39-30-0020`, a 2-circuit Mini-Fit Jr. 5569 right-angle header. Existing manufacturer evidence gives 13 A maximum per contact, while Molex `PS-5556-004-001` Rev B1 gives application-dependent 8 A/circuit for 16-AWG phosphor-bronze terminals in 2–3 loaded circuits at a 30 °C terminal-rise basis. It is not a 40 A continuous / 45 A peak single positive/return source. This is a connector-selection problem, not proof that a manufacturer-defined input interface is unavailable.

## Candidate 1 — one high-current connector system

**Samtec PowerStrip/40:** board terminal `PET-08-02-T-VT-LC` mated to `PES-08-02-T-VT` and a configured `PESS` cable. Samtec's released product record identifies a 0.250 in (6.35 mm) pitch, two-to-eight power positions, dual-blade contact and 58.7 A maximum product rating. Samtec's released power report `TC0919-PES/PET-2456`, Rev 2, tests the PES/PET system and reports, after 20% derating at 30 °C rise, 48.5 A/contact with two adjacent energized contacts; its all-eight-contact case is 29.4 A/contact. The two-energized-contact case is the relevant one-positive/one-return screening configuration, but it still needs Product/Power Authority to bind the 45 A/100 ms pulse, cable MPN, ambient, board copper, and installation margin.

Samtec publishes a product print and footprint for the configured PET part on the manufacturer page. The source packet retained metadata and extracted values only; the exact configured footprint bytes were not copied. Package Authority must retrieve the exact PET/PES print for the selected configuration before CAD. This is an obtainable manufacturer-interface path, not an irreducible vendor-authorization dependency.

**Anderson PP15/45:** `ASMPR45-1X2-RK` / `3-5912P1` and `3-5913P1` right-angle PCB contacts with 10-AWG harness contacts. Anderson's `DS-PP1545` gives 45 A UL / 40 A CSA-TUV PCB-to-wire, 0.500 mOhm average PCB-contact pair resistance and a 2.3–3.8 mm PCB thickness range. Released `B02021S` Rev 6 supplies the connector layout envelope and nominal contact/accessory-hole relationships. It does not specify finished contact-tail drill/slot, pad/annulus or mask dimensions. Anderson is therefore a valid electrical/mechanical candidate but not a fully manufacturer-defined exact PCB land pattern on the retained record; it requires an explicit internal prototype-footprint assumption or further manufacturer package data.

## Candidate 2 — multiple conventional GPU/Tesla-style connectors

The private architecture-sanity record confirms the Benchoff SXM2-to-PCIe carrier uses two 2x3 PCIe power headers, and other public V100 carrier families expose dual or three 8-pin inputs. These are public implementation precedents only; no CAD or protected expression is imported.

A manufacturer-defined prototype candidate is a **three-connector Molex Mini-Fit Jr. 5569 six-circuit system**, for example three `39-30-1060` (or tray/gold variant `39-30-1061`) right-angle headers mated to six-circuit 5557 housings such as `39012020/39012060/39012065` with the selected 5556 terminals. The released Molex sales drawing `55690002-SD` (PDF `039300040_sd.pdf`, title-block Rev D, released 2018-02-22) identifies the 6-circuit part numbers, 4.20 mm row/column pitch, 1.78 mm maximum PCB thickness for the recommended hole layout, mounting-peg option and the same hole layout for circuit sizes 6–24. The drawing explicitly says the parts are **not designed for current sharing**, so each connector must be an independently protected branch; contact-parallelization inside one connector cannot be claimed. Molex's current PS-5556 table gives 7 A/circuit for 16-AWG phosphor-bronze terminals in 4–6 loaded circuits at a 30 °C rise. Three six-circuit connectors therefore screen at 3 connectors × 3 positive contacts × 7 A = 63 A positive (and the same return capacity), above the 40 A continuous / 45 A peak source contract, subject to branch balance, fusing, harness and PCB thermal analysis. This is a screening calculation, not an authority decision.

A **six-connector two-circuit system** using the already-authorized `0039300020` footprint is another released-interface fallback: six independent positive/return pairs at 8 A/circuit screen to 48 A aggregate. It is larger and more harness-heavy, and it still needs explicit branch balance and no-contact-sharing treatment. It demonstrates that the exact-footprint blocker is not irreducible even without a new connector family.

The two-header Benchoff pattern alone should not be promoted to a 40 A closure: the retained Molex conservative table yields 21 A per fully loaded six-circuit header, or 42 A for two, leaving no 45 A pulse and installation margin. It remains precedent, not a PiSXMe rating.

## Source and package status

- Molex `55690002-SD`, PDF `039300040_sd.pdf`, manufacturer sales drawing; official URL: <https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/salesdrawingpdf/556/5569/039300040_sd.pdf>. It identifies `39-30-1060/1061`, the 4.20 mm 5569 family geometry, and the recommended hole-layout constraints. No vendor PDF is retained locally.
- Molex `PS-5556-004-001`, Rev B1, manufacturer Mini-Fit Jr. specification; existing Library brief `molex-5556-ps004-v21-20260913.md` and source IDs `molex-5556-ps004-v21-20260913`, `molex-5569-series-20260914`, `molex-5557-series-39012020-20260914`.
- Samtec `PET-08-02-T-VT-LC`, official product page and published print/footprint links: <https://www.samtec.com/products/pet-08-02-t-vt-lc>.
- Samtec `TC0919-PES/PET-2456`, Rev 2 power report: <https://suddendocs.samtec.com/testreports/tc0919--2456_report_rev_2_pwr.pdf>. The report is proprietary; only citation and extracted facts are retained.
- Anderson PP15/45 source IDs and hashes are indexed in `anderson-pp45-contact-land-pattern-20260918`.
- Public carrier precedent is indexed in `sxm2-carrier-architecture-sanity-20260917`.

## Librarian disposition

The source set does **not** justify retaining `external:vendor-footprint-authorization` as a campaign-wide irreducible blocker. At least one practical route exists using a released manufacturer-defined Molex 5569 six-circuit interface (and an even more conservative six-unit 2-circuit fallback), while Samtec offers a compact single-connector route with published print/footprint resources. The exact selected connector, branch topology, fuses, harness, derating and thermal acceptance remain Product/Power/Package Authority decisions. No CAD was changed and no connector was selected by Librarian.
