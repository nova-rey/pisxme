# Assembly and service sequence

## Recommended assembly order

1. Populate the bare PCB and inspect underside clearances.
2. Install J3/J4 harnesses only after polarity and `12V ONLY` marking are
   verified.
3. Install the CM5 into J2 and confirm the module can be removed without
   contacting the USB edge or cooler reservation.
4. Install the V100 SXM2 module.
5. Install the selected cooler/backplate using the cooler-owned volume and
   retention datum contract.
6. Connect fan/pump harnesses and then external USB/power cables.
7. Bring up over UART/SERVICE before attaching optional USB storage/NIC loads.

## Recommended removal order

1. Remove raw 12 V input cables and USB/service/debug cables.
2. Remove fan/pump cables while preserving access to the latch.
3. Remove cooler hardware if it masks V100 retention hardware.
4. Remove V100 only after power is confirmed discharged.
5. Remove CM5 from J2.
6. Service F1/protection only with the cooler and V100 clear of the work area.

## Blocking findings

- F1/Q1 currently enter the cooler-owned XY reservation; this can make fuse or
  protection service impossible with a cooler installed.
- The fan/pump housing models are absent, so the 8 mm header pitch is not a
  proven service sequence.
- J11 and UART require an enclosure cutout/accessory definition before claiming
  in-situ recovery.

The sequence is otherwise viable because the CM5 and SXM2 are adjacent but do
not occupy the right-edge I/O corridor.
