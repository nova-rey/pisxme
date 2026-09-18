# PiSXMe U11/U12 package authority brief

Date: 2026-09-18. Queue package: `P24-PACKAGE-AUTHORITY-U12-U11`.
This brief is indexed in `Library/indexes/package-authority-u11-u12-20260918.json`.
It is evidence for Package/DFM Authority; it does not modify CAD.

## U12 HD3SS6126RUAR

TI's retained SLAS975A datasheet and package outline `RUA0042A`, drawing
`4219139/A` dated 03/2020, are primary manufacturer evidence. The package is a
42-pin RUA WQFN, nominal body 9.00 x 3.50 mm. The package drawing and example
land pattern specify 0.50 mm pitch, 42 lands of 0.60 x 0.25 mm, row-center
spacing 3.30 mm, exposed pad 43 of 2.05 x 7.55 mm, and a 0.125 mm stencil
example with 69% printed coverage.

The current local footprint has the correct pad count, land sizes, and exposed
pad size, but its pad centers use 0.40 mm increments, side-row centers at
x=+/-1.80 mm and y=-3.20..+3.20 mm, and end-row centers at 0.40 mm increments.
Those values contradict the primary package drawing. The 0.40 mm footprint is
therefore rejected as package-authoritative and must not be routed or promoted.
The authority contract is resolved to the TI 0.50 mm geometry; an isolated CAD
producer must regenerate the footprint and revalidate pin mapping before any
integration.

## U11 JMS583-QHFA3A

JMicron PDS-17001 Rev 2.1 Figure 4 is primary package evidence. It specifies a
QFN64 8 x 8 mm body, e=0.400 mm terminal pitch, terminal width b=0.150--0.250
mm, terminal length L=0.300--0.500 mm, exposed pad D2/E2=4.360--4.560 mm
(nominal 4.460 mm), and package warpage max 0.08 mm.

The local footprint has 64 signal pads plus exposed pad 65, 0.400 mm pitch,
0.70 x 0.20 mm signal lands, 4.46 x 4.46 mm exposed copper, and a 9.2 x
9.2 mm courtyard. These measured values are compatible with the package
outline as a derived prototype land. JMicron does not publish a complete PCB
land-pattern, solder-mask, stencil, or courtyard drawing in the retained
packet.

TI's primary general QFN/SON attachment note SLUA271C is used only as
assembly guidance: copper-defined/NSMD lands are preferred, 0.20 mm pad width
is a 0.4 mm-pitch printing guide, 0.100--0.150 mm stencils are typical, and
exposed-pad paste should be windowed to approximately 50--70% coverage to
limit float and voiding. The current full exposed-pad paste aperture is not a
production-ready stencil treatment. For Rev A prototype CAD, signal-pad land
geometry is authorized as a derived implementation, the exposed pad remains
thermally/electrically soldered, and the stencil producer must create the
windowed 50--70% paste pattern and record the chosen aperture geometry. DFM,
reflow, and X-ray/void inspection remain explicit prototype-validation steps;
this is not a production qualification claim.

## Authority disposition

- `P24-U12-PACKAGE-GEOMETRY`: **RESOLVED** to TI RUA0042A 0.50 mm contract;
the retained footprint is a rejected producer input and requires a new
isolated footprint candidate.
- `P24-U11-LAND-TREATMENT`: **RESOLVED WITH PROTOTYPE DISPOSITION**;
package geometry and derived signal land are accepted for prototype work under
the stated NSMD/assembly assumptions; EP stencil windowing and assembly
validation remain required downstream gates.

No restricted/reference CAD bytes were copied into the public project. The
private Library retains the source metadata, extracted facts, and lawful local
copies identified by SHA-256 in the structured index.
