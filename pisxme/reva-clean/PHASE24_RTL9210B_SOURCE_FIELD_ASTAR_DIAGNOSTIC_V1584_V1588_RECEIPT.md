# RTL9210B source-field obstacle-router diagnostic — V1584–V1588

Date: 2026-09-10

## Method

The disposable router `phase24_rtl9210b_refclk_astar_v1584.py` was changed
from an isolated REFCLK overlay into a six-net source-field diagnostic. It
removed only the saved local copper for REFCLK P/N and PCIe lane-0 P/N, built
layer-specific obstacles from native pads/tracks/vias, and searched F.Cu/B.Cu
ordinary-through-via paths. The fixed Claude V1575 orientation and V1517
package geometry were unchanged. Native DRC remains the acceptance gate.

## Results

With centerline reservation, the P-first V1584 search found REFCLK_P alone;
with N-first V1585 it found REFCLK_N alone. The six-net V1587 ordering found
valid paths for LANE0_TXP, LANE0_TXN, LANE0_RXP, and LANE0_RXN plus REFCLK_N,
but no legal remaining REFCLK_P path. The V1588 ordering found REFCLK_P,
LANE0_TXN, and LANE0_RXP before no legal remaining path. These are planner
diagnostics only; they did not save a complete candidate and are not passes.

## Disposition

The result distinguishes two issues: the obstacle-aware authoring path is
able to find individual native-net paths, while the current two-layer source
field cannot accommodate all six paths without coordinated treatment of the
adjacent field. No clearance, layer, or DRC rule was relaxed. The next
implementation must co-author the source-field support and lane fanout, or
use a manufacturer-verified alternate land-pattern escape. Orientation and
Path A remain unchanged.
