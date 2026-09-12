# Phase 24 M-key USB3 support graft — 2026-09-12

## Disposition

**REJECTED — route implementation / placement mismatch.** The disposable
candidate copied 43 native track/via objects from the validated
`PHASE24_STORAGE_SUPPORT_U12_COAUTHOR_TX_RX_FAR_V150` support fixture into the
current M-key actual-pad candidate. No synthetic connectivity edges were
created.

## Evidence

The four J7→U12 source links remained native-connected. The RX support links
`USB_RXP1` and `USB_RXN1` passed, but `USB_TXP1`, `USB_TXN1`, `JMS_USB3_TXP`,
and `JMS_USB3_TXN` were disconnected at the current saved placement. Native
KiCad 10.0.5 DRC reported **617 violations / 425 unconnected items**.

Raw report: `PHASE24_STORAGE_MKEY_USB3_SUPPORT_V150_GRAFT_20260912-drc.rpt`.

## Classification and next action

This is a **route implementation / placement-coordinate mismatch**, not a
failure of the storage architecture. The V150 support copper is not
portable by coordinate alone. Retain the V150 topology as reference only;
derive the next support route from the current saved pads and local geometry.
