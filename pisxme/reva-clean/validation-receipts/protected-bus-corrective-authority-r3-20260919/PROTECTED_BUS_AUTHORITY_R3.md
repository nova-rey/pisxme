# Protected-bus corrective authority R3

- **Package:** `P24-PROTECTED-BUS-AUTHORITY-R3`
- **Decision:** `PISXME-P24-PROTECTED-BUS-CORRECTIVE-20260919-R3`
- **Status:** `BINDING_DECISION_FOR_PRODUCER; REQUIRES_PROTOTYPE_VALIDATION`
- **Authority:** Product / Power Authority
- **Originating package:** `P24-PROTECTED-BUS-AUTHORITY-R3`
- **Canonical HEAD reviewed:** `0b1b08af2b036bceb916f8984c8bebe365e31178`
- **CAD changed:** no
- **Hardware operated:** no
- **Production qualification claimed:** no

## Decision

Retain the selected conventional protected/distributed 12 V topology and the
three Molex 2x3 source headers with nine independently protected positive /
return pairs. Reallocate the complete source-to-J1 positive-plus-return hot
resistance contract to **8.50 mOhm maximum**. This is a stricter sub-limit
inside the fixed 10.0 mOhm requirement and is required by the protected-voltage
screen at the 45 A bound.

The existing common protection cohort remains `U1 = LM74700QDBVRQ1`,
`Q1 = CSD19536KCS`, `D1 = SMBJ18A`, and `C3 = 100 nF`. Q1 is not being
described as a 2.0 mOhm hot part. TI specifies 2.3 mOhm typical and 2.7 mOhm
maximum at 25 degC, VGS=10 V, ID=100 A. TI Figure 4-8 gives approximately
1.6 normalized RDS(on) at Tc=125 degC, VGS=10 V, ID=100 A. R3 therefore binds
**4.32 mOhm (2.70 x 1.60) as the Q1 design hot bound**, with Q1 case
temperature limited to 125 degC. This is a calculation from a typical curve,
not a production guarantee; the assembled device must be measured or bounded
more tightly before release.

No replacement protection device is selected. The retained exact-NFET record
has no alternative with a guaranteed hot RDS(on) at the actual LM74700 gate
drive and complete VDS/SOA evidence. A replacement may be proposed only by a
new signed authority revision.

## Fixed product and source contract

| Item | Binding value |
|---|---:|
| Source voltage window | 11.4--12.6 V DC; 12.0 V nominal |
| V100 product load | 300 W sustained; 330 W for 100 ms |
| Source capability | 40 A continuous; 45 A for 100 ms |
| Protected-bus screen | 11.05 V minimum at sustained product load; 11.00 V minimum at peak product load; 12.60 V maximum |
| Complete positive-plus-return contract | <=10.0 mOhm hot; R3 implementation cap <=8.50 mOhm hot |
| Ambient / thermal design point | 40 degC ambient, Q1 Tc <=125 degC; exact installed thermal path is a validation gate |
| Fault and sharing policy | no N-1 credit, no passive-sharing credit, no six-loop precision-regulator revival |

The 40/45 A values are source capability and fault/transient screens. The
protected-voltage minima are evaluated both at those current bounds and at the
calculated product current. A 45 A current at 11.4 V through 8.50 mOhm gives
11.0175 V, so it clears the 11.00 V peak screen by 17.5 mV. A 40 A current
gives 11.060 V, clearing the 11.05 V sustained screen by 10 mV. These margins
are intentionally small and require Kelvin measurement; they are not a
claim that the current PCB passes.

At 90% conversion efficiency and 22.7 W of declared low-voltage load:

```text
I_sustained = (300 + 22.7) / (0.90 x 11.4) = 31.452 A
I_peak      = (330 + 22.7) / (0.90 x 11.4) = 34.376 A
drop_31.452A = 0.26734 V; protected = 11.13266 V
drop_34.376A = 0.29220 V; protected = 11.10780 V
```

The source-capability arithmetic leaves 8.548 A continuous and 10.624 A
peak margin over the product-load calculation. It does not prove source
regulation, load-step behavior, or installed connector sharing.

## Complete hot resistance budget

Each number is the maximum for the complete positive-plus-return path at the
specified worst branch. The producer must report the extracted value for every
branch and the common path; unused budget is not evidence and may not be
reassigned without a new authority revision.

