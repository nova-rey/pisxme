# P24-POWER-SOURCE-CONTRACT — bounded internal authority escalation

Status: `BLOCKED_INTERNAL_AUTHORITY`  
Package: `P24-POWER-SOURCE-CONTRACT`  
Package base: `adbda0a2692837f4e3bcc9ca1d967190044fd366`  
Inspection head: `bc5ceeff1762c236d6b43f51db63ab3bca4c98e2`  
CAD changed: **no**  
PCB routing or source connectivity was not edited.

## Decision

The current source cannot be promoted to the six-loop implementation basis.
The contradiction is internal and bounded: the canonical source defines two
input branches, while the conditionally signed V2.2 product envelope requires
six independently current-limited 12-V/return loops. The retained source
records do not select a 12-V active current-limiter/eFuse that satisfies the
6.4 A hard branch limit, nor do they qualify the complete six-header mating
assembly. A PCB-only addition would create synthetic connectivity.

This is an authority dependency, not a user/product blocker. Power Authority
must select the current-limit/protection role and Package Authority must close
the exact assembly. MPA then binds the added cohorts and corridors. No new
architecture is being selected here, and the 300 W sustained / 330 W peak
product envelope remains unchanged.

## Current canonical source census

`POWER_INPUT.kicad_sch` at the inspection head contains only:

| Role | Existing source instances | Existing contract |
|---|---|---|
| Input headers | J5, J6 | `0039300020`, `Molex_0039300020_5569_2P_RA`; one 12-V pin and one return each |
| Raw nets | `12V_IN_A`, `12V_IN_B` | one net per existing header |
| Fuse stages | F1, F2 | `0297015.U` in `178.6165.0001`; 15-A candidate, not a 6.4-A limiter |
| Reverse/protection controllers | U1, U2 | `LM74700QDBVRQ1` |
| Pass FETs | Q1, Q2 | `CSD19536KCS` |
| TVS | D1, D2 | `SMBJ18A` candidate |
| Branch outputs | `FUSED_12V_A`, `FUSED_12V_B`, then common `12V_PROTECTED` | two source paths only |

The source also contains C3/C4 VCAP support. No authoritative C–F branch
nets, four additional headers, or four additional independent current-limit
stages exist. Existing J7 and J8 are assigned to CM5/storage elsewhere, so
they must not be reused for power entry.

## Required source contract for the next authority decision

The following is the minimum contract that the authority correction must bind;
it is recorded here as a requirement and is not represented in CAD yet.

1. Six physical headers, one 12-V contact and one return contact per header,
   using the qualified `0039300020` / 5569 family unless Package Authority
   approves a mechanically equivalent alternative. J5/J6 remain A/B. Four
   unused canonical references must be assigned for C–F by the source owner;
   J7/J8 are unavailable. Suggested reserved references are J9–J12 only
   after a collision-free native source census.
2. Six distinct raw nets: `12V_IN_A` through `12V_IN_F`.
3. Six distinct post-fuse nets: `FUSED_12V_A` through `FUSED_12V_F`.
4. Six distinct post-limiter nets: `12V_PROTECTED_A` through
   `12V_PROTECTED_F`. These may join the common protected bus only after each
   branch has its own qualified limit, fault response, reverse-current policy,
   and thermal path. No passive sharing is a substitute for those stages.
5. Six distinct return nets, `POWER_RETURN_A` through `POWER_RETURN_F`, with
   a documented controlled join to the `POWER_GND` return plane. The join and
   copper must preserve the six return-loop current/drop budget.
6. Each branch requires a fuse or other upstream energy coordination,
   bidirectional/reverse-current protection as applicable, a 12-V-rated active
   current limit with a guaranteed maximum at or below 6.4 A, fault reporting,
   thermal shutdown, and a defined inhibit/latch response. The existing
   15-A F1/F2 choice alone does not satisfy this item.
