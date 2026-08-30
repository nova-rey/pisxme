# Hostile Placement Review

## Attack 1 — Can CM5 move closer?

Moving J2 left in the existing 0° orientation reaches the cooler boundary after
only approximately 5 mm. The 180° rotation is the only explored compact
orientation that moves the PCIe field to approximately x=162.5 mm while keeping
the connector courtyard east of the cooler-owned x=160 boundary. A closer
placement would require invading the published cooler envelope or changing the
connector/mechanical architecture.

## Attack 2 — Is the USB placement actually improved?

Yes at the placement level, after correcting the first invalid local trial. The
muxes/ESD parts now sit outside the rotated J2 body in upper/lower I/O corridors,
and the Type-C receptacles remain edge-accessible. The corrected trial routes
expose real HD3SS3212/ESD pin-order crossings, so the placement is not being
declared USB production-ready. The crossings are localized and suitable for a
deliberate multilayer escape in the next phase; the previous 40–46-via
whole-edge detours are no longer structurally required.

## Attack 3 — Did board expansion help?

No. The expanded 180° candidate has the same high-speed geometry as Candidate C
but adds 67 cm². The expanded 270° candidate provides no mechanical benefit and
its CM5 STEP model protrudes beyond the board envelope. The compact 220 x 140 mm
outline therefore remains the provisional winner.

## Attack 4 — Did power/cooling move?

The SXM2, cooler zone, backplate keepout, dual 12 V inputs, and distributed V100
power fanout were not moved. Candidate C places the CM5/USB support region to the
right and upper/lower-right, away from the high-current input/fuse fanout. The
corrected placement DRC has no new courtyard, hole-clearance, or pad-short
finding. The next phase must re-check local 5 V and USB power routing after the
high-speed corridor is routed.

## Attack 5 — Is the PCIe route truly solved?

It is improved, not solved. The measured direct trial is 63–68 mm, zero vias,
and ACCEPTABLE under the phase bands. It remains longer than the original
20–40 mm goal and has untuned pair mismatches up to 1.433 mm in the lightweight
probe. The next phase must use the final 90-ohm rules, preserve L1/L2 continuity,
and match the pairs without serpentine excess.

## Review conclusion

No evidence-backed mechanical placement blocker remains for Candidate C. The
board is **not** a routed release: the next phase must perform the actual PCIe
and USB3 routing, then re-run DRC, SI, power, and thermal reviews.
