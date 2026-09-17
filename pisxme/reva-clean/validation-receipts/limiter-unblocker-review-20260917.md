# Limiter Unblocker Review

- Package: `P24-6A-LIMITER-UNBLOCKER-REVIEW`
- Review disposition: **INTERNAL_ROUTE / DOMAIN_AUTHORITY**
- Date: 2026-09-17

The retained evidence does not bind a production limiter. MAX17527A and TPS1663 violate the HPQ4 window; LTC4281/LTC4282 exceed the error budget before calibration; ADM1175 with the WSK2512 screen calculates 6.042710–6.458652 A and lacks qualified hot-path, gate-drive, reverse/fault, SOA/I2t, thermal, and production-test evidence.

Required next capability level: one bounded Product/Power system-qualification decision using retained candidates, supported by Power Integrity, Package/DFM, and Thermal authority. It must either bind a calibrated controller/shunt/FET assembly against the six-loop 6.000–6.400 A contract and <=57 mOhm hot path, or issue a precise no-go with one narrowly scoped evidence dependency. No further family search, HPQ4 relaxation, or CAD release is authorized.
