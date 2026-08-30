# HD3SS3212 polarity-inversion rules

Date: 2026-08-23  
Authority: [HD3SS3212 datasheet](https://www.ti.com/lit/ds/symlink/hd3ss3212.pdf)
and TI TIDA-00987 documentation.

## Datasheet rule

The HD3SS3212 tolerates differential polarity inversion on all differential
signals of Ports A, B and C. The critical constraint is relational: for a
selected channel, the polarity presented on Port A must be maintained
consistently on the corresponding B/C paths. In other words, if the A-side
signal is inverted for a channel, the corresponding B and C paths must use the
same inversion relationship. The mux is otherwise a transparent SuperSpeed
switch; no USB protocol conversion is involved.

The device data sheet also makes the Port-A-versus-Ports-B/C relationship
explicit: a polarity inversion is legal on the differential channels, but the
same polarity relationship must be maintained across the selected path. This
does not mean that arbitrary B/C lane reassignment is free; B/C selection is
still controlled by `SEL`. PiSXMe keeps the existing B/C branch identities and
only remaps P/N within each corresponding channel.

## Design consequences

* A P/N swap may be used to avoid a physical crossover at the mux, ESD array or
  Type-C receptacle.
* A swap must be applied to the complete selected channel relationship, not to
  a single isolated conductor.
* The CM5 does not need a software setting to know about the physical swap.
  USB3 polarity handling is part of the electrical path.
* USB2 D+/D− is separate and is not changed by a SuperSpeed P/N remap.
* The remap does not authorize crossing the TX and RX channels or changing the
  selected A/B/C channel topology. It only changes differential polarity.
* ESD devices remain shunt protection devices. A physical trace-through
  arrangement around/through the footprint must not be represented as a
  series electrical connection to an NC pin.

## PiSXMe application rule

PiSXMe will use the following trial rule: keep one polarity relationship for
each HD3SS3212 channel across A and B/C, make any swap visible in the
schematic/net map, and validate the resulting physical fanout on disposable
copies before changing the active design. This is a routing optimization, not
a license to hide a net swap in PCB-only pad assignments.
