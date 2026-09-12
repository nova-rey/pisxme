# Phase 24 JMS583 outer VDDREG escape V1 rejection

Starting from the crystal-local V1 candidate, this disposable trial replaced
the rejected same-layer VDDREG route with a local F.Cu/B.Cu/F.Cu escape using
ordinary 0.60/0.30 mm through-vias at `(134,132)` and `(134,125)`.

The explicit complete-support audit passes all ten JMS support endpoint joins
and its trace-removal negative control, including `JMS_VDDREG_5V`. Native
KiCad 10.0.5 DRC nevertheless reports 653 violations / 409 unconnected
items, versus 594/412 for the cumulative AVDDL-U12 baseline and 637/410 for
the crystal-only V1. The candidate is rejected for physical implementation
quality; no VDDREG copper was promoted.
