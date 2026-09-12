# Phase 24 storage USB3 support V6 receipt

Candidate: `PHASE24_STORAGE_MKEY_USB3_EAST_SUPPORT_V6_20260912.kicad_pcb`

V6 is a materially different routing topology, not a coordinate perturbation:
the TX pair owns the upper B.Cu corridor and the RX pair owns a lower B.Cu
corridor, with staggered U12 returns. U11 bottom-row pads escape outward before
the pair corridors begin. The selected RTL9210B/JMS583 and U12 orientations,
the east source handoff, and the storage architecture are unchanged.

## Native evidence

The actual-pad ten-link audit passes, including the four J7-to-U12 links, both
AC-coupled TX links, and both direct RX links. Native KiCad 10.0.5 DRC after
refill reports 428 violations / 421 unconnected items.

The V6 report has no USB3-specific `shorting_items` or `tracks_crossing`
findings. The remaining native DRC issues include inherited board findings,
the inherited `STORAGE_SEL`/`STORAGE_3V3` short, and the explicit local 0.15 mm
U11 escape segments being checked against the board-wide 0.20 mm minimum.
Therefore V6 is route evidence, not a production closure.

Fresh EDA Light validation from committed ref `8375090b` reproduces the same
class under KiCad 10.0.6: 430 violations / 421 unconnected items. Its only
shorting-class finding is the inherited `STORAGE_SEL`/`STORAGE_3V3` issue; no
USB3-specific short or crossing is reported. The two-count DRC delta from
local KiCad 10.0.5 is retained as a tool-version difference, not merged away.

## Geometry decision

The 0.15 mm width is confined to the immediate U11 bottom-edge fanout. It is
the least aggressive geometry used so far that clears the 0.4 mm-pitch row
without a USB3-specific short or crossing;
all longer corridors use 0.20 mm traces and ordinary 0.60/0.30 mm through
vias. Promotion requires expressing this local manufacturable exception in
the board rules (or returning to 0.20 mm if a native-clear escape permits it)
and rerunning full DRC. No global rule relaxation is authorized.

V6 remains rejected as a complete board route only for implementation-rule
and inherited-board findings. It does not reopen the frozen RTL9210B
orientation, Path-B architecture, or accepted downstream launch.
