# Branch fuse and holder authority

Checked: 2026-08-30. Status: `CLOSED` for selection, land pattern, and contact
mapping; electrical integration and copper/thermal validation remain Phase 14
gates.

## Selected parts

- Fuse: Littelfuse `0297015.U`, MINI 297 automotive blade, 15 A, 32 VDC,
  fast-blow, active status.
- PCB holder: Littelfuse `178.6165.0001`, ATO FLR PCB holder, active series,
  through-hole, eight-hole mechanical holder with a central spigot.

The holder is not an electrical two-pad SMT component. The project-local
footprint preserves the manufacturer's eight-hole mechanical/contact pattern,
central spigot clearance, and assembly/replacement envelope; the fuse itself is a separate
replaceable part. The selected 15 A value is provisional until the full Rev-A
rail budget, cold-plug behavior, and holder derating are calculated.

## Procurement evidence

DigiKey's exact `0297015.U` record showed Active status, 24,049 in stock,
MOQ 1, 16-week manufacturer lead time, and USD 0.46 at quantity 1 (USD 0.20658
at 1,000) on the captured 2026-08-30 page. The record includes CAD models.
Littelfuse identifies the 297 MINI series as a 15 A / 32 V automotive fuse.

Mouser's exact `178.6165.0001` record showed 14,956 in stock, MOQ 1, about
USD 4.78 at quantity 1 and USD 2.32 at 5,000, with a 21-week factory lead
for quantities above stock. Littelfuse's holder drawing identifies the
`178.6165.0001` eight-hole PCB holder and `178.6165.0002` as the alternate
packaging variant. DigiKey CAD/model availability is recorded for the fuse;
the holder drawing is the land-pattern authority. The corrected project-local
pattern uses eight 1.40 mm finished holes at x = -6.40, -2.90, +2.90, +6.40
mm and y = -1.25, +1.25 mm, matching the manufacturer's 5.8±0.05 mm,
3.5±0.07 mm and 2.5±0.07 mm callouts in drawing `CVP-PE40-0006 Rev A`.
Pads 1-4 are the input contact and pads 5-8 are the fused-output contact. A
conservative 3.00 mm central NPTH reserves clearance for the 2.4±0.1 mm
mechanical spigot.

Sourcing risk: `LOW` for quantity-1 fuse and holder availability; assembly
risk `MEDIUM` because the holder is through-hole and serviceable. The holder
and fuse are intentionally not represented as one two-pin component in the
final BOM.

## Sources and provenance

- Littelfuse product: https://www.littelfuse.com/ja-jp/products/fuses-overcurrent-protection/fuses/automotive-fuses/blade-fuses-shunt/mini/297/0297015-u
- Littelfuse fuse datasheet: https://www.littelfuse.com/assetdocs/littelfuse_mini_datasheet.pdf
- Littelfuse holder drawing: https://www.littelfuse.com/assetdocs/1786165?assetguid=8044f5c2-ee81-46f8-8b17-a6b53163d395
- DigiKey exact fuse record: https://www.digikey.com/en/products/detail/littelfuse-inc/0297015-U/3427481
- Mouser exact holder record: https://www.mouser.com/ProductDetail/Littelfuse/178.6165.0001
- RS exact-MPN description: https://au.rs-online.com/web/p/fuse-holders/8207268/

Littelfuse documents are retained by URL and summarized here; no vendor CAD
file is redistributed in this repository.

## Exact PiSXMe decision closed

Each mandatory cold-plug 12 V branch reserves one `0297015.U` fuse in a
`178.6165.0001` PCB holder ahead of its LM74700 reverse-current controller;
the electrical selection, exact local eight-hole holder footprint, central
spigot clearance, and 1-4-to-input/5-8-to-output contact mapping are closed.
The footprint remains a through-hole
wave/hand-solder operation; copper routing and thermal margin are separate
Phase 14 gates.
The 15 A rating is not yet a Phase 5 pass: current sharing, inrush, I²t,
temperature rise, and protected-rail voltage drop must be signed off before
routing.
