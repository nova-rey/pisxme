# Protected-bus Heavy v2 2.75 GiB attempt — bounded stall

- Base/dispatch: `d1265bac`
- Image: `pisxme-kicad-heavy:v2`
- Digest: `sha256:39fdae0176135aec42a0dacc8fb250bf8cbf915e01ad67a342e8f8bb2de44344`
- Container limit: 2,883,584,000 bytes (2.75 GiB)
- Session: private Xvfb, KiCad 10.0.6; `pcbnew` remained alive (`OOMKilled=false`).
- GUI reached the authorized J5.2 route and produced `pre-route.png`, `after-via.png`, and `gui-session.json`.
- After-via state remained in active routing at approximately `(24.5,25.0)` with B.Cu selected; no In2-to-F2.1 completion, save, reopen, candidate SHA, or validation was produced within the bounded attempt.
- Container was stopped after the bounded stall; no canonical CAD changed.
- Classification: implementation/control-path stall, not evidence of corridor impossibility or an OOM contradiction.
- Next action: Tier-2 GUI-control method reassessment; do not repeat this unchanged interaction sequence.
