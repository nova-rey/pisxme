# PiSXMe Rev A V100/SXM2 prototype first-power contract

- **Package:** `P24-V100-PROTOTYPE-FIRST-POWER-CONTRACT`
- **Contract:** `PISXME-P24-V100-FIRST-POWER-20260917`, revision `1.0`
- **Assigned base:** `c2e0194c432e712d6f8386b9682f038dd06188e6`
- **Status:** `SIGNED_PROTOTYPE_VALIDATION_CONTRACT`
- **Signed scope:** PiSXMe Board Bring-up / Power Supervisor
- **Date:** 2026-09-17
- **CAD changed:** no
- **Hardware operated:** no
- **Production qualification claimed:** no

This contract defines the safe, staged procedure for first power and initial
V100/SXM2 bring-up after a prototype board exists. It is a validation plan and
stop rule set. It is not evidence that fabricated hardware works and it does
not waive any open Phase 24 source, protection, copper, thermal, sequencing,
or integrated ERC/DRC requirement.

## Governing authority

The signed Product/Power decision
`PISXME-P24-POWER-ARCH-20260917` selects an adequately rated external 12 V
input assembly feeding an ordinary protected common/distributed 12 V V100
power plane. It permits separately protected input paths where the exact input
assembly requires them, gives no passive-sharing credit until that assembly is
qualified, and does not require precision current regulation per SXM2 contact
group.

The product requirements remain 300 W sustained V100 operation and a retained
330 W bounded design-peak allowance. Those values are product requirements,
not measurements made by this procedure. The source voltage tolerance,
connector/harness assembly, protection energy, bus drop, thermal installation,
and load-step contract must close before a full-envelope test is attempted.

The following are explicitly `REQUIRES PROTOTYPE VALIDATION` because the
current evidence does not establish a complete standalone endpoint contract:

- V100/SXM2 enable, reset, inhibit, and power-good sequencing at this carrier;
- startup current, peak/load-step amplitude and slew at the installed carrier;
- current distribution through the mapped SXM2 contact field;
- installed connector, harness, copper, protection, and cooler temperature
  rise under load;
- behavior after input brownout, protection trip, controlled shutdown, and
  restart;
- PCIe enumeration and GPU firmware/driver behavior on the assembled system.

The old six-loop, no-passive-sharing, 6.000--6.400 A, precision-limiter, and
57 mOhm allocation is historical evidence only. This procedure does not use
those superseded constraints as acceptance criteria.

## Preconditions and equipment

Do not begin the V100 stages until these preconditions are recorded:

1. The assembled board revision, J1 orientation, input connector/harness
   parts, fuses or equivalent fault-isolation parts, protection parts, cooler,
   and mechanical supports match the released assembly record.
2. The integrated Phase 24 candidate has passed its applicable schematic,
   connectivity, ERC/DRC, source/bus, return, protection, and DFM gates. An
   open CAD power row is not converted into a hardware experiment by this
   contract.
3. A Power Authority source/bus record names the exact source voltage range,
   current capability, connector/harness limits, protection thresholds,
   shutdown behavior, and allowable drop/temperature margins. Until that
   record exists, only the low-energy board-only checks below are allowed.
4. Cooling hardware is installed or the particular stage is explicitly
   declared cooling-independent. Fans/pump control, power, and tach/flow
   observation are ready before V100 enable.
5. The operator has an accessible source-disable or emergency disconnect,
   a current-limited regulated source with current readback, two DMMs, and a
   scope or equivalent transient recorder. A differential probe or isolated
   measurement method is required for floating/high-current nodes.
6. A calibrated current probe or known Kelvin shunt, thermocouples or a
   calibrated thermal camera, and a host log path are available. Record serial
   numbers, calibration status, bandwidth/range, and sample rate in the run
   record; do not invent values when an instrument is unavailable.

The source is initially set to **12.0 V**. Do not exceed the exact source
maximum later approved by Power Authority. The staged current limits below are
test-energy ceilings, not claims about the current required by the V100:

