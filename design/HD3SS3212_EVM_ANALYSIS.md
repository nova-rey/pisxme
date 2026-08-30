# HD3SS3212 EVM analysis

Date: 2026-08-23  
Source: `references/usb3/TIDA-00987/HD3SS3212EVM-user-guide.pdf`, TI product
documentation, and the HD3SS3212 datasheet.

## What the EVM isolates

The EVM uses SMP connectors for the high-speed A/B/C interfaces rather than a
reversible Type-C receptacle. This removes the Type-C A/B contact fanout from
the experiment and exposes the preferred mux package treatment directly.

The user guide specifies:

* equal-length signal traces of 1119 mil;
* 50-ohm single-ended trace intent for the SMP environment;
* equal calibration-trace length so calibration fixtures do not dominate the
  measurement;
* 220 nF capacitors on B/C by default and a 0-ohm path on A in the EVM setup,
  because the mux requires the appropriate biasing arrangement.

## What the EVM does not prove

The acquired guide does not include an editable KiCad/Altium PCB source or
full Gerber package. It therefore does not provide a second independently
measured 0.5 mm Type-C fanout geometry. It is strong evidence for the mux
being a transparent high-speed device and for disciplined equal-length
calibration routing, but not a numeric source for PiSXMe’s local escape rule.

## PiSXMe lesson

Use the EVM as a package/measurement precedent:

1. keep the A/B/C paths electrically symmetric where they are intended to be
   compared;
2. do not place coupling capacitors on both sides without considering the
   mux biasing requirement;
3. accept a symmetric layer transition if needed rather than creating an
   asymmetric P/N transition;
4. keep the fine-pitch package region short and transition to the intended
   main-route geometry quickly.

This supports a coupon gate, not automatic authorization to use the EVM’s
50-ohm SMP trace value on the PiSXMe USB3 route.
