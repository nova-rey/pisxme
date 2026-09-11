# Phase 24 ERC cluster remediation map — 2026-09-11

## Current authoritative census

Fresh native KiCad 10.0.5 full-severity ERC on the canonical clean schematic
reports **483 warnings and 0 errors** after the PWR_FLAG namespace repair.
The
current raw receipt is `PHASE24_CLEAN_SCHEMATIC_ERC_REGULATOR_PIN_STUB_PROMOTED_20260911.rpt`
(SHA-256 `1acb82e1ac8e4abf1afac4fabc9762579b8aebe88e811d40f62dc03c041200c2`).
The 777-warning receipt below is retained as historical pre-stub-repair
evidence.
No findings are waived.

| Cluster | Count | Scope/signature | Shared cause hypothesis | Confidence | Safe next repair |
|---|---:|---|---|---|---|
| endpoint_off_grid | 197 | Root and child hierarchy endpoints; repeated 2.54/3 mm coordinates | Residual legacy grid geometry remains after hierarchy association repair; duplicate POWER_INPUT wire serialization is closed | High | One complete sheet/label/direct-link transformation, or retain as bounded ERC cleanup work |
| isolated_pin_label | 232 | Root/child boundary labels, especially repeated contract ports | Residual contract labels are electrically associated but still reported as isolated by native ERC; removal/renaming is intent-sensitive | High | Analyze by identity and native netlist parity; no suppression |
| unconnected_wire_endpoint | 0 | Root/child contract wire families | Closed by removal of 84 unowned 1 mm regulator pin stubs after exact native netlist parity | High | Regression only; do not remove owned contract wires |
| same_local_global_label | 30 | Repeated boundary names in root and child sheets | Deliberate-looking boundary aliases are serialized as both local and global labels | High | Review ownership; rename/remove only with exact netlist parity |
| multiple_net_names | 24 | Mostly STORAGE aliases and NC/support labels | Superseded storage edits left multiple names on common items | Medium | Resolve only proven aliases; preserve intentional isolation |
| no_connect_dangling | 0 | CORE_CM5 stale duplicate records | Closed by native-correlated removal of 11 stale records | High | No further repair; regression remains required |
| lib_symbol_mismatch | 0 | Former embedded standard PWR_FLAG copies | Closed by project-local namespace repair with exact netlist parity | High | Regression only; do not reintroduce `power:PWR_FLAG` instances |

The first three classes form a **433-warning residual hierarchy geometry/contract
cluster**. The naming cluster is 54 warnings and two PWR_FLAG library
findings remain. A lower count is not
acceptance: the required checks are native ERC, exact netlist parity, and
preserved electrical intent.

## Current remediation state

The identity-preserving repair closed the native hierarchy-error defect and
the promoted regulator-stub and duplicate-wire repairs reduced the live census from 777 to 485
without changing
the 338-net native netlist. The remaining 197 endpoint findings are not
evidence that the promoted association is wrong: the root-x-only disposable
normalization increased total findings and reintroduced hierarchy errors;
the later duplicate POWER_INPUT wire repair is separately promoted.
The next discriminator is therefore a complete owner-aware grid transform,
not coordinate-only edits. Naming and PWR_FLAG clusters remain independent
and must be handled with the same netlist-parity guard.

The corrected bounded STORAGE alias-removal probe was rejected: removing one
co-located `NC_*` label reduced `multiple_net_names` by one and native ERC to
776 warnings, but changed the exported netlist from 338 to 339 nets and
changed the `/STORAGE/JMS_VDDREG_5V` node set. No canonical source changed.
Receipt:
`PHASE24_MULTIPLE_NET_NAME_PROBE_REJECT_RECEIPT_20260911.md`.

The complete root-coordinate grid probe was also rejected. It preserved native
hierarchy structure and exact 338-net/node parity but left ERC unchanged at
489 warnings, proving that the residual endpoint findings are not solved by
an indiscriminate root-x/grid transform. Receipt:
`PHASE24_ROOT_GRID_PROBE_REJECT_RECEIPT_20260911.md`.

The direct KiCad 10 installed-library substitution for the two embedded
`PWR_FLAG` definitions was rejected: native ERC remained at 489 warnings and
both `lib_symbol_mismatch` findings remained. Receipt:
`PHASE24_PWRFLAG_LIBRARY_PROBE_REJECT_RECEIPT_20260911.md`.

