# Binding-MPA protected-bus producer failure receipt

The clean producer asserted the binding MPA coordinates before routing: Q1=(61,22), Q2=(61,54), F1=(32,22), F2=(32,54), D1=(49,8), D2=(49,70), U1=(49,22), U2=(49,54), J5=(12,25), and J6=(12,45). It preserved the Molex 39301082 geometry.

KiCad Light targeted DRC returned 710 violations and 499 unconnected items. The candidate is rejected. This is the first valid test of the binding placement; the failures expose a structural placement/corridor contradiction requiring one bounded MPA revision. No canonical CAD changed.
