# Phase 24 PWR_FLAG installed-library probe — rejected

A disposable copy replaced the embedded `power:PWR_FLAG` definition with the
KiCad 10.0.5 installed `power.kicad_sym` definition. Native ERC remained
**489 warnings / 0 errors**, including both `lib_symbol_mismatch` findings.
No canonical source changed.

The direct library substitution is therefore not the correct serialization
repair for these embedded instances. The two mismatches remain open; any
future repair must preserve the instance contract while matching the native
library definition, then prove exact netlist parity.
