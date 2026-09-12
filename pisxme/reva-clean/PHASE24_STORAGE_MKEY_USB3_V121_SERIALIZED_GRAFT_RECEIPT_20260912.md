# Phase 24 M-key USB3 V121 serialized graft — 2026-09-12

## Disposition

**REJECTED for integrated promotion; retained as the current best source
escape basis.** The historical V121 fixture was independently known to have
zero DRC violations in isolation and complete four-net J7-to-U12 endpoint
connectivity. Its route objects could not be iterated by the current pcbnew
binding, so the four-net native serialized segment/via records were recovered
from the saved KiCad file and grafted into the current M-key power candidate.

## Native evidence

The current saved-board four-link audit passes all four J7-to-U12 USB3 pairs
and its serialized-track removal negative control. KiCad 10.0.5 integration
DRC reports **505 violations / 427 unconnected items**. The new launch has
real crossings and clearance/hole-clearance interactions at U12, including
crossing the existing `CM5_PERST` corridor; it is not production-ready.

Fresh detached KiCad Light validation reproduced all four endpoint passes and
the negative control, and reported **507 violations / 427 unconnected items**.
The two-count tool-version delta is recorded; it does not alter the rejection.

## Classification

This is a **route integration failure**, not a failure of the V121 source
escape topology or the M-key storage architecture. The recovered V121
geometry is the preferred starting basis for the next local U12 launch
repair, with actual current-board obstacles explicitly reserved.
