# RTL9210B Path-B V676 — retained adjacent-source basis

V676 starts from V672 and removes the old U1.40 departure. It routes native
U1.39 RTL_3V3 west to an ordinary transition at (91.0,68.4), while U1.40
RTL_1V1 turns down to its transition at (92.0,70.0). This is the around-
the-via allocation, rather than the rejected same-side pair in V675.

Native KiCad 10.0.5 DRC found 12 findings and 24 expected/incomplete
unconnected items. There are no signal short, crossing, clearance,
solder-mask, or footprint errors. The findings are dangling disposable
tails, inherited isolated-copper/duplicate-via/silkscreen warnings, and
expected incomplete Path-B support connections.

Disposition: retain V676 as the source-field basis. Its short B.Cu tails are
intentionally not promoted as final routing; the next experiment should
extend each transition to its native rail collector independently and then
run full connectivity/DRC.
