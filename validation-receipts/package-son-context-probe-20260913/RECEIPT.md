# Package_SON footprint context probe

Base: `d85c7adb`. The project `fp-lib-table` was provisionally extended with
qualified system `Package_SON.pretty` at `${KICAD10_FOOTPRINT_DIR}`. No PCB or
schematic content was changed by the probe.

Light DRC reported **303 violations / 499 unconnected items**, removing the
two `lib_footprint_issues` from the 305-violation baseline. All physical
families were otherwise unchanged; no shorting class appeared. This is a
validation-context correction candidate pending canonical integration and
fresh exact-head validation.
