# U12 corrected footprint validation — rejected candidate — 2026-09-12

Candidate producer commit: `26192244de387ce921200f2841713291a2af00f7`.
Fresh Light validation reported **401 DRC violations / 499 unconnected items**.
The corrected 0.50 mm perimeter geometry introduced solder-mask bridge errors,
including JMS_AVDDL against U12 pad 35 NC_35; therefore this candidate is
rejected and is not integrated. The existing canonical board remains unchanged.
The report is retained as `u12-drc.txt` because KiCad emitted its native text
report despite the requested `.json` filename.
