# Clearance repair producer rejection

- Workstream: `clearance-repair-producer`
- Base SHA: `c8710a84cc142b6ca8a04697e40b89576591eb26`
- Candidate: rejected local removal of redundant `GATE_B` via UUID `1e3bc3eb-a350-4fff-8eeb-557e90b4d4bd` at `(12.54,108)`, co-located with Q2 pad 3 (through-hole).
- Ownership boundary: only clearance/edge-clearance/hole/dangling/courtyard/crossing families; excluded storage/JMS, power/return, J1, and scoped high-speed nets.
- Producer image/tool: `pisxme-kicad-light:v1`, KiCad `10.0.6`, 1 CPU/1 GiB.

## Evidence

Untouched baseline and restored baseline both report 312 violations and 499 unconnected items, with no `shorting_items`.
The candidate reports 310 violations and 499 unconnected items, but introduces one `shorting_items` violation: `USB_TXP1` versus `JMS_AVDDL`. It therefore fails the no-shorts acceptance condition and was not committed or integrated.

The candidate removed one redundant via only; no schematic, project, rules, libraries, outline, placements, or non-owned routes changed. The candidate board and patch are retained for audit.

## Output hashes

- baseline-drc.json: `aa6674fffcce5b9f90a634db1d23685c6ce42f2e1f595dee96b233d5a114071c`
- restored-baseline-drc.json: `84dafdb8dca740f74dacae134a63b512dfcb8108bc7f37c304c1bacb254b56e8`
- candidate-drc.json: `bcc4bfa1cb6e38d36840c6d64c04ae9c7b9a81c9167ee6ff8e47c5dbd63be9e8`
- candidate-board-rejected.kicad_pcb: `866bba6beff59814ad5166537f1d9a8eebd48fdb4186eb63969ecd367ff525dd`
- candidate-rejected.patch: `563688f086c3762757b0d01f62f77e3755c70d02902e196509c79baa6599b1e9`

## Decision

Reject candidate; stop this hole-removal method for this bounded attempt. The worker is restored to clean base `c8710a84`.
