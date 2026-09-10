# RTL9210B staggered handoff checkpoint — V1601

Date: 2026-09-10

V1601 replaced the 0.4 mm disposable JH1 row with six 1.0 mm-pitched
staggered handoff contacts and routed each U1 source pad through an explicit
orthogonal breakout. Native saved-board connectivity passed all six U1 to
JH1 links. Six trace-removal negative controls also passed: removing the
actual U1-attached segment caused the corresponding link audit to fail.

Native DRC reported no source-breakout shorting, crossing, or clearance
errors. The remaining findings are inherited/incomplete support-fixture
warnings and opens, so V1601 is accepted only as a local handoff primitive,
not as an integrated production route. V1602 is the associated rejected
launch attempt.
