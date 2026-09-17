# PiSXMe ADM1175 Limiter Authority Reassessment — HPQ4

- Decision ID: `PISXME-P24-ADM1175-LIMITER-QUALIFICATION-20260917`
- Package: `P24-ADM1175-LIMITER-AUTHORITY-REASSESSMENT`
- Review base: `02334352a16321a28f52f4b4c579aa8030f6d6ec`
- Authority: Product / Power Authority
- Date: 2026-09-17
- CAD changed: **no**
- Product envelope changed: **no**
- Status: `CANDIDATE_REJECTED_FOR_BINDING`
- Dependency retained: `authority:6A-limiter-qualification`

## Binding decision

`ADM1175-1ARMZ-R7` and `ADM1175-2ARMZ-R7` are evidence-backed candidate
controllers, but neither is promoted as a qualified PiSXMe production limiter.
The HPQ4 contract remains binding: six independent loops, 6.000--6.400 A over
full tolerance and temperature, no passive-sharing credit, and a complete hot
limiter allocation no greater than 57 mOhm. The 300 W sustained / 330 W peak
product envelope is unchanged.

The variant distinction is material: the `-1` is automatic retry and the `-2`
is latched off. The appropriate fault policy cannot be selected until the
external FET, protection, reverse behavior, V100 inhibit/reset, and fault-energy
contract are closed.

## Manufacturer evidence

The Analog Devices Rev. C datasheet establishes 3.15--16.5 V operation,
97--103 mV current-limit threshold, external N-channel FET gate drive, a
4--10 us fast overcurrent response (guaranteed by design and not production
tested), TIMER-based fault handling, I2C readback, and Kelvin-sense guidance.
It supplies the current equations used below. The product record lists both
requested orderable models as production parts. These facts establish
candidate compatibility; they do not qualify the complete installed branch.

## Screening calculation

The Librarian packet screened a hypothetical **16.13 mOhm nominal Kelvin shunt**
with 0.1% initial tolerance and 10 ppm/C tempco. Applying a conservative
0.165% resistance envelope gives:

| Quantity | Result |
|---|---:|
| `R_SENSE_MIN` | 16.1033855 mOhm |
| `R_SENSE_MAX` | 16.1566145 mOhm |
| `I_LIMIT_MIN = 97 mV / R_MAX` | 6.0037330222 A |
| `I_LIMIT_MAX = 103 mV / R_MIN` | 6.3961705444 A |
| shunt power at maximum current | 0.6588055661 W |
| remaining 57 mOhm hot allocation after `R_MAX` | 40.8433855 mOhm |
| margin above 6.000 A floor | 0.0037330222 A |
| margin below 6.400 A ceiling | 0.0038294556 A |

This is a screening result only. The small current margins are not a
production residual allowance. The exact shunt MPN/package, Kelvin geometry,
external FET and installed path have not been qualified.

## Open qualification gates

1. **Exact shunt and current window:** identify the production shunt and prove
   tolerance, tempco, Kelvin implementation, calibration residual, and six-loop
   full-temperature limits.
2. **Hot path:** the assumed shunt consumes up to 16.1566145 mOhm, leaving
   40.8433855 mOhm for FET, copper, Kelvin interconnect and other series terms.
   No exact FET or installed hot maximum is bound.
3. **Fault and reverse behavior:** the controller's fast-trip and TIMER
   mechanisms do not establish PiSXMe reverse-current/reverse-polarity policy,
   clamp, fuse/TVS, harness-inductance waveform, FET SOA or I2t.
4. **Thermal and production test:** controller limits are component facts;
   installed FET/shunt/copper thermal rise, fixture limits, retention and lot
   traceability are not defined.

## Resumption dependency

`authority:6A-limiter-qualification` remains owned by Product / Power Authority.
To release the source contract and downstream CAD, the authority must select
exact shunt and external FET parts, close the complete <=57 mOhm hot path,
bind reverse/fault/thermal/harness/copper behavior, and define production
calibration/test residuals. The exact nFET and protection packages remain
waiting on this dependency. No user/product decision or external blocker is
claimed.

## Evidence and validation

The deterministic screening equations are in
`ADM1175_SCREEN_CALC.py`; the machine-readable decision is in
`ADM1175_LIMITER_AUTHORITY.json`. The private Library brief and index are
hash-pinned in that JSON. Validation is arithmetic only; no bench,
fabricated-hardware, vendor approval, or thermal measurement is claimed.
