# PiSXMe Rev A Clean — Phase 5 calculation record

Checked: 2026-08-30. Status: `PHASE5_CALCULATIONS_CLOSED_WITH_REV_A_EMPIRICAL_RISK`.
The reproducible numerical checks are in
`validation/phase3/phase14_power_calculations.py`.

This is the calculation worksheet for the native power architecture. Values
marked `DESIGN_ENVELOPE` are conservative Rev-A design assumptions and must
not be presented as measured hardware results.

## Locked source and load envelope

The source is a regulated, current-limited 12 V cold-plug bench supply. Two
Molex `0039300020` input branches are mandatory. The electrical design
envelope is:

| Consumer | Envelope | Basis |
|---|---:|---|
| V100/SXM2 | 250 W at 12 V | `DESIGN_ENVELOPE`; endpoint sequencing remains empirical risk |
| CM5 5 V | 3 A | `DESIGN_ENVELOPE`, TPSM output limit is 6 A |
| bridge 3.3 V | 2 A | `DESIGN_ENVELOPE`, TPSM output limit is 6 A |
| bridge 1.1 V | 1 A | `DESIGN_ENVELOPE`, TPSM adjustable-output calculation |

At 90% conversion efficiency, the V100 input current is
`250/(12*0.90) = 23.15 A`. The low-voltage loads add
`(5*3 + 3.3*2 + 1.1*1)/(12*0.90) = 2.10 A`, for a total design-envelope
input current of 25.25 A. A 15 A fuse per branch is therefore acceptable only
with a documented current-sharing limit of at least 12.81 A/branch and a
source/current-limit policy that prevents one branch from carrying the full
load. A single branch cannot carry the full 25.61-A envelope; this is an
explicit system requirement, not a passive-sharing claim. At the shared
envelope, the selected CSD19536KCS has at most
`12.625^2 * 2.7 mOhm = 0.430 W` conduction loss per branch FET. If one branch
carries the full envelope, the same calculation is 1.72 W and violates the
sharing assumption. Sharing, connector, holder, copper, and cold-plug
behavior retain `REV_A_EMPIRICAL_RISK` until routed and fabricated hardware
are checked.

## TPSM63606 calculations

TI datasheet revision B, pages 3–4 and 17, is the calculation authority. The
5 V and 3.3 V divider values are:

| Rail | RFBB | RFBT | Nominal FB check |
|---|---:|---:|---:|
| CM5_5V | 10 kOhm | 40.2 kOhm | `1.0*(1+40.2/10) = 5.02 V` |
| BRIDGE_3V3 | 10 kOhm | 23.2 kOhm | `1.0*(1+23.2/10) = 3.32 V` |

The datasheet requires minimum *effective* COUT of 30 uF at 5 V and 50 uF
at 3.3 V, with 22 pF and 47 pF feed-forward capacitors respectively. The
working implementation therefore starts with multiple 22-uF, 16-V X7R
1210 capacitors, but the count is not closed until the manufacturer DC-bias
curves demonstrate the effective values at each rail. The 1.1 V rail is within
the datasheet's adjustable 1 V minimum. Using `VOUT = 1 V * (1 + RFBT/RFBB)`
gives `RFBT = 1 kOhm`, `RFBB = 10 kOhm`, or 1.10 V nominal. The nearest TI
Table 8-1 frequency row is 1.2 V: `RRT = 2 kOhm`, 400–600 kHz. Rev A uses
that conservative 2-kOhm selection for the 1.1-V rail; switching frequency
and transient behavior remain subject to the vendor-layout review. The conservative
1 V table requirement of 300 uF effective is retained. Sixteen
`GRM32ER71C226KEA8K` 22-uF, 16-V 1210 capacitors are fitted; a documented
Rev-A derating floor of 90% gives `16 * 22 uF * 0.90 = 316.8 uF` effective.
The final DC-bias curve check remains `REV_A_EMPIRICAL_RISK`: the selected
Murata authority is obtainable and the electrical value is known, but the
retained public evidence does not provide a complete exact-part,
board-temperature/DC-bias curve for this 16-part operating point. The 90%
floor is a conservative design assumption, not a vendor measurement.

TI specifies two 10-uF, 50-V input ceramics per module and 68–100 uF bulk
input damping. The native implementation now uses the exact TDK
`C3216X7R1H106K160AC` candidate for those six local input positions.
Each VIN1/VIN2 pair must have local input capacitors to PGND. VLDOIN must be
biased according to the output-voltage condition and receive the specified
optional 0.1–1 uF bypass. AGND and PGND join at the vendor-recommended point.
PG requires a 10–100 kOhm pull-up; EN/SYNC is a separate explicit enable/UVLO
net. CBOOT/RBOOT remain at the internal default unless a slew-rate change is
calculated.

## Closure status

The schematic connectivity and 1.1-V divider/COUT implementation are now
machine-checked by `validation/phase3/test_phase5_power_audit.py` and native
ERC. The V100 endpoint return is explicitly on the shared global
`POWER_GND` net with the dual input-return pins before board routing. The
electrical Phase 5 gate is closed. Residual physical items—branch
sharing, connector/holder temperature, routed-copper drop, exact ceramic
DC-bias at temperature, and vendor-layout thermal overlay—are explicit
`REV_A_EMPIRICAL_RISK` and binding constraints for later routed-board and
fabrication validation.

Provenance: equations and electrical requirements are transcribed from the
local TI `TPSM63606.pdf` and `LM74700-Q1.pdf`; load figures marked
`DESIGN_ENVELOPE` are PiSXMe Rev-A assumptions, not manufacturer claims.
