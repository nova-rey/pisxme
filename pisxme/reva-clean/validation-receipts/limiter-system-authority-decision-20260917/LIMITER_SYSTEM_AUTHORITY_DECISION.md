# PiSXMe retained six-amp limiter system authority decision

- **Package:** `P24-6A-LIMITER-SYSTEM-AUTHORITY-DECISION`
- **Decision ID:** `PISXME-P24-6A-LIMITER-SYSTEM-NO-GO-20260917`
- **Review base:** `ae58ad438f2fb9b7ace00f4eaa07d7858d147a07`
- **Authority:** Product / Power / Package / Thermal Authority
- **Status:** `NO_GO_RETAINED_CANDIDATES`
- **CAD changed:** **no**
- **Product envelope changed:** **no**

## Binding decision

No retained candidate binds the complete HPQ4 six-loop limiter system. The signed
contract remains binding: six independent loops, 6.000--6.400 A per loop over
full tolerance and temperature, no passive-sharing credit, a maximum 57 mOhm hot
limiter allocation, S0 of 12.05--12.60 V sustained and 12.10--12.60 V for the
100 ms peak, 300 W sustained V100 operation, and 330 W peak design allowance.

The no-go is scoped to the retained limiter candidates. It does not lower the
product envelope, release source or PCB work, or authorize another family search.

## Candidate disposition

| Retained candidate | Current-window result | Other mandatory gates | Disposition |
|---|---|---|---|
| MAX17527AATP+T + external FET | **FAIL:** 5.7542457542--6.2462462462 A; the independent minimum is below 6.000 A | Hot path, fault waveform, SOA/I2t, thermal and six-loop fail-safe behavior remain unproven | Rejected; negative control only |
| TPS1663 | **FAIL:** 5.58--6.42 A; misses both limits; 31 mOhm is typical | Hot maximum, fault/reverse, thermal and six-loop behavior remain unproven | Rejected; negative control only |
| LTC4281/LTC4282 + Kelvin shunt + external FET | **FAIL/UNPROVEN:** 32.88--35.87 mV threshold ratio is 1.0909367, above the complete allowed 1.0666667 ratio before other errors | Calibration residual, fixture, retention, hot path, FET, reverse/fault, SOA/I2t, thermal and production traceability remain unbound | Closest candidate; not promoted |
| ADM1175 + WSK2512R0160BEA + documented FET screens | **FAIL:** 6.042710--6.458652 A; upper limit exceeds 6.400 A without an authorized calibration contract | Exact shunt/MPN installation, gate-drive minimum, hot FET, reverse/fault, SOA/I2t, thermal and production-test limits remain unproven | Rejected for binding; candidate evidence only |
| Documented FET screens | Not a limiter | Exact system gate drive, hot RDS(on), fault and thermal installation remain unproven | Not limiter options |

No candidate is promoted merely because it is voltage-compatible or has a favorable
25 C/typical resistance screen.

## Gate result

| Gate | Result | Reason |
|---|---|---|
| Six-loop 6.000--6.400 A full-temperature contract | **FAIL/UNPROVEN** | Every retained active candidate fails the window or lacks a complete calibration proof |
| Complete installed limiter path <=57 mOhm hot | **UNPROVEN** | No complete shunt, pass-FET, sense-copper, via and connector hot qualification exists |
| Source compatibility | **PARTIAL** | Voltage classes are compatible where documented; the installed limiter system is not qualified |
| Calibration residual / fixture / retention / traceability | **UNPROVEN** | No PiSXMe production contract is retained |
| Gate drive and hot FET RDS(on) | **UNPROVEN** | Screens do not bind minimum drive and hot installed resistance |
| Reverse / surge / TVS / fuse / harness / SOA-I2t | **UNPROVEN** | No exact system waveform and coordination record exists |
| Thermal / package / DFM / procurement | **UNPROVEN** | No exact coordinated architecture has been selected |
| Six-loop fail-safe FLAG/inhibit/reset | **UNPROVEN** | No binding truth table and implementation contract exists |

## Sole resumption dependency

`authority:6A-limiter-qualification` remains open as one internal authority
dependency: **one exact qualified six-loop limiter-system record**. The record
must identify the retained controller, shunt, pass FETs and packages; prove the
6.000--6.400 A window over tolerance and temperature on every loop; bind
calibration target, residual, fixture accuracy, temperature corners, retention
and lot traceability; prove the complete <=57 mOhm hot installed path and gate
drive/hot RDS(on); coordinate reverse/fault, TVS, fuse, harness and SOA/I2t;
and close thermal, DFM, procurement and six-loop fail-safe behavior.

After that record exists, requalify the exact nFET/protection assembly, then
release the source contract and downstream CAD through normal serialized
integration and fresh KiCad Light validation. Until then,
`P24-POWER-SOURCE-CONTRACT` and `P24-EXACT-NFET-ENERGY-AUTHORITY` remain waiting
on this dependency.

## Scope and evidence boundary

This is an internal authority decision and arithmetic reconciliation. It makes no
bench measurement, vendor approval, fabricated-hardware, thermal or production
claim. Private Library source material remains outside the public repository.
The reproducible check is `LIMITER_SYSTEM_AUTHORITY_CALC.py`; its output and the
full machine-readable decision are retained beside this receipt.

### Signature

**SIGNED_NO_GO — Product / Power / Package / Thermal Authority — 2026-09-17**

Basis: signed HPQ4 v2.0.0, retained prior limiter authority, ADM1175 component
path receipt, exact-nFET receipt, and Librarian indexed evidence at the review
base above.
