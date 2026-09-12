# Phase 24 BRIDGE_1V1 plane probe rejection

Date: 2026-09-12  
Base: `fc44ebca` normalized ground-return candidate

A disposable native `pcbnew` probe added a full-acreage F.Cu
`BRIDGE_1V1` power zone with 0.20 mm clearance and full pad connection,
then refilled zones. Native KiCad DRC remained 440 violations / 265
unconnected items, with no connectivity improvement. The probe is rejected;
no canonical PCB or power architecture was changed.
