# P24-POWER-INPUT-ARCHITECTURE producer receipt — structural contradiction

Status: `BLOCKED` at the smallest producer task; no CAD candidate was created.

## Package and base

- Package: `P24-POWER-INPUT-ARCHITECTURE`
- Producer workstream: `p24-power-storage-producer-v2`
- Base commit: `adbda0a2692837f4e3bcc9ca1d967190044fd366`
- Selected PCB: `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- Selected PCB SHA-256: `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`
- Toolchain: KiCad `10.0.6`, qualified image `pisxme-kicad-light:v1`
- MPA basis: `validation-receipts/mpa-binding-six-loop-reconciliation-20260914/MPA_DECISION.json`
- Power basis: `validation-receipts/power-envelope-authority-redesign-20260914/POWER_ENVELOPE_AUTHORITY_V2.2_CANDIDATE.json`

## Bounded operations

1. Fresh isolated worker prepared from the committed base.
2. Baseline native DRC:
   `kicad-cli pcb drc --output baseline-drc.rpt PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
   - return code `0`
   - `300` violations, `499` unconnected items
3. Read-only `pcbnew` census of the selected PCB and canonical schematic marker.
   - return code `0`
   - raw result: `structural-contradiction.json`

No footprint, net, route, rule, schematic, or configuration was changed. No
route variant was attempted.

## Authority-to-current-design comparison

The binding MPA/Power Authority contract requires six physical 12-V/return
loops, six independent current limits at `6.4 A`, six returns, and no passive
sharing. The current integrated PCB contains:

- two and only two qualified `0039300020` / 5569 headers: `J5`, `J6`;
- only `12V_IN_A`, `12V_IN_B`, `FUSED_12V_A`, and `FUSED_12V_B` branch nets;
- only `U1/U2` LM74700 protection stages and `Q1/Q2` high-side paths;
- no authoritative C–F branch nets, four additional headers, or four additional
  independent protection/current-limit stages.

The package qualification packet also retains open exact-assembly, harness,
thermal-installation, fuse-I2t, and source-document-hash conditions; MPA names
connector qualification as a dependency.

Adding C–F nets, headers, protection components, or copper only in the PCB
would create synthetic connectivity absent from the canonical source contract.
It would violate the no-synthetic-connectivity requirement and could not return
an acceptable producer candidate.

## Result and escalation

`STRUCTURAL_CONTRADICTION`: the six-loop authority contract cannot be
materialized from the current schematic/PCB source without a bounded authority
correction that defines the four missing authoritative branch nets, connector
instances, protection/current-limit stages, and their qualified package
geometry. Return this evidence to Macro Placement Authority / Package Authority
for one bounded source/net/component-contract decision. Do not launch route
variants or mutate CAD until that decision is recorded.

Affected invariant rows include `INV-PRODUCT-V100-300W`,
`INV-PRODUCT-V100-330W-PEAK`, `INV-INPUT-CAPACITY`, `INV-COPPER`, and
`INV-PROTECTION`: the current implementation remains `FAIL` or `UNPROVEN`;
this receipt does not waive or close any row. Path-A storage implementation
was not changed or falsely marked complete.
