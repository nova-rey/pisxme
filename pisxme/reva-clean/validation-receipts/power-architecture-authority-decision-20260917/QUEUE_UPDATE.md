# Queue update — P24 power architecture correction

Package: `P24-POWER-ARCHITECTURE-AUTHORITY-DECISION`
Decision: `PISXME-P24-POWER-ARCH-20260917` revision 1.0

Root queue actions after importing the signed authority record:

1. Complete this authority package from its candidate receipt. It changed no CAD.
2. Mark the superseded six-loop limiter package and its dependent exact-nFET,
   six-loop connector, six-loop protection, and six-loop harness work as
   `SUPERSEDED_BY PISXME-P24-POWER-ARCH-20260917`, preserving their receipts and
   HPQ #5 history. Do not leave `hpq:nova-rey/codex-config-backup#5` as an
   active dependency for the replacement architecture.
3. Add `P24-PROTOTYPE-SOURCE-BUS-CONTRACT` as READY. It owns exact source
   voltage/tolerance, current/peak budget, input assembly, ordinary protection,
   common bus, return, drop and thermal calculations. It does not select a
   six-loop limiter.
4. Add `P24-PROTOTYPE-POWER-BUS-PRODUCER` waiting on the source-bus contract;
   it may receive CAD work only after that authority contract and current
   corridor ownership are closed.
5. Add `P24-PROTOTYPE-POWER-BUS-INTEGRATION-VALIDATION` waiting on the producer;
   it requires serialized integration and fresh Light validation at the exact
   integrated SHA.
6. Add `P24-V100-PROTOTYPE-FIRST-POWER-CONTRACT` as READY in parallel. It defines
   current-limited bring-up, rail/enable/reset observations, measurement limits,
   shutdown criteria and `REQUIRES PROTOTYPE VALIDATION` records.
7. Keep independent Phase 24 storage, SI, mechanics, firmware/provenance and
   acceptance work running. Do not start Phase 25 or Phase 26.

The queue controller remains Root-owned. This file is the deterministic handoff
for the required transitions; it is not a second queue authority.
