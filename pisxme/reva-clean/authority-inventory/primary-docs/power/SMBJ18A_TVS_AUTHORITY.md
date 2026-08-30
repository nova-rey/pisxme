# 12 V input TVS authority

Checked: 2026-08-30. Status: `PHASE5_TVS_AUTHORITY_CANDIDATE`.

## Selected candidate

Littelfuse `SMBJ18A`, unidirectional 600-W TVS, DO-214AA/SMBJ, is the
selected Rev-A input-transient candidate. Its 18 V working standoff is above
the locked 12 V source while its 29.2 V maximum clamp at 20.6 A is below the
42 V absolute maximum input rating of LM74700-Q1. This is a protection
coordination calculation, not a claim that every possible supply fault is
contained; the fuse, wiring inductance, MOSFET SOA, and source current limit
must still be reviewed together.

## Candidates considered

| Candidate | Result | Evidence/risk |
|---|---|---|
| Littelfuse `SMBJ18A` | selected | Active DigiKey listing; 600 W, 18 V standoff, 29.2 V clamp, DO-214AA; current listing showed 0 stock and 3,000 expected 2026-09-22; 30-week manufacturer lead time |
| Vishay `SMBJ18A-E3/52` | compatible backup | Mouser listing showed 10,255 in stock; same nominal 18 V/29.2 V class; verify exact marking and package drawing before substitution |
| Diodes Inc. `SMBJ18A-13-F` | compatible backup | DigiKey substitute listing showed 67,199 available at approximately $0.56 each; verify current datasheet and pulse-rating equivalence |

The selected Littelfuse part is therefore sourcing risk `MEDIUM` despite its
active lifecycle: the exact manufacturer listing was temporarily out of
stock, but two reputable multi-source replacements are available. MOQ is 1
for distributor cut tape; ordinary SMT DO-214AA assembly is practical but
larger than a basic chip diode and requires a real thermal/current copper
landing.

Local asset saved: `PiSXMe_RevA_Clean.pretty/TVS_SMBJ18A_DO214AA.kicad_mod`.
It is a two-pad DO-214AA/SMBJ land-pattern transcription from the legacy
provisional `TVS_SMB` geometry, renamed into the clean namespace. It still
requires a pad/drawing overlay against the Littelfuse package drawing before
the footprint can be promoted from candidate to closed authority.

## Sources and provenance

- Littelfuse primary SMBJ family datasheet:
  `https://www.littelfuse.com/~/media/electronics/datasheets/tvs_diodes/littelfuse_tvs_diode_smbj_datasheet.pdf.pdf`
- DigiKey Littelfuse exact MPN and current stock/price snapshot:
  `https://www.digikey.com/en/products/detail/littelfuse-inc/SMBJ18A/285984`
- Mouser Vishay backup:
  `https://www.mouser.com/en/ProductDetail/Vishay-Semiconductors/SMBJ18A-E3-52`
- DigiKey Diodes backup is linked as a direct substitute from the exact
  Littelfuse listing.

License/provenance: the Littelfuse datasheet is retained as design authority;
distributor pages are procurement snapshots. No third-party CAD is copied.

## Exact PiSXMe decision

This closes the candidate identity, electrical class, package, lifecycle, and
second-source strategy for the 12 V TVS. It does not yet close Phase 5:
the TVS must be represented in both cold-plug branches, its exact footprint
must be verified, and the final fuse/TVS/MOSFET surge and thermal coordination
must be calculated against the actual source and copper envelope.
