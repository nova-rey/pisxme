# Phase 24 Branch-B power-envelope reassessment

Date: 2026-09-14
Work package: `P24-POWER-ENVELOPE-REASSESS`
Issue: `nova-rey/codex-config-backup#2`
Canonical source branch: `reva-clean`
Canonical source at review: `eab799b1f12d8b0cad8a6db31add18576eb8056a`

## Decision

The Sol result is narrowed, but it remains an external/product-architecture
blocker. The combined PiSXMe specification requires the SXM2 V100 product
power envelope, while the selected J5/J6 connector topology provides one
12-V contact and one return contact per branch. The exact Mini-Fit Jr.
wire-to-board current table for the selected 2-circuit 5556/5557/5569
system rates a two-circuit 16/18-AWG assembly at 8 A per circuit under the
manufacturer's 30 C temperature-rise test. Thus two branches provide a
connector-limited 16 A total before PCB, fuse, harness, or thermal derating.

NVIDIA specifies 300 W maximum consumption for the V100 SXM2. At a 12 V
input this is 25 A before the CM5 buck and other board loads. The CM5 5-V
design envelope adds approximately 1.16 A at 12 V when using the existing
2.5 A / 90% design screen:

```text
I_V100 = 300 W / 12 V = 25.00 A
I_CM5_in ~= (2.5 A * 5 V) / (12 V * 0.90) = 1.16 A
I_total ~= 26.16 A > 2 * 8 A = 16 A
```

The historical 330 W peak allowance is 27.50 A at 12 V before auxiliary
loads, and the earlier 28.5 A / 34.3 A figures are design allowances rather
than measured behavior. No source found in the existing corpus establishes a
V100 SXM2 load-step magnitude, slew, or transient current contract for this
carrier.

Power Authority therefore cannot silently bind a full-product continuous or
peak current value that the selected connector topology cannot carry. Closing
this contradiction requires one product/architecture decision: change the
input contact topology and harness, or explicitly accept a lower V100 power
envelope. It is not a missing calculation that can be repaired by routing.

## Field classification

| Required field | Class | Evidence and bounded conclusion |
|---|---|---|
| connector/harness limits | A | Molex PS-43879-001, section 4.3, rates the exact 5556 Mini-Fit Jr. wire-to-board system at 8 A per circuit for a 2-circuit 16/18-AWG assembly and requires application derating. J5/J6 each serialize one 12-V contact and one return. The generic Molex family “up to 13 A” figure is not substituted for the exact selected terminal/application. |
| continuous current | D | Full-product requirement is at least 25 A for the documented 300 W V100 SXM2, plus CM5 and board loads. The selected two-branch contact envelope is 16 A before derating. Power Authority may set an internal 16 A limit, but that would change the V100 product requirement and needs product/architecture authority. |
| peak current | D | The 330 W design allowance is 27.50 A at 12 V before auxiliary loads; no authoritative module peak-current contract was found. A 16 A internal cap would be a product derating, while a full-power peak requires a changed input architecture or module-specific product authority. |
| branch imbalance | C | Internal rule: do not assume equal sharing; each branch is independently limited to the exact connector/harness bound, with shutdown on an over-limit branch. This is implementable after the continuous/peak product decision. |
| shutdown behavior | C | Internal rule can require branch fault isolation, V100 power-enable inhibit, `/PERST` held asserted until all required power-good signals are valid, and controlled recovery. TI TPSM63606 protection/soft-start behavior supplies component context but does not define V100 sequencing. |
| surge/load-dump limits | A/B/C | Selected fuse and TVS records provide 32 V fuse rating, 308 A2s typical fuse I2t, 18 V TVS standoff, 29.2 V clamp at 20.6 A, and LM74700 42 V absolute maximum context. Power Authority can bind a board transient screen below those component limits; source-specific load-dump waveform remains a validation input. |
| thermal limits | A/B/C | Molex's 8 A table is based on 30 C maximum temperature rise; connector housing is documented to 105 C class. Selected semiconductor and TVS records provide component temperature limits. Power Authority can bind board-level rise and junction-margin requirements without claiming a hardware measurement. |
| current sharing | A/C | Molex explicitly says the connector system is not designed or tested for current sharing. Internal policy must therefore avoid equal-share arithmetic, cap each branch independently, and require branch monitoring or fault isolation. |
| load-step requirements | C | Power Authority can define a carrier-level load-step test at the accepted branch envelope, with rail deviation, slew, recovery, and instrumentation criteria. No V100 module-specific load-step contract is available; the result cannot be used to claim full-product V100 closure until the D fields are resolved. |

