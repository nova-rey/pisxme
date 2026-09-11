# Storage M.2 power local-zone V88 experiment

The full storage candidate `PHASE24_STORAGE_CM5_USB4_MONOTONIC_V79_M2_POWER_OWNER`
failed the native M.2 power-owner audit on nine J3 power contacts. The V88
author added a local F.Cu pickup zone, an outboard In1 trunk, and ordinary
through-via returns without changing the schematic or global layer contract.

Saved-board connectivity then passed for all nine J3 contacts, including the
audit's actual trace-removal negative control. This proves the power-owner
repair topology reaches the socket in the saved native objects.

However, native KiCad DRC on the resulting candidate reports 608 violations
and 341 unconnected items. The source V79 candidate reports 601 violations;
therefore V88 is not promoted as a clean candidate. The result is retained as
useful route evidence: **connectivity repair passes, production DRC gate does
not**. The next implementation must preserve the successful source-to-J3
connectivity while resolving the added/new physical conflicts; no severity
relaxation is allowed.
