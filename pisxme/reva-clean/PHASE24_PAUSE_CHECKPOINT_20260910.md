# Phase 24 pause checkpoint — RTL9210B Path-B routing

Date: 2026-09-10
Branch: `reva-clean`
Purpose: safe GitHub checkpoint before resuming productive Path-B work.

## Current authoritative state

- Accepted RTL9210B orientation is closed: U1 `RTL9210B-CG`, top side, 0°,
  pin 1 southwest, V1517 lineage. Orientation search must not be reopened.
- The isolated candidate is
  `PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb`, generated from
  the current V1523 support baseline by
  `phase24_rtl9210b_integrate_v1603_v1517.py`.
- The accepted six-net U1-to-J1 high-speed launch is present and natively
  connected. The current layer-transition audit reports 72 physical vias and
  zero transitions without a via.
- The corrected QFN land-pattern audit passes: 69 SMD pads on F.Cu, with the
  exposed pad assigned to GND; no through-hole metadata remains.
- Current native candidate DRC is clean: zero violations, zero unconnected
  pads, and zero footprint errors.
- Native high-speed connectivity and support-parity audits pass, including
  their trace-removal negative controls. RESET_N has the restored TP6 test
  access. The support receipt records `ISOLATEB` and `PERST_N` as explicit
  boundary-only nets rather than silently inventing support edges.

## Work paused

The active task is the RTL9210B Path-B implementation, specifically converging
the accepted orientation into a coherent six-net physical-envelope-aware
launch and completing support authority. This pause interrupts no production
Path-A work and does not promote the isolated fixture into the acreage PCB.

The working tree contains many historical and disposable experiments. They
are intentionally not staged or deleted. The accepted baseline and its
receipts remain the resumption point.

## Remaining gates

1. Continue from the accepted V1517/V1603 candidate; do not generate another
   orientation family.
2. Resolve or explicitly bound the remaining support boundaries, especially
   the documented `ISOLATEB` and `PERST_N` ownership/termination decisions,
   using actual schematic/package authority rather than synthetic graph edges.
3. Complete the production-level RTL9210B support, firmware/configuration,
   procurement, mode, power, mechanical, and signal-integrity evidence.
4. Reconcile the isolated result with the Path-A fallback and only then make
   a documented promotion decision.
5. Continue the broader Phase 24 closure only after the Path-B side quest is
   complete, as directed by the current steering.

## Resumption command/context

Resume with the saved candidate, current generator, support-parity receipt,
native DRC report, layer-transition audit, and high-speed audit. Ordinary
implementation fixes are allowed; orientation search and unrelated acreage
floorplan work remain out of scope.
