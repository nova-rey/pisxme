# Final blocker review v2

Date: 2026-08-20
Question: is there any evidence-backed reason that routing now would be
premature?

## Findings

| Area | Hostile check | Result |
|---|---|---|
| KiCad validation | Can ERC/DRC produce machine-readable evidence? | Yes, via lock-free copy; results are not clean (185 ERC warnings, 231 DRC findings). |
| SXM2 pins | Are K18/K19 classifications consistent with the preserved source? | Corrected: K18/K19 are unresolved auxiliary/protection contacts; K19 is no longer incorrectly classified as GND. |
| SXM2 footprint | Is the 400-pad land pattern manufacturer-matched? | No. Coarse pitch/count passes, exact land/mask/paste/orientation/courtyard remains open. |
| contact current | Does the 0.45 A/contact arithmetic fail? | No: 25–27.5 A V100 load distributes to 0.192–0.212 A per 12 V contact and 0.147–0.162 A per ground contact. PCB thermal/current sharing remains open. |
| PCIe topology | Are TX/RX, coupling, REFCLK, reset, and CLKREQ internally consistent? | Yes at contract level. V100 endpoint acceptance and timing remain empirical. |
| V100 sequence | Is there public NVIDIA timing/enable authority? | No. OCP/OEM material supports platform concepts; simple-carrier evidence supports a direct first attempt. Hardware validation remains required. |
| impedance | Is 85 Ω geometry calculated from a real stackup? | Yes, JLC API returned 84.9966 Ω at 5.2 mil / 2.7847 mil. Fab tolerance and rounded release geometry are not yet quote-confirmed, and the official CM5 90 Ω guidance still needs reconciliation with the requested 85 Ω target. |
| footprints | Are all critical footprints release quality? | No. SXM2, CM5 connector, fuse, fan, UART, and I/O study footprints remain open or unresolved. |
| power | Is high-current input fully pin/thermal resolved? | No. The topology is defined, but final LM74700/MOSFET/fuse/bulk implementation and copper are not routed or thermally signed off. |
| placement | Does the corridor remain plausible? | Yes conceptually; the placement PCB still has no production traces, vias, or zones and has DRC placement violations. |

## Why routing remains premature

1. The hidden 400-joint SXM2 connector has not been matched to an official
   land pattern in the local KiCad footprint.
2. ERC warnings and placement DRC errors are observable, reproducible, and not
   all benign.
3. The JLC calculator result is strong routing input but not a final fab
   tolerance/coupon confirmation.
4. K18/K19 and exact V100 power/reset sequence are still module-validation
   questions. The corrected audit prevents a wrong K19-to-GND connection but
   does not prove that leaving both contacts NC is safe.
5. Several assembly-critical footprints are still study geometry.

## Review result

There is an evidence-backed reason to defer routing. The correct status is
**NOT_READY_FOR_ROUTING**.
