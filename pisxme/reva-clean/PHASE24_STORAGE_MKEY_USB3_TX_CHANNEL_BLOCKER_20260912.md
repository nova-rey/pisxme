# Phase 24 storage USB3 TX-channel blocker

## Status

`BLOCKED` for the current U12 USB3 integration route only. The Path-B
orientation, storage architecture, and accepted V121 source escape remain
unchanged. This is a route-implementation/physical-capacity blocker, not an
electrical or architecture verdict.

## Evidence

The accepted baseline is U12 translated 5 mm left, with the local 0.15 mm
U12 pad-field clearance and the R80 relocation. The saved-pad audit passes
all four J7-to-U12 USB3 endpoint links and its actual trace-removal negative
control.

Three materially different physical-envelope-aware TX strategies were tested
with native KiCad 10.0.5 DRC after zone refill:

| Strategy | Result | Native DRC / unconnected | Decisive failure |
|---|---|---:|---|
| Staggered F.Cu channel | rejected | 405 / 427 | TX power shorts/crossing were removed, but the left TX channel violated the existing RX_P trunk clearance |
| B.Cu TX channel | rejected | 408 / 427 | TX power shorts were removed, but TX return vias/top dogbones collided with RX_P and a U12 control pad |
| B.Cu west-return channel | rejected | 406 / 427 | west return still crossed/cleared the RX_P trunk illegally; TX_P return also violated U12 pad clearance |

Candidates and raw reports are preserved as the three `...TX_CHANNEL...`,
`...TX_BCU_CHANNEL...`, and `...TX_BCU_WEST_RETURN...` artifacts in this
directory. All three used native PCB objects, ordinary 0.60/0.30 mm
through-vias, no plane-layer signals, and the 0.13208 mm V121 local escape
width. The focused endpoint audit passed for each and the negative control
failed closed as expected. Full storage closure was not claimed.

Fresh detached `pisxme-worker` KiCad Light validation from commit `319edcfd`
independently reproduced the west-return candidate at 408 DRC violations /
427 unconnected items (`validation-storage-usb3-tx-blocker-drc-20260912T030304Z`).

As a bounded follow-up to the blocker, a coordinated 5 mm west U12 migration
and a coordinated 20 mm north migration were also tested. The west move
overlapped U11/support geometry; the north move put source vias over U12
no-connect pads and crossed the existing B.Cu V100_PET0 corridor. A south
acreage migration kept U12 clear of U11 but crossed the frozen CM5_PERST
corridor and still produced TX via/pad conflicts. The south candidate passed
the four-link audit and negative control but remained at 436/427 native DRC.
These are placement/handoff evidence, not promotions.

## Exact missing resource

The present U12 handoff has no legal two-conductor TX corridor between the
existing RX_P F.Cu trunk at approximately x=147 mm and the U12 exposed/power
pad field while retaining ordinary through-via envelopes and the current
source escape. Changing only R80, TX turn coordinates, or return-via side
does not create that missing capacity.

## Smallest upstream change

Reopen the storage-local U12 USB3 handoff as one coordinated four-pair
placement/routing unit. Move U12 and regenerate all four local J7-to-U12
handoffs so RX and TX corridors are assigned before pad escape; the minimum
credible move is enough additional westward separation to put the TX
return-via envelope outside the RX_P trunk. Preserve the frozen RTL9210B
orientation, CM5, PCIe/V100 path, layer contract, and storage architecture.

Do not generate a fourth arbitrary route variant. Resume with a fresh
coordinated U12 four-pair handoff, then rerun the focused saved-pad audit,
negative control, native DRC, and fresh `pisxme-worker validate` before
promotion.
