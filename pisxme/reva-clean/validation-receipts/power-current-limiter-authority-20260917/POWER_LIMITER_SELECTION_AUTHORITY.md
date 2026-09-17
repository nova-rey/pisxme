# PiSXMe Power Limiter Selection Authority — HPQ4

- Decision ID: `PISXME-P24-POWER-LIMITER-SELECTION-20260917`
- Package: `P24-POWER-LIMITER-SELECTION-AUTHORITY`
- Review base: `a5572d6a02e94cf349e4619c5c07bae9bc31ca78`
- Authority: Product / Power Authority
- Date: 2026-09-17
- CAD changed: **no**
- Product envelope changed: **no**
- Status: `NO_QUALIFIED_PRODUCTION_MPN; WAITING_ON knowledge:authoritative-6A-window-limiter`

## Binding decision

No retained limiter option is authorized as the production current limiter for
HPQ4. The six-loop contract remains binding:

- six independent A--F loops;
- each loop guarantees **6.000 A minimum** and has a full-tolerance
  non-fault ceiling of **6.400 A**;
- the limiter allocation is at most **57 mOhm hot**;
- no passive current sharing may repair a deficient loop;
- the 300 W sustained / 330 W peak product envelope remains unchanged.

The prior conditional `MAX17527AATP+T` selection is superseded as a production
current-contract basis by HPQ4 v2.0.0. It remains historical qualification
provenance only. No alternative MPN is promoted, and no source schematic or
PCB producer may be released from this decision.

## Retained-option dispositions

| Option | Evidence-backed screen | Authority disposition |
|---|---|---|
| `MAX17527AATP+T` with 6.25 kOhm, 0.1% SETI | Documented current-limit range tops out at 6.000 A nominal with +/-4% accuracy. Full-tolerance range is `5.7542457542..6.2462462462 A`; shortfall to the 6.000 A floor is `0.2457542458 A`. Raising the nominal above 6 A is outside the documented selected range. | **REJECTED** as HPQ4 production limiter. Its earlier 57 mOhm maximum RON screen does not cure the independent current-floor failure. |
| `TI TPS1663` family | Retained research record gives 0.6--6 A adjustment, +/-7% accuracy, and 31 mOhm typical integrated FET. At the maximum 6 A setting, the screen is `5.58..6.42 A`: it misses the floor and exceeds the 6.400 A ceiling. The 31 mOhm value is typical, not a hot maximum contract. | **REJECTED** on retained evidence; it cannot satisfy both current limits and has no retained hot-resistance guarantee. |
| `LM74700-Q1` + `CSD19536KCS` or existing pass-FET stage | This is a reverse-blocking/controller and nFET arrangement, not a retained 6.000--6.400 A active limiter contract. Existing CSD evidence is not guaranteed at the required gate/temperature and does not establish branch limiting. | **REJECTED** as a limiter selection; may not be relabeled as one. |
| `STL125N10LF8AG`, `BSC096N10LS5`, `DMT6007LFG`, `CSD18536KCS` | Retained dossier identifies these as external nFET candidates. They do not provide the required active six-amp limiter function. Their gate, hot RDS, VDS and fault-energy gaps remain under the separate nFET authority package. | **NOT LIMITER OPTIONS**; retain only as unqualified nFET evidence. |
| `0297015.U` fuse / `SMBJ18A` TVS | Passive protection candidates do not establish a full-tolerance 6.000--6.400 A branch current contract. | **NOT LIMITER OPTIONS**; retain for later coordinated protection qualification. |

## Exact unresolved dependency

`knowledge:authoritative-6A-window-limiter` is the sole resumption dependency
for this authority decision. Librarian must first search the private corpus,
then commission bounded Researcher acquisition if needed, for a Tier-1
manufacturer source or an explicitly authorized component/controller design
that provides all of the following in one auditable contract:

1. exact production MPN and package/footprint identity;
2. 12-V operating compatibility over the HPQ4 source range;
3. guaranteed full-tolerance and temperature current-limit window with a
   minimum of 6.000 A and maximum of 6.400 A per independent branch;
4. a hot limiter resistance maximum no greater than 57 mOhm at the declared
   operating point, rather than a typical value;
5. current-limit tolerance, set-point method, fault timing, thermal shutdown,
   reverse-current/reverse-polarity behavior, and control-pin limits;
6. manufacturer provenance sufficient for Package, Power, Thermal and MPA
   authorities to coordinate fuse/I2t, nFET, TVS, harness, copper and
   fail-safe FLAG/inhibit behavior.

If no single integrated limiter meets the contract, Power Authority must return
one new bounded architecture authority packet for a controller plus externally
limited stage. That packet must preserve the same six-loop current and hot-loss
limits and must not silently convert a passive fuse or a typical resistance
value into a guaranteed limiter.

## Queue impact

- `P24-POWER-SOURCE-CONTRACT`: remains `WAITING` on this exact authority/
  knowledge dependency; no six-loop source/net contract is released.
- `P24-EXACT-NFET-ENERGY-AUTHORITY`: remains `WAITING` because actual gate
  drive, fault timing and SOA/I2t cannot be bound before the production limiter.
- `P24-POWER-INPUT-ARCHITECTURE` remains downstream and unreleased.
- Independent non-power acceptance work is unaffected.

This is an internal evidence/authority dependency, not a user-owned product
blocker and not a campaign-wide hard block. No CAD, footprint, rule, source
connectivity, or product-envelope change is authorized.

## Evidence and validation

The decision was checked against the signed HPQ4 contract and retained
limiter/protection/harness records. The MAX17527A shortfall is directly
recomputed as `6.000 * 0.96 / 1.001 = 5.7542457542 A`; the TPS1663 screen is
`6.000 * (1 +/- 0.07) = 5.58..6.42 A`. These are contract-level calculations,
not fabricated-hardware measurements. No bench, vendor approval, or thermal
qualification is claimed.
