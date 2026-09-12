# Phase 24 JMS583 support-escape blocker packet

Date: 2026-09-12  
Blocker ID: `PHASE24_JMS583_LOCAL_ESCAPE`  
Status: `SUPERSEDED_BY_LOCAL_ESCAPE_PASS` (historical blocker evidence)

## CURRENT STATE — 2026-09-12

The user-authorized bounded exception is implemented and passes the local
JMS583 escape discriminator in fresh KiCad Light. See
`PHASE24_JMS583_FINE_ESCAPE_RECEIPT_20260912.md` and
`PHASE24_JMS583_FINE_QFN_ESCAPE.kicad_pcb`. The decision boundary below is
historical: the local rule is now selected, not awaiting authorization. The
full-acreage DRC and remaining Phase 24 gates are still open.

## Placement-authority implementation result — 2026-09-12

The bounded local placement decision is now implemented by
`phase24_jms583_local_support_authority_candidate.py` and independently run
from committed ref `df6f9867` in a fresh KiCad Light workspace. The corrected
candidate passes all ten support endpoint assertions and the trace-removal
negative control. Native KiCad DRC reports 625 violations / 409 unconnected
items, including these local implementation failures:

* XIN/XOUT dogbones short/cross at the Y10/U11 pad field. The native DRC
  identifies XOUT pad 2 at `(137.10,127.25)` against the XIN track and XIN/XOUT
  tracks against the adjacent U11 pads 49/52. The route uses 0.15 mm copper;
  the tightest adjacent-pad clearance is 0.0754 mm against a 0.10 mm pad
  clearance requirement.
* The inherited AVDDL branch still crosses the existing USB3 B.Cu corridor;
  this is outside the three-branch local escape and is not a placement proof
  against the U11 support pocket.

The first valid standard-geometry test therefore closes the specialist/local
placement discriminator: the support endpoints can be placed coherently, but
the immediate 0.4 mm-pitch QFN escape cannot satisfy the current general
0.20/0.20 rule. The accepted placement remains frozen.

The smallest next experiment is a local JMS583 exception using 0.10 mm trace
and 0.10 mm clearance (or a less aggressive documented equivalent), with
ordinary 0.60/0.30 mm vias retained and normal 0.20 mm routing restored outside
the immediate pad escape. This exception is not yet authorized for JMS583.

## Exact failed gate

The current committed storage baseline is
`PHASE24_STORAGE_MKEY_USB3_AVDDL_U12_LOCAL_20260912.kicad_pcb` at ref
`a8343bc2`. The corrected saved-object audit, run in a fresh KiCad Light
workspace, reports:

| JMS583 support branch | Result |
|---|---|
| `JMS_REXT` | PASS |
| `XIN` | FAIL |
| `XOUT` | FAIL |
| `JMS_RESET_N` | PASS |
| `JMS_AVDD33` | PASS |
| `JMS_AVDDL` | PASS |
| `JMS_VCCO` | PASS |
| `JMS_VCCK` | PASS |
| `JMS_VDDREG_5V` | FAIL |
| `LXO` | PASS |

Native KiCad 10.0.5 baseline census is 592 DRC violations / 412
unconnected items. The fresh KiCad Light 10.0.6 reproduction fails the same
three required branches (with the expected three enum-property assertions).
The result is therefore not a stale narrative or validator-only failure.
Receipt: `PHASE24_STORAGE_SUPPORT_AUDIT_LIGHT_V3_RECEIPT_20260912.md`.

## Evidence already exhausted

The following materially different, disposable implementation classes were
tested and rejected without changing canonical copper:

1. Full support cohort relocation: complete support and USB3 audits pass, but
   native DRC introduces 7 shorts and 3 crossings (453/401).
2. Local crystal relocation plus outer VDDREG escape: support audit can pass,
   but native DRC is 653/409 and includes a local LXO-via clearance defect.
3. Fixed crystal / straight escape / outer VDDREG: complete support audit
   passes, but native DRC is 641/409 with 5 shorts and 4 crossings.
4. North co-located support replay: VDDREG connects but already accepted
   XIN/XOUT/AVDD33/VCCO/VCCK branches are lost (611/404).
5. Three-corridor V1/V2 channel planning: complete audit passes, but source
   field, reset, and adjacent-support shorts/crossings remain (640/409 and
   644/409).

These are route/placement failures, not evidence that the JMS583 architecture
or selected support network is electrically invalid. The current baseline is
retained because it preserves every accepted branch and has no newly
introduced storage-local short/crossing class.

## Precise resource that is missing

The current U11 QFN support field has insufficient legal clearance under the
general 0.20 mm trace/clearance and 0.60/0.30 mm through-via rules for all
remaining `XIN`, `XOUT`, and shared `JMS_VDDREG_5V` source-to-support escapes.
Centerline paths exist, and complete endpoint connectivity has been achieved
in disposable candidates, but their physical copper/via envelopes collide
with the reset spine, QFN adjacent/no-net pads, or accepted USB3/support
copper under native DRC.

This is a local manufacturability/routing-rule or local-placement boundary;
it is not a request to reopen RTL9210B orientation, the storage architecture,
the macro-floorplan, or the accepted USB3 topology.

## Smallest continuation options

1. **Recommended:** authorize a documented, local JMS583 QFN escape exception
   using the least aggressive manufacturer/fabricator-supported trace and
   clearance geometry, returning to 0.20 mm rules immediately outside the
   escape. Retain ordinary through-vias unless a smaller via is proven
   necessary. This is analogous in scope to the already-authorized local
   RTL9210B QFN exception, but it is not currently authorized for JMS583.
2. Authorize one bounded coherent move of U11 plus its crystal and affected
   support cohort, preserving the validated USB3 corridor and revalidating
   all changed connections. This changes local placement rather than rules,
   but prior relocation classes have already caused collateral failures.
3. Replace the JMS583 Path-A bridge with another documented/sourceable bridge.
   This is a component/architecture decision and is materially larger than
   the two local repairs above.

No validation severity has been changed, no warning has been waived, and no
canonical PCB copper has been promoted from the rejected candidates.

## Independent work that remains active

The canonical ERC cleanup remains independently actionable at 311 warnings / 0
errors (132 endpoint-off-grid, 126 isolated-pin-label, 30 same-local-global,
23 multiple-net-names). The RTL9210B V1603 six-net audit and its negative
controls remain passing. Neither is blocked by the JMS583 local escape.

## Resume condition

After one of the two local options is explicitly selected, implement only that
bounded repair, validate it with native DRC plus the saved-object support and
USB3 negative-control audits, and continue Phase 24. Until then the dependent
JMS583 support-closure gate is paused at this exact decision boundary.