## D fields and exact required decision

Only these fields remain Class D:

1. **Continuous current** — decide whether the product must sustain the
   documented 300 W V100 SXM2 plus board loads. If yes, authorize a changed
   connector/contact/harness topology with a new package and PCB contract. If
   no, authorize and document the lower V100 power envelope.
2. **Peak current** — decide the product peak envelope and whether the 330 W
   allowance is retained. If retained, authorize an input architecture that
   can carry it and provide the module/source transient contract. If removed,
   authorize the lower bounded envelope and its load-step test policy.

No user-supplied numerical invention is requested. These are the minimum
product/architecture choices that remain after Library inspection, targeted
manufacturer research, component calculations, and Power Authority review.

## Sources and provenance

Existing private Library and repository authority records were inspected first:

- `PiSXMe-Library/Library/subsystems/power-protection.md`, SHA-256
  `14474c1af63917cd8085fc712495364aed869fda70b8289a1f55a478a4137483`
- `PiSXMe-Library/design/POWER_ARCHITECTURE_V1.md`, SHA-256
  `e110923ff7d7158e96daf6316d70f878c7cf3bc19972b2c220e1d4946cb7e418`
- `authority-inventory/primary-docs/power/MOLEX_0039300020_AUTHORITY.md`,
  SHA-256 `37d7642bf413385e3980aabb6b63ef758b9d3398a69f500a45b0bf2b861608c3`
- `authority-inventory/primary-docs/power/LITTELFUSE_0297015U_17861650001_AUTHORITY.md`,
  SHA-256 `d2e617125ae28bef0e977f69211e3c5a08eabce184f172b91e5d4bc20fcab389`
- `authority-inventory/primary-docs/power/SMBJ18A_TVS_AUTHORITY.md`, SHA-256
  `4e63353741e69f7f6186e314f8caf93b4b62265166f97e2a32445d1d25280158`
- `PHASE24_POWER_RETURN_GAP_AUDIT_20260912.md`, SHA-256
  `bf8bc8ed7358f564b78a95c897b22bfaed36cba31151b156fd3dcb5e0103e3d2`
- `PHASE24_MPA_STORAGE_POWER_DECISION_20260913.md`, SHA-256
  `59dc70cd64a7ae399c571dac1c7ba15f2916403b91a6b6b46de912025a0bef6f`

Targeted primary-source research added these references to the reassessment:

- Molex, **PS-43879-001-001**, Mini-Fit family product specification,
  section 4.3 current table and derating note:
  <https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/productspecificationpdf/438/43879/PS-43879-001-001.pdf>
- Molex, **PS-5556-001**, Mini-Fit Jr. system specification identifying
  5556/5557/5569 series:
  <https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/productspecificationpdf/555/5556/PS-5556-001-001.pdf>
- TI, **TPSM63606 Rev. B**, 6-A output, current limit, hiccup, and soft-start:
  <https://www.ti.com/lit/ds/symlink/tpsm63606.pdf>
- Raspberry Pi, **CM5 datasheet**, 5-V input and rail context:
  <https://pip-assets.raspberrypi.com/categories/944-raspberry-pi-compute-module-5/documents/RP-008180-DS/cm5-datasheet>
- Littelfuse, **MINI 297 fuse datasheet**, 15-A / 32-V and typical I2t:
  <https://www.littelfuse.com/assetdocs/littelfuse_datasheet_297_mini32v.pdf?assetguid=42c9dd21-a88e-4328-8e67-2f832444faf1>
- NVIDIA, **Tesla V100 GPU Accelerator datasheet**, SXM2 maximum power:
  <https://images.nvidia.com/content/technologies/volta/pdf/tesla-volta-v100-datasheet-letter-fnl-web.pdf?nvid=nv-int-gc27-14212>

The source classes are manufacturer specifications or NVIDIA product data;
the 300 W to current conversion and CM5 input estimate are engineering
calculations. No fabricated-hardware result is claimed.

## Disposition

Issue #2 remains `external-blocker`, narrowed to the two D fields above. The
main queue must not return the integrated corridor package to READY until a
product/architecture decision resolves the current-capacity contradiction.
No CAD was changed and no Phase 25 or Phase 26 action is authorized.
