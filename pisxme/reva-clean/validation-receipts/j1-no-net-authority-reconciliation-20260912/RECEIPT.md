# J1 no-net authority reconciliation

- Source PCB candidate: `c8710a84`
- KiCad/toolchain context: `pisxme-kicad-light:v1`, KiCad 10.0.6
- Authority record: `authority-inventory/primary-docs/sxm2/SXM2_J1_AUTHORITY_REASSESSMENT_20260912.md`
- Library map: `sxm2-benchoff-contact-map-20260912`

The fresh pad census reports 400 physical J1 pads, with 7 schematic-expected
signal contacts, 130 `12V_PROTECTED`, 170 `POWER_GND`, and 93 no-net contacts.
The 93 no-net contacts reconcile to the approved authority categories:

- 60 published PCIe contacts intentionally unassigned because PiSXMe is an x1
  product;
- 31 source-declared NC/project-unknown contacts;
- 2 auxiliary/protection unknown contacts, K18 and K19.

The arithmetic is `7 + 130 + 170 + 60 + 31 + 2 = 400`. No net assignments
were added. The no-net contacts remain unknown/NC as applicable, and the
selected Path A storage authority is unaffected. This closes the scope gap in
the bidirectional pad audit for J1, while integrated connectivity, DRC, DFM,
and electrical acceptance rows remain open.

The retained `pad-parity-bidirectional-20260912/surplus.txt` is a bounded
listing rather than a complete 93-contact dump; the count and category totals
come from the retained census receipt and the authority record. A future
validation run must preserve the complete machine-readable J1 listing.
