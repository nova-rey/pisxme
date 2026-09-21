# HPQ #7 authority reconciliation

The HPQ #7 contradiction is resolved by the existing signed Product/Power Authority R3 artifact from commit `627ec337a28ce0c732df7744dc3ba360414464db`, reconciled against current HEAD.

Binding correction:

- Q1 CSD19536KCS hot bound: 2.70 mOhm maximum at 25 C x 1.6 = 4.32 mOhm.
- Complete positive-plus-return hot path: 8.50 mOhm maximum inside the 10.0 mOhm outer contract.
- Effective terms: source 1.80, fuse/holder/contact 0.55, nine-branch PCB neck network 0.65, joins/vias 0.45, Q1 4.32, Q1 leads/pads 0.15, protected copper to J1 0.25, J1 field 0.25, residual 0.08 mOhm.
- Source: 11.4–12.6 V; product 300 W sustained / 330 W for 100 ms; source capability 40 A continuous / 45 A for 100 ms; protected minima 11.05 V sustained / 11.00 V peak.
- Branch policy: nine independently observed branches, 4.444 A continuous / 5.0 A pulse targets, 7 A contact screen, <=10% qualified imbalance, no passive-sharing or N-1 credit.

The later effective-network correction supersedes the mis-scoped per-branch 0.65 mOhm and 1.80 mOhm rules while retaining the 8.50 mOhm effective network budget. Hardware load-step, PDN, installed connector/harness resistance, thermal and SXM2 behavior remain `REQUIRES_PROTOTYPE_VALIDATION`.

Authority artifacts:
- `validation-receipts/protected-bus-corrective-authority-r3-20260919/PROTECTED_BUS_AUTHORITY_R3.json` SHA256 `8da4ebc9809e181d4db03f6692a8201546f89ff5f308f10d3013d614f9ec0d11`
- `validation-receipts/protected-bus-corrective-authority-r3-20260919/PROTECTED_BUS_AUTHORITY_R3.md` SHA256 `a96dbe66f6f5b3f1c2ef465c5e95da14271d4f6c833ea4d5b5b4180357c0c84e`
- `validation-receipts/protected-bus-effective-network-budget-20260921/POWER_AUTHORITY_DECISION.md` SHA256 `3ce8b18ff2506989a22b987712b9a7ecaf20195270cfaa3cb64c3443f5f6e19f`
