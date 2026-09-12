# JMS583 local support-cohort placement decision

Date: 2026-09-12  
Scope: U11 support cohort only  
Decision status: `AUTHORITATIVE_LOCAL_BASELINE`

## Decision

Keep U11 `JMS583-QHFA3A` at `(140.00, 135.00)`, top side, rotation 0°.
Move the directly related support as follows:

| Ref | Position | Rotation | Reason |
|---|---:|---:|---|
| `Y10` | `(138.20, 126.40)` | 0° | places crystal pads directly north of U11 XIN/XOUT pads |
| `L10` | `(142.00, 130.00)` | 0° | keeps VDDREG/LXO support in the north-east U11 pocket |

The remaining accepted support components stay at their current locations for
this bounded implementation. No RTL9210B orientation, USB3 corridor,
storage architecture, or macro-floorplan change is authorized by this record.

## Native geometry basis

Fresh KiCad Light inspection of the committed storage baseline reports U11
support exits:

| U11 pad | Net | Native position |
|---:|---|---:|
| 1 | `JMS_VDDREG_5V` | `(136.35,132.00)` |
| 50 | `XIN` | `(137.40,131.40)` |
| 51 | `XOUT` | `(137.80,131.40)` |
| 64 | `LXO` | `(143.00,131.40)` |

At the selected Y10 position, its XIN/XOUT pads are approximately
`(137.10,125.55)` and `(137.10,127.25)`, respectively. At the selected L10
position, its LXO/VDDREG pads are approximately `(140.85,130.00)` and
`(143.15,130.00)`. These are saved native-pad transforms, not schematic
drawing coordinates or pin-list ordering.

## Physical/topological rationale

The prior baseline split the crystal and L10 support into an upper field and
left a long, congested escape back to U11. The selected arrangement makes the
two crystal connections a short monotonic northward pair and puts the two
L10-related terminations in the same local U11 pocket. It preserves U11
orientation and the accepted USB3 source/corridor geometry. It is a placement
baseline, not a claim that routing or native DRC has passed.

## Implementation constraints

1. Clear and re-author only `XIN`, `XOUT`, `JMS_VDDREG_5V`, and `LXO` in the
   disposable candidate; preserve all other accepted support copper.
2. Use saved native pad positions and ordinary through-vias only.
3. Keep the XIN/XOUT pair together, use the selected 0.10/0.10 mm local
   exception only in the immediate QFN/Y10 field, and return to the normal
   0.20 mm board rule at the handoff.
4. Reserve the VDDREG/LXO corridor before adding secondary support copper.
5. Validate all ten JMS support branches, USB3, native DRC, and actual-object
   negative controls in a fresh KiCad Light workspace.

## Provenance and limitation

The specialist authority sessions were unavailable after bounded waits. This
record is the Root Foreman local-equivalent decision required by the current
operating protocol, based on the native saved-pad inspection above and the
retained JMS583 land-pattern/reference evidence in
`PHASE24_JMS583_LAND_PATTERN_RECONCILIATION.md`. It is one bounded decision,
not an invitation to reopen orientation search. If standard geometry fails on
this placement, the failure must identify the exact local resource before any
fine-pitch exception is considered.
