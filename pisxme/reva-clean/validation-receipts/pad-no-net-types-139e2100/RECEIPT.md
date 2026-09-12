# No-net pad type census

- Source commit: `139e2100`
- Worker: `pisxme-kicad-light:v1`, KiCad 10.0.6
- Scope: no-net pads only, classified by reference, pad number, attribute and pin type.
- J1: 93 no-net contacts, all SMD, corresponding to unknown/auxiliary SXM2 contacts that remain intentionally unassigned pending authority.
- U7: 24 no-net SMD pads; U11.65 and U13.43 are passive no-net pads.
- J3/J4: key/mechanical no-net contacts include M1/M2/S1/S2 and A8/B8/S1/S2.
- J2: key/mechanical and unassigned contacts include pads 4/5 plus six NPTH contacts.
- F1/F2/J5/J6/J7: no-net mechanical/thermal or NC pads.

This is a physical census, not an authorization to assign nets. J1 unknown contacts and any active-pad no-net cases require explicit no-connect/unknown disposition before bidirectional acceptance can close.
