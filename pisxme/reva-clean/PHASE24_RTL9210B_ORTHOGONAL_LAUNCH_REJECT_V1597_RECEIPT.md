# RTL9210B orthogonal launch rejection — V1597

Date: 2026-09-10

V1597 stripped all non-target tracks and vias from the V1590 handoff fixture,
then tested six-net orthogonal F.Cu/B.Cu launch channels. Native KiCad DRC
reported **20 violations** and 39 unconnected items in the intentionally
incomplete fixture. The remaining launch-specific defects include 0.6 mm via
clearance at 0.5 mm-pitch J1 contacts, connector-side pair shorting, and
crossing/dogbone conflicts. No candidate was promoted and no rule was relaxed.

This discriminator separates the launch problem from inherited RTL9210B
support copper. The next trial must place connector-side vias outside the
J1 contact pitch and use explicit offset dogbones; the fixed U1 orientation
and accepted QFN escape remain unchanged.
