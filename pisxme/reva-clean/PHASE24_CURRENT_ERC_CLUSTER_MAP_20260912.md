# Phase 24 current ERC cluster map

Date: 2026-09-12  
Source: native KiCad 10.0.5 report `PiSXMe_RevA_Clean-erc.rpt` generated from
the canonical clean root at committed checkpoint `dad809ec`.

## Live census

| Class | Root | CORE_CM5 | STORAGE | Total | Current interpretation |
|---|---:|---:|---:|---:|---|
| `endpoint_off_grid` | 132 | 0 | 0 | 132 | repeated generated-coordinate/grid contract; investigate transformation before hand edits |
| `isolated_pin_label` | 126 | 0 | 0 | 126 | mixed intentional single-pin labels and authoring patterns; classify by label role before repair |
| `same_local_global_label` | 23 | 5 | 2 | 30 | remaining repeated boundary/circuit naming pattern; must preserve net identity |
| `multiple_net_names` | 0 | 0 | 23 | 23 | STORAGE alias/ownership cluster; resolve from pin/net contracts, never by deleting labels for count reduction |
| **Total** | **155** | **5** | **25** | **311** | zero native severity-error findings |

## Remediation order

1. `endpoint_off_grid`: highest leverage if one generator/coordinate cause is
   confirmed. Use a disposable source transformation, native ERC, and exact
   netlist parity before promotion. Do not normalize coordinates by warning
   count alone.
2. `isolated_pin_label`: classify local labels, global labels, hierarchy
   contracts, and no-connect intent. Promote only identity-preserving repairs;
   isolated labels attached to an intentional single pin are not automatically
   defects.
3. `multiple_net_names`: inspect the 23 STORAGE findings against the native
   pin contracts and current alias decisions. Preserve intentional aliases and
   reject any change that alters net ownership or node sets.
4. `same_local_global_label`: repair only after the label's scope and intended
   cross-sheet contract are proven; the earlier duplicate hierarchical-label
   repair is already promoted and must not be re-decided.

## Gate and evidence boundary

This map is analysis, not a waiver. Every systemic repair must be tested on a
disposable copy with native ERC, exact semantic netlist comparison, and the
relevant hierarchy/parity checks. The current canonical source remains open;
the zero-error count does not close the warning clusters.
