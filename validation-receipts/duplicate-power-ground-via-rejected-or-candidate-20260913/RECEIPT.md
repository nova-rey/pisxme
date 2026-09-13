# Duplicate POWER_GND via producer

Base: `5a34b9a0`.

Removed only via UUID `be09a526-b287-430c-bef8-9e3629ff4a5f` at
`(75.032441,66.207106)`, retaining the identical same-net via
`208f5214-e669-4004-ac41-44ca9cca6e86`.

Light DRC result: **311 violations / 499 unconnected items**. The only family
change from the 312-violation baseline is `holes_co_located` 9→8. Clearance,
width, edge, dangling, courtyard, crossing, and library families are
unchanged; no shorting class appeared. This is a candidate producer result;
integration and fresh validation remain Root-owned.
