# M6 reconstruction status

The source-bound M6 reconstruction did not pass. The active schematic is a flat
legacy design with no authoritative Ethernet, JMS578/M.2, or fixed-UFP SERVICE
hierarchy. Disposable PCB compositions used proxy/reference objects and are
not source authority. The old FAST-A/FAST-B connector-side fragments are
disconnected or stale, and the USB corridor failed under the current placement.

Approved restart boundary: prove the schematic-authoring/tooling path first,
then create source-bound ETHERNET, STORAGE, and SERVICE islands and generate a
disposable PCB through normal schematic/netlist authority. Only a candidate
with native KiCad validation, parity, deliberate returns, pin-map proof, and
mechanical/power closure may be migrated into active PiSXMe.
