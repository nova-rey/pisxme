# Phase 24 regulator long-wire probe — rejected

A disposable probe removed the two remaining 65 mm `REGULATORS` wires. The
two endpoint-grid findings changed into two `label_dangling` findings; total
native ERC remained **489 warnings / 0 errors**. Exact exported netlist parity
remained 338 nets with zero changed node sets.

**REJECTED.** These wires are electrically owned by the rail labels and cannot
be removed as unowned stubs. Canonical CAD was not changed.
