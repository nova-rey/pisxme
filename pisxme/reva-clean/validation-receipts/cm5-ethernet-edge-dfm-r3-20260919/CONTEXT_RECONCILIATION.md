# CM5/Ethernet edge r3 context reconciliation

The prior integrated rejection used native Light DRC without `--refill-zones` against a candidate whose producer receipt had only run refill in memory; its saved board retained stale zone geometry. That invocation reported 298 violations, including C48–C51 solder-mask/clearance and CM5_5V hole/clearance items.

This bounded r3 producer reapplied the exact local delta from base `ab9e8c73` and persisted a native `pcbnew.ZONE_FILLER` result before saving. The standard no-refill Light command then reports 264 violations / 393 unconnected, matching the refill result and eliminating the lower-edge artifacts. No rule, protected-bus, J1, or high-speed edit was made.

Baseline same-context no-refill: 280 violations / 393 unconnected. Candidate no-refill and fresh detached Light: 264 violations / 393 unconnected; zero shorts, library issues, XIN/XOUT width findings, solder-mask bridges, hole-clearance findings, or copper-edge-clearance findings. C7/C8 courtyard overlap is clear. Remaining DRC findings are outside this package.

The standard command used for the fresh receipt was:
`kicad-cli pcb drc --format json --severity-all --output /workspace/output/fresh-r3-candidate-drc.json --exit-code-violations PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
