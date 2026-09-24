# Tier-2 Unblocker — explicit via-only selection

- Package: P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER
- Prior failure: second split transaction selected existing `12V_IN_A` B.Cu copper instead of the committed `PWR_SRC_J5_P2` via.
- Root cause: all selection classes enabled; ambiguous board click.
- Method change: after first transaction and In2 selection, disable `All items`, enable only `Vias`, click via near `(24.5,25.0)`, open properties and verify net `PWR_SRC_J5_P2`, cancel without edits, then press `x` and require route status `PWR_SRC_J5_P2` at 0.2 mm before continuing to F2.1.
- No topology, rules, placement, or corridor change.
