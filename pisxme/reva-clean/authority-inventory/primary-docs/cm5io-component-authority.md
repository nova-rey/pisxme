# CM5 carrier connector and Ethernet MagJack authority

Checked: 2026-08-29. These supporting authorities are inherited from the
official Raspberry Pi CM5IO Rev 2 reference; they do not authorize importing
its schematic or PCB.

## CM5 carrier connector

- Selected MPN: Amphenol `10164227-1001A1RLF`, BergStak 0.40 mm, 100-position,
  1.5 mm stack-height receptacle, surface-mount.
- Manufacturer authority: Amphenol product page and drawing; Raspberry Pi CM5
  forward-design guidance also names this mating part. Local STEP and
  footprint are in `cm5io-rev2/`.
- Procurement snapshot: Amphenol shows Active/Stocked; DigiKey shows 8,092
  in stock at about $1.77 quantity 1 and $0.96732 at 5,000; Newark shows
  9,449 in stock, quantity-1 cut tape about $2.10, and 9-week standard lead.
  MOQ is 1 cut tape/re-reel; full reel is 5,000.
- Risk: `LOW` for prototype procurement, `MEDIUM` for supply timing.
- Decision: `CLOSED`; Phase 3 may regenerate a project-local footprint from
  the manufacturer drawing and use the local STEP only as model provenance.

## Ethernet MagJack

- Reference MPN: `TRJG0926HENL`, the exact CM5IO BOM/reference connector and
  local footprint/STEP. CM5IO schematic and BOM are reference-only authority
  for native CM5 Ethernet pin mapping.
- Procurement snapshot: JLCPCB lists exact name as extended part
  `C9900198333`, plugin/wave assembly, minimum 444, full reel 500, but current
  in-stock quantity is 0 and it is consign-only. No authoritative manufacturer
  drawing, lifecycle statement, or dependable major-distributor listing was
  found in this capture.
- Risk: `HIGH`; this is not a released clean-BOM choice. A mainstream
  magnetics-integrated RJ45 may be selected in Phase 3 only after matching
  CM5 PHY magnetics, LED polarity, mechanical envelope, and shield/ESD.
- Decision: `REV_A_EMPIRICAL_RISK`; public sourcing cannot close the exact
  legacy part's manufacturer/procurement authority, and a generic MagJack
  substitution changes the electrical and mechanical contract. Phase 3 must
  obtain a manufacturer drawing/sample or select a fully documented compatible
  replacement before release.

Provenance: official CM5IO archive SHA-256
`48b14a6757b0edc0ac110331445f35a4212b5ce432bdcec6605c99431b59496b`;
Amphenol product/distributor pages for the carrier connector; JLCPCB exact
part page for the MagJack status. Manufacturer copyrights and model terms
remain with their owners; local copies are retained for design provenance and
comparison only.
