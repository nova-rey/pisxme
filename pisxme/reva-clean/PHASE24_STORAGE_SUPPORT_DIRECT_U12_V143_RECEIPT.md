# Phase 24 storage USB3 support V143 receipt

V143 tested direct F.Cu exits from the U12 bridge pads with widely separated
through-vias and ordered B.Cu support lanes. The experiment moved the series
capacitors and source corridors out of the inherited PERST y=150 area.

Native DRC reports 17 violations, including real U12 POWER_GND/pad-field
shorts and target-via/track interactions, plus two silk warnings. The reduced
fixture retained the expected omitted support/power unconnected groups.

V143 is rejected. The direct-exit idea is retained as evidence, but these
coordinates are not a production route and no validation rule was relaxed.
