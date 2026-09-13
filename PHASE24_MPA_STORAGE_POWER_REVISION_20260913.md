# Phase 24 MPA bounded revision — 2026-09-13

Authority: Macro Placement Authority, bounded reassessment after rejected producer `b0614be9`.

The rejected producer did not demonstrate a structural contradiction. Its 1083 DRC / 499 unconnected result included 50 shorts and 27 crossings caused by guessed non-pad launches, a shared Port-A via, a shared STORAGE_SEL via, invalid 0.10 mm geometry, and F2 overlap with J2 courtyard.

Binding implementation basis for one producer attempt:

- Keep U13 at (180,135), top-side, 180 degrees; keep C30/C32/C33/C31 at (103.5,116/120/128/132), top-side, 180 degrees.
- Move F2 to (90,60) and D2 to (110,60), preserving orientation; keep J1/J2/J3/J5/J6/J7/U1/U2/Q2/C4/U7/U11/U12/U14 fixed.
- Route from exact native pads. Keep four distinct Port-A J3 transition vias and separate ordered corridors. Give STORAGE_SEL and AUTO_PEDET dedicated control corridors.
- Route Branch-B J6 to F2, F2 to D2/Q2/U2, and protected power through dedicated corridors with approved net-class geometry and ordinary through-vias.
- Protect existing CM5 PER0/REFCLK, USB3, CM5_PERST, U11/U12, J3 STORAGE_3V3, J1 PCIe/reference, GATE_B, VCAP_B, and power/ground zones.

The producer must run targeted native connectivity/DRC, then fresh KiCad Light validation. A failure can escalate only as a structural contradiction if it demonstrates infeasibility after exact-pad routing under valid project rules. No additional speculative placement search is authorized.
