# ADM1175 Six-Amp Limiter Search Validation

- Package: `P24-6A-LIMITER-RESEARCH-ESCALATION`
- Private Library commit: `4794c3613f7047bfff058ac33b13d1f3624a05c9`
- Validation date: 2026-09-17

The private Library brief and machine index parse successfully and identify the
Analog Devices ADM1175 production family and Rev. C data sheet. The retained
screen uses a 16.13 mOhm, 0.1%, 10 ppm/C shunt and calculates 6.003733–6.396171 A,
with 0.658806 W maximum shunt dissipation and approximately 40.843 mOhm remaining
of the 57 mOhm hot-path budget.

Disposition: **PASS — candidate-ready for Product/Power Authority; not a qualified production limiter.**
Open authority terms are exact shunt provenance, external FET hot RDS(on)/gate
behavior, complete hot path, reverse behavior, SOA/fault energy, and production
calibration/test limits.
