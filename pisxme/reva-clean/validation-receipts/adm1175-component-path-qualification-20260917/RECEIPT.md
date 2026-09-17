# Receipt — ADM1175 component-path qualification

- **Package:** `P24-ADM1175-COMPONENT-PATH-QUALIFICATION`
- **Base state:** `d3efe794`
- **Changed scope:** sanitized authority evidence under this receipt directory only
- **CAD/product envelope:** unchanged
- **Private Library:** `4794c3613f7047bfff058ac33b13d1f3624a05c9` plus the companion private evidence index
- **Disposition:** `WAITING authority:6A-limiter-qualification`

## Work performed

The review reconciled the ADM1175 Rev. C controller limits against exact
manufacturer component candidates. It corrected the earlier hypothetical-shunt
screen by using the documented Vishay WSK2512 16 mΩ candidate and a conservative
temperature/tolerance envelope. It screened three exact/derived FET MPNs,
including the Infineon IRLS4030-7PPbF with manufacturer SOA/avalanche data.

The fail-closed calculator reproduces the manufacturer Equations 1--3 and the
independent resistance-ratio proof. The WSK2512 candidate yields
`6.0427101243--6.4586520856 A`; the upper endpoint violates the 6.400 A HPQ4
limit. The 57 mΩ residuals shown for the FETs are 25 °C component screens only.

## Result returned upward

`CANDIDATE_READY` for Power/Package/DFM authority review, with a precise
residual qualification dependency. No candidate is promoted as a production
limiter. The exact remaining gates are:

1. an in-window controller/calibration contract with bounded residual;
2. guaranteed ADM1175 gate minimum at the 12.05--12.60 V source and hot FET
   `RDS(on)` at that drive;
3. complete installed hot-path resistance including reverse protection;
4. harness transient, TVS/fuse, SOA/I²t and fail-safe coordination;
5. installed thermal/DFM evidence; and
6. production calibration, fixture, retention and lot-traceability limits.

These are internal authority/evidence gates, not an external blocker. Source
contract and exact-nFET work remain waiting on
`authority:6A-limiter-qualification`.

## Validation

```text
python3 ADM1175_COMPONENT_PATH_CALC.py > ADM1175_COMPONENT_PATH_CALC.json
```

The generated JSON was inspected for the expected failing current window and
ratio test. Hashes for all receipt artifacts are in `SHA256SUMS`.
