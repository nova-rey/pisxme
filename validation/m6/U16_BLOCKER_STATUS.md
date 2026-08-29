# U16 blocker status

U16 is a TPSM63606 USB/5 V regulator implementation that was not closed by
the disposable trials. The target FB graph can be made continuous, but RT and
PG support-field routes crossed or shorted ground/other corridors in the
available placement. Input/output capacitors, AGND/PGND, thermal copper, RT,
FB, and PG must be rebuilt from the TI reference layout or U16 must be
removed/replaced if the approved I/O architecture no longer needs it.

No disposable U16 trial is promotion evidence and no active source was changed.
