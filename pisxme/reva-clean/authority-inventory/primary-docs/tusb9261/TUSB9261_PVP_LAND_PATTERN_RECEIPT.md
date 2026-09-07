# TUSB9261IPVP PVP0064A land-pattern receipt

Checked: 2026-09-06. Source: Texas Instruments TUSB9261 Rev-I datasheet,
package pages 24–26, local copy `TUSB9261-datasheet-revI.pdf`.

The current TI package drawing identifies `PVP0064A PowerPAD HTQFP` and its
example board layout explicitly specifies:

- 64 perimeter pads;
- 0.4-mm pad pitch;
- 1.2-mm pad metal length;
- 0.2-mm pad metal width;
- exposed PowerPAD 65;
- solder-mask/stencil guidance and optional exposed-pad vias.

The project-local `TUSB9261IPVP_PVP0064A.kicad_mod` matches those electrical
land-pattern dimensions and has radial pad orientation. The native board
replacement discriminator confirms that embedding the project-local footprint
does not change the eight-endpoint SATA audit or remove the remaining route
classes.

The remaining 0.1746-mm diagonal pad-to-pad findings in the disposable route
are therefore not evidence of a malformed U7 footprint. They result from the
generic 0.20-mm KiCad clearance basis being stricter than the exact TI
geometry. JLC's current six-layer capability advertises 0.15-mm trace/space,
but no production rule is changed by this receipt. A future rule-basis change
must be separately justified against the selected fabrication option and must
not waive true shorts, crossings, or opens.

Authoritative source:

- <https://www.ti.com/lit/ds/symlink/tusb9261.pdf>

