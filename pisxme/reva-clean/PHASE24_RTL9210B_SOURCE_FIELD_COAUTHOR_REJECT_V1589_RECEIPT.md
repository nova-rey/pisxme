# RTL9210B complete source-field coauthor rejection — V1589

Date: 2026-09-10

V1589 used the fixed Claude-selected 0-degree U1 orientation and the V1517
native pad field, removed the six disposable REFCLK/PCIe-lane copper nets and
all local source-field rail/return tracks and vias in the U1 envelope, then
searched all six nets together with an obstacle map built from saved pads,
tracks, and vias. Native geometry was otherwise preserved.

The search found paths for four nets (`REFCLK_P`, `LANE0_TXN`, `LANE0_RXP`,
and `LANE0_RXN`) before no legal path remained for `REFCLK_N`; it did not save
a complete candidate. This is diagnostic route-implementation evidence, not
a pass. It shows that merely removing inherited local rail congestion is
insufficient: the remaining constraint is the combined QFN source escape and
closely spaced J1 launch topology. No rules were relaxed and no orientation
or Path-A change was made.
