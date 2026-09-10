# Phase 24 storage U12 power-pad fanout — V1572

Status: REJECTED route implementation

V1572 tested a distinct U12.13 source-field class: a 0.10 mm F.Cu escape
from the native pad at (153.5,136.6) to an ordinary 0.80/0.40 mm through-via
at (149.0,136.6), followed by a 0.60 mm In2 handoff. Native connectivity was
not used as a substitute for DRC.

Native KiCad DRC found 605 violations / 341 unconnected pads. The new route
introduced a 0.10 mm track-width violation, a real track-crossing involving
the existing CM5_PERST corridor, and retained the QFN pad-field clearance
defects. It is rejected. No schematic, footprint authority, or integrated
board was changed. The result confirms that simply narrowing the local escape
does not close the U12 power fanout under the current saved geometry and
rules; a different footprint/source-field or coherent local regeneration is
required.
