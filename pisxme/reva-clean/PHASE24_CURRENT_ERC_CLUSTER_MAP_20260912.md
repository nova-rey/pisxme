# Phase 24 current ERC cluster map

Date: 2026-09-12  
Source: fresh native KiCad Light report generated from the canonical clean root
at committed checkpoint `097de6a4`; worker environment classifications are
listed separately from project electrical warnings.

## Live census

| Class | Root | CORE_CM5 | STORAGE | Total | Current interpretation |
|---|---:|---:|---:|---:|---|
| `endpoint_off_grid` | 121 | 0 | 0 | 121 | repeated generated-coordinate/grid contract; Ethernet support-group grid repair is promoted |
| `isolated_pin_label` | 126 | 0 | 0 | 126 | mixed intentional single-pin labels and authoring patterns; classify by label role before repair |
| `same_local_global_label` | 23 | 5 | 2 | 30 | remaining repeated boundary/circuit naming pattern; must preserve net identity |
| `multiple_net_names` | 0 | 0 | 22 | 22 | STORAGE alias/ownership cluster; one safe M2_GND normalization is promoted |
| **Total electrical** | **143** | **5** | **25** | **300** | zero native severity-error findings |

Fresh Light additionally reports 53 `lib_symbol_issues` and 3
`footprint_link_issues` from the worker environment, for 356 total findings.

## Remediation order

1. `endpoint_off_grid`: the Ethernet support-group coordinate cause is now
   repaired and validated; the remaining 121 require separate classification.
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