| Stage | Initial source-current ceiling | Purpose |
|---|---:|---|
| Unloaded board and rail checks | 1 A | Catch shorts and protection faults with limited energy |
| CM5-only checks | 2 A, then 5 A only after stable review | Bring up host and local rails without V100 load |
| V100 installed, inhibit asserted | 1 A, then 5 A | Check installation and standby path without enabling the endpoint |
| First enabled low-load test | 10 A, then 20 A | Incremental observation before any declared product envelope |
| Full-envelope test | Only the signed source/bus limit | Requires completed source, drop, protection, thermal, and load-step gates |

If a lower limit is required by the signed source contract or component
ratings, the lower limit governs. If a stage repeatedly reaches its current
ceiling after capacitive settling, disable the source and investigate; do not
raise the limit merely to force progress.

## Staged procedure

### 0. Unpowered inspection and resistance checks

With the source disconnected and all modules removed:

- Inspect the board under magnification for solder bridges, damaged pads,
  reversed parts, connector orientation, fuse population, exposed copper,
  cooler/backplate interference, and foreign material.
- Verify raw input polarity, protection direction, fuse continuity, return
  continuity, and that service USB VBUS is disabled before an external host is
  connected.
- Measure resistance and diode behavior from each raw input, protected 12 V,
  `CM5_5V`, `BRIDGE_3V3`, `BRIDGE_1V1`, service VBUS, and the mapped J1 12 V
  contacts to their returns. Record the time-dependent charging behavior and
  final value. A stable near-short, unexpected diode path, or a value
  inconsistent with the assembled capacitor/regulator model is an abort.
- Verify no unknown SXM2 contact is tied to a driven net solely to obtain
  parity with a contact map. Unknown contacts remain no-connect until an
  authority record changes that disposition.

### 1. Cold-plug and protected-bus check, modules absent

Set the regulated source to 12.0 V with a 1 A current ceiling. Keep CM5,
V100, storage devices, and other removable loads absent; hold all enables,
resets, and V100 inhibit in their safe inactive state.

Capture source voltage/current, raw input voltage, protected-bus voltage,
input polarity, protection status, and any inrush waveform. Confirm that no
USB/service input back-powers the board, no protection device heats
unexpectedly, and no source current limit remains engaged after capacitive
settling. Power off if the source enters current limit persistently, a rail
rises without its enable, or a protection fault cannot be explained.

### 2. Local regulator and control-rail check

With V100 and CM5 still absent, enable only the rails allowed by the
schematic's cold-plug policy. Increase the source ceiling only within the
staged table and signed source contract. Measure at the regulator output and
at the load-side test point:

- `CM5_5V`: 5.0 V nominal, using the exact TPSM63606/regulator tolerance and
  load limits in the released power record;
- `BRIDGE_3V3`: 3.3 V nominal, using the exact regulator tolerance and load
  limits in the released power record;
- `BRIDGE_1V1`: 1.1 V nominal, using the exact regulator tolerance and load
  limits in the released power record;
- each `EN`, `PG`, reset, and inhibit signal, including asserted/deasserted
  polarity and timing relative to the rail;
- raw/protected 12 V at the source, input protection, and J1 field, with
  differential measurements where return drop matters.

Do not substitute nominal values for the manufacturer's min/max limits. A
rail outside its allowed range, unstable power-good, unintended enable, or
reset/inhibit transition is a failure and requires power-off before probing
or rework.

### 3. CM5-only bring-up

Install the CM5 and its support/cooling hardware while V100 remains absent.
Start at a 2 A source ceiling after the unloaded rail check; raise to 5 A only
after the source, input protection, and rails remain stable. Confirm CM5 5 V,
ground/reference behavior, boot, UART, service USB role, USB3 paths, Ethernet,
storage-control signals, fan/pump controls, and reset/recovery behavior.

Keep service VBUS disabled before attaching an external recovery or
provisioning host. Record whether any role transition is explicit and
measured; do not assume automatic VBUS handoff is safe.

Abort on source current limit, rail droop outside its declared range, reset
loop, unexpected back-power, loss of cooling control, or a temperature rise
that approaches the applicable component/connector limit.

### 4. V100 installation and inhibited-power check

