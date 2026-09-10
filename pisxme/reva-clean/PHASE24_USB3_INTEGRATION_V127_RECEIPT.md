# Phase 24 USB3 integration V127 receipt

V127 starts from the V123 PERST-safe, refilled candidate and moves only the
storage-local JMS583 REXT support resistor R80 from the USB3 corridor to
(166.0, 130.0). No CM5, PCIe, PERST topology, or USB3 copper was changed.

Evidence:

- Native J7.128/130/140/142 to U12.16/15/12/11 connectivity: PASS.
- Native DRC: 146 violations / 499 opens.
- No `shorting_items`, `tracks_crossing`, or `track_width` findings.
- The remaining first errors are inherited CM5_REFCLK clearance findings;
  whole-board opens and other inherited mechanical/edge findings remain.

V127 is not yet a Phase 18 or Phase 24 pass because support routing and the
full storage island are incomplete. It is the best current integrated USB3
route-development candidate and preserves the proven V121 source escape plus
the V123 PERST repair.
