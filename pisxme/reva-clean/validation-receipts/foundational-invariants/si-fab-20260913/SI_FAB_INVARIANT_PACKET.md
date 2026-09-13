# P24-SI-FAB Foundational Invariant Evidence Packet

**Package:** `P24-SI-FAB`  
**Base:** `c06876d2bb3c244d29ad04e883a253eefd35c265`  
**Scope:** independent SI, stack, fabrication and return-path evidence only.  
**Edit boundary:** no schematic, PCB, rules, project configuration, queue, or final invariant matrix edits.

## Result

The selected six-layer stack and its intended high-speed geometry are a valid
design basis, but they are not a fabrication or SI closure result. The current
integrated board contains route geometry outside the authorized normal basis,
and current saved geometry does not establish impedance, return continuity, or
fabricated-board capability. Those are acceptance-impacting findings; this
packet does not repair them.

## Current design and source identity

| Item | Identity |
|---|---|
| PCB | `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb` |
| PCB SHA-256 | `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c` |
| Project | `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pro` (`f965a4a405f1f2c0fa54a96a22d4bffaa0ee04e5787ad21db31c9c3bcf990143`) |
| Rules | `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_dru` (`d5473e6262fdf3b53d5de051626f0ed76dedf7257ba591f79ab8ad55f5b411ec`) |
| Schematic | `PiSXMe_RevA_Clean.kicad_sch` (`6eef63bd3d2b0b9fafc0150d3c34f636ce24a48b2ecbd3d28a5f0bfec167e9f1`) |
| Toolchain | KiCad Light 10.0.6; image `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9` |

The exact-head saved-geometry census records 329 segments, 90 through-vias,
216 F.Cu segments, 113 B.Cu segments, and no signal segments on the four
inner layers. `POWER_GND` has 47 segments, 11 vias, and three zones. These are
serialized-object observations, not proof of filled copper or manufactured
electrical performance.

## Invariant evidence

| ID | Statement and quantitative basis | Class | Current state | Verification / owner |
|---|---|---|---|---|
| `SI-FAB-STACK-001` | Use the selected six-layer JLC06161H-7628 design basis: nominal 1.6 mm board, 1 oz outer copper, 0.5 oz inner copper, ordinary through-vias. | B/C | **PASS (design declaration only)** | Parse PCB stack and reconcile fab order; Fabrication Authority. `PHASE13_STACK_RECEIPT.md`; `JLC06161H-7628_IMPEDANCE_INPUTS.md`. |
| `SI-FAB-IMP-001` | Controlled differential targets are 90 ohm for PCIe/USB3/USB2 and 100 ohm for SATA/1000BASE-T; released starting geometry is 0.13208 mm width / 0.2032 mm pair gap on the selected outer-to-adjacent-GND stack. | B/D | **UNPROVEN** | Fresh route/netclass audit plus order-specific field/coupon result; SI and Fabrication Authorities. Calculator inputs are a design target, not a measured board result. |
| `SI-FAB-REF-001` | High-speed pairs use outer layers over adjacent solid GND: F.Cu over In1.GND and B.Cu over In4.GND; inner-layer signal routing is excluded by the selected policy. | D/B | **UNPROVEN** | Exact-board native refill and transition/return-via audit, then integrated Light validation; SI/Return Authority. Saved layer roles agree, but zone continuity and every transition remain unproven. |
| `SI-FAB-GEO-001` | Normal trace/clearance geometry is at least 0.20 mm; the authorized 0.10 mm fine escape is limited to the named JMS583 XIN/XOUT region. | D/B | **FAIL** | Native rule-scope audit and DRC on the integrated candidate; Fabrication/DFM Authority with Storage Authority. Retained integrated evidence records U11 0.15 mm fanout outside the authorized XIN/XOUT region. |
| `SI-FAB-NETCLASS-001` | PCIe/USB3 controlled channels must retain their approved netclass geometry, and storage USB3 routes must be assigned to the appropriate controlled class before SI closure. | B/D | **UNPROVEN** | Inspect exact project netclass binding and route widths against all required nets; SI Authority. Current census records several USB3 paths at 0.15/0.20 mm rather than the 0.13208 mm starting geometry. Width alone does not prove impedance, so this is not promoted to PASS or a measured impedance failure. |
| `SI-FAB-VIA-001` | Through-via drill, diameter, annular ring, land clearance, and return-via geometry remain inside the selected fab/package capability; no unapproved via-in-pad is permitted. | B/D | **UNPROVEN** | Native pad/via parser, DRC, package overlay, and fab capability/order review; Package/DFM Authority. Current board has 90 through-vias, but the count does not establish all package and return constraints. |
| `SI-FAB-COUPON-001` | Release requires an order-specific controlled-impedance coupon and retained stack/copper/dielectric tolerances for the actual fabrication run. | B/D | **UNPROVEN** | Retain fab order, coupon result and acceptance limits in the Phase 25 manifest; Fabrication Authority. No coupon or manufactured-board measurement is retained. |
| `SI-FAB-RETURN-001` | Every critical pair transition has an electrically continuous reference plane and adequate local return path; plane splits and uncontrolled reference changes are prohibited. | A/D | **UNPROVEN** | Native refill, layer-transition graph, return-via review and SI evidence on one integrated SHA; SI/Return Authority. Three `POWER_GND` zones and saved vias show intent only. |

