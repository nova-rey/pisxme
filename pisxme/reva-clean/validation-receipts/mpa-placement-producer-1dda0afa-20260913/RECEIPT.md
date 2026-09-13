# MPA placement producer candidate — 2026-09-13

Producer base: `c7d02acf`; disposable Light workspace; candidate commit `1dda0afa` (worker-local). This candidate materializes only the MPA-authorized native transforms for U13, C30–C33, F2, and D2. No routing or rule changes were made.

Targeted native KiCad 10.0.6 DRC on the producer candidate reported 391 violations, 499 unconnected items, and no reported shorting-items. Raw DRC, return code, changed-position list, patch, candidate PCB, and hashes are retained here. The result is a producer candidate, not an integration or closure result. It worsens the baseline census from 300 to 391 DRC violations, so no integration is authorized without MPA reassessment or a materially bounded route implementation that explains the context.