7. The source contract must assign exact MPNs, package/footprint identities,
   limit-setting values and tolerances, source references, and pin-level net
   mapping for all six stages. Generic placeholders such as `CL_C` are not
   sufficient for a producer candidate.
8. The contract must preserve the V2.2 electrical screens: 11.4–12.6 V
   source window, 40 A continuous / 45 A bounded peak source requirement,
   5.8 A normal branch target, 6.4 A hard branch limit, six-loop return
   budget, 0.350 V sustained and 0.400 V peak protected-bus drop screens,
   and fail-safe V100 inhibit on branch fault.

## Evidence and why it does not yet close

- `POWER_INPUT.kicad_sch` is the current source of truth for the two existing
  channels. Its SHA-256 is
  `075ae680e3754e06bf995739db15cf30774432f8cf9fb487b5df20b3034c286b`.
- `POWER_ENVELOPE_AUTHORITY_V2.2_CANDIDATE.json` defines six loops, 6.4 A
  hard branch limits, and no passive sharing, but explicitly leaves exact
  assembly qualification and the source PDF hash open.
- `MPA_DECISION.json` requires six headers, six independent current limits,
  six returns, and no synthetic connectivity.
- `QUALIFICATION_PACKET.json` closes the header family, terminal class,
  16-AWG basis, 8-A/circuit manufacturer screen, 10-mΩ contact screen and
  30 °C rise basis, but leaves mating housing/plating, crimp, harness loop,
  ambient/airflow, fuse I²t, six-header thermal installation and source-PDF
  byte hash open.
- The private Library currently has no indexed 12-V active current-limiter
  contract for this branch. The bounded official-source search found TI's
  TPS1663 family (4.5–60 V, adjustable 0.6–6 A, ±7%, 31-mΩ typical FET,
  20-pin HTSSOP option), but the 6-A setting has a 6.42-A upper specification
  and therefore cannot be silently adopted as a guaranteed 6.4-A limit. It
  is research input for Librarian/Power Authority, not an approved selection.
  See the official [TI product page](https://www.ti.com/product/TPS1663) and
  [TPS1663 data sheet](https://www.ti.com/lit/ds/symlink/tps1663.pdf).

## Exact internal decision required

Power Authority shall choose one production current-limit/protection stage
for A–F and state the tolerance calculation that guarantees `I_BRANCH <= 6.4
A` over source voltage, temperature, load and part tolerance. The decision
must also state whether LM74700/Q1–Q2 remain as separate reverse-block stages
or are replaced by the selected eFuse's qualified behavior. Package Authority
shall then qualify the exact MPN/package, six-header installation, mating
5557/5556 assembly, harness loop resistance, thermal environment and fuse/I²t
coordination. MPA shall assign nonconflicting source references and positions
while preserving its fixed anchors and protected corridors.

This escalation does not request a user decision. It asks for one bounded
internal authority packet. It must return either an exact source/net/component
contract or a new evidence-backed contradiction; no route variants are
authorized meanwhile.

## Queue disposition and producer resumption

Affected invariant rows remain open: `INV-PRODUCT-V100-300W`,
`INV-PRODUCT-V100-330W-PEAK`, `INV-INPUT-12V`, `INV-INPUT-CAPACITY`,
`INV-MOLEX-8A` (component-level PASS only), `INV-BRANCH-SHARING`,
`INV-PROTECTION`, `INV-COPPER`, `INV-RETURN`, and `INV-THERMAL`.

The waiting `P24-POWER-INPUT-ARCHITECTURE` producer cannot return `READY` from
this packet. It remains waiting on `authority:power-source-contract` and the
separate `P24-POWER-CONNECTOR-QUALIFICATION` evidence dependency. Once the
two authorities return an exact contract, Root may move the producer to READY
for one isolated schematic/PCB producer, serialized integration, targeted
connectivity/DRC, and fresh Light validation. No candidate, route, or
integrated acceptance row is closed by this receipt.
