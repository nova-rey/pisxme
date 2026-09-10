# Phase 24 storage clock escape receipt — V63–V68

Date: 2026-09-09  
Scope: disposable Path-A storage routing only; production PCB unchanged.

## Result

V63–V66 are rejected XOUT escape implementations. Each preserved the native
USB3 and SATA endpoint audits, but the U11 QFN clock-pad field produced new
XOUT contacts/crossings with adjacent pads or vias.

V67 co-authored XOUT with a rehomed `JMS_XAVDDH` transition. It removes the
prior XOUT/JMS_XAVDDH short and passes the USB3 and complete SATA native
connectivity audits. Native DRC reports 597 violations / 350 unconnected
items, but exposes one selector-side `NC_26`/`STORAGE_SEL` shorting item, so
V67 is not promoted.

V68 repeats V67 without refilling zones. It retains the same selector-side
short and reports 602 violations / 350 unconnected items. This is a control,
not a promotion. The difference between V67 and V68 is saved zone-fill state,
not a claim that the selector issue is solved.

## Authority checks

Both V67 and V68 pass:

- complete CM5-to-JMS583 USB3 endpoint connectivity;
- complete bridge-to-selector-to-M.2 SATA endpoint connectivity;
- no synthetic graph edges were used by the focused audits.

The selector-side short remains a native-board finding and must be resolved
before a clock repair can be promoted. Path-B RTL9210B qualification remains
isolated and is not changed by these Path-A experiments.

## Follow-up selector trials — V69–V71

V69 routes `STORAGE_SEL` north of U13 but introduces XOUT and U14 supply-field
collisions. V70 uses a B.Cu bypass but places its U14 transition too close to
`STORAGE_3V3`. V71 moves that transition outside the U14 pad row and removes
the selector-side `NC_26` short, but native DRC reports a new
`JMS_AVDDL`/`POWER_GND` collision. All are rejected; V54 remains the clean
parent and no production routing changed.
