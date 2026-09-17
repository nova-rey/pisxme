# Exact nFET / energy requalification against HPQ4

Package: `P24-EXACT-NFET-ENERGY-AUTHORITY`  
Status: `WAITING_ON authority:power-current-limiter-selection`  
Review base: `a49ed4d9b381ffe9f68bd22224861cd656bae490` (`reva-clean`)  
CAD changed: **no**  
Product envelope changed: **no**

## Binding result

The signed HPQ4 Product/Power Authority contract requires each of six
independent loops to deliver **6.000–6.400 A**, requires an nFET hot
`RDS(on) <= 15.625 mOhm`, and requires separate proof of actual gate drive,
VDS/reverse-current behavior, fault waveform, SOA/I2t, TVS, fuse, harness and
protected-copper interactions. HPQ4 explicitly rejects the prior
`MAX17527AATP+T` with 6.25 kOhm as the production current-contract basis
because its guaranteed minimum is 5.754245754 A.

Consequently, the production limiter and its actual external gate-drive/fault
contract are not yet bound. No nFET can be promoted or released to CAD from
this package. This is an internal authority dependency, not an external
blocker.

## Candidate screen

| Candidate | Evidence that helps | Closure failure |
|---|---|---|
| `STL125N10LF8AG` | 100 V, 5.8 mOhm maximum at 4.5 V / 30 A / 25 C, -55..175 C, 100% avalanche tested, published SOA | No guaranteed 4.45 V maximum; hot RDS curve is typical; a 5.8 mOhm 25 C value would need a temperature/installation multiplier no greater than `15.625/5.8 = 2.69397x`; VDS transient and system fault energy remain unbound |
| `BSC096N10LS5` | 100 V, 12.5 mOhm maximum at 4.5 V / 10 A / 25 C, SOA through 175 C | No guaranteed 4.45 V maximum; only `1.25x` hot allowance; system transient remains unbound |
| `CSD18536KCS` | 2.2 mOhm maximum at 4.5 V / 100 A / 25 C, SOA data | 60 V VDS is not accepted without the PiSXMe negative/transient envelope; no guaranteed 4.45 V maximum |

The ST datasheet's 4.5 V value is a maximum at 25 C; its hot curve is
characterization data. The current HPQ4 contract therefore does not permit
silently treating it as a 15.625 mOhm hot guarantee.

## Fault and energy reconciliation

The ADI MAX17527A record remains useful only as a legacy controller oracle:
its public datasheet describes 4.45 V minimum / 4.75 V typical / 4.95 V
maximum external gate drive, an internal fast-trip comparator that turns off
its internal nFET within 3 us at a typical 24 A threshold, the external nFET
remaining on during that event, approximately 200 us internal re-enable
sequencing, and typical reverse-current response values of 108 ns fast and
17 us slow. A conservative illustrative `32 A, 3 us` screen is
`0.003072 A^2 s`; at the 15.625 mOhm cap the simplified FET energy is 48 uJ.
These are not production closure values because the controller itself is
rejected by HPQ4 and the screen omits harness inductance, TVS clamp trajectory,
fuse clearing, source impedance, PCB copper and actual limiter tolerances.

At the HPQ4 static ceiling, an idealized FET at the hot cap dissipates 0.5625 W
at 6.000 A and 0.6400 W at 6.400 A. These are contract screens, not installed
thermal evidence.

## Gate disposition

| Gate | State | Required resume evidence |
|---|---|---|
| Production limiter and actual gate drive | `WAITING` | Power Authority selection satisfying HPQ4 6.000–6.400 A and 57 mOhm hot limiter cap, with guaranteed gate-drive range |
| nFET hot RDS at actual minimum gate | `UNPROVEN` | Manufacturer guarantee or bounded production qualification at actual minimum gate and temperature |
| VDS / reverse / TVS envelope | `UNPROVEN` | Signed source, reverse-polarity, harness L/R and TVS clamp envelope |
| Fast-fault SOA/I2t | `UNPROVEN` | Exact limiter/fuse/TVS/harness/copper waveform and worst-case SOA/I2t calculation |
| Six-loop fault policy | `UNPROVEN` | Fail-safe FLAG aggregation, V100 inhibit/reset and branch-loss truth table |
| Installation thermal/package/copper | `UNPROVEN` | MPA/Thermal authority installation and extracted protected-copper margins |

## Sources and provenance

- Signed HPQ4 input: `validation-receipts/power-budget-correction-20260914/POWER_BUDGET_CORRECTION.json`, SHA-256 `321e4d14c3696d1d24c9ccb54c17526e339786b527e73b54b1ebd0100c501eae`.
- Librarian packet: `validation-receipts/exact-nfet-energy-dossier-20260914/EXACT_NFET_ENERGY_DOSSIER.json`.
- ST DS14632 Rev 3: https://www.st.com/resource/en/datasheet/stl125n10lf8ag.pdf
- ADI MAX17527A Rev 0: https://www.analog.com/media/en/technical-documentation/data-sheets/max17527a.pdf

No vendor PDF or restricted material was copied into public project history.
No measurements, vendor approval, production qualification or CAD release is
claimed.

## Next action

Keep this package waiting on `authority:power-current-limiter-selection`.
After that authority returns, recompute the nFET gate-drive, VDS, reverse,
fault waveform, SOA/I2t and thermal checks against the exact selected limiter;
then return a new authority candidate for independent review.
