# Phase 24 JMS583 local fine-pitch escape receipt

Date: 2026-09-12  
Status: `LOCAL_ESCAPE_PASS`

## Decision

The authorized local exception is implemented on the frozen U11/Y10 support
placement: XIN and XOUT use 0.10 mm tracks in the immediate QFN/crystal escape,
with the normal routing profile restored outside that field. No smaller vias,
microvias, via-in-pad, blind vias, or buried vias were introduced.

The XIN departure leaves U11 pad 50 north, then uses a west-side monotonic
corridor. XOUT uses the corresponding east-side corridor. The VDDREG source
keeps its separate ordinary-via path and no longer crosses XIN.

## Fresh KiCad Light evidence

Candidate source ref: `0bbc29c1`  
Worker: `jms583-fine-escape-v9`  
Native KiCad DRC: 612 violations / 409 unconnected items on the inherited
acreage baseline. There are no `shorting_items`, `solder_mask_bridge`, or
JMS583-local `tracks_crossing` findings. Two reported crossings are inherited
`JMS_AVDDL`/`USB_RXN1` full-board copper. The remaining DRC population is also
inherited or outside this local escape and remains open for Phase 24 closure.

Saved-object checks all pass:

| Check | Result |
|---|---|
| Complete ten-branch JMS583 support connectivity | PASS |
| Trace-removal negative control | PASS |
| Native U11 support endpoint audit | PASS, 7/7 |
| Fine-rule saved-board scope | PASS |
| XIN/XOUT local 0.10 mm geometry | PASS |
| Fine-net via policy | PASS, none present |
| USB3/storage architecture | unchanged; recheck required at integration |

The subsequent fresh-Light storage-integrated recheck also passes the
dual-mode USB3 endpoint set (10/10), M.2 power-owner connectivity (9 contacts)
and its negative control, the JMS583/selector library audit, the dual-mode
schematic audit, and the AUTO/FORCE mode contract. Its raw native DRC is
retained as `PHASE24_STORAGE_AFTER_JMS_FINE_ESCAPE-drc.rpt`.

Known KiCad 10.0.6 enum-property assertions during load are the same tool
noise recorded by prior fresh-Light receipts; they do not alter the saved
board or the audit result.

## Promotion boundary

This closes the JMS583 local escape discriminator, not the full acreage DRC or
Phase 24. The generated board and raw DRC/negative-control artifacts are
retained as the promotion candidate. Canonical production copper is not
silently replaced until the candidate is integrated and the affected storage,
USB3, parity, and native full-board checks are rerun.