| Path term | Hot maximum (mOhm) | Evidence / required closure |
|---|---:|---|
| Selected source harness, mating contacts, and crimps, one positive-plus-return loop | 1.80 | Exact Molex `0039300060 / 39-30-0060` assembly, terminal, wire, length, crimp, and ambient are not yet measured; four-wire hot measurement required |
| One branch fuse, holder, and holder/contact interfaces | 0.55 | `0297015.U` / `178.6165.0001`; retained fuse value is typical and does not qualify holder or hot contact resistance |
| Raw branch PCB positive + return necks | 0.65 | Extract from released stackup, copper thickness, neck geometry, and via field; no trace-width-only credit |
| `12V_BRANCH_JOIN` and `POWER_RETURN_JOIN`, including transition vias | 0.45 | Distributed In2/In4 fields; ordinary through-vias only; no single via carries 40 A |
| Q1 CSD19536KCS channel at hot design bound | 4.32 | TI 2.7 mOhm maximum at 25 degC x 1.6 normalized curve factor at Tc=125 degC; VGS=10 V, ID=100 A data basis |
| Q1 package leads, pads, and positive transition | 0.15 | Kelvin extraction or measurement; not included in the RDS(on) number |
| `12V_PROTECTED` positive + return copper and vias to the J1 field | 0.25 | Native geometry and released fabrication stackup extraction required |
| J1 contact field and local positive/return spreading | 0.25 | SXM2 contact sharing and field spreading remain unmeasured; mapped contacts only |
| Explicit residual accounting margin | 0.08 | Reserved for extraction uncertainty; no unidentified term may consume it silently |
| **R3 total** | **8.50** | **Must be <=8.50 mOhm hot; otherwise candidate fails** |

Q1 dissipation at the hot-bound resistance is 6.91 W at 40 A continuous
and 8.75 W for a 45 A, 100 ms pulse. At the calculated product currents it
is 4.27 W sustained and 5.10 W for the 100 ms peak. TI gives Q1 RthetaJC
maximum 0.4 degC/W and RthetaJA maximum 62 degC/W under its specified test
conditions. The 62 degC/W value cannot be used to claim operation at these
losses. The producer must define the installed copper/heatsink/airflow path,
keep Tc <=125 degC, and return a junction-temperature calculation. A bare
TO-220 board footprint without that path receives no thermal credit.

## Branch enforcement and current sharing

The nine branches are exactly those in the signed nine-branch contract:
J5/J6/J9 pads 1--3 positive, pads 4--6 return, paired 1-4, 2-5, 3-6;
F1--F9 are one positive-series `0297015.U` per pair. Each branch target is
4.444 A continuous and 5.000 A for 100 ms, with a 7.000 A loaded-contact
screen. The 15 A fuse is **fault isolation only** and is not a 5 A current
limiter.

The source assembly and producer validation must enforce these limits by
independent branch access and observation: every branch gets a four-wire
resistance point and a current measurement point; the nine branch currents
must be recorded at 40 A aggregate and during the controlled 45 A/100 ms
pulse. No aggregate source credit is granted until every energized branch is
<=7 A, branch balance is within 10% of the mean, and the worst branch meets
the 1.80 mOhm hot source-assembly term. Any open fuse, missing return,
branch over 7 A, or imbalance over 10% inhibits V100 enable and fails the
source contract. No N-1 or passive current-sharing credit is allowed.

## Power-tree review and sequencing contract

| Rail / path | Static limit and margin | Transient / return / thermal disposition |
|---|---|---|
| Raw source and J5/J6/J9 | 11.4--12.6 V, 40 A continuous, 45 A/100 ms capability; 8.50 mOhm path gives 0.340/0.3825 V at 40/45 A | Harness inductance, connector contact bounce, crimp heating, and source load-step impedance are unmeasured; measure at source and connector Kelvin points |
| Nine fused positive branches | 4.444 A target, 5 A pulse, <=7 A/contact screen; one fuse per branch | Fuse I2t is a typical source value; opening time, holder heating, fault energy, and return path are prototype gates |
| Common TVS / LM74700 / Q1 | 12V_PROTECTED <=12.60 V; Q1 hot design bound 4.32 mOhm | SMBJ18A clamp and energy are waveform-dependent; LM74700 EN/reverse-current behavior, Q1 SOA, gate loop inductance, and TVS/fuse coordination are unproven |
| `12V_PROTECTED` to J1 | 11.05/11.00 V screens above; mapped J1 contacts only | Plane impedance, loop inductance, J1 current sharing, package inductance, and ground bounce require extraction or scope measurement |
| `CM5_5V` U3 | 5.0 V nominal, 3 A design load versus TPSM63606 6 A; 50% nominal utilization; >=30 uF effective output C | TI layout/thermal/PG/EN guidance must be followed; load-step droop, DC-bias capacitance, local return, and thermal rise remain unproven |
| `BRIDGE_3V3` U4 | 3.3 V nominal, 2 A versus 6 A; 33.3% utilization; >=50 uF effective output C | Current canonical census has zero serialized bridge copper/vias; route, loop inductance, PG/EN, return, and thermal closure remain open |
| `BRIDGE_1V1` U5 | 1.1 V nominal, 1 A versus 6 A; 16.7% utilization; prior screen 253.44 uF effective C is below 300 uF conservative screen | Current canonical census has zero serialized bridge copper/vias; DC-bias C, transient droop, thermal, and vendor-layout overlay remain open |
| `POWER_GND` and J1 returns | All nine returns remain distinct to `POWER_RETURN_JOIN`, then `POWER_GND`; no signal/shield return substitution | Static pad/segment/via counts do not establish Zreturn. Ground bounce is `I x Zreturn`; PDN/package data and measured return impedance are missing |

