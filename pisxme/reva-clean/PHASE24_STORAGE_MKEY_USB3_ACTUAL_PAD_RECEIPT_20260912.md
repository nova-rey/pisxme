# Phase 24 M-key USB3 actual-pad probe — 2026-09-12

## Disposition

**REJECTED as an integrated routing candidate; retained as native endpoint
evidence.** The probe was generated from the saved M-key power candidate and
derived all J7/U12 endpoints from native PCB pads. It is not promoted to the
authoritative board.

## What passed

`phase24_dual_mode_storage_usb3_native_connectivity_audit.py` passed the four
CM5 J7-to-U12 USB3 endpoint pairs using KiCad's saved pads, tracks, and vias.
The selector-to-JMS583 legs were intentionally not authored by this probe.

## Why it was rejected

Native KiCad 10.0.5 DRC reported **518 violations / 427 unconnected items**.
The new paths crossed inherited CM5-area copper, placed ordinary 0.60/0.30 mm
vias too close to the 0.4 mm USB3 pad pitch, and created real pair-to-pair
short/clearance and plane-zone/hole-clearance violations.

Raw report: `PHASE24_STORAGE_MKEY_USB3_ACTUAL_PAD_PROBE_20260912-drc.rpt`.

## Engineering classification

This is a **route implementation failure**, not evidence against the M-key
storage architecture or the TE connector authority. The endpoint audit is
useful native-pad evidence; the copper is disposable and must not be reused.

## Next action

Continue from the M-key pad-authority/power checkpoint with a bounded,
physical-envelope-aware USB3 source/selector route using the actual CM5 escape
geometry and existing validated local support primitives. A fresh KiCad Light
worker validation is required before any focused USB3 PASS is promoted.
