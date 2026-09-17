# ADM1175 component-path qualification — bounded evidence result

- **Package:** `P24-ADM1175-COMPONENT-PATH-QUALIFICATION`
- **Review base:** `d3efe794` (`Dispatch ADM1175 component path qualification`)
- **Private Library evidence:** `4794c3613f7047bfff058ac33b13d1f3624a05c9` plus this review's private index
- **Decision ID:** `PISXME-P24-ADM1175-COMPONENT-PATH-QUALIFICATION-20260917`
- **Scope:** component and installed-path evidence only; no CAD, source-contract, or product-envelope edits
- **Status:** `RESIDUAL_GAP` / `WAITING authority:6A-limiter-qualification`

## Result

The bounded review identified exact manufacturer part and package candidates, but
it does not establish a binding ADM1175 limiter path. The closest practical
candidate is one `ADM1175-1ARMZ-R7` or `ADM1175-2ARMZ-R7` per independent loop,
a four-terminal 16 mΩ shunt, and an external 100 V N-channel FET. The current
window cannot be claimed from the exact Vishay shunt candidate with the
untrimmed ADM1175 threshold: the recalculated range is **6.042710--6.458652 A**.
The upper limit fails the HPQ4 6.400 A ceiling. This corrects the earlier
hypothetical 16.13 mΩ / 10 ppm screening assumption; that assumption was not an
exact procurable component.

No MPN is promoted, no footprint is selected, and no source or PCB producer is
released.

## Manufacturer evidence

The Analog Devices ADM1175 Rev. C data sheet is the controller authority. It
specifies 3.15--16.5 V operation, `VLIM = 97--103 mV`, a charge-pumped external
N-channel gate drive, Kelvin sense guidance, 4--10 µs fast-overcurrent response
(guaranteed by design and not production tested), 90 mV timing threshold,
115 mV fast-trip threshold, and `tFAULT ≈ 21.7 × C_TIMER ms/µF`. The data sheet
also specifies gate-drive ranges only at 3.15 V, 5 V, and 16.5 V; it does not
give a guaranteed minimum `VGATE − VCC` at the signed 12.05--12.60 V source
range. Its single-FET application does not provide reverse blocking.

Primary source: [ADI ADM1175 Rev. C data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ADM1175.pdf),
retrieved 2026-09-17, especially Tables 1--3, Equations 1--7, and the Kelvin
connection section. The requested orderable controllers are
`ADM1175-1ARMZ-R7` (automatic retry) and `ADM1175-2ARMZ-R7` (latched off).

The candidate shunt is derived from Vishay's documented global numbering, not
from a retained vendor byte:

| MPN / family | Manufacturer evidence | Screening disposition |
|---|---|---|
| `WSK2512R0160BEA` | Vishay WSK2512, 2512, four-terminal, 1 W at 70 °C, 0.01--0.2 Ω range at ±0.1%, ±35 ppm/°C component TCR, −65--+170 °C; the B/EA codes mean ±0.1% and lead-free tape/reel | Candidate part identity; untrimmed ADM1175 window fails |
| `WSK1206R0160BEA18` | Vishay WSK1206 high-power, 1206, four-terminal, 0.5 W, ±0.1%, ±35 ppm/°C, 16 mΩ orderable listing | Reject for sustained 6.4 A screening: `I²R = 0.655 W` nominal exceeds 0.5 W rating |
| Ohmite `CS10` family | 4-terminal Kelvin, 10 W, 1--500 mΩ, ±0.1% available, ±5--100 ppm/°C, −55--+150 °C | Custom-value candidate only; no exact 16.13 mΩ orderable MPN or PiSXMe installation contract retained |