Install the V100, cooler, backplate, and required mechanical supports only
after CM5-only checks are stable. Confirm fan/pump operation before applying
V100 power. Keep V100 enable/inhibit asserted safe and set the source ceiling
to 1 A, then 5 A only after the first check is stable.

Check J1 seating and orientation, raw/protected 12 V at the mapped power
field, all returns, auxiliary/standby observations permitted by the verified
J1 contract, and the `PERST#`/inhibit/enable state. Do not drive an unknown
contact or infer a required contact-group current from the presence of a
power pad.

### 5. First enabled low-load test

Enable the V100 only when cooling is active, the control truth table is in its
approved state, and stages 0--4 have passed. Use the lowest reproducible GPU
load. Set a 10 A source ceiling, observe for a defined dwell recorded in the
run log, then power down before changing the ceiling. A 20 A ceiling may be
used for the next bounded step only when the prior step has no abnormality and
the source/bus record permits it.

At each step capture synchronized source/protected-bus voltage, input current,
J1 power-field voltage, rail voltage, `EN`/`PG`/reset/inhibit state, GPU/CM5
telemetry, connector/harness/copper/protection/regulator temperatures, fan or
pump response, and PCIe/driver logs. A source current-limit event is a fault
observation, not a passing load point.

### 6. Product-envelope testing

Only after the exact source/bus, protection, copper/return, thermal, cooling,
and load-step gates are signed may the operator test the 300 W sustained
requirement or retained 330 W bounded peak allowance. Define the load waveform,
duration, source impedance, measurement bandwidth, allowable droop/recovery,
thermal limits, and shutdown policy in the Power Authority run sheet first.

This contract supplies the safe sequence and observations; it does not claim
that the full product envelope has been reached or measured.

## Mandatory shutdown criteria

Disable the source immediately and preserve the run record if any of the
following occurs:

- smoke, odor, arcing, visible damage, connector discoloration, unexpected
  mechanical movement, or loss of cooler contact;
- source current reaches its ceiling after capacitive settling, a fuse or
  protection device trips unexpectedly, or a parallel input path shows an
  imbalance outside its signed assembly limit;
- raw/protected 12 V or any low-voltage rail leaves the exact declared
  operating range, shows uncontrolled overshoot/oscillation, or droops and
  fails to recover as specified;
- `EN`, `PG`, reset, `PERST#`, or V100 inhibit has an unsafe state, unexpected
  transition, or restart loop;
- any component, connector, harness, copper region, or cooler reaches its
  published absolute maximum or the lower test limit established by the
  Power/Thermal Authority margin;
- temperature rises beyond the applicable connector/harness temperature-rise
  limit, rises rapidly without stabilizing, or its measurement is invalid;
- cooling/fan/pump operation is lost, GPU telemetry is unavailable when it is
  required for the test, or PCIe failure is accompanied by abnormal rails or
  current;
- an operator cannot explain the current path, return voltage, power-good
  state, or protection response from the captured evidence.

For a fault, assert V100 inhibit or disable the endpoint first when that
control is responsive, then remove source power using the emergency
disconnect. Allow rails to discharge, verify no hazardous residual voltage,
and do not reapply power until Power/Bring-up Authority reviews the captured
state. Never clear a protection trip by cycling power without recording why it
tripped.

## Run record and acceptance

The run record must include the contract revision and board/source SHA, board
revision and serials, component/harness/fuse identities, instrument IDs and
calibration status, source setpoints/readbacks, current limits, all rail and
control measurements, synchronized waveforms, temperatures, cooling state,
host/PCIe/GPU logs, operator, timestamp, and raw artifact hashes.

Each stage is recorded as `PASS`, `FAIL`, `UNPROVEN`, or
`REQUIRES_PROTOTYPE_VALIDATION`. `PASS` means only that the stated stage's
measurements satisfy the exact declared limits at that run. It does not prove
the entire board, 300 W product capability, manufacturing readiness, or
fabricated-hardware behavior beyond the measured scope.

The contract is complete as a design artifact when this procedure, its
machine-readable stage/limit/stop records, and its receipt are committed at a
known source SHA. The prototype remains unvalidated until a future run
produces the raw evidence described above.

