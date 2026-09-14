# Receipt: P24-POWER-CURRENT-LIMITER-AUTHORITY

- Result: `CONDITIONALLY_SIGNED_SELECTION`
- Queue dependency resolved: `authority:power-current-limiter-signature`
- Selection: six `MAX17527AATP+T`, one per loop A-F
- SETI: `6.25 kOhm`, `0.1%`; nominal regulated limit `6.000 A`
- Calculated regulated range: `5.75424575--6.24624625 A` per branch
- `6.400 A` hard screen scope: post-blanking regulated branch limit
- Fast fault: `20--32 A` device threshold, `3 us` typical response; separate SOA/I2t qualification required
- Mode: latch-off; `220 kOhm` CLMODE resistor to GND; fail-safe aggregated FLAG/inhibit/reset required
- CAD changed: no; source-contract/CAD insertion: not authorized
- Remaining: exact external nFET, fuse/TVS/I2t/SOA, FLAG/reset, six harness loops, MPA/thermal installation, ADI provenance retention

See `LIMITER_SELECTION_SIGNED_RECEIPT.md` and `.json`.
