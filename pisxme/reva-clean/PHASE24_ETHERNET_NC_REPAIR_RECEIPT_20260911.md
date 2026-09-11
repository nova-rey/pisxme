# Phase 24 CM5 Ethernet no-connect repair receipt — 2026-09-11

Removed exactly four stale `No Connect` records in `CORE_CM5.kicad_sch` at
the required Ethernet launch pins:

- J7 pin 4 — `CM5_GBE_TD1_P`
- J7 pin 6 — `CM5_GBE_TD1_N`
- J7 pin 10 — `CM5_GBE_TD0_N`
- J7 pin 12 — `CM5_GBE_TD0_P`

The corresponding live Ethernet labels and topology are unchanged.

Validation:

- Native KiCad 10.0.5 ERC: 863 warnings, 0 errors, down from 867.
- All four corresponding `no_connect_connected` findings disappeared.
- `validation/phase3/test_phase24_native_final_authority.py`: PASS.

One unrelated connected-NC finding remains on a GND pin and is still open;
no other no-connect marker was changed.
