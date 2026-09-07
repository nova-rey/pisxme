# Path-B support-corridor decision

## Current evidence

The preferred V11 disposable fixture has native endpoint proof for XTAL_IN,
XTAL_OUT, RTL_5V, and the asserted RTL_1V1 endpoints. Its remaining support
opens are not evidence of missing schematic authority.

The native QFN map shows these measured constraints:

- U1 pad 34 (RTL_3V3) has only a short right-side F.Cu escape before the
  RTL_5V bus at x=85.0, y=59.2.
- A direct pad-34 B.Cu escape reaches one endpoint but shorts RTL_5V and
  crosses the RTL_1V1 bus: 9 native DRC violations / 24 opens.
- U2-side 3V3 B.Cu trunks connect additional endpoints but cross SPI and
  RTL_1V1 corridors: 8 native DRC violations / 22 opens.
- Crystal V11 is valid at the endpoint level; its remaining native DRC is
  dominated by inherited control/thermal findings plus the support field.

## Decision

Further isolated 3V3 or crystal trace nudges are rejected as a solution
class. The next candidate must relocate the complete 3V3/1V1 support branch
(including its decoupling/bus transitions) as one coherent island, or move
the local bridge-support island while preserving all net authority. Any
candidate remains disposable until native DRC, full endpoint connectivity,
and negative-control evidence pass.

Production CAD and Path A remain unchanged.
