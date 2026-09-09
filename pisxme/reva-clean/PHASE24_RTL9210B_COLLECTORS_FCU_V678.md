# RTL9210B Path-B V678 — rejected F.Cu collector join

V678 replaced the V676 disposable B.Cu tails with F.Cu joins: U1.39
RTL_3V3 to the existing trunk at (93.0,64.0), and U1.40 RTL_1V1 to the
existing collector at (88.0,68.8). Native KiCad DRC found 12 findings and
22 expected/incomplete unconnected items. It introduced a real RTL_3V3
source-field crossing with the retained RTL_1V1 field and left both source
vias single-layer.

Disposition: reject V678 as a route implementation. Retain V676 only as a
source-escape discriminator; do not promote either collector path. The next
bounded class pivots to the native-clean orientation-180 support lineage.
