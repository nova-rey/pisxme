# P24-POWER-CURRENT-LIMITER-AUTHORITY

## Bounded result

Status: `CANDIDATE_READY_FOR_POWER_AUTHORITY_REVIEW`; no CAD changed.

The bounded component search identifies one exact active production limiter
candidate for each of the six independent 12-V loops:

- Active MPN: `MAX17527AATP+T`
- Vendor: Analog Devices (Maxim)
- Function: 5.5–60 V, 6 A power limiter with adjustable UV/OV, thermal
  protection, fault flag, reverse-current/reverse-polarity support with an
  external nFET, and selectable continuous/auto-retry/latch-off behavior.
- Package: 20-pin TQFN-EP, package code `T2055+6C`, 5 mm x 5 mm.
- Six instances: one independent instance on each loop A–F.
- SETI resistor: `6.25 kOhm`, 0.1% (one per instance).
- CLMODE: latch-off configuration using the vendor-prescribed 220 kOhm
  resistor to ground; the system supervisor must aggregate FLAG faults and
  deassert V100 enable/hold reset until controlled restart.
- PLIM: disabled only if Power Authority confirms the input power-limit
  function is not being used as a substitute for the branch current limit;
  otherwise its effect must be included in the limit proof. This receipt
  assumes PLIM is disabled by tying it to ground.

The exact MPN is a candidate for binding authority signature. It is not yet a
CAD-selection authorization, because external nFET, fuse/I2t, thermal copper,
and system fault aggregation remain separate qualification items.

## Current-limit calculation

The MAX17527A datasheet specifies current-limit accuracy of +/-4% for a
programmed 3–6 A limit over the full operating temperature range. Its SETI
relationship is `RSETI(kOhm) = 37.5 / ILIM(A)`; 6.25 kOhm therefore programs
6.000 A nominally.

Including the selected resistor's 0.1% tolerance:

- minimum branch limit = `6.000 * 0.96 / 1.001 = 5.75425 A`;
- maximum branch limit = `6.000 * 1.04 / 0.999 = 6.24625 A`;
- maximum versus the product hard limit = `6.24625 <= 6.400 A`, margin
  `0.15375 A`;
- six-loop minimum aggregate = `6 * 5.75425 = 34.52547 A`;
- V2.2 low-voltage peak screen = `34.37622 A`, aggregate margin
  `0.14925 A`.

This is a narrow aggregate margin. It is valid only if the V2.2 peak screen is
accepted as the six-loop source requirement and the declared branch-balance,
harness-drop, thermal, and startup assumptions are separately qualified. It
must not be represented as bench evidence or as proof that an arbitrary load
can be redistributed across the six loops.

The MAX17527A's absolute maximum DC input current is 6.3 A; the calculated
6.24625 A worst-case regulated limit remains below that rating by 0.05375 A.
Power Authority should retain this margin in the final signed calculation and
must not round the limit up to 6.4 A.

## Protection and fault evidence

The vendor datasheet records:

- input operating range 5.5–60 V, covering the approved 11.4–12.6 V source;
- internal 30 mOhm typical nFET and 57 mOhm maximum specified RON condition;
- current-limit range 0.6–6.0 A and +/-4% accuracy in the selected range;
- continuous, auto-retry, and latch-off current-limit modes;
- open-drain FLAG for overcurrent voltage-drop, UVLO, OVLO, thermal shutdown,
  and invalid SETI conditions;
- latch-off after the blanking interval, reset by EN below 0.4 V for at least
  30 us typ or input cycling;
- fast short-circuit turn-off within 3 us typ when internal overcurrent
  protection threshold is exceeded, with 20–32 A specified threshold range;
- thermal foldback around 150 degC typ and thermal shutdown above 165 degC
  typ, with latch-off retained in latch-off mode;
- external nFET required for reverse-polarity and reverse-current protection;
- manufacturer layout requirements for short wide IN/OUT copper, exposed-pad
  grounding and thermal vias, and large copper heat-spreading areas.

The short-circuit numbers establish a protection response and an engineering
energy screen, not a complete system SOA proof. Using the worst stated fast-trip
threshold and response as a first screen gives `32^2 * 3 us = 0.003072 A^2 s`
before parasitic and retry effects. The external nFET, fuse, harness
inductance, TVS/clamp, and PCB copper must be selected and verified so their
actual I2t/SOA exceeds the resulting fault waveform. The vendor explicitly
requires an output clamp for inductive hard shorts within the allowed pin
voltage range. That system qualification is still open.

## Authority and dependency disposition

This packet binds the following proposed component contract for review:

`6 x MAX17527AATP+T + 6 x 6.25 kOhm 0.1% SETI + latch-off CLMODE + per-loop FLAG aggregation`,
with one branch per A–F and no passive current sharing.

It does not authorize reduction of the 300 W sustained or 330 W peak product
envelope. It does not authorize PCB-only insertion of six stages. Source
ownership, four missing source loops, MPA placement, exact external nFET,
fuse/I2t, thermal installation, fault aggregation, and fresh integrated
validation remain required.

### Exact evidence gap

Power Authority must either sign this contract or return a bounded contrary
calculation. The remaining non-authority qualification is:

1. Package/Power must select an exact external nFET and verify its reverse
   polarity/reverse-current SOA and gate-drive limits with the MAX17527A.
2. Package/Power must coordinate the existing or revised fuse with the
   MAX17527A fast-trip/retry behavior, harness inductance, TVS/clamp and
   PCB copper, including a retained I2t/SOA calculation.
3. System authority must define whether the 6.4 A invariant applies to the
   regulated post-blanking branch limit (the interpretation used here) or to
   every sub-3 us fault transient. The latter cannot be claimed from this
   datasheet alone and requires a system transient/energy requirement.
4. Librarian must index the official ADI product page and datasheet in the
   private Library and record the exact retrieved byte hash. Direct shell
   retrieval was unavailable during this bounded pass; no substitute hash is
   claimed.

If the authority interprets the last item as indispensable to the invariant,
this package is `WAITING_ON authority:power-current-limiter-signature` with the
candidate retained. No alternate same-class eFuse search is authorized in
this package without materially new evidence.

## Primary sources

- Product page and lifecycle/package records:
  https://www.analog.com/en/products/MAX17527A.html
- Datasheet Rev 0, 19-101626, 2022-11:
  https://www.analog.com/media/en/technical-documentation/data-sheets/max17527a.pdf
- Existing PiSXMe power envelope:
  `validation-receipts/power-envelope-authority-redesign-20260914/POWER_ENVELOPE_AUTHORITY_V2.2_CANDIDATE.json`
- Existing source-contract escalation:
  `validation-receipts/power-source-contract-20260914/POWER_SOURCE_CONTRACT_ESCALATION.json`

No vendor document has been copied into the public repository.
