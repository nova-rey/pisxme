# Phase 24 STORAGE NC-alias probe — rejected

## Hypothesis

Remove an `NC_*` ordinary label whenever a non-`NC_*` label occupies the same
exact coordinate, to eliminate redundant `multiple_net_names` warnings.

## Disposable result

The probe was run against the promoted duplicate-label baseline in an isolated
copy. Native KiCad 10.0.5 ERC changed from 377/0 to 369/0:

| class | baseline | probe |
|---|---:|---:|
| endpoint_off_grid | 197 | 197 |
| isolated_pin_label | 126 | 139 |
| same_local_global_label | 30 | 30 |
| multiple_net_names | 24 | 3 |

The exported semantic netlist changed from 338 nets to 354 nets: zero missing
baseline names, 16 extra names, and 11 changed node sets. The apparent warning
reduction therefore changes electrical/netlist intent and is rejected. No
canonical source changed. The `NC_*` labels remain current until each alias is
classified from its symbol/pin contract.
