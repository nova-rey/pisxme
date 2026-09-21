# Protected-bus footprint geometry authority

The isolated native-pcbnew probe demonstrates a coordinate-frame construction error in the corridor producer, not a manufacturer-geometry gap.

Evidence: `p24-protected-bus-corridor-producer/output/pad-geometry.txt` and `probe2.txt`, generated with KiCad 10.0.6 from candidate base `9e6b0000`.

The cloned Molex footprint has its first pad at the footprint origin, but subsequent pads remain at board-origin-relative coordinates after `FOOTPRINT(base_header)` and `SetPosition`. For J5 at (12,25), pad 2 was reported at (4.2,0) instead of (16.2,25); the same transform error appears on J6/J9. The fuse clone shows the analogous frame error.

Binding correction:

- Copy the released project-local footprint geometry without changing pad dimensions, drill, pitch, or numbering.
- Set the footprint position before adding it to the board.
- Set every pad position in the footprint-local frame, then verify absolute positions after board insertion.
- Molex J5/J6/J9 pads: positive pads 1/2/3 at local x=0/4.2/8.4, y=0; return pads 4/5/6 at local x=0/4.2/8.4, y=5.5. Absolute positions are the anchor plus those local offsets.
- Preserve the audited 0039300060 footprint dimensions and the F1-F9 holder geometry; no pad remap or connector architecture change is authorized.

Acceptance before corridor routing: independent geometry census must show all 18 connector pads and all F1-F9 holder pads at their intended absolute coordinates, with no pad at board origin, and fresh Light footprint/DRC checks must be retained.

This authority corrects only the isolated producer construction method. It does not close connectivity, DRC, path-budget, thermal, or DFM rows.
