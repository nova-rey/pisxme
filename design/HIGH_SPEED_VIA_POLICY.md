# PiSXMe high-speed via policy

Date: 2026-08-23  
Status: **AUTHORITATIVE FOR ALL REMAINING HIGH-SPEED WORK**

## Governing rule

Via count is a cost term, not a hard design objective. The selected topology
must minimize the number of transitions that are useful for the complete
electromagnetic path, while preserving connectivity, polarity, reference
planes, impedance continuity, and manufacturability.

The priority order is:

1. correct connectivity and polarity;
2. continuous or intentionally transitioned reference-plane structure;
3. no crossings or pathological fanout;
4. short/direct path;
5. low pair asymmetry;
6. sensible impedance continuity;
7. minimal layer transitions;
8. minimal total via count.

Therefore:

* zero vias with clean routing is excellent, but zero vias at any cost is not
  a requirement;
* one deliberate symmetric transition per conductor can be the best result;
* two or more transitions are acceptable when the stackup and return path make
  them electrically and geometrically worthwhile;
* repeated layer bouncing without a specific SI or fanout reason is not
  acceptable;
* blind, buried, or microvia processes are not introduced merely to reduce a
  reasonable through-via count.

## Required transition record

Every high-speed receipt must report, for each transition:

| Field | Required content |
|---|---|
| Reason | the concrete crossing, reference, or fanout problem solved |
| Pair symmetry | P/N locations, lengths, and transition treatment |
| Layer before/after | exact signal layers |
| Reference before/after | exact adjacent or intentional reference planes |
| Via geometry | pad, drill, aspect/process assumption |
| Return path | nearby ground stitching/return-via strategy |
| Stub treatment | why a stub is absent or acceptable |
| Removal comparison | whether removing the transition improves or worsens the path |

Any via that exists only because of poor placement or routing convenience must
be flagged and removed or justified.

## USB3 application

The corrected-package coupon and second-layer coupon establish the allowed
pattern:

```text
bounded fine-pitch escape -> deliberate symmetric transition when useful
-> controlled-impedance route on a referenced signal layer
```

USB3 fanout work must not force the entire mux/ESD/Type-C topology onto F.Cu
when that creates crossings, excessive neck-down, or clearance failures. The
next complete-port study must select the cleanest logical division of channels
between controlled signal layers, calculate/verify geometry for each layer,
and add return-path stitching where the reference context changes.

The local fine-pitch rule remains spatially bounded. It does not authorize a
global clearance reduction.

## PCIe application

The existing PCIe L1/L2 route remains frozen and is not changed by this policy
amendment. For future PCIe work, F.Cu over continuous L2 GND remains the
baseline, but a clean controlled transition is permitted when it materially
improves the complete route. The old zero-via preference must not be treated as
an absolute limit.
