# MPA binding storage/power placement and corridor decision — 2026-09-13

Authority: Macro Placement Authority. This decision supersedes speculative route attempts and is the sole producer basis for the next storage/power implementation.

Baseline candidate: `5e891537`; PCB SHA-256 `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`; fresh Light result 300 DRC violations, 499 unconnected, zero shorts, two inherited crossings, 15 open Path-A pairs.

## Binding placement

- U13 `(180,135)`, top, 180 degrees.
- C30 `(103.5,116)`, C32 `(103.5,120)`, C33 `(103.5,128)`, C31 `(103.5,132)`, top, 180 degrees.
- F2 `(90,60)`, top, 0 degrees.
- D2 `(110,60)`, top, 0 degrees.

Fixed: board outline, J1/J3/J5/J6/J7, U1/U2/Q1/Q2/C4/F1/U7/U11/U12/U14, U11 support, GATE_B copper, CM5 USB3/PERST, V100_PET0, J1 PCIe/reference, J3 storage-power copper, and power/ground zones. U4/U5 cohorts remain power-authority owned.

## Binding corridor ownership

- U7 to C30–C33: short F.Cu escapes, then separate B.Cu lanes.
- C30–C33 to U13: separated TX F.Cu and RX B.Cu channels, clear of USB_RXN1.
- U13 SATA ports to J3: four ordered differential corridors with transitions outside keepouts.
- STORAGE_SEL: dedicated lower/east corridor U12.9/U13.9 to U14.4.
- AUTO_PEDET: J3.69 to J8.2; MODE_IN remains U14.2 to J8.4.
- Branch-B raw: J6.1 to F2.1–4, then U2.3/C4.2.
- Branch-B fused: F2.5–8 to D2.1, then U2.6/Q2.1; GATE_B and Q2 pad 3 untouched.

Use ordinary through-vias and normal net-class geometry. The authorized fine-pitch exception remains limited to its existing scope. No shared vias, guessed coordinates, synthetic connectivity, global rule relaxation, or controlled-impedance width widening.

The producer must materialize these transforms from native footprints, route incrementally in one isolated qualified KiCad Light worker, and return a candidate plus targeted connectivity/DRC. A structural contradiction may return once to MPA; no unrestricted variants are authorized.
