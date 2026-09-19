# PiSXMe Rev-A mechanical 3D envelope authority contract

**Contract:** `PISXME-P24-MECHANICAL-3D-ENVELOPE-20260919-R1`  
**Base:** `dd3fe9591758a617d26cc347849e75ddea18fd73`  
**Status:** signed bounded authority contract with explicit `UNPROVEN` fields  
**Scope:** L10/Y10 XY and Z envelope dispositions, J8 DNP/populated service contract, J1/J3 mating/service boundaries, and the Rev-A cooler/backplate boundary. No CAD was edited.

The machine-readable contract in `MECHANICAL_3D_ENVELOPE_AUTHORITY.json` is the governing artifact. Its content digest is recorded in `CONTRACT_SHA256`; the source evidence hashes are in `SOURCE_MANIFEST.sha256`.

## Binding results

- **L10:** `L_2520_6332Metric`, 4.7 uH, position `(143.00,127.80)`. The current courtyard `[141.355,126.355]–[144.645,129.245]` is the binding XY limit. Exact MPN, body height, and 3D model remain `UNPROVEN`.
- **Y10:** `Crystal_3225_4Pad`, 25 MHz, position `(138.20,126.40)`. The current courtyard `[136.455,125.005]–[139.945,127.795]` is the binding XY limit. Exact MPN, body height, and 3D model remain `UNPROVEN`.
- **J8:** current source state is in-BOM, on-board, `DNP=false`, with `FORCE_SATA`, `AUTO_PEDET`, `FORCE_NVME`, and `MODE_IN` on pins 1–4. DNP conversion is not authorized by this contract. The exact accessory, mating part, keying, height, and service procedure remain `UNPROVEN`; simultaneous FORCE_SATA and FORCE_NVME selection is prohibited.
- **J1:** Amphenol/FCI `74221-101LF`, 400 contacts, 1.27 mm array, 4.0 mm mated height, 0.45 A/contact, 50 cycles, and 5.10 mm rework-perimeter guidance are binding external-contract inputs. Exact final local mating/rework/3D assembly remains `UNPROVEN`.
- **J3:** JAE `SM3ZS067U410ABR1000`, B-key, 67 contacts, 0.5 mm pitch, 4.10 mm body height, 0.5 A/contact, 60 cycles, and 2280 insertion/retention datum are binding. Existing J3/2280 envelope DRC findings remain open; this contract grants no waiver.
- **Cooler/backplate:** Rev-A reserves a module-mounted cooler contract only. It does not reserve an unverified carrier-mounted cooler/backplate or generic 150×95 mm underside exclusion. The selected module cooler, standoffs, enclosure, and thermal/service assembly still require prototype validation.

## Evidence boundary

Current retained evidence establishes the 2D bounds and component identity where stated. It does not establish absent MPNs, exact package heights, 3D mating models, J8 service hardware, a populated 2280 card sweep, or a selected cooler/backplate assembly. Those fields are explicitly `UNPROVEN` or `REQUIRES_PROTOTYPE_VALIDATION`; no green mechanical acceptance is manufactured.

## Authority attestation

Signed by the Mechanical/DFM Authority delegate in this work package on 2026-09-19 using the SHA-256 content digest recorded in `CONTRACT_SHA256`. Root retains canonical integration and queue-state authority.
