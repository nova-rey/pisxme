# Phase 24 JMS583 crystal-local V1 rejection

The disposable `phase24_jms583_local_crystal_repair.py` candidate moves Y10 to
`(131,124)` and reconnects U11.50 `XIN` to Y10.1 and U11.51 `XOUT` to Y10.2.
The corrected complete-support audit was run explicitly against this
candidate and its negative-control output.

Results:

- `XIN`: connected, negative control passed
- `XOUT`: connected, negative control passed
- other retained support branches: connected
- `JMS_VDDREG_5V`: still disconnected
- native KiCad 10.0.5 DRC: 637 violations / 410 unconnected items

The DRC includes a real local clearance defect at the LXO via and other
candidate-specific route/placement findings. This V1 crystal route is
rejected evidence; it is not promoted and does not reopen RTL9210B or storage
architecture decisions. Raw candidate and DRC are retained separately.