The two remaining 65 mm `REGULATORS` wires were tested as a separate removal
class. Native ERC stayed at 489 warnings and replaced the two endpoint-grid
findings with two `label_dangling` findings; exact 338-net/node parity held.
The wires are therefore owned rail connections and were not removed. Receipt:
`PHASE24_REGULATOR_LONG_WIRE_PROBE_REJECT_RECEIPT_20260911.md`.

## Structural evidence

`validation/phase3/phase24_hierarchy_structure_audit.py` now inventories the
actual root sheet-pin order, child hierarchical-label order, embedded contract
pin names/numbers, and serialized contract-instance pin UUIDs.  It confirms
that these sequences are not interchangeable:

* `REGULATORS` root order is `12V_PROTECTED, CM5_5V, STORAGE_3V3,
  BRIDGE_1V1_3V3, BRIDGE_3V3, BRIDGE_1V1`, while the child labels begin with
  `BRIDGE_3V3, BRIDGE_1V1` and the embedded definition/instance currently
  serialize only the first four ports.
* `CORE_CM5` has 15 labels/root pins but its embedded contract definition and
  instance serialize 12 pins.
* `ETHERNET` has 3 labels/root pins but its embedded contract definition and
  instance serialize pins 1, 3, and 4.
* `STORAGE` has 7 labels/root pins but its embedded contract definition and
  instance serialize only the first five.

These are concrete source-authoring facts, not inferred graph edges.  Any
repair must use a per-child name/UUID table and preserve the native instance
association semantics.

## Bounded experiment and disposition

`phase24_native_contract_identity_probe.py` created a disposable output that
regenerated all contract definitions/instances from root names and child
label UUIDs, while moving hierarchy geometry together.  Native KiCad ERC on
the actual disposable path produced 919 findings, including four
`pin_not_connected` hierarchy errors and additional `label_dangling` and
`lib_symbol_mismatch` findings.  Receipt:
`.phase24_native_contract_identity_probe/identity-erc3.rpt` (SHA-256
`c2cb6f3271426e0078bc9fc3b9fff02af91e5c1b3222db2357f62bf2b53c97ce`).

**Disposition: REJECTED.**  The canonical schematic was not modified.  The
probe proves that changing contract pin order/definition and geometry in one
pass is still insufficient when the native association semantics are guessed;
the next experiment must obtain/compare the exact native-authored association
or preserve the complete existing association records while repairing only
the validated geometric owner mapping.  Earlier partial coordinate and
contract-order probes remain historical rejected evidence.

## Next bounded repair

Use the structural inventory to build one native-authoring-equivalent,
identity-driven transformation.  For every port, explicitly preserve the
mapping:

`root sheet pin ↔ root wire/endpoint ↔ child label ↔ embedded contract pin ↔
contract-instance pin UUID ↔ child wire endpoint`.

Do not edit the canonical source until the disposable result has:

1. native reopen and full ERC with no new hierarchy errors;
2. exact exported netlist name/node parity with the canonical source;
3. no new pin-not-connected findings;
4. unchanged real circuit symbols and net names; and
5. a regression fixture that rejects a missing/altered association.

The PWR_FLAG and 54-name clusters remain independent side work, but neither
should be used to mask the hierarchy contract defect.

## Representation probe — synthetic contract removal

A corrected disposable probe copied the local symbol/footprint tables before
removing only the embedded `_Contract_1_1` definitions, their placed contract
instances, and the generated label-to-contract marker wires. Native KiCad
reported 826 warnings, but introduced 87 `label_dangling` findings and
removed the synthetic contract libparts from the exported netlist. Receipt:
`.phase24_no_synthetic_contract_probe2/no-contract-erc.rpt` (SHA-256
`e3e2845c5a5b2a3132bdc8246e623e5afa89312d7e536942dc85d0ec02282c8a`).

**Disposition: REJECTED.** Simply deleting the generated contract layer
discards required connectivity and changes the netlist. The live child
circuitry and port associations must be re-authored coherently.

## Residual endpoint probe — root-x-only normalization

After the identity repair was promoted, a disposable root-x-only normalization
was tested against the remaining endpoint cluster. Native ERC produced 867
findings, including four hierarchy `pin_not_connected` errors, three
`label_dangling` findings, and increased isolated/unconnected counts. Receipt:
`.phase24_native_contract_identity_probe/identity-erc9.rpt` (SHA-256
`96f595467beff500d7622a18af0acec22eecffe9676731bd937e10f3a6e85c33`).

**Disposition: REJECTED.** Root wires cannot be normalized independently of
sheet geometry and direct-link ownership. The promoted canonical source is
unchanged by this experiment.
