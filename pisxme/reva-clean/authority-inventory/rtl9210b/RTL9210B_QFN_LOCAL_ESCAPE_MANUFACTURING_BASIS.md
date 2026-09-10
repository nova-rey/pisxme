# RTL9210B local QFN escape manufacturing basis

Date: 2026-09-10  
Status: `AUTHORIZED_LOCAL_EXCEPTION_PENDING_NATIVE_IMPLEMENTATION`

## Selected local rule

Use the least-aggressive exception that is expected to clear the 0.4-mm
RTL9210B QFN pad row:

| Region | Trace width | Copper clearance | Via | Via drill |
|---|---:|---:|---:|---:|
| Immediate U1 QFN escape/fanout only | 0.15 mm | 0.15 mm | 0.60 mm | 0.30 mm |
| Normal board routing after handoff | 0.20 mm | 0.20 mm | 0.60 mm | 0.30 mm |

The 0.60/0.30-mm via was retained because the native source-row breakout
passes with it; a smaller via is therefore unnecessary. No via-in-pad,
blind/buried via, or microvia is authorized.

## Manufacturing evidence

JLCPCB's current rigid-PCB capability page states for multilayer boards:

- minimum 1-oz trace width/spacing: 0.09/0.09 mm;
- minimum via hole/diameter: 0.15/0.25 mm, with 0.20-mm hole preferred;
- blind/buried vias are not supported in the stated standard process;
- multilayer 1-oz PTH annular ring: 0.20 mm recommended, 0.15 mm absolute;
- pad-to-track clearance: 0.10 mm minimum;
- via-hole-to-track clearance: 0.20 mm;
- 0.15/0.15-mm trace/clearance is listed as a covered-trace capability.

Source: [JLCPCB PCB Manufacturing & Assembly Capabilities](https://jlcpcb.com/capabilities/pcb-capabilities/),
accessed 2026-09-10. The selected 0.15/0.15-mm local traces are above the
published 0.09/0.09-mm multilayer minimum. The selected 0.60/0.30-mm via
uses the existing ordinary through-via contract and has a 0.15-mm annular
ring.

## Scope containment

The exception rule is width- and net-gated, and applies only to named U1
RTL9210B source-escape nets inside the explicit QFN escape window recorded by
the implementation receipt.
The generator must return to 0.20-mm traces/clearance and 0.60/0.30-mm vias
at the physical handoff. Native DRC must prove both local dimensions and
absence of leakage into the downstream V1603 launch.

This document is manufacturing capability evidence, not a DRC waiver. A
candidate passes only when the saved PCB, native DRC, connectivity audit,
negative controls, and local-rule census all agree.
