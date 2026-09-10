# V113 storage-placement regeneration receipt

V113 ran `phase24_place_dual_mode_storage_island.py` from the selected
macro ancestor and used the repository's JLC rule profile for native DRC.
The generator produced a native placement candidate, but it intentionally
retains donor copper and therefore is not a routed production candidate.

- Artifact: `PHASE24_STORAGE_REGEN_JLC_V113.kicad_pcb`
- Rule profile: repository JLC fixture profile, 0.15-mm clearance and
  0.13208-mm minimum track width
- Native DRC: 297 violations / 499 unconnected pads
- Shorting entries: none in the report; crossings remain
- Decision: REJECT as an integrated route; retain as authoring-boundary
  evidence

This confirms that the placement generator must be paired with a targeted
storage-copper scrub/regeneration step. Donor copper is not authoritative
after component replacement.