Primary sources: [Vishay WSK2512 data sheet](https://www.vishay.com/docs/30108/wsk2512.pdf),
[Vishay WSK1206 high-power data sheet](https://www.vishay.com/docs/30325/wsk120618.pdf),
[Ohmite CS10 series](https://www.ohmite.com/res-cs10/), all retrieved 2026-09-17.

The external-FET candidates below are component candidates, not qualified
installed paths:

| MPN | Package | Manufacturer limits used | Remaining 57 mΩ at 25 °C only |
|---|---|---|---:|
| `IRLS4030-7PPbF` | D2PAK 7 / TO-263 7 | 100 V; 4.1 mΩ max at `VGS=4.5 V`, `ID=94 A`, 25 °C; 175 °C `TJmax`; 0.40 °C/W `RθJC`; data sheet includes SOA and avalanche characterization | 36.8476 mΩ |
| `BSC070N10LS5ATMA1` | PG-TDSON-8 / SuperSO8 5×6 | 100 V; 8.5 mΩ max at 4.5 V; 79 A; 150 °C; active/preferred Infineon record | 32.4476 mΩ |
| `BSC096N10LS5ATMA1` | PG-TDSON-8 / SuperSO8 5×6 | 100 V; 12.5 mΩ max at 4.5 V; 40 A; 175 °C; active Infineon record | 28.4476 mΩ |

Primary sources: [Infineon IRLS4030-7P data sheet](https://www.infineon.com/assets/row/public/documents/24/49/infineon-irls4030-7p-datasheet-en.pdf),
[BSC070N10LS5 product record](https://www.infineon.com/part/BSC070N10LS5), and
[BSC096N10LS5 product record](https://www.infineon.com/part/BSC096N10LS5),
retrieved 2026-09-17.

## Recalculation and failure boundary

For `WSK2512R0160BEA`, use the manufacturer component limits and a conservative
65 °C worst reference span from 25 °C to −40 °C:

- combined resistance variation = `0.1% + 35 ppm/°C × 65 °C = ±0.3275%`;
- `R_SENSE_MIN = 15.9476 mΩ`, `R_SENSE_MAX = 16.0524 mΩ`;
- `I_LIMIT_MIN = 97 mV / R_MAX = 6.0427101243 A`;
- `I_LIMIT_MAX = 103 mV / R_MIN = 6.4586520856 A`;
- maximum shunt dissipation at that screen = `0.6696128 W`;
- nominal 25 °C-only residual after the candidate `IRLS4030-7PPbF` is `36.8476 mΩ`.

The resistance ratio is the decisive proof: HPQ4 requires
`R_MAX/R_MIN ≤ (97 mV / 6.000 A) / (103 mV / 6.400 A) = 1.0045307443`.
The exact WSK2512 candidate has `R_MAX/R_MIN = 1.0065715217`, so no change of
nominal shunt value can repair the ratio while retaining the untrimmed ADM1175
97--103 mV threshold. A calibrated production scheme could change this result
only if its residual, temperature-corner behavior, fixture accuracy, retention,
and lot traceability are explicitly bounded by authority.

The reproducible arithmetic is in `ADM1175_COMPONENT_PATH_CALC.py` and its JSON
output. It is screening arithmetic, not a hardware or vendor qualification.

## Required gates that remain open

1. **Exact shunt contract:** obtain an exact production MPN/value with tolerance,
   full-temperature TCR, self-heating, Kelvin geometry, power derating, and
   procurement provenance. The documented WSK2512 candidate is unsuitable for
   an untrimmed 6.000--6.400 A window.
2. **Controller calibration:** either use a controller/limiter whose guaranteed
   threshold ratio fits HPQ4 or bind a production calibration procedure with
   residual, fixture accuracy, temperature corners, configuration retention, and
   lot traceability.
3. **Gate-drive proof:** obtain a guaranteed ADM1175 gate-drive minimum at
   12.05--12.60 V and use FET `RDS(on)` specified at or below that minimum and at
   hot junction. The 4.5 V data points are useful screens only.
4. **Hot path:** measure or calculate the complete installed path, including
   shunt, FET, copper, Kelvin interconnect, reverse-protection devices, vias and
   connectors, at the operating temperature; the total must remain ≤57 mΩ.
5. **Reverse/fault energy:** select reverse blocking, TVS, fuse/harness and any
   back-to-back FETs; close the actual harness-inductance waveform, fast-trip /
   TIMER behavior, FET SOA/I²t and six-loop fail-safe inhibit/reset contract.
6. **Thermal/DFM:** close the selected package land pattern, assembly thermal
   path, copper spreading, derating and service/production test access.

These gates are an internal authority/evidence dependency, not an external
blocker. The source-contract and exact-nFET packages remain waiting on
`authority:6A-limiter-qualification`. No CAD changes are justified by this
packet.
