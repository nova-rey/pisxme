# Signed nine-branch source topology materialization

- Package: `P24-PROTECTED-BUS-SOURCE-TOPOLOGY-MATERIALIZATION`
- Base SHA: `627ec337a28ce0c732df7744dc3ba360414464db` (producer workspace base; canonical commit is `3e2db539`)
- Worker: `protected_bus_r3_issue7_producer_2`
- Image: `pisxme-kicad-light:v1`
- Method: native `pcbnew` API, explicit pad/net assignment, inherited branch copper removed

The isolated producer starts from the retained nine-branch geometry seed and assigns the exact signed source contract:

- J5/J6/J9 pads 1-3: `PWR_SRC_<J>_P<n>`.
- J5/J6/J9 pads 4-6: `PWR_RET_<J>_P<n>`.
- F1-F9 pads 1-4: corresponding source net.
- F1-F9 pads 5-8: corresponding `PWR_FUSED_<J>_P<n>` net.

The topology assertion passes for all three headers and all nine fuses. The materialized candidate is retained as a topology candidate only; it contains no claim of routed closure. Native Light DRC reports 1039 violations and 499 unconnected items because inherited unrelated copper and the protected corridor remain unresolved. This is expected at the source-topology stage and is not a Phase 24 acceptance result.

The candidate is ready for the protected-bus producer to consume as its corrected source base. Routing remains serialized behind this source artifact and must use the R3 MPA geometry with explicit per-branch micro-batches.

## Validation receipts

- Exact topology: PASS, `signed_source_topology.json`; all J5/J6/J9 pads 1-6 and F1-F9 source/fused pad groups are present with exact signed names.
- Native net census: PASS, `native_net_census.json`; all 27 signed branch nets have nonzero pad ownership.
- Native Light DRC: recorded as a source-stage baseline only (`1039` violations, `499` unconnected); it is not a routing or Phase 24 closure claim.
