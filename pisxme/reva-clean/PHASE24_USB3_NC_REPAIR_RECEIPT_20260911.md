# Phase 24 CM5 USB3 no-connect repair receipt — 2026-09-11

## Change

Removed only the four stale `No Connect` records in `CORE_CM5.kicad_sch` at
the required CM5 USB3 launch pins:

- J7 pin 128 — `CM5_USB3_RX_N`
- J7 pin 130 — `CM5_USB3_RX_P`
- J7 pin 140 — `CM5_USB3_TX_N`
- J7 pin 142 — `CM5_USB3_TX_P`

The corresponding live global labels remain unchanged. No other no-connect
record, net name, component, or topology was edited.

## Validation

- Native KiCad 10.0.5 ERC: 867 warnings, 0 errors, down from 871 warnings.
- All four USB3 `no_connect_connected` findings disappeared.
- `validation/phase3/test_phase24_native_final_authority.py`: PASS.
- Existing focused USB3 saved-fixture endpoint audit: PASS for all four
  J7-to-U7 USB3 pairs, including its existing negative-control coverage.

The remaining five `no_connect_connected` warnings are unrelated Ethernet or
GND records and remain open/unwaived. A separate historical root-USB3 audit
was not promoted because its selected fixture lacks the expected U12 selector;
that is a fixture-input mismatch, not evidence against this source repair.
