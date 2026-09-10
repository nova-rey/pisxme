# Phase 24 storage R81 power primitive — V1570

Date: 2026-09-10  
Status: ACCEPTED FOCUSED PRIMITIVE; not a full-board closure

## Scope

V1570 is a disposable descendant of the source-corrected V79 storage board.
It adds only the JMS583 reset-pullup power attachment for R81.2 (`STORAGE_3V3`)
to the existing In2 power handoff. The F.Cu escape is a 0.30 mm diagonal
dogbone from R81.2 at (125.5,145.0) to an ordinary 0.80/0.40 mm through-via at
(126.5,144.2). The via transitions to In2 and joins the existing power spine
through a corridor above the known USB field. No signal is routed on a plane
layer, and no via-in-pad or microvia is used.

## Native evidence

- `phase24_storage_r81_native_audit.py`: PASS for native R81.2 → U14.5
  `STORAGE_3V3` connectivity.
- The same audit removes each saved-board `STORAGE_3V3` track/via in disposable
  copies and requires a failed native connectivity result: PASS negative
  control.
- `phase24_storage_m2_power_owner_audit.py`: PASS for all nine native J3
  `STORAGE_3V3` contacts and its trace-removal negative control.
- Native KiCad DRC: 604 total findings / 341 unconnected pads. This is an
  inherited open-board baseline plus the focused primitive, not a clean-board
  claim. No new local `STORAGE_3V3`–`JMS_RESET_N` short is present; the prior
  V1569 horizontal escape failure is rejected evidence.
- The new path is physically connected by saved pads, tracks, via, and filled
  zones; expected connectivity is used only as an assertion.

## Decision

Accept V1570 as the current R81-only power primitive. U12/U13 QFN support-pad
power attachments remain open because the tested ordinary-via classes create
real pad-field clearance/crossing defects. Continue with a different
source/support fanout strategy; do not promote V1570 to the integrated board
or declare Phase 24 closed.
