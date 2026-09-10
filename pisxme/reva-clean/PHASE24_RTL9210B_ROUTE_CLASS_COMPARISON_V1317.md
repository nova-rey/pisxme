# Phase 24 RTL9210B route-class comparison — V1317

This receipt compares disposable native KiCad evidence by route class. DRC
counts are not treated as complete-board quality; each candidate's scope and
open connections are recorded separately.

| Basis | U1 orientation | Scope | Native DRC | Connectivity evidence | Decision |
|---|---:|---|---:|---|---|
| V1258 | 0° | complete U1-to-J1 lane-0 path | 0 | four endpoint and source-removal controls pass | accepted lane basis |
| V857 | 90° | SPI, PERST, crystal/RSET, GND support | 0 | support audits pass; 32 unrelated opens | accepted support primitive |
| V850 | 180° | ordered SPI/control source field | 0 electrical, isolated-fill warning | three SPI endpoint/negative controls pass | accepted support primitive |
| V1311 | 90° | four-lane rotated launch | 10 | four endpoint/negative controls pass | rejected route implementation |
| V1315 | 90° | allocated rotated lane launch | 14 | four endpoint/negative controls pass | rejected route implementation |
| V1316 | 180° | V850 support plus four lanes | 14 | four endpoint/negative controls pass | rejected route implementation |

## Decision

The rotated-QFN orientations provide useful SPI/control ordering evidence but
do not presently provide a valid lane launch when combined with their native
support fields. The next implementation class must preserve the V1258 0°
lane geometry and regenerate the RTL9210B support/source field in that same
orientation. Copying V857/V850 copper or treating their lower DRC counts as a
complete Path-B result is invalid because those fields are transformed around
different U1 orientations and have different open-connection scopes.

Path A remains untouched. This is a Path-B route-class decision only; no
production CAD is promoted by this receipt.