## Acceptance impact and disposition

- `SI-FAB-GEO-001` is a real current-design contradiction and must receive a
  bounded corrective work package. It does not authorize a global rule
  relaxation or removal of required copper.
- `SI-FAB-STACK-001` is reusable scoped evidence for the selected design basis.
  It does not prove a fabricated board, coupon, or production release.
- `SI-FAB-IMP-001`, `SI-FAB-REF-001`, `SI-FAB-NETCLASS-001`,
  `SI-FAB-VIA-001`, `SI-FAB-COUPON-001`, and `SI-FAB-RETURN-001` remain open
  requirements. They are dependent on the current power/J1/corridor decisions
  where those decisions change routing, and must be revalidated on the final
  integrated candidate.
- No impedance measurement, TDR/eye result, fab approval, or fabricated
  hardware evidence is claimed.

## Exact evidence used

- `PHASE13_STACK_RECEIPT.md` (selected stack and released targets).
- `authority-inventory/primary-docs/jlc/JLC06161H-7628_IMPEDANCE_INPUTS.md`
  (SHA-256 `ff4a4d904dde588d9d5deb17e39cee5a146de0ce68583edfa2c5b54b8161295a`).
- `authority-inventory/primary-docs/jlc/JLC06161H-7628-stack-api-20260830.json`
  (SHA-256 `d05b35679338f41986ca756bafe88ee655775b37a86a07cf2bbc107fbb6e58e0`).
- `validation-receipts/si-layer-census-current-head-20260913/RECEIPT.md`
  (saved route lengths, vias and proxy skews).
- `validation-receipts/si-power-reference-current-head-61085fe0/RECEIPT.md`
  (exact-head geometry, layer roles, rule context and current DRC context).
- `validation-receipts/si-provenance-72df93fc-20260913/RECEIPT.md`
  (rule-scope limits and current validation limitation).
- `PHASE24_JMS583_FINE_ESCAPE_RECEIPT_20260912.md` and the current integrated
  DRC/route receipts for the authorized local-escape boundary.

## Return to Root

`P24-SI-FAB` is **CANDIDATE_READY** as an evidence packet at base
`c06876d2bb3c244d29ad04e883a253eefd35c265`. Root should integrate this packet
into the foundational invariant synthesis and queue only after checking the
base SHA and retaining the evidence hash. No CAD workspace was allocated and
no candidate PCB was produced.
