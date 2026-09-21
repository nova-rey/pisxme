# Protected-bus R3 S-expression authoring attempt

- Base: canonical `ec40bd2e`
- Method: deterministic S-expression insertion of explicit In2/In3 copper and through-vias, with F.Cu `POWER_GND` zone removal
- KiCad Light validation: `10.0.6`
- Candidate SHA-256: `2089cfcaf1c960677534bee2d42fa2ff36fb5bc6b0af8746c91467317f81f5cf`
- DRC report SHA-256: `f2eda97d449f667e3f3cb94bbdce81468ed358e4bdefdfd1c04bd17f47df04a3`
- Native result: **938 violations / 499 unconnected items**
- Result: **FAIL; not eligible for integration**

This avoided the crashing SWIG construction path and wrote a parseable board, but the generated star corridors do not satisfy the integrated topology. No canonical CAD was changed.
