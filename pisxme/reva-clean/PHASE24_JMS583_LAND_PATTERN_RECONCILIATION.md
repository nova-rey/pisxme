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

The datasheet Figure 4 also establishes the package body as 8.0 mm BSC,
terminal width `b = 0.15–0.20 mm`, exposed-pad nominal dimensions `D2/E2 =
4.46 mm`, and a 0.40 mm terminal pitch. The local footprint was corrected to
use a 0.20 mm terminal width, an 8.0 mm body courtyard basis, and a grounded
4.46 mm exposed pad. The prior 0.22 mm terminals and TI RUA0042A description
are preserved only in pre-reconciliation probe artifacts. Paste windowing,
mask expansion, and a manufacturer-recommended courtyard remain unprovided;
those fields are still review gates rather than silently inferred authority.

## Current decision

Keep Path A and continue native routing/validation on disposable candidates.
The locally derived copper geometry is now tied to the manufacturer package
drawing, but production promotion still requires explicit footprint review
for paste/mask/courtyard treatment and native DRC/assembly suitability. No
DRC result from the current fixture alone closes this gate.
