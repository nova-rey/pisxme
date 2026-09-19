# M2 integrated validation receipt

Integrated candidate SHA: `9c2a6df5`.

Fresh detached Light validation used KiCad 10.0.6 and returned exit 0: 257 violations and 393 unconnected items. The M2-specific J8/MECH_M2_2280 courtyard and PTH findings are absent; the two remaining courtyard overlaps are unrelated J7/C14 and C5/C6. Existing broad DRC/unconnected findings remain open elsewhere in Phase 24.

The integrated board contains J8 at `(205,140)`, fixed TE M-key J3 at `(220,165)`, the complete `[220,149]–[300,171]` card envelope, and separate card-body and connector-mating mechanical representations. Existing pad/net signatures remain unchanged at 1,270 pads.

KiCad Heavy 10.0.6 rendered the candidate successfully with `kicad-heavy:v1`; `m2-heavy-render.png` is retained. The render is a representation check only. Exact TE stack height, retention hardware, insertion/removal force, and prototype mating/service fit remain `REQUIRES_PROTOTYPE_VALIDATION` under the signed mechanical authority; no fabricated-hardware result is claimed and no DRC waiver is granted.
