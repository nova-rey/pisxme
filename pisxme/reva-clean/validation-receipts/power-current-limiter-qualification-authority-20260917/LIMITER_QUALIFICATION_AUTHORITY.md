# PiSXMe six-amp limiter qualification authority — HPQ4

- Decision ID: `PISXME-P24-6A-LIMITER-QUALIFICATION-20260917`
- Package: `P24-6A-LIMITER-QUALIFICATION-AUTHORITY`
- Review base: `92902ef1e92bc287eb31aa516ffc117b0b26712c`
- Authority: **Product / Power Authority**
- Date: `2026-09-17`
- CAD changed: **no**
- Product envelope changed: **no**
- Status: `NO_QUALIFIED_LIMITER_ARCHITECTURE`
- Residual dependency: `authority:6A-limiter-qualification`

## Binding disposition

No production limiter architecture is promoted by this review. The signed HPQ4
contract remains binding: six independent loops, 6.000–6.400 A per loop over
full tolerance and temperature, no passive sharing credit, a maximum 57 mOhm
hot limiter allocation, the 12.05–12.60 V sustained / 12.10–12.60 V peak source
contract, and the 300 W sustained / 330 W peak product envelope.

The Librarian packet is sufficient for authority reassessment. It does not
qualify a production MPN. The closest candidate is an LTC4281 or LTC4282 with
Kelvin sensing, an external low-resistance FET assembly, controlled trim, and
production qualification. It remains a candidate only.

## Why LTC4281/LTC4282 do not close the contract

The ADI Rev. C electrical tables specify a 32.88–35.87 mV full-scale current
limit DAC range over the full operating temperature range. Its symmetric spread
is about 4.346%, while the complete HPQ4 current window permits at most
3.225806% symmetric total error. That comparison is before shunt tolerance,
shunt temperature coefficient and self-heating, sense-copper variation,
calibration residual, FET hot resistance, and any production-test uncertainty.

The programmable adjustment is 3.1 mV per code over a 12.5–34.4 mV range. A
code step is about 9.012% of the full-scale setting, so it cannot be treated as
a guaranteed fine trim for a 6.000–6.400 A window. The data sheet mentions
final-test trimming against measured copper, but it does not establish the
PiSXMe residual, temperature-corner, EEPROM-retention, fixture-accuracy, or
lot-traceability contract needed to turn that feature into a production
qualification.

Both parts have relevant 12 V gate-drive, foldback, timer and telemetry
functions. Those facts are useful architecture evidence; they do not close the
complete hot-resistance, reverse-current, surge, fault-energy, SOA, thermal,
or six-loop fail-safe contract.

## Alternative dispositions

- `LM5066H`: rejected for the exact window; retained threshold examples are
  wider than the total error budget.
- `LTC4218` and `LTC4286`: rejected for the exact window on retained roughly 5%
  current-limit accuracy.
- `MAX5977A`: building block only; no closed active 6 A limiter or fault/path
  contract is retained.
- `TPS24750RUVR`: voltage-compatible candidate class, but the indexed packet
  lacks a verified full-temperature 6.000–6.400 A table and complete hot/fault/
  reverse evidence.
- `MAX17527A`, `TPS1663`, reverse controllers, nFETs, fuses and TVS parts retain
  their prior rejection or non-limiter dispositions.

No alternative is promoted merely because it is nominally compatible.

## Exact residual authority gap

Product / Power Authority must either qualify the calibrated LTC4281/LTC4282
assembly or acquire a manufacturer-guaranteed in-window limiter. The decision
packet must bind all of the following:

1. A six-loop full-tolerance/full-temperature calculation proving 6.000–6.400 A
   on every loop.
2. Calibration target, residual, fixture accuracy, temperature corners,
   configuration retention and production traceability.
3. Complete hot limiter resistance, including sense path and pass FET, at or
   below 57 mOhm; exact gate-drive minimum and hot FET RDS(on).
4. Fault timing, reverse-current/reverse-polarity, TVS clamp, fuse, harness
   inductance and nFET SOA/I2t coordination.
5. Six-loop fail-safe FLAG/inhibit/reset behavior and installed thermal/package
   qualification.
6. Exact MPN/package/footprint/procurement provenance.

Until those records exist, `P24-POWER-SOURCE-CONTRACT` and
`P24-EXACT-NFET-ENERGY-AUTHORITY` remain waiting on
`authority:6A-limiter-qualification`; no source schematic or PCB producer is
released. This is a scoped authority dependency, not an external blocker, and
it does not authorize changing the product envelope or editing CAD.

## Reproducibility

The machine-readable decision and all source hashes are in
`LIMITER_QUALIFICATION_AUTHORITY.json`. Primary sources are the ADI
[LTC4281 Rev. C data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ltc4281.pdf),
[LTC4282 Rev. C data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/LTC4282.pdf),
and their [LTC4281](https://www.analog.com/en/products/ltc4281.html) and
[LTC4282](https://www.analog.com/en/products/ltc4282.html) product records.
No CAD, product-envelope change, measurement, vendor approval or fabricated
hardware claim is made.
