# P24 package authority receipt — U12/U11 — 2026-09-18

Queue package: `P24-PACKAGE-AUTHORITY-U12-U11`
Decision: `P24-PACKAGE-AUTHORITY-U12-U11-20260918-R1`

## Result

**AUTHORITY_READY.** The named dependencies are resolved for queue use:

- `P24-U12-PACKAGE-GEOMETRY`: resolved to TI RUA0042A 0.50-mm geometry. The
  retained 0.40-mm footprint is explicitly rejected for routing and requires a
  separate isolated producer.
- `P24-U11-LAND-TREATMENT`: resolved with a prototype disposition. The
  retained QFN64 package/land geometry is compatible with JMicron Figure 4;
  EP stencil windowing, DFM, reflow and inspection remain required prototype
  gates.

## Evidence

- `AUTHORITY_DECISION.md` / `.json`: binding package/DFM authority record.
- `GEOMETRY_AUDIT.py` / `.json`: read-only measurement audit of exact local
  footprint files and hashes.
- TI SLAS975A / `RUA0042A` 4219139/A; local retained PDF SHA256
  `ce9c29d4c051738737e76a24ca40202e926db58a8b4665581bf905a4bd11b2ee`.
- JMicron PDS-17001 Rev 2.1 Figure 4; local retained PDF SHA256
  `27a491efa2361a5b3363d61ebf43b0983ce0c2407a49a5e949a3ff9b83b88529`.
- TI SLUA271C general QFN/SON assembly guidance; private Library local SHA256
  `4693fd4df14f57f67088d881b9509a56db4a084a333caac53f81bc5c800b23ce`.

No schematic, PCB, footprint, library table, or global rule was changed.
No restricted or third-party reference CAD was copied into public history.
The private Library index/brief is `package-authority-u11-u12-20260918`.

## Queue next action

Resolve both authority dependencies against this receipt. Create separate
producer work for the U12 0.50-mm footprint and U11 EP stencil treatment;
route every candidate through serialized integration and fresh Light
validation. This receipt is not an integrated candidate and does not close
native ERC/DRC, DFM, or assembly acceptance rows.
