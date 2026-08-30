# Critical-component sourcing reality check v2

Date: 2026-08-20
This is a small-quantity sourcing review, not a purchase commitment or live
quote. Stock changes and PCBA-house approved-part lists must be rechecked at
order time.

| Item | Manufacturer state | Authorized-distributor signal | PCBA-house risk | Result |
|---|---|---|---|---|
| Amphenol 74221-101LF | Amphenol marks it Active; product page showed distributor stock during this review | Mouser stock was shown on the page, but may change | fine-pitch/BGA assembly and X-ray; house may require customer-supplied part | **sourceable but single critical source** |
| Amphenol 10164227-1004A1RLF | active product family; official CM5 datasheet names it as the 4 mm option | distributor/house stock must be checked by date code | fine-pitch mezzanine, mating-height and placement restrictions | **sourceable with allocation risk** |
| TI TPSM63606RDLR | TI product is active; 36 V/6 A module | authorized stock varies by package suffix | QFN/HotRod thermal pad and paste/via requirements | **sourceable; verify exact suffix** |
| TI LM74700-Q1 | active automotive ideal-diode controller | common authorized part; check DBV/variant suffix | SMT assembly straightforward | **low/medium risk** |
| TI CSD19536KCS | active MOSFET family | authorized stock varies; TO-220 may be customer-supplied | through-hole/secondary assembly and heatsinking | **medium risk** |
| Molex 39301082 / 39012085 | active Mini-Fit Jr parts | cable-side housing and contacts are common but exact mating set must be ordered | through-hole/right-angle insertion and cable clearance | **medium risk** |
| Murata GRM21BR71H224KA01# | standard active MLCC family | common distributor/house alternatives exist | final DC-bias and voltage rating must be preserved | **low risk** |
| 0297015.U + 178.6165.0001 | active fuse/holder family appears obtainable | authorized stock needs point-in-time confirmation | holder is through-hole and may require hand/secondary insertion | **medium risk** |
| 4-pin PC PWM header | MPN not yet frozen in the placement study | use a keyed/shrouded 2.54 mm part with a released footprint | exact connector and cable clearance unresolved | **unresolved** |
| JST B4B-PH-K-S UART | common active connector family | typically obtainable | exact land pattern, keying, and assembly orientation unresolved | **unresolved** |
| Ethernet/USB connector | no final MPN in the current study | cannot assess | no release footprint or supplier path | **unresolved / remove from routing gate** |

## Manufacturer links

- [Amphenol 74221-101LF](https://www.amphenol-cs.com/product/74221101lf.html)
- [Amphenol CM5 connector](https://www.amphenol-cs.com/product/101642271004a1rlf.html)
- [Molex 39301082](https://www.molex.com/en-us/products/part-detail/39301082)
- [Molex 39012085](https://www.molex.com/en-us/products/part-detail/39012085)
- [TI TPSM63606](https://www.ti.com/product/TPSM63606)
- [TI LM74700-Q1](https://www.ti.com/product/LM74700-Q1)
- [TI CSD19536KCS](https://www.ti.com/product/CSD19536KCS)

## Procurement conclusion

The major semiconductor and power-connector choices are plausible for a
prototype, but the assembly-critical interconnects are not yet fully released.
The SXM2 receptacle is active and not inherently unobtainable, but its hidden
400-joint assembly means that a PCBA house's approved-part and X-ray policy is
as important as distributor stock. No sourcing fact upgrades the unresolved
manufacturer-land-pattern audit to a fabrication signoff.
