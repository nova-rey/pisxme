# Active-design hash verification

The architecture sanity audit was read-only with respect to the active design.

| File | Before audit | After audit | Result |
|---|---|---|---|
| `pisxme/PiSXMe.kicad_pcb` | `de3f3ff6e375029b62e4f4cd4285d9477d88a7dbf1137c34498adb9a6b580f4e` | `de3f3ff6e375029b62e4f4cd4285d9477d88a7dbf1137c34498adb9a6b580f4e` | IDENTICAL |
| `pisxme/PiSXMe.kicad_sch` | `b9ba4290d6274e85caf82b1111fd5f1badba00299a08014cec9e36bdbce92406` | `b9ba4290d6274e85caf82b1111fd5f1badba00299a08014cec9e36bdbce92406` | IDENTICAL |
| `pisxme/PiSXMe.kicad_dru` | `681a9397b053ed62c006af1e01f83fb4994368c1022a30ac9f2760edb727afd9` | `681a9397b053ed62c006af1e01f83fb4994368c1022a30ac9f2760edb727afd9` | IDENTICAL |

The USB-A board and all supporting routing artifacts are disposable and live
under `experiments/usb-a-simplification/`.
