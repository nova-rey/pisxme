# Phase 24 storage USB3 support V138 receipt

V138 is a reduced local fixture with U12 rotated 180 degrees. This tests the
storage-local selector orientation as a distinct launch class while retaining
the same U11, C86/C87, net ownership, JLC rules, and ordinary-via policy.

Results:

- Native local support connectivity remains present for all six U11/U12 USB3
  support nets.
- Native DRC: 4 violations: two real target-via shorts into the opposite RX
  corridors and two silkscreen warnings.
- No production board, schematic, or accepted V127 copper was changed.

V138 is rejected. The orientation reduces but does not eliminate the target
launch conflict. A clean continuation requires coordinated U12 pad-launch
regeneration (including the CM5 source escape) or a different validated local
selector/package implementation; it is not justified to waive the native
shorts.
