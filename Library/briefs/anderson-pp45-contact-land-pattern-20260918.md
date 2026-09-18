# Anderson PP15/45 PCB-contact evidence — bounded land-pattern reassessment

Requesting package: `P24-POWER-INPUT-ANDERSON-CONTACT-EVIDENCE`  
Retrieved: 2026-09-18  
Role: Librarian evidence packet; no connector selection or CAD authorization.

## Existing Library search

The private Library record `high-current-gpu-input-assembly-20260917` already
covers PP15/45 system ratings, the `ASMPR45-1X2-RK` assembly identity, and the
3-5912P1/3-5913P1 contact family. It did not contain the released contact-land
records or a retained dimensional audit. The earlier isolated Anderson audit
(`anderson-prototype-footprint-producer`, commit `43ea38cb`) correctly parked
this question after finding that the available records did not specify the
finished contact land.

## Retrieved first-party records

| Source ID | Released record | Useful facts | Local retrieval hash |
|---|---|---|---|
| `anderson-3-5912p1-product-20260918` | [Anderson 3-5912P1 product page](https://www.andersonpower.com/product/powerpole-15-45-45a-right-angle-bottom-pcb-contacts-tin-plated/) | Exact SKU; 45 A right-angle bottom-row tin PCB contact; 10,000 mating cycles; -20 to 105 C; 20–10 AWG family; up to 45/55 A page range; manufacturer says right-angle contacts are for wire-contact mating and must not mix with 25 A PCB contacts. | HTML retrieval; no byte hash retained |
| `anderson-3-5913p1-product-20260918` | [Anderson 3-5913P1 product page](https://www.andersonpower.com/product/powerpole-15-45-45a-right-angle-top-pcb-contacts-tin-plated/) | Exact SKU; same rating/environment and top-row identity. | HTML retrieval; no byte hash retained |
| `anderson-b02021s-rev6-20260918` | [B02021S High Power PCB Series 45 Amp Powerpole sales outline](https://p1.aprimocdn.net/idealindustries/03480861-2607-4e12-aed3-b3f00073a52e/ap-web_product-assets_default_drawings_b02021s_Original%20file.pdf) | Rev 6; two sheets; sheet 2 is the manufacturer sample PCB layout. It shows 7.9 mm typical contact spacing, 1.27 mm typical row spacing, 1.20 mm diameter staple-accessory holes, 4.57 mm diameter wing-accessory screw holes, 5.23/6.86/7.32/14.78/18.24/24.31/26.16 mm layout references, and the 1336G1/1337G1 bottom/top-row identities. It says accessory openings may be expanded as necessary per application. | `7a32189a34ff2feea3bf173c788f3dd63229ea98dfefed8009b1bc5738e8cd2c` |
| `anderson-ds-pp1545-current-20260918` | [DS-PP1545 PP15/45 datasheet](https://p1.aprimocdn.net/idealindustries/5d665ad6-38c3-4088-98b6-b3f0007370ef/ap-web_product-assets_default_data-sheets_DS-PP1545_Original%20file.pdf) | Current 13-page manufacturer PDF; 45 A PCB-to-wire 45 A UL / 40 A CSA-TUV screen, 0.500 mOhm PCB-contact-to-contact average, plated-through-hole mounting, 2.3–3.8 mm PCB thickness, 10-AWG-equivalent recommended copper for 45 A PCB traces, and references B02021S for the contact geometry. PDF metadata creation 2026-08-05; no printed revision field located. | `ac39c286d44528efab30061b96df6e64e6eeafb6e154af7a03397d518f45a04f` |
| `anderson-1s6479-rev02-20260918` | [1S6479 Rev 02 assembly instructions](https://p1.aprimocdn.net/idealindustries/ca37b04f-0364-452e-83ac-b3f00073ac16/ap-web_product-assets_default_instructions_1S6479_Original%20file.pdf) | Manufacturer instruction explicitly says to insert all solder tails into PCB plated through holes and identifies B02021S (power) and B02060S1 (ground) as the PCB-footprint references. It does not add tail drill, slot, pad, annulus, or mask dimensions. | `a9a5b77fcb5cb8df9dca700c770cb24cf9c2ef5edfab14dd47dc3151046a64e7` |
| `anderson-pp45pcb-dr-20260918` | [PP45 PCB derating chart](https://p1.aprimocdn.net/idealindustries/8d9e9f19-d1b7-4eb1-81af-b3f000736f30/ap-web_product-assets_default_charts_pp45pcb-dr_Original%20file.pdf) | Current-vs-ambient chart only; it is not a land-pattern drawing and cannot close footprint geometry. | `c4e38cf4e3fdd0be7a67604890bd1d112b77f18941075ef52f11c95f55947e9a` |
| `anderson-111038s2-tool-rev0-20260918` | [111038S2 insertion/extraction tool drawing](https://p1.aprimocdn.net/idealindustries/6fdb6c7f-1678-4026-8885-b3f000737d86/ap-web_product-assets_default_drawings_111038s2_Original%20file.pdf) | Rev 0, dated 2001; dimensions the 111038G2 tool only. It is not a 3-5912P1 or 3-5913P1 contact/land drawing. | `d7a7c2aca4b0840fce8a6e6aace23ace287e96002f208b61fe36bdcc32eb3af6` |
| `anderson-contact-drawing-faq-20260918` | [Anderson FAQ on 3D drawings](https://www.andersonpower.com/resources/faq/) | Manufacturer states that contact 3D drawings are not provided; product 3D files require account access. This corroborates why no contact-tail model or hidden land pattern was treated as released evidence. | HTML retrieval; no byte hash retained |

The B02021S drawing is the controlling released mechanical-layout record found
for the power contact. Its title block is `B02021S`, Rev 6, with Rev 6 change
`ECRN-15763`, dated 2015-01-15; sheet 2 was added in Rev 3 and the layout
 tolerances were added in Rev 4. The current datasheet and assembly instruction
point back to this drawing rather than to a separate 3-5912P1/3-5913P1 land
file.

## Contact and footprint field audit

| Required field for an exact project-local KiCad footprint | First-party result | State |
|---|---|---|
| 3-5912P1 / 1336G1 and 3-5913P1 / 1337G1 identity and row role | Explicit in product pages, B02021S and DS-PP1545 | **RESOLVED** |
| 7.9 mm inter-contact pitch | Explicit, typical | **RESOLVED as nominal/typical; tolerance is drawing general tolerance only** |
| 1.27 mm row spacing | Explicit, typical | **RESOLVED as nominal/typical** |
| PCB mounting type | Explicit plated-through-hole in 1S6479 and DS-PP1545 | **RESOLVED** |
| PCB thickness range | 2.3–3.8 mm in DS-PP1545 | **RESOLVED** |
| Contact-tail center coordinates in an unambiguous 1x2 datum | Sample layout gives relationships and expansion references, but does not declare an exact 1x2 datum/origin or a unique contact-tail coordinate table | **UNRESOLVED** |
| Finished contact drill/slot width and length | Not specified in B02021S, DS-PP1545, 1S6479, or the product pages | **UNRESOLVED** |
| Plated-hole finished size/tolerance | PTH requirement is specified; finished drill/slot and tolerance are not | **UNRESOLVED** |
| Copper pad shape, pad dimensions, annulus | Not specified; B02021S shows a sample layout and says accessory openings may expand per application | **UNRESOLVED** |
| Solder-mask expansion / paste treatment | Not specified | **UNRESOLVED** |
| Staple-hole coordinates and plating | 1.20 mm diameter is shown; complete datum, tolerance, and plating are not | **PARTIAL / UNRESOLVED for an authoritative retention footprint** |
| Wing-hole coordinates and plating | 4.57 mm diameter is shown; complete datum, tolerance, and plating are not | **PARTIAL / UNRESOLVED for an authoritative accessory footprint** |
| Mechanical housing envelope and installation references | B02021S/DS provide envelope references, row identity, and assembly guidance | **RESOLVED for envelope planning; not a complete 3D/keepout model** |
| Copper/thermal current guidance | DS-PP1545 gives contact ratings, resistance screen, PTH mounting and 10-AWG-equivalent PCB copper recommendation | **RESOLVED for electrical authority inputs; not a footprint land pattern** |

The source set is therefore sufficient to establish a practical PP15/45
assembly envelope and electrical screen, but it is **not sufficient to claim an
exact manufacturer-authorized contact land pattern**. Filling the missing
finished drill/slot and pad/mask values from an open-source footprint, a
visual measurement, or an engineer's preferred annulus would be an internal
prototype assumption, not a released-manufacturer dimensional audit.

## Secondary public precedent (not package authority)

The public `zeroping/PowerPoleDist` KiCad project was inspected only as a
sanity check. Pinned shallow-clone commit `ccbf9a5e51634844b1ac192991d3c6db3d6d4788`
contains `PowerPole_PP45_1336G1_1x2_Horizontal.kicad_mod` (SHA-256
`c745e6931e96cc0b06c9756a2a9c4b6fd3e615c1cdf7901eb5a105c8ceff88c2`). It uses
7.9 mm pitch, pad size 5.55 x 2.10 mm, and oblong drill 4.55 x 1.10 mm.
Those values demonstrate that a prototype footprint is practically constructible,
but the repository does not establish that the values are Anderson-released or
that they satisfy the intended contact-tail tolerance. They remain secondary
implementation precedent and are not imported into PiSXMe.

## Disposition to requesting package

- The previous `external:vendor-footprint-authorization` blocker is **not** an
  irreducible vendor-information blocker for the campaign as a whole: the
  released manufacturer sources establish the PP15/45 assembly's rating,
  pitch, row geometry, PTH requirement, and installation envelope, while the
  already indexed Molex 39301082 option has a complete released drawing for an
  exact project-local footprint.
- The Anderson-specific exact-footprint gate remains open unless Package/
  Footprint Authority explicitly accepts a documented prototype assumption and
  a mating sample/fit check. That acceptance would be an internal engineering
  decision, not a claim that Anderson released the missing land data.
- No Anderson footprint or public CAD was created by this packet. No restricted
  or vendor bytes were copied into the private Library or public repository.
- Recommended next authority action: keep Anderson as a high-current assembly
  option and use its B02021S coordinates/envelope for placement screening; use
  the documented Molex architecture for immediate canonical CAD integration if
  the product authority requires a footprint fully defined by released data.
