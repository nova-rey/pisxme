# High-current input connector reassessment

- Package: `P24-POWER-INPUT-GEOMETRY-AUTHORITY`
- Decision: `INTERNAL_FOOTPRINT_AUTHORITY_ROUTE`
- Date: 2026-09-18
- Scope: prototype input connector architecture; no production AVL or supplier qualification claim

## Governing requirement

PiSXMe Rev A must support the signed 300 W sustained / 330 W bounded-peak V100 envelope. The source screen remains 40 A continuous and 45 A for 100 ms, with complete source-to-J1 positive-plus-return resistance and thermal closure still required.

## Architecture comparison

| Candidate | Result |
|---|---|
| One Anderson Powerpole PP15/45 `ASMPR45-1X2-RK` | Selected prototype baseline. One dedicated positive/return path avoids passive sharing. Released Anderson data gives 45 A UL / 40 A CSA-TUV PCB-to-wire screening, 10 AWG wire compatibility, and exact contact/housing families. The 45 A/100 ms behavior remains a prototype validation item; it is not claimed as a published pulse rating. |
| Multiple Molex Mini-Fit Jr GPU-style headers | Accepted comparison only. Official Molex data gives 13 A maximum/contact and 4.20 mm pitch, but application screens and the manufacturer's no-current-sharing note make two headers insufficiently bounded for the full peak without additional branches and fusing. Three or more headers increase area and branch/fault complexity. They remain a fallback architecture, not the selected baseline. |
| Samtec PowerStrip/40 | Not selected. Electrical evidence is promising, but configured footprint and harness details remain proprietary/unbound. |

## Authority route

`external:vendor-footprint-authorization` is removed as an irreducible dependency. The prototype may author a local footprint from released manufacturer dimensions. Footprint Authority must use Anderson `B02021S` revision 6, the `DS-PP1545` data sheet, the official `ASMPR45-1X2-RK` product record, and the official `pp45pcb` layout chart. The exact selected contact variant (`3-5912P1` bottom-row or `3-5913P1` top-row) must be fixed before release.

The footprint audit must record pad/hole coordinates, contact spacing, mounting-staple/accessory holes, polarity and housing orientation, board-edge and mating envelope, tolerances, and service clearance. DFM/mechanical authority must independently verify the result. The footprint is prototype-authorized only after that audit; no production supplier/AVL claim is implied.

## Remaining engineering closure

The selected connector does not by itself close Phase 24. The producer must still bind the exact 10 AWG harness, crimp/tooling, fuse/reverse/TVS/inrush protection, complete hot positive/return resistance, PCB copper/via thermal margins, and 45 A/100 ms prototype test limits. No passive sharing is credited.

## Sources

- Anderson Powerpole product record: `https://www.andersonpower.com/product/powerpole-15-45-single-row-1x2-assemblies-dc-2-wire-standard/`
- Anderson `DS-PP1545.pdf`, retrieved 2026-09-18, SHA-256 `ac39c286d44528efab30061b96df6e64e6eeafb6e154af7a03397d518f45a04f`
- Anderson `B02021S` sales outline drawing, revision 6, official product drawing referenced by the product record
- Anderson `pp45pcb-dr.pdf` / `pp45pcb-tr.pdf` layout charts, official product resources
- Molex `39301082` product record: `https://www.molex.com/en-us/products/part-detail/39301082`
