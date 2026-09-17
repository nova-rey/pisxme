# Receipt — retained six-amp limiter system authority

- **Package:** `P24-6A-LIMITER-SYSTEM-AUTHORITY-DECISION`
- **Result:** `DONE / NO_GO_RETAINED_CANDIDATES`
- **Review base:** `ae58ad438f2fb9b7ace00f4eaa07d7858d147a07`
- **Decision artifact:** `LIMITER_SYSTEM_AUTHORITY_DECISION.json`
- **Arithmetic check:** `LIMITER_SYSTEM_AUTHORITY_CALC.py` -> `PASS_ARITHMETIC_NO_GO`
- **CAD changed:** no
- **Product envelope changed:** no

The retained MAX17527A, TPS1663, LTC4281/LTC4282, ADM1175/WSK2512 and
documented FET screens do not bind the complete HPQ4 six-loop system. The sole
resumption dependency is `authority:6A-limiter-qualification`, defined as one
exact authority-reviewed six-loop limiter-system record with current-window, hot
path, calibration, gate-drive, reverse/fault, SOA/I2t, thermal, procurement and
fail-safe evidence.

No further family search, HPQ4 relaxation, product-envelope change or CAD edit
is authorized by this result. The dependent source and exact-nFET packages remain
waiting on that dependency; unrelated Phase 24 work may continue.
