# Storage rail completeness trial V93 — 2026-09-10

V93 attempted a coherent In1 `STORAGE_3V3` power zone with pad-aware
ordinary-via dogbones from the U12/U13/U14/R81 storage-rail pads, while
retaining the V92 F.Cu J3 edge drops.

Native results:

* the nine-contact J3 power audit failed because the no-via J3 drops were not
  tied into the In1 plane;
* native DRC reported 619 violations / 344 unconnected items;
* the broad plane and QFN-side via escapes introduced real
  `STORAGE_3V3` shorts to SATA, JMS_AVDDL, and CM5 USB3 copper.

V93 is rejected. The experiment confirms that a broad storage power plane
cannot be added over the current mixed-side island without a coordinated
via/escape redesign. V92 remains the best current physical-power basis; no
production CAD or DRC rule was changed.
