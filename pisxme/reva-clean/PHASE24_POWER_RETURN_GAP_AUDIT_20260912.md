# Phase 24 integrated power/return gap audit — 2026-09-12

Scope: read-only audit of canonical integrated candidate at HEAD before any power CAD edit. Source PCB SHA is the retained current integrated geometry (`20da22d72b4d…386720` after the C16/C17/C19 silk candidate); qualified toolchain evidence remains KiCad Light 10.0.6.

Findings:

- Raw branch B (`12V_IN_B`, `FUSED_12V_B`) has no PCB copper or vias; J6/F2/U2/Q2 are assigned but physically unrouted.
- Protected 12 V has only six short segments and one via, no distribution zone, and 146 unconnected groups including the J1 power field and regulator inputs.
- The 170-contact J1 `POWER_GND` field has 171 unconnected groups requiring native connector-field/plane audit.
- U4 `BRIDGE_3V3` and U5 `BRIDGE_1V1` outputs have no PCB segments/vias; CM5 5 V remains partially open.
- Storage 3.3 V and JMS583 local rails retain open support/return groups.
- Cooling/V100 power/control nets remain schematic contracts without validated physical paths.
- Historical power calculations conflict (250 W/25.25 A versus 300 W nominal, 330 W peak, 28.5 A continuous, 34.3 A peak); the current integrated candidate has no current-specific IR, transient, PDN, or thermal measurement evidence.

Required next bounded work: reconcile one approved current envelope, then generate a native rail/pad/track/via/zone census with negative controls, followed by owned power-corridor repair and fresh Light validation. Historical Phase 14 geometry cannot close current-candidate power evidence. The power acceptance row remains OPEN.
