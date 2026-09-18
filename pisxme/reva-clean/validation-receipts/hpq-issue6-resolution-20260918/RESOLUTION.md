# HPQ Issue #6 resolution packet

**Outcome:** `resolution-ready`

Issue #6 proved a binding structural contradiction in MPA R1. No PCB candidate was emitted. R1 must not be retried or partially integrated.

## Binding disposition

Upstream topology/package authority must change the available board region, fuse-holder envelope, or preserved macro geography, then issue one new dimensioned placement/corridor decision. The protected-bus producer remains parked until that authority result exists.

## Evidence

- Base: `c74789d72910ebf4e7f1edc8caf0b17548a4609a`.
- Task Force packet commit: `13a9176696176719789572d35f2270e93590de69`.
- Transport bundle SHA-256: `528812c4fc73174e36d6744e9cbe4f50f70035f228e730ae4e9fbd233f84efd6`.
- F7/F8 fuse courtyards conflict with J7 holes and preserved geometry; the third row has no legal centerline.
- The actual 24.25 mm courtyard on a 25 mm pitch leaves 0.75 mm, contradicting the prior 3 mm rationale.
- The x=104..106 join corridor alone exceeds the 10 mOhm complete path cap.
- Native counts were 300/499 source, 307/499 untouched round-trip, and 532/499 rejected R1 probe.

The rejected placement probe, historical failed boards, and conditional Q1 replacement are evidence only. They are not canonical candidates. The original transport bundle is no longer present in the local HPQ workspace; the GitHub Issue result and this normalized authority receipt are the durable provenance.
