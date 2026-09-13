# Rejected branch-B single-route producer

Base: `d7f0455b`. The experiment routed only `12V_IN_B` from J6.1 to F2.1 on
B.Cu using a constrained path. Fresh Light DRC reported **307 violations /
499 unconnected items**, including one new `shorting_items` error between
`POWER_GND` J6.2 and the new `12V_IN_B` track at J6. The copper was rejected
and not integrated.
