# RTL9210B fixed-orientation REFCLK implementation rejection — V1581/V1582

Date: 2026-09-10

## Scope

Two disposable REFCLK implementations were evaluated on the accepted
`PHASE24_RTL9210B_U155_REHOME_V1517.kicad_pcb` basis. The Claude-selected
RTL9210B orientation was not changed, and no production or Path-A asset was
modified.

## V1581 — shared west transition

Native KiCad 10.0.5 DRC: **6 violations, 4 unconnected pads, 0 footprint
errors**. The route produced four track crossings and two shorts (REFCLK_N to
XTAL_OUT and REFCLK_P to REFCLK_N). XTAL_IN and XTAL_OUT remained open at the
crystal/support group. Raw board, generator, and DRC report are retained.

## V1582 — separated west transitions

Native KiCad 10.0.5 DRC: **15 violations, 4 unconnected pads, 0 footprint
errors**. Separating the two transitions did remove the direct P/N overlap at
the shared transition, but the resulting B.Cu corridors crossed existing
RSET, RTL_3V3, RTL_1V1, and each other. Native DRC also reported a REFCLK_N to
RTL_1V1 short and multiple via/pad and hole-clearance violations. The crystal
support endpoints remained open. Raw board, generator, and DRC report are
retained.

## Disposition

Both route classes are **REJECTED**. They are implementation failures against
the existing source-field copper, not evidence against the fixed 0° U1
orientation or the RTL9210B architecture. No rule severity was changed, and
no open was waived. The next Path-B implementation must co-author the crystal,
REFCLK, and rail/source fanout as one field or use a manufacturer-verified
alternate escape/package authority; orientation search remains closed.
