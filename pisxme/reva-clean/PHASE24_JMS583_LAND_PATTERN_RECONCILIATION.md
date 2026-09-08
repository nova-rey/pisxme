# JMS583 land-pattern reconciliation

Status: `OPEN — package identity is established; final production land-pattern
authority is not yet closed` (2026-09-08).

The live generator now reuses the reviewed 64-pin JMS583 map from
`phase24_integrate_dual_mode_storage.py`; it no longer carries a second,
stale partial map. The generated support grid is also constrained inside the
300 x 180 mm disposable acreage outline. These are authoring corrections, not
release approval.

## Evidence

- JMicron's [JMS583 Product Brief](https://www.jmicron.com/file/download/1002/JMS583_Product%2BBrief.pdf)
  establishes the USB 3.1 Gen 2 to PCIe Gen 3 x2 function and QFN64 package.
- The retained [Rev 2.1 datasheet mirror](https://snapeda.s3.amazonaws.com/datasheets/2115-PDS-17001_JMS583_Datasheet_%28Rev._2.1%29_20190716.pdf)
  corroborates the 64-pin assignment and support requirements.
- [JLCPCB C9900032798](https://jlcpcb.com/partdetail/JMicron-JMS583/C9900032798)
  identifies the current assembly listing as JMS583 / QFN64_8x8.
- The [LCEDA footprint listing](https://lceda.cn/component/7ed4b3711810454eb69c8505d68afa0a)
  corroborates QFN-64, 8.0 x 8.0 mm, 0.40 mm pitch, and EP4.5.

These sources establish package identity and pitch, but do not provide a
complete manufacturer land-pattern drawing with pad length/width, paste,
mask, courtyard, and exposed-pad treatment. The current local footprint is
therefore a disposable routing fixture only; its old TI-package description
must not be treated as authority. The pad-width sensitivity report remains
experimental evidence, not a basis for changing the production footprint.

## Current decision

Keep Path A and continue native routing/validation on disposable candidates.
Before production promotion, recover a traceable JMicron/JLC land-pattern
artifact or independently review and sign off a locally derived footprint
against the package drawing. No DRC result from the current fixture closes
this gate.
