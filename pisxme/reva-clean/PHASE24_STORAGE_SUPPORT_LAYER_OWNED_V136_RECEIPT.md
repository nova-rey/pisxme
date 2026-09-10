# Phase 24 storage USB3 support V136 receipt

V136 is a disposable local fixture derived from the V127 support parent with
only U11, U12, C86, and C87 retained. It tests package-aware mixed-layer
support routing from the saved native pads, independently of acreage copper.

Results:

- Native dual-mode endpoint audit: the six local U11/U12/cap assertions pass.
- Native DRC: 4 violations, comprising one U11 source-via clearance, one U12
  target crossing, and two silkscreen warnings; 32 omitted support/power
  connections are expected in this reduced fixture.
- No synthetic graph edges were used.

The result is rejected. The local fixture separates inherited-board failures
from an intrinsic package-escape constraint: the current QFN pad-field
dogbones/via placement do not meet the active 0.15 mm clearance profile. The
next candidate must use a different package-aware escape/side assignment or a
properly authoritative footprint/routing basis; it must not be promoted by
waiving the native findings.
