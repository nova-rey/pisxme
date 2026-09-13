# Duplicate POWER_GND via producer 2

Base: `e0d128eb`. Removed only via UUID `57bff9c4-de30-4919-95e1-6c11410dab5e`
at `(78.9,65.699999)`, retaining its identical same-net mate.

Light DRC: **310 violations / 499 unconnected items**. `holes_co_located`
reduced 8→7; all other violation families are unchanged and no shorting class
appeared. Integration and fresh exact-head validation remain Root-owned.
