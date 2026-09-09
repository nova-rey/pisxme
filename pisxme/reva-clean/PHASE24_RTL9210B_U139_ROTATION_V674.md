# RTL9210B Path-B V674 — all-pad U1.39 rotation discriminator

V674 removed all surrounding components, copper, and zones but retained the
complete native U1 footprint with every neighboring pad's saved net identity.
For each U1 rotation it added the same 0.20-mm F.Cu U1.39 escape, an ordinary
0.60/0.30-mm through-via, and a short B.Cu tail. This corrects the limitation
of the earlier V666 package probe, which blanked neighboring pad ownership.

Native KiCad 10.0.5 results:

| U1 rotation | DRC violations | unconnected pads | disposition |
|---:|---:|---:|---|
| 0° | 11 | 13 | reject |
| 90° | 1 warning | 13 expected fixture opens | retain |
| 180° | 10 | 13 | reject |
| 270° | 6 | 13 | reject |

The 90° result has no pad short, crossing, clearance, or footprint error;
its one warning is the intentionally free B.Cu tail endpoint. The test does
not close the integrated rail/source field, but proves that the corrected
package and 90° orientation can escape U1.39 when the neighboring 1V1
departure is co-authored.

Raw boards and native reports are retained as
`PHASE24_RTL9210B_U139_ROTATION_{0,90,180,270}_V674.*`.
