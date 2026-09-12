# Phase 24 M-key USB3 probe V2 — 2026-09-12

## Disposition

**REJECTED — route implementation.** This materially different disposable
route used direct B.Cu source fanout from the actual J7 pads, four separated
long corridor lanes, and one ordinary transition near U12. It preserved the
frozen storage placement and normal 0.20 mm / 0.60-0.30 mm rules.

## Native evidence

The route failed the native four-link saved-pad audit at
`CM5_USB3_RX_N -> J7.128/U12.16`. KiCad 10.0.5 DRC reported **475
violations / 431 unconnected items**. The failure includes source-pad escape
disconnection because the CM5 connector pads are not available on B.Cu,
connector-side crossings, and an existing `V100_PET0_N` corridor collision.

## Classification

This is a **route implementation failure**. It does not invalidate the M-key
storage architecture, the connector, or the accepted local support authority.
The candidate remains disposable evidence only.
