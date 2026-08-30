# Hostile simplicity review

Mandate: assume early AI-derived assumptions may have created inherited
complexity; identify deletions that preserve only the actual PiSXMe
requirements.

## Independent review result

The delegated read-only reviewer returned **PASS WITH RESERVATIONS**. It found
no second-SXM2/NVLink/x16 implementation, no accidental HDMI/MIPI/SD/RJ45/hub
block, and no proven redundant via family. It independently identified the
reversible Type-C FAST ports as the material simplification opportunity and
recommended a USB-A future variant.

The reviewer’s reservations remain valid: the current package is an
external-review artifact rather than a final fabrication release, D1 requires
pre-fab provenance closure, and any USB-A replacement still needs a complete
power/ESD/USB2 implementation.

## Attacks and findings

| Attack | Finding | Disposition |
|---|---|---|
| Remove unused PCIe lanes | Only lane 0 is present; no unused lane copper or AC caps | Already minimal |
| Remove second GPU/NVLink baggage | None found; one J1 only | Already minimal |
| Remove native Ethernet/HDMI/MIPI/SD | None implemented | Already minimal |
| Remove Type-C muxes | Direct official CM5IO Type-A precedent and clean disposable trial support removal in a future revision | Recommended future simplification |
| Remove Type-C CC logic | Valid for fixed host Type-A, not for current Type-C | Recommended only with connector change |
| Remove all USB3 ESD | Official CM5IO USB3 sheet does not identify dedicated USB3 ESD, but board protection is a separate risk decision | Do not remove silently; re-evaluate in variant |
| Remove VBUS current limiting | Unsafe for host ports | Must retain in future variant |
| Remove service DRP/recovery | Breaks provisioning/debug requirement | Keep |
| Remove UART | Leaves no independent boot/debug path | Keep |
| Remove fan/pump controls | Conflicts with 300 W-class thermal contract | Keep |
| Remove debug test points | Possible BOM/area saving, but harms Rev-A bring-up | Optional, not urgent |

## Review conclusion

The active board is not secretly a general-purpose carrier, but its Type-C
FAST-port choice is a real inherited complexity multiplier. The disposable
USB-A result is strong enough to recommend changing the architecture before a
new external-review submission, while preserving the active board for
traceability.
