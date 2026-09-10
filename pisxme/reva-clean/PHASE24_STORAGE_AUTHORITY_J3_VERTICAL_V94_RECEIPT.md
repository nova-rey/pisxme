# V94 storage-rail connector escape — 2026-09-10

V94 starts from source-authority-corrected V91 and uses the U14.5 storage
rail. It replaces V92's same-net horizontal joins in the fine-pitch J3 field
with individual F.Cu vertical dogbones into a common south bus. No vias or
plane-layer signal routing are used.

Native evidence:

* 9/9 J3 `STORAGE_3V3` contacts: PASS;
* trace-removal negative control: PASS;
* schematic/PCB parity: 814 authoritative nodes / 1263 pads / 0 mismatches;
* USB3 and SATA endpoint audits: PASS;
* native DRC: 597 violations / 341 unconnected items, no storage-rail
  shorting entry.

V94 is the preferred disposable storage-power basis. It is not production
closure: full-board opens, inherited crossings, and manufacturing findings
remain open.
