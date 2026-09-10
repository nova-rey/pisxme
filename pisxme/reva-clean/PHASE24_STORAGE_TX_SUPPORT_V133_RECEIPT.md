# Phase 24 storage TX support V133 receipt

V133 shifted the TX coupling-cap support corridor to y=160/165 and moved
C86/C87 coherently, keeping the V127 CM5 USB3 source escape and storage
topology. Native DRC rejected the candidate at 192 violations / 499 opens.
Real findings include crossings/shorts into JMS_AVDD33, BRIDGE_1V1, and the
live U12 support field, plus local clearance and via findings.

Decision: reject. A simple downward translation does not solve the storage
support integration; it trades the TP5/PERST obstruction for regulator-island
obstructions. The next candidate must change local layer ownership or use a
different support-side corridor, not repeat a vertical translation.
