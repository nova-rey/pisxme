# Power input geometry authority report

Package/Footprint Authority reviewed the existing input footprint and all bounded candidates.

## Binding dispositions

- Existing Molex `0039300020 / 39-30-0020` at J5/J6 is legacy-only and electrically disqualified: the exact application evidence is 8 A/circuit, versus the 40 A continuous / 45 A 100 ms source contract.
- Samtec PET/PES PowerStrip/40 is electrically promising, but no authorized configured KiCad footprint, exact pad/NPTH/polarity convention, 3D/mating envelope, or complete harness contract is available. Its manufacturer print is proprietary and cannot be copied or used to synthesize a footprint under this package.
- Anderson PP15/45 is an electrical fallback, but its selected contact-row variant, land pattern, polarity convention, 3D/mating envelope, and complete harness contract are likewise not authorized in the project.
- Amphenol M-CRPS is not evidence-complete for this 12 V application.

## Resume condition

The producer may resume only after either (1) manufacturer-authorized ECAD/land-pattern and 3D data for the exact configured assembly plus complete mating/harness data arrive, or (2) explicit PiSXMe authority authorizes footprint authorship from the manufacturer drawing with the exact contact variant, pad/NPTH, mask, courtyard/fab, polarity, mating envelope, and assembly constraints. No guessed footprint or proprietary drawing copy is permitted.

No CAD or library files were changed. The producer blocker and untouched baseline remain retained in `validation-receipts/power-bus-corrective-blocker-20260918/`.
