# RTL9210B V667 full SPI allocation — rejected

V667 is a disposable five-net SPI allocation from native U1/U2 pad centers on
the V595 rail/PEDET/CLKREQ base. It used 0.20-mm F.Cu source dogbones,
ordinary through-vias, separated B.Cu channels, and no plane-layer signals.

Native KiCad 10.0.5 DRC result:

- 35 violations;
- 11 unconnected items;
- real SPISO3/SPICS and SPI/RTL_3V3 shorts;
- source-field crossings with retained RTL_1V1 and rail geometry.

Disposition: reject this route implementation. It does not reject the
RTL9210B package, pin map, or Path-B architecture. The next SPI attempt must
co-author all five source escapes with the retained RTL_3V3/RTL_1V1 field, or
move the isolated support cluster coherently before routing. Path A and
production CAD remain unchanged.