Static IR drop is `I x Rhot`. Transient droop is a separate quantity,
approximately `deltaI x ESR + Lloop x dI/dt + control-loop response`; bulk
energy is `0.5 x C x (V_hi^2 - V_lo^2)` and cannot be credited without the
declared load step, capacitor bias/temperature values, source impedance,
package inductance, and recovery limit. Adding capacitors alone is not an
analysis. No load-step, complete PDN, package, or installed SXM2 contact-field
data exists in the retained evidence, so transient and ground-bounce confidence
is explicitly limited.

Enable/reset/brownout policy is binding for the producer and prototype run:
hold V100 enable/inhibit asserted and endpoint reset held whenever the source
or protected bus is outside 11.00--12.60 V, a branch/protection fault is
reported, a fuse/return continuity check fails, or controlled shutdown is
active. Assert V100 inhibit before source removal where responsive; require
protected-bus discharge and a fresh power-good observation before restart.
Exact SXM2 endpoint sequencing, reset polarity/timing, firmware behavior,
brownout hysteresis, and restart waveform remain `REQUIRES_PROTOTYPE_VALIDATION`.

## Producer scope and stop conditions

The producer may implement only the already-authorized nine-branch source
topology and the R2 fuse placement/corridor authority. It must return:

1. fresh native schematic/netlist/ERC/DRC and exact branch/pad/fuse census;
2. per-branch positive/return copper, via, current-density, and hot resistance;
3. complete path extraction proving every term in the R3 table and total <=8.50 mOhm;
4. Q1 gate voltage, SOA/VDS, hot-loss, case/junction temperature, TVS/fuse I2t,
   connector/harness/contact, and regulator thermal evidence;
5. source/protected/J1 Kelvin measurement points and synchronized current,
   EN/PG/reset/inhibit and temperature capture points.

It may not revive the six-loop limiter, credit U2/Q2 as a parallel protection
stage, assume equal passive sharing, use a 15 A fuse as a 5 A limiter, relax
global design rules, change J1 mapping, or edit unrelated corridors. Failure
to meet any R3 term, branch screen, thermal bound, sequencing rule, or native
connectivity requirement returns a bounded evidence packet to Product/Power;
it does not authorize another unbounded routing attempt.

## Provenance and confidence limits

- HPQ #7 result: `/home/nyx/.local/state/codex-hard-problems/runs/20260919T175244Z-7-sol/result.json`; artifact manifest SHA-256 `7c9ab32f02fd703744a5f8d750c0d0c532d457b8d078be464780b253803e7b7b`.
- TI `CSD19536KCS` local datasheet SHA-256 `046e4114e22acea247ff45074005c749c498012656cd69f2c79922549df0534e`.
- TI `LM74700-Q1` local datasheet SHA-256 `e16b3a8c0023201fafa5825436f5f2dd6f885b92b84e65602b3f50d741c58b6f`.
- `SMBJ18A` authority SHA-256 `4e63353741e69f7f6186e314f8caf93b4b62265166f97e2a32445d1d25280158`.
- R2 upstream authority: `validation-receipts/protected-bus-upstream-authority-revision-20260918/`, fixed source window, nine branches, connector identity, and prior 10 mOhm contract.
- Nine-branch contract: `validation-receipts/power-input-nine-branch-contract-20260918/`, exact branch identities, 7 A contact screen, and no passive-sharing rule.
- Integrated failure: `validation-receipts/protected-bus-integrated-validation-20c9cb12/`, 0.278699 ohm segment-only protected path and 0.6314 ohm segment-only return path before pads, planes, contacts, and thermal effects.

The calculated hot budget is an authority screen, not measured evidence. Load
step amplitude/slew, PDN impedance, capacitor ESR/ESL under bias and temperature,
package inductance, connector/harness hot resistance, via current sharing,
fuse clearing, thermal airflow, and SXM2 endpoint behavior remain confidence
limits and must be labeled `REQUIRES_PROTOTYPE_VALIDATION`.

**Signed scope:** Product / Power Authority, R3 review agent
`/root/power_authority_r3`, 2026-09-19. Any change requires a new decision
version and a new receipt.
