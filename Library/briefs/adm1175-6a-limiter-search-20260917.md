# P24-6A-LIMITER-RESEARCH-ESCALATION — bounded manufacturer evidence brief

- **Requesting package:** `P24-6A-LIMITER-RESEARCH-ESCALATION`
- **Owner:** Librarian
- **Retrieved:** 2026-09-17
- **Search disposition:** one new manufacturer family search completed; no production architecture selected and no CAD changed.
- **Evidence class:** primary manufacturer component authority; candidate system synthesis is project-derived and requires Product/Power Authority review.

## Question and search boundary

The HPQ4 contract requires six independent 12-V loops, each with a guaranteed full-tolerance and temperature current window of **6.000–6.400 A**, a complete hot limiter allocation of **≤57 mΩ**, fault/reverse/SOA/thermal coordination, and a production-testable implementation. The private Library was searched first. Existing MAX17527A, TPS1663, MAX17526A, LM5066H, LTC4218, LTC4281, LTC4282, LTC4286, MAX5977A, fuse, TVS, harness, and nFET records were not re-run. The bounded new-family search targeted the Analog Devices **ADM1175** production hot-swap controller because its current-limit contract is explicitly tighter than the previously rejected families.

## New primary sources

1. [ADM1175 product page](https://www.analog.com/en/products/adm1175.html), Analog Devices, production part page, retrieved 2026-09-17. It lists ADM1175-1ARMZ-R7 and ADM1175-2ARMZ-R7 as production models, 3.15–16.5 V operation, external N-channel FET drive, adjustable current limit, retry/latch options, and ±3% accurate hot-swap current limit.
2. [ADM1175 datasheet Rev. C](https://www.analog.com/media/en/technical-documentation/data-sheets/ADM1175.pdf), Analog Devices, Rev. C, document page dated 2012-11-09, retrieved 2026-09-17. Table 1 specifies `VCC = 3.15–16.5 V`, `TA = -40..+85 °C`, and `VLIM = 97..103 mV`; Equations 1–5 define the current-limit, timing-threshold, and fast-trip calculations. The datasheet gives 4–10 µs fast-overcurrent response (guaranteed by design), a programmable TIMER fault interval, and -40..+85 °C operating range / 150 °C junction absolute maximum.

Vendor bytes were not retained and no local hash is claimed; the Library stores metadata, links, extracted facts, and this bounded working calculation only.

## Candidate calculation

The manufacturer equations are:

- `I_LIMIT_MIN = 97 mV / R_SENSE_MAX`
- `I_LIMIT_MAX = 103 mV / R_SENSE_MIN`
- nominal `I_LIMIT = 100 mV / R_SENSE`

A candidate authority input for one loop is a **16.13 mΩ nominal Kelvin shunt**, assumed for this screening calculation to be **0.1% initial tolerance and 10 ppm/°C**, with the manufacturer and package to be selected by Power Authority. Applying a conservative ±0.165% resistance envelope over -40..+85 °C gives:

- `R_SENSE_MIN = 16.1033855 mΩ`
- `R_SENSE_MAX = 16.1566145 mΩ`
- `I_LIMIT_MIN = 6.0037330 A`
- `I_LIMIT_MAX = 6.3961705 A`
- maximum shunt dissipation at the upper limit: `0.6588056 W`

This screening result is inside the 6.000–6.400 A window, but it is **not a qualified selection**. It depends on the exact shunt’s tolerance/tempco, Kelvin layout, and production measurement procedure. The 16.13 mΩ shunt leaves at most approximately **40.843 mΩ** of the 57 mΩ hot allocation for external FET, copper, sense interconnect, and any other series resistance. The external FET must be characterized at the ADM1175’s actual minimum gate drive and hot junction; the ADM1175 datasheet does not close that path.

## Manufacturer-backed facts and gaps

| HPQ4 field | ADM1175 evidence | Disposition |
|---|---|---|
| 12 V compatibility | VCC operating range 3.15–16.5 V | **Candidate evidence**; compatible with the signed 12.05–12.60 V source range |
| 6.000–6.400 A threshold | 97–103 mV full-temperature limit plus the manufacturer equations; screened 16.13 mΩ shunt result is 6.0037–6.3962 A | **Candidate architecture**, pending exact shunt authority and assembly qualification |
| Hot limiter path | External FET and shunt are explicitly required; no complete RDS(on)/PCB/hot-path guarantee | **Unresolved**; remaining allocation is 40.843 mΩ after screening shunt |
| Fault timing / fast fault | 90 mV minimum timing-threshold equation, 115 mV maximum fast-trip equation, TIMER equation `tFAULT ≈ 21.7 × C_TIMER ms/µF`, and 4–10 µs fast response | **Candidate evidence**; external FET SOA and PiSXMe fault-energy coordination remain open |
| Thermal behavior | -40..+85 °C operating range and 150 °C junction absolute maximum; external FET thermal/SOA is external | **Unresolved system qualification** |
| Reverse behavior | No reverse-current blocking or reverse-polarity contract was identified in the product page/datasheet | **Gap**; authority must provide external reverse protection or reject the candidate |
| Production testability | I²C 12-bit voltage/current readback, up to four addresses, and latch-off/retry variants | **Candidate evidence**; six-loop fixture, calibration residual, traceability, and test limits remain to be defined |
| Production availability | ADI product page marks ADM1175-1ARMZ-R7 and ADM1175-2ARMZ-R7 `PRODUCTION` | **Provenance evidence**, not an allocation or lifecycle guarantee for PiSXMe |

## Librarian disposition

`ADM1175-1ARMZ-R7` / `ADM1175-2ARMZ-R7` is a **new evidence-backed candidate architecture**: one controller, a Kelvin precision shunt, and an external N-channel FET per independent loop. It is closer to the HPQ4 current window than the previously rejected candidates, and the data sheet supplies the exact equations needed for a bounded screening calculation. It does **not** qualify a production PiSXMe limiter because reverse behavior, exact hot path, external FET gate-drive/SOA, fault-energy coordination, exact shunt provenance, and production calibration/test limits remain open.

Return this packet to Product/Power Authority for one decision: either qualify the ADM1175 assembly with exact component choices, margins, reverse/fault coordination, and a production test plan, or reject it on those gaps. This bounded search is complete. Do not repeat the prior families or begin another search under this package without a new authority request.
