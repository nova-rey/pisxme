# Protected-bus Heavy v2 execution unblocker

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Classification: `IMPLEMENTATION`
- Outcome: `INTERNAL_ROUTE`
- Capability: qualified `pisxme-kicad-heavy:v2`

The authorized corridor is not disproven. The first GUI candidate saved but failed fresh Light validation (919 baseline DRC versus 929 candidate, with an illegal/dangling via). A second execution exited before saving. A subsequent launch stopped in KiCad setup/load flow. The next bounded method is a Heavy runtime preflight: verify committed project load and live pcbnew PID, route only J5.2 to F2, save through the qualified session, confirm the saved PCB diff, reopen/check the saved artifact, and return raw session evidence plus candidate SHA. No placement, rule, layer, or product constraint changes are authorized.

Reassessment trigger: saved candidate with raw session evidence plus fresh Light DRC/connectivity/path-budget validation, or reproducible startup/save failure after this preflight.
