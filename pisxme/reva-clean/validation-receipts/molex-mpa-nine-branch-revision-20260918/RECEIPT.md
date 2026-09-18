# Binding MPA local placement/corridor decision — Molex nine branch revision

- **Package:** `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- **Decision:** `PISXME-P24-MOLEX-NINE-BRANCH-MPA-20260918-R1`
- **Authority:** Macro Placement Authority
- **State:** `BINDING_DECISION`
- **Decision file:** `MPA_DECISION.md`
- **Machine record:** `MPA_DECISION.json`

The rejected native producer receipt reports 1,135 violations, including 44
shorting items and 21 track crossings. Its geometry retained duplicate legacy
`OLD_J5`/`OLD_J6` footprints, used 22-mm fuse spacing that overlapped the
24-mm fuse courtyards, assigned the connector contacts in an alternating
positive/return order contrary to the signed nine-branch contract, and routed
all raw/fused branches as one F.Cu fanout. This decision changes placement,
pad ownership, and layer ownership together.

The sole placement is the fixed J1/J5/J6/J9 anchor geography, a 3x3 fuse grid
at x=`36/64/92` and y=`26.25/51.25/76.25`, and a protection column left of the
J1 courtyard. Positive branches fan out in ordered In2 lanes; branch returns
use distinct In4 lanes; only post-primary-protection copper enters the In3
protected plane. Existing unrelated/high-speed copper, J1 assignments,
six-layer roles, and source/protection requirements remain protected.

`TP2` moves to `(114,60)` and is bound to `12V_BRANCH_JOIN` by the source owner
before copper. The producer must remove/replace the two legacy two-pin
footprints and obsolete named power copper, assert all coordinates and the
correct pads 1–3 positive / 4–6 return contract before routing, and return
native connectivity, targeted DRC, path resistance/drop, via/current, and
thermal evidence. No alternate placement or unrestricted route campaign is
authorized.
